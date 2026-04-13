#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟交易回测 —— 单文件版
==========================
策略逻辑：
  每日 T 预测完成后，取 filter_ret.csv 中 avg_score 最高的前 N 只股票，
  于 T+1（下一个交易日）收盘价买入 SHARES_PER_STOCK 股，
  于 T+2（再下一个交易日）收盘价全部卖出，
  计算每笔交易的盈亏并累计。

费率说明（A股，2023 年后）：
  印花税 (stamp_tax)  : 0.05%，仅卖出方向收取
  佣金   (commission) : 0.03%，买卖均收取，单边最低 5 元
  过户费 (transfer)   : 0.001%，买卖均收取（沪市，深市免）
  注意：qlib 行情数据使用了缩放因子，绝对金额仅供比率参考，
        收益率（百分比）与实盘一致。

用法：
  cd roll
  python sim_trade.py                         # 使用默认 config.yaml
  python sim_trade.py --top_n=10              # 指定持仓数量
  python sim_trade.py --out=../my_result.csv  # 指定输出路径

输出 CSV 字段：
  date_T        预测日期（T 日）
  date_buy      买入日期（T+1 日）
  date_sell     卖出日期（T+2 日）
  instruments   买入股票列表（逗号分隔）
  buy_price_sum 买入总金额（调整价 × 股数，含佣金/过户费）
  sell_price_sum卖出总金额（调整价 × 股数，扣印花税/佣金/过户费）
  gross_profit  毛利润（不含费用）
  net_profit    净利润（含所有费用）
  return_pct    净收益率 %
  cum_profit    累计净利润
"""

import os
import re
import sys
import yaml
from pathlib import Path
from typing import Optional

import pandas as pd
from loguru import logger

# ── 将 roll/ 目录加入 sys.path，方便直接 python sim_trade.py 运行 ──
_ROLL_DIR = Path(__file__).resolve().parent
if str(_ROLL_DIR) not in sys.path:
    sys.path.insert(0, str(_ROLL_DIR))

from utils import TradeDate  # noqa: E402  (在 sys.path 设置之后导入)

# ──────────────────────────────────────────────
# 全局参数
# ──────────────────────────────────────────────
SHARES_PER_STOCK = 1_000      # 每只股票买入股数
COMMISSION_RATE  = 0.0003     # 佣金率 0.03%
MIN_COMMISSION   = 5.0        # 单边最低佣金（元）
STAMP_TAX_RATE   = 0.0005     # 印花税率 0.05%（仅卖出）
TRANSFER_RATE    = 0.00001    # 过户费率 0.001%（沪市双向）


# ──────────────────────────────────────────────
# 费用计算
# ──────────────────────────────────────────────

def _commission(amount: float) -> float:
    return max(amount * COMMISSION_RATE, MIN_COMMISSION)


def _transfer_fee(amount: float) -> float:
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
# 配置加载
# ──────────────────────────────────────────────

def load_config(config_path: str = "config.yaml") -> dict:
    p = Path(config_path)
    if not p.exists():
        # 尝试相对于本文件所在目录
        p = _ROLL_DIR / config_path
    if not p.exists():
        raise FileNotFoundError(f"配置文件未找到: {config_path}")
    with open(p, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    # 展开 ~ 路径
    for key in ("provider_uri", "uri_folder", "analysis_folder"):
        if key in cfg and cfg[key]:
            cfg[key] = str(Path(cfg[key]).expanduser())
    return cfg


# ──────────────────────────────────────────────
# qlib 初始化（延迟，避免不必要开销）
# ──────────────────────────────────────────────

def init_qlib(provider_uri: str):
    import qlib
    from qlib.constant import REG_CN
    qlib.init(provider_uri=provider_uri, region=REG_CN)
    logger.info(f"qlib 已初始化，数据源: {provider_uri}")


def get_close_prices(instruments: list, date: str) -> dict:
    """
    返回指定日期各股票的复权收盘价字典 {instrument: close_price}。
    使用 qlib D.features，与原始 get_orignal_data 保持一致。
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
    result = {}
    for _, row in df.iterrows():
        inst = row["instrument"]
        result[inst] = float(row["close"])
    return result


# ──────────────────────────────────────────────
# 扫描 qlib_score_csv 目录（与 ModelReviewHelper 逻辑一致）
# ──────────────────────────────────────────────

def get_score_subdirs(qlib_score_dir: Path) -> Optional[list]:
    if not qlib_score_dir.exists():
        logger.error(f"目录不存在: {qlib_score_dir}")
        return None
    subdirs = [d for d in qlib_score_dir.iterdir() if d.is_dir()]

    def _extract_date(subdir: Path) -> str:
        m = re.match(r"selection_(\d{8})_", subdir.name)
        return m.group(1) if m else ""

    return sorted(subdirs, key=_extract_date)  # 升序，方便按时间顺序处理


def extract_date_from_csv(subdir: Path) -> Optional[str]:
    for f in subdir.iterdir():
        m = re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", f.name)
        if m:
            return m.group(1)
    return None


# ──────────────────────────────────────────────
# 核心：单日模拟交易
# ──────────────────────────────────────────────

def simulate_one_day(
    subdir: Path,
    trade_date: TradeDate,
    top_n: int,
) -> Optional[dict]:
    """
    处理一个 selection 子目录，返回当日模拟交易结果字典，
    无法处理时返回 None。
    """
    date_str = extract_date_from_csv(subdir)
    if not date_str:
        logger.warning(f"[{subdir.name}] 未找到日期 CSV，跳过")
        return None

    idx = trade_date.get_date_index(date_str)
    if idx is None:
        logger.info(f"[{date_str}] 不在交易日历中，跳过")
        return None

    trade_list = trade_date.get_trade_date_list()
    if idx + 2 >= len(trade_list):
        logger.info(f"[{date_str}] T+1/T+2 尚未到来，跳过")
        return None

    buy_date  = trade_date.get_next_date(date_str, 1)
    sell_date = trade_date.get_next_date(date_str, 2)

    filter_csv = subdir / f"{date_str}_filter_ret.csv"
    if not filter_csv.exists():
        logger.warning(f"[{date_str}] 缺少 filter_ret.csv，跳过")
        return None

    df = pd.read_csv(filter_csv)

    # 截掉 KMID 及右侧（与原始 review 逻辑一致）
    if "KMID" in df.columns:
        kmid_idx = df.columns.get_loc("KMID")
        df = df.iloc[:, :kmid_idx]

    if "avg_score" not in df.columns or "instrument" not in df.columns:
        logger.warning(f"[{date_str}] filter_ret.csv 缺少必要列，跳过")
        return None

    # 取 avg_score > 0 的前 top_n 只股票（与复盘逻辑一致）
    top_df = (
        df[df["avg_score"] > 0]
        .sort_values("avg_score", ascending=False)
        .head(top_n)
    )
    if top_df.empty:
        logger.info(f"[{date_str}] avg_score > 0 的股票不足，跳过")
        return None

    instruments = top_df["instrument"].tolist()

    # 获取 T+1（买入日）收盘价
    buy_prices  = get_close_prices(instruments, buy_date)
    # 获取 T+2（卖出日）收盘价
    sell_prices = get_close_prices(instruments, sell_date)

    if not buy_prices or not sell_prices:
        logger.info(f"[{date_str}] 行情数据不足（买入日={buy_date}, 卖出日={sell_date}），跳过")
        return None

    # 只保留两日均有行情的股票
    valid_instruments = [i for i in instruments if i in buy_prices and i in sell_prices]
    if not valid_instruments:
        logger.info(f"[{date_str}] 无有效股票行情，跳过")
        return None

    total_buy  = 0.0
    total_sell = 0.0
    total_gross = 0.0
    detail_rows = []

    for inst in valid_instruments:
        bp = buy_prices[inst]
        sp = sell_prices[inst]
        bc = buy_cost(bp, SHARES_PER_STOCK)
        sr = sell_revenue(sp, SHARES_PER_STOCK)
        gross = (sp - bp) * SHARES_PER_STOCK
        net   = sr - bc
        detail_rows.append({
            "instrument": inst,
            "buy_price":  round(bp, 4),
            "sell_price": round(sp, 4),
            "shares":     SHARES_PER_STOCK,
            "buy_cost":   round(bc, 2),
            "sell_revenue": round(sr, 2),
            "gross_profit": round(gross, 2),
            "net_profit":   round(net, 2),
        })
        total_buy  += bc
        total_sell += sr
        total_gross += gross

    net_profit = total_sell - total_buy
    return_pct  = net_profit / total_buy * 100 if total_buy else 0.0

    return {
        "date_T":       date_str,
        "date_buy":     buy_date,
        "date_sell":    sell_date,
        "instruments":  ",".join(valid_instruments),
        "stock_count":  len(valid_instruments),
        "buy_total":    round(total_buy, 2),
        "sell_total":   round(total_sell, 2),
        "gross_profit": round(total_gross, 2),
        "net_profit":   round(net_profit, 2),
        "return_pct":   round(return_pct, 4),
        "_detail":      detail_rows,  # 内部使用，不写入汇总 CSV
    }


# ──────────────────────────────────────────────
# 主流程
# ──────────────────────────────────────────────

def main(
    config: str = "config.yaml",
    top_n: int = 10,
    out: str = "../sim_trade_result.csv",
    detail_out: str = "../sim_trade_detail.csv",
    qlib_score_dir: str = "../qlib_score_csv",
):
    """
    参数：
      config        配置文件路径（默认 config.yaml，与 roll.py 共用）
      top_n         每日买入股票数量（默认 10）
      out           汇总结果 CSV 输出路径
      detail_out    明细结果 CSV 输出路径（每只股票一行）
      qlib_score_dir qlib_score_csv 目录路径
    """
    cfg = load_config(config)
    provider_uri = cfg.get("provider_uri", "~/.qlib/qlib_data/cn_data/")

    logger.info("初始化 qlib...")
    init_qlib(provider_uri)

    trade_date = TradeDate(provider_uri)
    score_dir  = Path(qlib_score_dir) if not Path(qlib_score_dir).is_absolute() \
                 else Path(qlib_score_dir)
    # 若相对路径，以本文件所在目录为基准
    if not score_dir.is_absolute():
        score_dir = _ROLL_DIR / qlib_score_dir

    subdirs = get_score_subdirs(score_dir)
    if not subdirs:
        logger.error("未找到任何 selection 子目录，退出。")
        return

    logger.info(f"共发现 {len(subdirs)} 个预测目录，开始模拟交易（top_n={top_n}）...")

    summary_rows = []
    detail_rows  = []
    cum_profit   = 0.0

    for subdir in subdirs:
        result = simulate_one_day(subdir, trade_date, top_n)
        if result is None:
            continue

        cum_profit += result["net_profit"]
        row = {k: v for k, v in result.items() if k != "_detail"}
        row["cum_profit"] = round(cum_profit, 2)
        summary_rows.append(row)
        logger.info(
            f"[{result['date_T']}] 净利润={result['net_profit']:.2f}  "
            f"收益率={result['return_pct']:.4f}%  累计={cum_profit:.2f}"
        )

        # 明细行附加公共字段
        for dr in result["_detail"]:
            dr["date_T"]     = result["date_T"]
            dr["date_buy"]   = result["date_buy"]
            dr["date_sell"]  = result["date_sell"]
            detail_rows.append(dr)

    if not summary_rows:
        logger.warning("没有可输出的结果（数据不足或行情尚未就绪）。")
        return

    # 输出汇总 CSV
    out_path = Path(out) if Path(out).is_absolute() else _ROLL_DIR / out
    df_summary = pd.DataFrame(summary_rows, columns=[
        "date_T", "date_buy", "date_sell",
        "instruments", "stock_count",
        "buy_total", "sell_total",
        "gross_profit", "net_profit",
        "return_pct", "cum_profit",
    ])
    df_summary.to_csv(out_path, index=False, encoding="utf-8-sig")
    logger.info(f"汇总结果已保存: {out_path}  ({len(df_summary)} 行)")

    # 输出明细 CSV
    det_path = Path(detail_out) if Path(detail_out).is_absolute() else _ROLL_DIR / detail_out
    df_detail = pd.DataFrame(detail_rows, columns=[
        "date_T", "date_buy", "date_sell",
        "instrument", "shares",
        "buy_price", "sell_price",
        "buy_cost", "sell_revenue",
        "gross_profit", "net_profit",
    ])
    df_detail.to_csv(det_path, index=False, encoding="utf-8-sig")
    logger.info(f"明细结果已保存: {det_path}  ({len(df_detail)} 行)")

    # 打印统计摘要
    total_net = df_summary["net_profit"].sum()
    win_days  = (df_summary["net_profit"] > 0).sum()
    total_days = len(df_summary)
    logger.info(
        f"\n=== 模拟交易统计 ===\n"
        f"  交易天数:  {total_days}\n"
        f"  盈利天数:  {win_days} ({win_days/total_days*100:.1f}%)\n"
        f"  累计净利润: {total_net:.2f}\n"
        f"  平均日净利润: {total_net/total_days:.2f}\n"
        f"==================="
    )


if __name__ == "__main__":
    import fire
    fire.Fire(main)
