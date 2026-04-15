#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟交易 CI 版 v2 —— 测试 pick_top_stocks.py 综合评分选股效果
================================================================
基于 sim_trade_ci.py 的交易模拟框架，将选股策略替换为
pick_top_stocks.py 中的 5 维综合评分（预测分数 35% + 模型一致性 25%
+ 低波动率 15% + 趋势动量 15% + 量价配合 10%），并与原始
avg_score 排名策略做对比回测。

输出：
  1. composite 策略的汇总 CSV + 明细 CSV
  2. baseline（纯 avg_score）策略的汇总 CSV + 明细 CSV
  3. 终端打印两种策略的逐日对比表 + 累计收益对比

用法：
  python tests/sim_trade_ci2.py \
      --provider_uri=~/.qlib/qlib_data/cn_data \
      --qlib_score_dir=./qlib_score_csv \
      --out=./tests/sim_trade_result_v2.csv \
      --detail_out=./tests/sim_trade_detail_v2.csv \
      --top_n=5
"""

from __future__ import annotations

import os
import re
import sys
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

# ──────────────────────────────────────────────────────────────────────
# 全局参数（A股费率，与 sim_trade_ci.py 保持一致）
# ──────────────────────────────────────────────────────────────────────
SHARES_PER_STOCK = 1_000       # 每只股票买入股数
COMMISSION_RATE  = 0.0003      # 佣金率 0.03%
MIN_COMMISSION   = 5.0         # 单边最低佣金（元）
STAMP_TAX_RATE   = 0.0005      # 印花税率 0.05%（仅卖出）
TRANSFER_RATE    = 0.00001     # 过户费率 0.001%（沪市双向）

# ──────────────────────────────────────────────────────────────────────
# 综合评分权重（与 pick_top_stocks.py 一致）
# ──────────────────────────────────────────────────────────────────────
WEIGHT_AVG_SCORE = 0.35
WEIGHT_POS_RATIO = 0.25
WEIGHT_LOW_VOL   = 0.15
WEIGHT_TREND     = 0.15
WEIGHT_VWAP      = 0.10

MIN_AVG_SCORE  = 0.0   # 基础过滤：avg_score > 0
MIN_POS_RATIO  = 0.5   # 基础过滤：pos_ratio >= 0.5


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 费用计算（复制自 sim_trade_ci.py）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 交易日历（自包含，复制自 sim_trade_ci.py）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class TradeDateCI:
    """管理交易日历，从 qlib 数据目录读取并用 akshare 补充"""

    def __init__(self, provider_uri: str):
        self.provider_uri = str(Path(provider_uri).expanduser())
        self.trade_date_file = os.path.join(self.provider_uri, "calendars", "day.txt")
        self.trade_date_list: list[str] = self._load_calendar()
        self._refresh_calendar_if_stale()

    def _load_calendar(self) -> list[str]:
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
            if not all_dates or latest_local >= all_dates[-1]:
                return
            new_dates = [d for d in all_dates if d > latest_local]
            if new_dates:
                self.trade_date_list.extend(new_dates)
                self.trade_date_list = sorted(set(self.trade_date_list))
                print(f"日历已补充 {len(new_dates)} 个交易日 (至 {self.trade_date_list[-1]})")
        except Exception as e:
            print(f"⚠️ 日历刷新失败: {e}")

    def get_date_index(self, date_str: str) -> Optional[int]:
        try:
            return self.trade_date_list.index(date_str)
        except ValueError:
            return None

    def get_next_trade_date(self, date_str: str, offset: int = 1) -> Optional[str]:
        idx = self.get_date_index(date_str)
        if idx is None:
            return None
        target = idx + offset
        if 0 <= target < len(self.trade_date_list):
            return self.trade_date_list[target]
        return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# qlib 初始化与获取收盘价（复制自 sim_trade_ci.py）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_qlib_inited = False

def init_qlib(provider_uri: str):
    global _qlib_inited
    if _qlib_inited:
        return
    try:
        import qlib
        from qlib.constant import REG_CN
        qlib.init(provider_uri=provider_uri, region=REG_CN)
        _qlib_inited = True
    except Exception as e:
        print(f"⚠️ qlib 初始化失败: {e}，将使用 akshare 获取价格")


def get_stock_price(instrument: str, date_str: str) -> Optional[float]:
    """
    获取指定股票在指定日期的收盘价（复权）。
    优先用 qlib D.features()，失败则用 akshare。
    """
    # 尝试 qlib
    try:
        from qlib.data import D
        df = D.features(
            [instrument],
            ["$close"],
            start_time=date_str,
            end_time=date_str,
        )
        if not df.empty:
            return float(df.iloc[0, 0])
    except Exception:
        pass

    # 尝试 akshare
    try:
        import akshare as ak
        code = re.sub(r"^(SH|SZ|BJ)", "", instrument)
        df = ak.stock_zh_a_hist(
            symbol=code,
            period="daily",
            start_date=date_str.replace("-", ""),
            end_date=date_str.replace("-", ""),
            adjust="qfq",
        )
        if not df.empty:
            return float(df.iloc[0]["收盘"])
    except Exception:
        pass

    return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 综合评分选股（复制自 pick_top_stocks.py 核心逻辑）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _normalize_minmax(series: pd.Series) -> pd.Series:
    """Min-Max 归一化到 [0, 1]；若所有值相同则返回 0.5"""
    mn, mx = series.min(), series.max()
    if mx - mn < 1e-12:
        return pd.Series(0.5, index=series.index)
    return (series - mn) / (mx - mn)


def _score_volatility(df: pd.DataFrame) -> pd.Series:
    """低波动率得分：STD 越低得分越高"""
    cols = [c for c in ["STD5", "STD20", "STD60"] if c in df.columns]
    if not cols:
        return pd.Series(0.5, index=df.index)
    avg_std = df[cols].mean(axis=1)
    return 1.0 - _normalize_minmax(avg_std)


def _score_trend(df: pd.DataFrame) -> pd.Series:
    """趋势动量得分：ROC 短>长 + 均线多头排列"""
    scores = pd.Series(0.0, index=df.index)
    for short, long_ in [("ROC5", "ROC10"), ("ROC10", "ROC20"), ("ROC20", "ROC30")]:
        if short in df.columns and long_ in df.columns:
            scores += (df[short] > df[long_]).astype(float)
    for short, long_ in [("MA5", "MA10"), ("MA10", "MA20")]:
        if short in df.columns and long_ in df.columns:
            scores += (df[short] > df[long_]).astype(float)
    return _normalize_minmax(scores)


def _score_vwap(df: pd.DataFrame) -> pd.Series:
    """量价配合得分：VWAP0 >= OPEN0 时得分高"""
    if "VWAP0" not in df.columns or "OPEN0" not in df.columns:
        return pd.Series(0.5, index=df.index)
    open0 = df["OPEN0"].replace(0, np.nan)
    ratio = (df["VWAP0"] - open0) / open0.abs()
    return _normalize_minmax(ratio.fillna(0.0))


def compute_composite_score(df: pd.DataFrame) -> pd.DataFrame:
    """计算 5 维综合评分，新增 composite_score 列"""
    result = df.copy()
    result["score_avg_score"] = _normalize_minmax(result["avg_score"])
    result["score_pos_ratio"] = _normalize_minmax(
        result["pos_ratio"] if "pos_ratio" in result.columns
        else pd.Series(0.5, index=result.index)
    )
    result["score_low_vol"] = _score_volatility(result)
    result["score_trend"]   = _score_trend(result)
    result["score_vwap"]    = _score_vwap(result)

    result["composite_score"] = (
        result["score_avg_score"] * WEIGHT_AVG_SCORE
        + result["score_pos_ratio"] * WEIGHT_POS_RATIO
        + result["score_low_vol"]   * WEIGHT_LOW_VOL
        + result["score_trend"]     * WEIGHT_TREND
        + result["score_vwap"]      * WEIGHT_VWAP
    )
    return result


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 两种选股策略
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def select_baseline(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """基线策略：纯按 avg_score 从高到低排序取 top_n"""
    if df.empty or top_n <= 0:
        return df.iloc[0:0].copy()
    ranked = df.dropna(subset=["instrument", "avg_score"]).copy()
    ranked["avg_score"] = pd.to_numeric(ranked["avg_score"], errors="coerce")
    ranked = ranked.dropna(subset=["avg_score"])
    ranked = ranked.sort_values("avg_score", ascending=False)
    return ranked.head(top_n)


def select_composite(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """综合评分策略：基础过滤 + 5 维打分排序取 top_n"""
    if df.empty or top_n <= 0:
        return df.iloc[0:0].copy()

    ranked = df.dropna(subset=["instrument", "avg_score"]).copy()
    ranked["avg_score"] = pd.to_numeric(ranked["avg_score"], errors="coerce")
    ranked = ranked.dropna(subset=["avg_score"])

    # 基础过滤
    mask = ranked["avg_score"] > MIN_AVG_SCORE
    if "pos_ratio" in ranked.columns:
        ranked["pos_ratio"] = pd.to_numeric(ranked["pos_ratio"], errors="coerce")
        mask = mask & (ranked["pos_ratio"].fillna(0) >= MIN_POS_RATIO)
    ranked = ranked[mask].copy()

    if ranked.empty:
        # 过滤太严则退化为 baseline
        return select_baseline(df, top_n)

    scored = compute_composite_score(ranked)
    scored = scored.sort_values("composite_score", ascending=False)
    return scored.head(top_n)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 目录扫描
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_score_subdirs(score_dir: Path) -> list[Path]:
    """扫描 qlib_score_csv 下 selection_* 子目录，按日期去重后排序"""
    subdirs = [d for d in score_dir.iterdir()
               if d.is_dir() and d.name.startswith("selection_")]
    if not subdirs:
        return []

    def _extract_date(subdir: Path) -> str:
        m = re.match(r"selection_(\d{8})_", subdir.name)
        return m.group(1) if m else ""

    subdirs_sorted = sorted(subdirs, key=lambda d: d.name)
    date_to_subdir: dict[str, Path] = {}
    for d in subdirs_sorted:
        date_key = _extract_date(d)
        if date_key:
            date_to_subdir[date_key] = d
    return sorted(date_to_subdir.values(), key=_extract_date)


def extract_date_from_csv(subdir: Path) -> Optional[str]:
    """从子目录中的 CSV 文件名提取日期 YYYY-MM-DD"""
    for f in subdir.iterdir():
        m = re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", f.name)
        if m:
            return m.group(1)
    return None


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 核心：单日模拟交易
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def simulate_one_day(
    subdir: Path,
    trade_date: TradeDateCI,
    top_n: int,
    hold_days: int = 1,
    buy_offset: int = 0,
    strategy: str = "composite",
    use_filter_ret: bool = True,
) -> Optional[dict]:
    """
    处理一个 selection 子目录，返回当日模拟交易结果字典。

    参数：
      strategy      "composite" 使用综合评分，"baseline" 使用纯 avg_score
      use_filter_ret True 优先用 filter_ret.csv，False 用 ret.csv
      hold_days     持仓天数（买入后持有的交易日数）
      buy_offset    买入偏移，0 = T日买入，1 = T+1日买入
    """
    date_str = extract_date_from_csv(subdir)
    if not date_str:
        return None

    idx = trade_date.get_date_index(date_str)
    if idx is None:
        return None

    # T+buy_offset 买入日，T+buy_offset+hold_days 卖出日
    buy_date = date_str if buy_offset == 0 else trade_date.get_next_trade_date(date_str, offset=buy_offset)
    sell_date = trade_date.get_next_trade_date(date_str, offset=buy_offset + hold_days)
    if not buy_date or not sell_date:
        return None

    # 读取 CSV：优先 filter_ret，退而求其次 ret
    csv_path = None
    if use_filter_ret:
        for f in subdir.glob("*_filter_ret.csv"):
            csv_path = f
            break
    if csv_path is None:
        for f in subdir.glob("*_ret.csv"):
            if "filter" not in f.name:
                csv_path = f
                break
    if csv_path is None:
        return None

    try:
        df = pd.read_csv(csv_path)
    except Exception:
        return None

    if df.empty or "instrument" not in df.columns or "avg_score" not in df.columns:
        return None

    # 选股
    if strategy == "composite":
        selected = select_composite(df, top_n)
    else:
        selected = select_baseline(df, top_n)

    if selected.empty:
        return None

    instruments = selected["instrument"].tolist()

    # 模拟买卖
    total_buy_cost = 0.0
    total_sell_rev = 0.0
    total_fee = 0.0
    buy_list = []
    sell_list = []
    detail_rows = []

    for inst in instruments:
        bp = get_stock_price(inst, buy_date)
        sp = get_stock_price(inst, sell_date)
        if bp is None or sp is None or bp <= 0:
            continue

        cost = buy_cost(bp, SHARES_PER_STOCK)
        rev = sell_revenue(sp, SHARES_PER_STOCK)
        fee = cost - bp * SHARES_PER_STOCK + sp * SHARES_PER_STOCK - rev
        gross = (sp - bp) * SHARES_PER_STOCK
        net = rev - cost

        total_buy_cost += cost
        total_sell_rev += rev
        total_fee += fee

        buy_list.append(inst)
        sell_list.append(inst)

        # 买入明细
        detail_rows.append({
            "交易日期": buy_date,
            "股票代码": inst,
            "操作": "买入",
            "价格": round(bp, 4),
            "股数": SHARES_PER_STOCK,
            "金额": round(cost, 2),
            "手续费": round(cost - bp * SHARES_PER_STOCK, 2),
            "净利润": "",
            "策略": strategy,
        })
        # 卖出明细
        detail_rows.append({
            "交易日期": sell_date,
            "股票代码": inst,
            "操作": "卖出",
            "价格": round(sp, 4),
            "股数": SHARES_PER_STOCK,
            "金额": round(rev, 2),
            "手续费": round(sp * SHARES_PER_STOCK - rev, 2),
            "净利润": round(net, 2),
            "策略": strategy,
        })

    if not buy_list:
        return None

    # 净利润 = 卖出到手 - 买入成本
    net_profit = total_sell_rev - total_buy_cost
    pct = (net_profit / total_buy_cost * 100) if total_buy_cost > 0 else 0.0

    return {
        "预测日期": date_str,
        "买入日期": buy_date,
        "卖出日期": sell_date,
        "持仓天数": hold_days,
        "策略": strategy,
        "买入股票": ",".join(buy_list),
        "买入股票数": len(buy_list),
        "买入总额": round(total_buy_cost, 2),
        "卖出总额": round(total_sell_rev, 2),
        "手续费": round(total_fee, 2),
        "净利润": round(net_profit, 2),
        "收益率%": round(pct, 4),
        "_detail_rows": detail_rows,
    }


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 单策略回测
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _run_one_strategy(
    strategy: str,
    hold_days: int,
    subdirs: list[Path],
    trade_date: TradeDateCI,
    top_n: int,
    buy_offset: int = 0,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """运行单个策略，返回 (汇总df, 明细df)"""
    summary_rows = []
    all_detail = []
    cum_net = 0.0

    for subdir in subdirs:
        result = simulate_one_day(
            subdir, trade_date, top_n,
            hold_days=hold_days,
            buy_offset=buy_offset,
            strategy=strategy,
        )
        if result is None:
            continue

        all_detail.extend(result.pop("_detail_rows", []))
        cum_net += result["净利润"]
        result["累计净利润"] = round(cum_net, 2)
        summary_rows.append(result)

    df_summary = pd.DataFrame(summary_rows) if summary_rows else pd.DataFrame()
    df_detail = pd.DataFrame(all_detail) if all_detail else pd.DataFrame()
    return df_summary, df_detail


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 对比报告
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def print_comparison(
    df_composite: pd.DataFrame,
    df_baseline: pd.DataFrame,
    hold_days: int,
):
    """终端打印两种策略的对比结果"""
    sep = "=" * 90
    print(f"\n{sep}")
    print(f"  📊 策略对比报告 —— 持仓 {hold_days} 天模式")
    print(sep)

    for label, df in [("🔵 综合评分策略 (composite)", df_composite),
                      ("🔴 纯分数策略 (baseline)", df_baseline)]:
        if df.empty:
            print(f"\n  {label}: 无交易数据\n")
            continue

        total_days = len(df)
        win_days = df[df["净利润"] > 0].shape[0]
        loss_days = df[df["净利润"] < 0].shape[0]
        total_net = df["净利润"].sum()
        avg_pct = df["收益率%"].mean()
        max_win = df["净利润"].max()
        max_loss = df["净利润"].min()
        win_rate = f"{win_days/total_days*100:.1f}%" if total_days > 0 else "N/A"

        print(f"\n  {label}")
        print(f"  {'─' * 40}")
        print(f"  交易天数:     {total_days}")
        print(f"  盈利天数:     {win_days} ({win_rate})")
        print(f"  亏损天数:     {loss_days}")
        print(f"  累计净利润:   {total_net:,.2f} 元")
        print(f"  平均日收益率: {avg_pct:.4f}%")
        print(f"  单日最大盈利: {max_win:,.2f} 元")
        print(f"  单日最大亏损: {max_loss:,.2f} 元")

    # 逐日对比表
    if not df_composite.empty and not df_baseline.empty:
        print(f"\n{'─' * 90}")
        print("  逐日对比：")
        print(f"  {'预测日期':<14} {'composite净利润':>16} {'composite收益率':>14}"
              f" {'baseline净利润':>16} {'baseline收益率':>14} {'差额':>12}")
        print(f"  {'─' * 82}")

        comp_map = {r["预测日期"]: r for _, r in df_composite.iterrows()}
        base_map = {r["预测日期"]: r for _, r in df_baseline.iterrows()}
        all_dates = sorted(set(list(comp_map.keys()) + list(base_map.keys())))

        total_diff = 0.0
        for d in all_dates:
            c = comp_map.get(d)
            b = base_map.get(d)
            c_net = c["净利润"] if c is not None else 0.0
            c_pct = c["收益率%"] if c is not None else 0.0
            b_net = b["净利润"] if b is not None else 0.0
            b_pct = b["收益率%"] if b is not None else 0.0
            diff = c_net - b_net
            total_diff += diff
            marker = "✅" if diff > 0 else ("❌" if diff < 0 else "➖")
            print(f"  {d:<14} {c_net:>14,.2f}元 {c_pct:>12.4f}%"
                  f" {b_net:>14,.2f}元 {b_pct:>12.4f}% {diff:>10,.2f}元 {marker}")

        print(f"  {'─' * 82}")
        verdict = "综合评分策略胜出 🎉" if total_diff > 0 else (
            "纯分数策略胜出" if total_diff < 0 else "两者持平")
        print(f"  累计差额: {total_diff:,.2f} 元 → {verdict}")

    print(f"\n{sep}\n")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 主入口
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main(
    provider_uri: str = "~/.qlib/qlib_data/cn_data",
    qlib_score_dir: str = "./qlib_score_csv",
    top_n: int = 5,
    hold_days: int = 1,
    buy_offset: int = 0,
    out: str = "./tests/sim_trade_result_v2.csv",
    detail_out: str = "./tests/sim_trade_detail_v2.csv",
):
    """
    综合评分选股 vs 纯分数选股 对比回测。

    参数：
      provider_uri    qlib 数据目录路径
      qlib_score_dir  qlib_score_csv 目录路径
      top_n           每日买入股票数量（默认 5）
      hold_days       持仓天数（1/3/5），默认 1
      buy_offset      买入偏移，默认 0（即 T 日买入）
      out             汇总结果 CSV 输出路径
      detail_out      明细结果 CSV 输出路径
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

    print(f"共发现 {len(subdirs)} 个预测目录")
    print(f"参数: top_n={top_n}, hold_days={hold_days}, buy_offset={buy_offset}")
    print(f"开始对比回测...\n")

    # ── 运行两种策略 ──
    print("▶ 运行综合评分策略 (composite)...")
    df_comp, det_comp = _run_one_strategy(
        "composite", hold_days, subdirs, trade_date, top_n, buy_offset)

    print("▶ 运行纯分数策略 (baseline)...")
    df_base, det_base = _run_one_strategy(
        "baseline", hold_days, subdirs, trade_date, top_n, buy_offset)

    # ── 打印对比报告 ──
    print_comparison(df_comp, df_base, hold_days)

    # ── 保存 CSV ──
    out_path = Path(out)
    det_path = Path(detail_out)

    # 合并两个策略的结果保存
    if not df_comp.empty or not df_base.empty:
        df_all = pd.concat([df_comp, df_base], ignore_index=True)
        df_all.to_csv(out_path, index=False, encoding="utf-8-sig")
        print(f"📄 汇总结果已保存: {out_path}")

    if not det_comp.empty or not det_base.empty:
        det_all = pd.concat([det_comp, det_base], ignore_index=True)
        det_all.to_csv(det_path, index=False, encoding="utf-8-sig")
        print(f"📄 交易明细已保存: {det_path}")

    # ── 额外：多持仓模式对比 ──
    if hold_days == 1:
        for hd in [3, 5]:
            print(f"\n{'─' * 50}")
            print(f"▶ 额外对比: 持仓 {hd} 天模式")
            df_c, _ = _run_one_strategy("composite", hd, subdirs, trade_date, top_n, buy_offset)
            df_b, _ = _run_one_strategy("baseline", hd, subdirs, trade_date, top_n, buy_offset)
            print_comparison(df_c, df_b, hd)

            # 保存
            suffix = f"_t{hd}"
            comp_out = out_path.with_stem(f"{out_path.stem}{suffix}")
            df_merged = pd.concat([df_c, df_b], ignore_index=True)
            if not df_merged.empty:
                df_merged.to_csv(comp_out, index=False, encoding="utf-8-sig")
                print(f"📄 T+{hd} 汇总已保存: {comp_out}")


if __name__ == "__main__":
    import fire
    fire.Fire(main)
