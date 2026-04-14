#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟交易 CI 版 —— 自包含单文件，不依赖 roll/ 模块
=================================================
专为 GitHub Actions 设计，可独立运行，不修改仓库中任何已有代码。

策略逻辑：
  每日 T 预测完成后，优先挑选 filter_ret.csv 中高置信度、低风险的股票，
  于 T+1（下一个交易日）收盘价买入 SHARES_PER_STOCK 股，
  按 3 种持仓模式分别计算盈亏并输出独立 CSV：
    1. T日买T+1日卖：T+1 买入，T+2 卖出（持仓 1 个交易日）
    2. T日买T+3日卖：T+1 买入，T+4 卖出（持仓 3 个交易日）
    3. T日买T+5日卖：T+1 买入，T+6 卖出（持仓 5 个交易日）
  注意：top_n 现在表示“最多买入多少只”，弱信号日期允许少买或空仓。

费率说明（A股，2023 年后）：
  印花税 (stamp_tax)  : 0.05%，仅卖出方向收取
  佣金   (commission) : 0.03%，买卖均收取，单边最低 5 元
  过户费 (transfer)   : 0.001%，买卖均收取（沪市双向）

输出说明：
  CSV 按实际交易日期组织，每行代表一个交易日的操作：
  - 预测日（如 20260306）本身不产生任何买卖，不会出现在输出中
  - 首个交易日（T+1）仅有买入，无卖出
  - 后续交易日同时包含卖出（上一轮持仓）和买入（新一轮预测）

汇总 CSV 字段：
  交易日期      实际发生交易的日期
  买入股票      当日买入的股票列表（逗号分隔）
  买入股票数    当日买入的股票只数
  买入总额      当日买入总金额（含佣金/过户费）
  卖出股票      当日卖出的股票列表（逗号分隔）
  卖出股票数    当日卖出的股票只数
  卖出总额      当日卖出总金额（扣印花税/佣金/过户费）
  手续费        当日总手续费（含买卖佣金、过户费、印花税）
  毛利润        当日卖出毛利润（不含费用）
  净利润        当日卖出净利润（含所有费用）
  收益率%       当日净收益率
  累计净利润    截至当日的累计净利润

明细 CSV 字段：
  交易日期      实际发生交易的日期
  股票代码      股票代码
  操作          买入 / 卖出
  价格          成交价格（复权）
  股数          成交股数
  金额          含费用后金额（买入为成本，卖出为到手）
  手续费        该笔交易的手续费
  净利润        卖出时的净利润（买入行为空）

用法：
  python tests/sim_trade_ci.py \\
      --provider_uri=~/.qlib/qlib_data/cn_data \\
      --qlib_score_dir=./qlib_score_csv \\
      --out=./tests/sim_trade_result.csv \\
      --detail_out=./tests/sim_trade_detail.csv \\
      --top_n=10
"""

from __future__ import annotations

import os
import re
import sys
import subprocess
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd

# ──────────────────────────────────────────────
# 全局参数（A股费率）
# ──────────────────────────────────────────────
SHARES_PER_STOCK = 1_000      # 每只股票买入股数
COMMISSION_RATE  = 0.0003     # 佣金率 0.03%
MIN_COMMISSION   = 5.0        # 单边最低佣金（元）
STAMP_TAX_RATE   = 0.0005     # 印花税率 0.05%（仅卖出）
TRANSFER_RATE    = 0.00001    # 过户费率 0.001%（沪市双向）

# 持仓越久，要求越高，只买更强的信号。
SELECTION_RULES = {
    1: {
        "min_avg_score": 0.0,
        "min_pos_ratio": 0.55,
        "score_quantile": 0.75,
        "position_ratio": 1.0,
    },
    3: {
        "min_avg_score": 0.01,
        "min_pos_ratio": 0.70,
        "score_quantile": 0.82,
        "position_ratio": 0.6,
    },
    5: {
        "min_avg_score": 0.02,
        "min_pos_ratio": 0.80,
        "score_quantile": 0.88,
        "position_ratio": 0.4,
    },
}

STD20_CAP = 0.03
STD20_CAP_QUANTILE = 0.75
ROC10_FILTER_CAP = 1.12
ROC20_FILTER_CAP = 1.15
STD20_PENALTY_WEIGHT = 8
STD60_PENALTY_WEIGHT = 6
ROC10_PENALTY_START = 1.08
ROC20_PENALTY_START = 1.15
ROC10_PENALTY_WEIGHT = 6
ROC20_PENALTY_WEIGHT = 4
MIN_CONFIDENCE = 0.65
CONFIDENCE_RANGE = 0.35


# ──────────────────────────────────────────────
# 费用计算（与 roll/sim_trade.py 一致）
# ──────────────────────────────────────────────

def _commission(amount: float) -> float:
    """单边佣金，不低于 MIN_COMMISSION"""
    return max(amount * COMMISSION_RATE, MIN_COMMISSION)


def _transfer_fee(amount: float) -> float:
    """过户费"""
    return amount * TRANSFER_RATE


def buy_cost(price: float, shares: int) -> float:
    """买入成本 = 成交金额 + 佣金 + 过户费"""
    amount = price * shares
    return amount + _commission(amount) + _transfer_fee(amount)


def sell_revenue(price: float, shares: int) -> float:
    """卖出到手 = 成交金额 - 佣金 - 过户费 - 印花税"""
    amount = price * shares
    return amount - _commission(amount) - _transfer_fee(amount) - amount * STAMP_TAX_RATE


# ──────────────────────────────────────────────
# 交易日历（自包含，不依赖 roll/utils.py）
# ──────────────────────────────────────────────

class TradeDateCI:
    """
    管理交易日历，复刻 roll/utils.py 中 TradeDate 的核心逻辑。
    初始化时从 qlib 数据目录的 calendars/day.txt 读取，并自动用
    akshare 补充缺失的近期交易日。
    """

    def __init__(self, provider_uri: str):
        self.provider_uri = str(Path(provider_uri).expanduser())
        self.trade_date_file = os.path.join(self.provider_uri, "calendars", "day.txt")
        self.trade_date_list: list[str] = self._load_calendar()
        self._refresh_calendar_if_stale()

    def _load_calendar(self) -> list[str]:
        """从 day.txt 读取交易日列表"""
        p = Path(self.trade_date_file)
        if not p.exists():
            print(f"⚠️ 日历文件不存在: {p}")
            return []
        content = p.read_text(encoding="utf-8")
        dates = []
        for line in content.strip().split("\n"):
            line = line.strip()
            if line and len(line) >= 10:
                dates.append(line[:10])
        return dates

    def _refresh_calendar_if_stale(self):
        """如果本地日历落后最新已知交易日，用 akshare 补充"""
        try:
            if not self.trade_date_list:
                return
            latest_local = self.trade_date_list[-1]
            import akshare as ak
            trade_cal = ak.tool_trade_date_hist_sina()
            cutoff = datetime(2000, 1, 1).date()
            today = datetime.now().date()
            all_dates = sorted([
                str(d)[:10] for d in trade_cal["trade_date"].tolist()
                if cutoff <= datetime.strptime(str(d)[:10], "%Y-%m-%d").date() <= today
            ])
            # 只在本地日历确实缺少已发生的交易日时才补充
            if not all_dates or latest_local >= all_dates[-1]:
                return
            print(f"本地日历最新日期 {latest_local} 落后最新交易日 {all_dates[-1]}，补充中...")
            existing_set = set(self.trade_date_list)
            new_dates = [d for d in all_dates if d not in existing_set]
            if new_dates:
                merged = sorted(existing_set | set(all_dates))
                self.trade_date_list = merged
                try:
                    Path(self.trade_date_file).write_text(
                        "\n".join(merged) + "\n", encoding="utf-8"
                    )
                    print(f"日历补充完成，最新日期: {merged[-1]}，新增 {len(new_dates)} 条")
                except Exception as e:
                    print(f"写回日历文件失败（仅内存更新）: {e}")
        except Exception as e:
            print(f"日历补充失败，使用本地数据: {e}")

    def get_trade_date_list(self) -> list[str]:
        return self.trade_date_list

    def get_date_index(self, date: str) -> Optional[int]:
        try:
            return self.trade_date_list.index(date)
        except ValueError:
            return None

    def get_next_date(self, date: str, offset: int) -> Optional[str]:
        idx = self.get_date_index(date)
        if idx is None:
            return None
        target = idx + offset
        if target >= len(self.trade_date_list):
            return None
        return self.trade_date_list[target]


# ──────────────────────────────────────────────
# qlib 初始化 & 行情获取
# ──────────────────────────────────────────────

_qlib_initialized = False


def init_qlib(provider_uri: str):
    """延迟初始化 qlib，全局仅一次"""
    global _qlib_initialized
    if _qlib_initialized:
        return
    import qlib
    from qlib.constant import REG_CN
    qlib.init(provider_uri=provider_uri, region=REG_CN)
    _qlib_initialized = True
    print(f"qlib 已初始化，数据源: {provider_uri}")


def get_close_prices(instruments: list[str], date: str) -> dict[str, float]:
    """
    返回指定日期各股票的复权收盘价字典 {instrument: close_price}。
    与 roll/sim_trade.py 中 get_close_prices 逻辑一致。
    """
    from qlib.data import D
    if not instruments:
        return {}
    df = D.features(
        instruments,
        ["$close * $factor"],
        start_time=date,
        end_time=date,
        freq="day",
    )
    if df is None or df.empty:
        return {}
    df.columns = ["close"]
    df = df.reset_index()
    result: dict[str, float] = {}
    for _, row in df.iterrows():
        result[row["instrument"]] = float(row["close"])
    return result


# ──────────────────────────────────────────────
# 扫描 qlib_score_csv 目录
# ──────────────────────────────────────────────

def get_score_subdirs(qlib_score_dir: Path) -> Optional[list[Path]]:
    """扫描 qlib_score_csv 下的 selection_* 子目录，按日期升序排列。
    同一日期如有多个目录，仅保留最新（目录名时间戳最大）的那个。"""
    if not qlib_score_dir.exists():
        print(f"⚠️ 目录不存在: {qlib_score_dir}")
        return None
    subdirs = [d for d in qlib_score_dir.iterdir() if d.is_dir()]
    if not subdirs:
        return None

    def _extract_date(subdir: Path) -> str:
        m = re.match(r"selection_(\d{8})_", subdir.name)
        return m.group(1) if m else ""

    # 按目录名排序（同日期的多个目录按时间戳升序），同日期保留最后一个（最新）
    subdirs_sorted = sorted(subdirs, key=lambda d: d.name)
    date_to_subdir: dict[str, Path] = {}
    for d in subdirs_sorted:
        date_key = _extract_date(d)
        if date_key:
            date_to_subdir[date_key] = d  # 同日期后出现的覆盖前者

    return sorted(date_to_subdir.values(), key=_extract_date)


def extract_date_from_csv(subdir: Path) -> Optional[str]:
    """从子目录中的 CSV 文件名提取日期 YYYY-MM-DD"""
    for f in subdir.iterdir():
        m = re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", f.name)
        if m:
            return m.group(1)
    return None


def _get_selection_rule(hold_days: int) -> dict[str, float]:
    rule = SELECTION_RULES.get(hold_days)
    if rule is not None:
        return rule
    if hold_days <= 1:
        return SELECTION_RULES[1]
    if hold_days <= 3:
        return SELECTION_RULES[3]
    return SELECTION_RULES[5]


def select_trade_candidates(
    df: pd.DataFrame,
    top_n: int,
    hold_days: int,
) -> pd.DataFrame:
    """
    根据预测分数、正向一致率和风险因子挑选待买入股票。
    `top_n` 为上限，弱信号日期可以少买或不买。
    """
    if df.empty or top_n <= 0:
        return df.iloc[0:0].copy()

    rule = _get_selection_rule(hold_days)
    ranked = df.copy()
    ranked = ranked.dropna(subset=["instrument", "avg_score"]).copy()
    if ranked.empty:
        return ranked

    ranked["avg_score"] = pd.to_numeric(ranked["avg_score"], errors="coerce")
    pos_ratio = (
        pd.to_numeric(ranked["pos_ratio"], errors="coerce")
        if "pos_ratio" in ranked.columns
        else pd.Series(0.5, index=ranked.index, dtype=float)
    )
    ranked["pos_ratio"] = pos_ratio.fillna(0.5)
    ranked = ranked.dropna(subset=["avg_score"])
    if ranked.empty:
        return ranked

    ranked = ranked[ranked["avg_score"] > 0].copy()
    if ranked.empty:
        return ranked

    ranked = ranked[ranked["pos_ratio"] >= rule["min_pos_ratio"]].copy()
    if ranked.empty:
        return ranked

    score_floor = max(
        rule["min_avg_score"],
        float(ranked["avg_score"].quantile(rule["score_quantile"])),
    )
    ranked["is_preferred"] = ranked["avg_score"] >= score_floor

    if "STD20" in ranked.columns:
        ranked["STD20"] = pd.to_numeric(ranked["STD20"], errors="coerce").fillna(0.0)
        std20_quantile = ranked["STD20"].quantile(STD20_CAP_QUANTILE)
        std20_cap = (
            STD20_CAP
            if pd.isna(std20_quantile)
            else min(STD20_CAP, float(std20_quantile))
        )
        ranked = ranked[ranked["STD20"] <= std20_cap].copy()
    else:
        ranked["STD20"] = 0.0

    if "STD60" in ranked.columns:
        ranked["STD60"] = pd.to_numeric(ranked["STD60"], errors="coerce").fillna(0.0)
    else:
        ranked["STD60"] = 0.0

    if "ROC10" in ranked.columns:
        ranked["ROC10"] = pd.to_numeric(ranked["ROC10"], errors="coerce").fillna(1.0)
        ranked = ranked[ranked["ROC10"] <= ROC10_FILTER_CAP].copy()
    else:
        ranked["ROC10"] = 1.0

    if "ROC20" in ranked.columns:
        ranked["ROC20"] = pd.to_numeric(ranked["ROC20"], errors="coerce").fillna(1.0)
        ranked = ranked[ranked["ROC20"] <= ROC20_FILTER_CAP].copy()
    else:
        ranked["ROC20"] = 1.0

    if ranked.empty:
        return ranked

    # 短期波动直接影响次日/短持有策略，因此给 STD20 更高权重。
    # STD20_PENALTY_WEIGHT / STD60_PENALTY_WEIGHT 仅做温和惩罚，避免过度放大。
    risk_penalty = (
        1
        + ranked["STD20"].clip(lower=0) * STD20_PENALTY_WEIGHT
        + ranked["STD60"].clip(lower=0) * STD60_PENALTY_WEIGHT
    )
    chase_penalty = (
        1
        # ROC10 > ROC10_PENALTY_START、ROC20 > ROC20_PENALTY_START 说明短期涨幅已偏高。
        # ROC10_PENALTY_WEIGHT / ROC20_PENALTY_WEIGHT 保持“抑制追涨”，但不至于完全抹掉高质量信号。
        + (ranked["ROC10"] - ROC10_PENALTY_START).clip(lower=0) * ROC10_PENALTY_WEIGHT
        + (ranked["ROC20"] - ROC20_PENALTY_START).clip(lower=0) * ROC20_PENALTY_WEIGHT
    )
    # pos_ratio 只做置信度加权，不完全主导排序。
    # 最低 MIN_CONFIDENCE、最高 MIN_CONFIDENCE + CONFIDENCE_RANGE，避免单一指标把高分股完全挤掉。
    confidence = MIN_CONFIDENCE + ranked["pos_ratio"] * CONFIDENCE_RANGE
    ranked["trade_score"] = ranked["avg_score"] * confidence / risk_penalty / chase_penalty

    max_positions = math.ceil(top_n * rule["position_ratio"])
    max_positions = max(1, max_positions)
    ranked = ranked.sort_values(
        by=["trade_score", "avg_score", "pos_ratio"],
        ascending=False,
    )

    preferred = ranked[ranked["is_preferred"]]
    if len(preferred) >= max_positions:
        return preferred.head(max_positions)

    selected = preferred.copy()
    missing = max_positions - len(selected)
    if missing > 0:
        selected = pd.concat(
            [selected, ranked[~ranked.index.isin(selected.index)].head(missing)]
        )
    return selected.head(max_positions)


# ──────────────────────────────────────────────
# 核心：单日模拟交易
# ──────────────────────────────────────────────

def simulate_one_day(
    subdir: Path,
    trade_date: TradeDateCI,
    top_n: int,
    hold_days: int = 1,
) -> Optional[dict]:
    """
    处理一个 selection 子目录，返回当日模拟交易结果字典。
    无法处理时返回 None。

    参数：
      hold_days  持仓天数（T日买入后持有的交易日数）
                 1 = T日买T+1卖（默认），3 = T日买T+3卖，5 = T日买T+5卖
    """
    date_str = extract_date_from_csv(subdir)
    if not date_str:
        print(f"[{subdir.name}] 未找到日期 CSV，跳过")
        return None

    idx = trade_date.get_date_index(date_str)
    if idx is None:
        print(f"[{date_str}] 不在交易日历中，跳过")
        return None

    sell_offset = 1 + hold_days  # 从预测日算起的卖出偏移
    trade_list = trade_date.get_trade_date_list()
    if idx + sell_offset >= len(trade_list):
        print(f"[{date_str}] T+1/T+{1 + hold_days} 尚未到来，跳过")
        return None

    buy_date = trade_date.get_next_date(date_str, 1)
    sell_date = trade_date.get_next_date(date_str, sell_offset)

    # 读取 filter_ret.csv
    filter_csv = subdir / f"{date_str}_filter_ret.csv"
    if not filter_csv.exists():
        print(f"[{date_str}] 缺少 filter_ret.csv，跳过")
        return None

    df = pd.read_csv(filter_csv)

    # 截掉 KMID 及右侧（与原始 review 逻辑一致）
    if "KMID" in df.columns:
        kmid_idx = df.columns.get_loc("KMID")
        df = df.iloc[:, :kmid_idx]

    if "avg_score" not in df.columns or "instrument" not in df.columns:
        print(f"[{date_str}] filter_ret.csv 缺少必要列(avg_score/instrument)，跳过")
        return None

    # 只买高置信度且风险更低的股票；top_n 作为上限
    top_df = select_trade_candidates(df, top_n=top_n, hold_days=hold_days)
    if top_df.empty:
        print(f"[{date_str}] 无满足高置信度条件的股票，跳过")
        return None

    instruments = top_df["instrument"].tolist()

    # 获取买入日（T+1）和卖出日收盘价
    buy_prices = get_close_prices(instruments, buy_date)
    sell_prices = get_close_prices(instruments, sell_date)

    if not buy_prices or not sell_prices:
        print(f"[{date_str}] 行情数据不足（买入日={buy_date}, 卖出日={sell_date}），跳过")
        return None

    # 只保留两日均有行情的股票
    valid_instruments = [i for i in instruments if i in buy_prices and i in sell_prices]
    if not valid_instruments:
        print(f"[{date_str}] 无有效股票行情，跳过")
        return None

    total_buy = 0.0
    total_sell = 0.0
    total_gross = 0.0
    total_fee = 0.0
    detail_rows: list[dict] = []

    for inst in valid_instruments:
        bp = buy_prices[inst]
        sp = sell_prices[inst]
        buy_amount = bp * SHARES_PER_STOCK
        sell_amount = sp * SHARES_PER_STOCK
        bc = buy_cost(bp, SHARES_PER_STOCK)
        sr = sell_revenue(sp, SHARES_PER_STOCK)
        buy_fee = bc - buy_amount          # 买入手续费
        sell_fee = sell_amount - sr         # 卖出手续费
        fee = round(buy_fee + sell_fee, 2)  # 单只股票总手续费
        gross = (sp - bp) * SHARES_PER_STOCK
        net = sr - bc
        detail_rows.append({
            "instrument": inst,
            "buy_price":  round(bp, 4),
            "sell_price": round(sp, 4),
            "shares":     SHARES_PER_STOCK,
            "buy_cost":   round(bc, 2),
            "sell_revenue": round(sr, 2),
            "fee":        fee,
            "gross_profit": round(gross, 2),
            "net_profit":   round(net, 2),
        })
        total_buy += bc
        total_sell += sr
        total_gross += gross
        total_fee += fee

    net_profit = total_sell - total_buy
    return_pct = net_profit / total_buy * 100 if total_buy else 0.0

    return {
        "date_T":       date_str,
        "date_buy":     buy_date,
        "date_sell":    sell_date,
        "instruments":  ",".join(valid_instruments),
        "stock_count":  len(valid_instruments),
        "buy_total":    round(total_buy, 2),
        "sell_total":   round(total_sell, 2),
        "total_fee":    round(total_fee, 2),
        "gross_profit": round(total_gross, 2),
        "net_profit":   round(net_profit, 2),
        "return_pct":   round(return_pct, 4),
        "_detail":      detail_rows,
    }


# ──────────────────────────────────────────────
# 主流程
# ──────────────────────────────────────────────

def _run_one_mode(
    hold_days: int,
    subdirs: list[Path],
    trade_date: TradeDateCI,
    top_n: int,
    out_path: Path,
    det_path: Path,
):
    """
    运行单种持仓模式的模拟交易并输出 CSV。

    参数：
      hold_days  持仓天数（1/3/5）
      subdirs    预测目录列表
      trade_date 交易日历对象
      top_n      每日买入股票数量
      out_path   汇总 CSV 输出路径
      det_path   明细 CSV 输出路径
    """
    mode_label = f"T日买T+{hold_days}日卖"
    print(f"\n{'='*50}")
    print(f"开始模拟交易模式: {mode_label}  (hold_days={hold_days})")
    print(f"{'='*50}")

    # ── 第一步：收集所有预测周期的模拟结果 ──
    all_results: list[dict] = []
    for subdir in subdirs:
        result = simulate_one_day(subdir, trade_date, top_n, hold_days=hold_days)
        if result is not None:
            all_results.append(result)

    if not all_results:
        print(f"[{mode_label}] 没有可输出的结果（数据不足或行情尚未就绪）。")
        return

    # ── 第二步：按实际交易日期重组数据 ──
    buy_on_date: dict[str, list[dict]] = defaultdict(list)
    sell_on_date: dict[str, list[dict]] = defaultdict(list)

    for result in all_results:
        buy_date = result["date_buy"]
        sell_date = result["date_sell"]
        instruments = result["instruments"].split(",")

        buy_on_date[buy_date].append({
            "instruments": instruments,
            "buy_total": result["buy_total"],
            "details": result["_detail"],
        })

        sell_on_date[sell_date].append({
            "instruments": instruments,
            "sell_total": result["sell_total"],
            "buy_total_for_sold": result["buy_total"],
            "total_fee": result["total_fee"],
            "gross_profit": result["gross_profit"],
            "net_profit": result["net_profit"],
            "details": result["_detail"],
        })

    # 获取所有实际交易日期并排序
    all_trade_dates = sorted(set(list(buy_on_date.keys()) + list(sell_on_date.keys())))

    # ── 第三步：构建汇总 CSV（每行 = 一个交易日） ──
    summary_rows: list[dict] = []
    detail_rows: list[dict] = []
    cum_profit = 0.0

    for date in all_trade_dates:
        buys = buy_on_date.get(date, [])
        sells = sell_on_date.get(date, [])

        # 聚合当日买入
        buy_instruments: list[str] = []
        day_buy_total = 0.0
        for b in buys:
            buy_instruments.extend(b["instruments"])
            day_buy_total += b["buy_total"]
            # 明细：买入操作
            for d in b["details"]:
                buy_amount = d["buy_price"] * d["shares"]
                buy_fee = round(d["buy_cost"] - buy_amount, 2)
                detail_rows.append({
                    "交易日期": date,
                    "股票代码": d["instrument"],
                    "操作": "买入",
                    "价格": d["buy_price"],
                    "股数": d["shares"],
                    "金额": d["buy_cost"],
                    "手续费": buy_fee,
                    "净利润": "",
                })

        # 聚合当日卖出
        sell_instruments: list[str] = []
        day_sell_total = 0.0
        day_sell_buy_cost = 0.0
        day_gross_profit = 0.0
        day_net_profit = 0.0
        day_total_fee = 0.0
        for s in sells:
            sell_instruments.extend(s["instruments"])
            day_sell_total += s["sell_total"]
            day_sell_buy_cost += s["buy_total_for_sold"]
            day_gross_profit += s["gross_profit"]
            day_net_profit += s["net_profit"]
            day_total_fee += s["total_fee"]
            # 明细：卖出操作
            for d in s["details"]:
                sell_amount = d["sell_price"] * d["shares"]
                sell_fee = round(sell_amount - d["sell_revenue"], 2)
                detail_rows.append({
                    "交易日期": date,
                    "股票代码": d["instrument"],
                    "操作": "卖出",
                    "价格": d["sell_price"],
                    "股数": d["shares"],
                    "金额": d["sell_revenue"],
                    "手续费": sell_fee,
                    "净利润": d["net_profit"],
                })

        cum_profit += day_net_profit
        return_pct = day_net_profit / day_sell_buy_cost * 100 if day_sell_buy_cost else 0.0

        summary_rows.append({
            "交易日期": date,
            "买入股票": ",".join(buy_instruments) if buy_instruments else "",
            "买入股票数": len(buy_instruments),
            "买入总额": round(day_buy_total, 2),
            "卖出股票": ",".join(sell_instruments) if sell_instruments else "",
            "卖出股票数": len(sell_instruments),
            "卖出总额": round(day_sell_total, 2),
            "手续费": round(day_total_fee, 2),
            "毛利润": round(day_gross_profit, 2),
            "净利润": round(day_net_profit, 2),
            "收益率%": round(return_pct, 4),
            "累计净利润": round(cum_profit, 2),
        })

        action_desc = []
        if buy_instruments:
            action_desc.append(f"买入{len(buy_instruments)}只")
        if sell_instruments:
            action_desc.append(f"卖出{len(sell_instruments)}只")
        print(
            f"[{date}] {'/'.join(action_desc)}  "
            f"净利润={day_net_profit:.2f}  累计={cum_profit:.2f}"
        )

    # ── 第四步：输出 CSV ──
    # 汇总 CSV
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_summary = pd.DataFrame(summary_rows, columns=[
        "交易日期", "买入股票", "买入股票数", "买入总额",
        "卖出股票", "卖出股票数", "卖出总额",
        "手续费", "毛利润", "净利润", "收益率%", "累计净利润",
    ])
    df_summary.to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"[{mode_label}] 汇总结果已保存: {out_path}  ({len(df_summary)} 行)")

    # 明细 CSV
    det_path.parent.mkdir(parents=True, exist_ok=True)
    df_detail = pd.DataFrame(detail_rows, columns=[
        "交易日期", "股票代码", "操作", "价格", "股数", "金额", "手续费", "净利润",
    ])
    df_detail.to_csv(det_path, index=False, encoding="utf-8-sig")
    print(f"[{mode_label}] 明细结果已保存: {det_path}  ({len(df_detail)} 行)")

    # 打印统计摘要
    total_net = df_summary["净利润"].sum()
    sell_days = int((df_summary["卖出股票数"] > 0).sum())
    total_days = len(df_summary)
    win_days = int((df_summary["净利润"] > 0).sum())
    win_pct = f"{win_days / sell_days * 100:.1f}%" if sell_days else "N/A"
    avg_net = f"{total_net / sell_days:.2f}" if sell_days else "N/A"
    print(
        f"\n=== 模拟交易统计 [{mode_label}] ===\n"
        f"  交易天数:  {total_days}\n"
        f"  含卖出天数: {sell_days}\n"
        f"  盈利天数:  {win_days} ({win_pct} of sell days)\n"
        f"  累计净利润: {total_net:.2f}\n"
        f"  平均日净利润: {avg_net}\n"
        f"==================="
    )


def main(
    provider_uri: str = "~/.qlib/qlib_data/cn_data",
    qlib_score_dir: str = "./qlib_score_csv",
    top_n: int = 3,
    out: str = "./tests/sim_trade_result.csv",
    detail_out: str = "./tests/sim_trade_detail.csv",
):
    """
    模拟交易主入口。支持 3 种持仓模式，分别输出 CSV：
      - T日买T+1日卖（hold_days=1）
      - T日买T+3日卖（hold_days=3）
      - T日买T+5日卖（hold_days=5）

    参数：
      provider_uri    qlib 数据目录路径
      qlib_score_dir  qlib_score_csv 目录路径（含 selection_* 子目录）
      top_n           每日买入股票数量（默认 10）
      out             汇总结果 CSV 输出路径（T+1 模式基准名，T+3/T+5 自动加后缀）
      detail_out      明细结果 CSV 输出路径（T+1 模式基准名，T+3/T+5 自动加后缀）
    """
    provider_uri = str(Path(provider_uri).expanduser())

    print(f"初始化 qlib... (provider_uri={provider_uri})")
    init_qlib(provider_uri)

    trade_date = TradeDateCI(provider_uri)

    score_dir = Path(qlib_score_dir)
    if not score_dir.is_absolute():
        score_dir = Path.cwd() / qlib_score_dir

    subdirs = get_score_subdirs(score_dir)
    if not subdirs:
        print("未找到任何 selection 子目录，退出。")
        return

    print(f"共发现 {len(subdirs)} 个预测目录，开始模拟交易（top_n={top_n}）...")

    # 3 种持仓模式：T日买T+1卖、T日买T+3卖、T日买T+5卖
    hold_days_list = [1, 3, 5]

    out_base = Path(out)
    det_base = Path(detail_out)

    for hold_days in hold_days_list:
        # 构造输出文件名：T+1 使用原始名，T+3/T+5 加后缀
        if hold_days == 1:
            out_path = out_base
            det_path = det_base
        else:
            out_path = out_base.with_stem(f"{out_base.stem}_t{hold_days}")
            det_path = det_base.with_stem(f"{det_base.stem}_t{hold_days}")

        _run_one_mode(
            hold_days=hold_days,
            subdirs=subdirs,
            trade_date=trade_date,
            top_n=top_n,
            out_path=out_path,
            det_path=det_path,
        )


if __name__ == "__main__":
    import fire
    fire.Fire(main)
