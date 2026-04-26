#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟交易 CI 版 —— 最终增强版 (已修复Bug版)
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

import pandas as pd

# ──────────────────────────────────────────────
# 全局参数（A股费率）
# ──────────────────────────────────────────────
SHARES_PER_STOCK = 500
COMMISSION_RATE = 0.0003
MIN_COMMISSION = 5.0
STAMP_TAX_RATE = 0.0005
TRANSFER_RATE = 0.00001


# ──────────────────────────────────────────────
# 费用计算
# ──────────────────────────────────────────────

def _commission(amount: float) -> float:
    return max(amount * COMMISSION_RATE, MIN_COMMISSION)

def _transfer_fee(amount: float) -> float:
    return amount * TRANSFER_RATE

def buy_cost(price: float, shares: int) -> float:
    amount = price * shares
    return amount + _commission(amount) + _transfer_fee(amount)

def sell_revenue(price: float, shares: int) -> float:
    amount = price * shares
    return amount - _commission(amount) - _transfer_fee(amount) - amount * STAMP_TAX_RATE


# ──────────────────────────────────────────────
# qlib 初始化 & 行情
# ──────────────────────────────────────────────

_qlib_initialized = False

def init_qlib(provider_uri: str):
    global _qlib_initialized
    if _qlib_initialized:
        return
    import qlib
    from qlib.constant import REG_CN

    qlib.init(provider_uri=provider_uri, region=REG_CN)
    _qlib_initialized = True
    print(f"qlib 已初始化，数据源: {provider_uri}")


def get_close_prices(instruments: list[str], date: str) -> dict[str, float]:
    from qlib.data import D

    if not instruments:
        return {}

    # 【修复3】为了计算连续收益，强烈建议使用复权价格。
    # 标准 qlib 数据中，如果有 $factor，通常用 $close * $factor 获取真实回测复权价
    # 如果你的 $close 已经是复权价，直接写 "$close" 即可，切忌使用 "$close / $factor"
    df = D.features(
        instruments,["$close * $factor"],  
        start_time=date,
        end_time=date,
        freq="day",
    )
    if df is None or df.empty:
        return {}

    df.columns = ["close"]
    df = df.reset_index()
    # 过滤掉 NaN 的行情
    df = df.dropna(subset=["close"])

    result: dict[str, float] = {}
    for _, row in df.iterrows():
        result[row["instrument"]] = float(row["close"])
    return result


# ──────────────────────────────────────────────
# 预测数据扫描与去重 (省略部分未改动的辅助函数)
# ──────────────────────────────────────────────
def get_score_subdirs(score_dir: Path) -> list[Path]:
    if not score_dir.exists(): return []
    subdirs =[d for d in score_dir.iterdir() if d.is_dir() and d.name.startswith("selection_")]
    if not subdirs: return[]
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

def extract_all_dates_from_csv(subdir: Path) -> list[str]:
    dates = set()
    for f in subdir.iterdir():
        m = re.match(r"(\d{4}-\d{2}-\d{2})_.*\.csv", f.name)
        if m: dates.add(m.group(1))
    return sorted(dates)

def load_all_filter_tables(score_dir: Path) -> dict[str, pd.DataFrame]:
    tables: dict[str, pd.DataFrame] = {}
    for subdir in get_score_subdirs(score_dir):
        for date_str in extract_all_dates_from_csv(subdir):
            csv_path = subdir / f"{date_str}_filter_ret.csv"
            if not csv_path.exists(): continue
            try:
                df = pd.read_csv(csv_path)
            except Exception:
                continue
            if "KMID" in df.columns:
                kmid_idx = df.columns.get_loc("KMID")
                df = df.iloc[:, :kmid_idx]
            if "instrument" not in df.columns or "avg_score" not in df.columns: continue
            df = df.copy()
            df["avg_score"] = pd.to_numeric(df["avg_score"], errors="coerce")
            df = df.dropna(subset=["instrument", "avg_score"])
            if df.empty: continue
            tables[date_str] = df
    return dict(sorted(tables.items(), key=lambda kv: kv[0]))

def select_trade_candidates(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    if df.empty or top_n <= 0: return df.iloc[0:0].copy()
    ranked = df.copy()
    ranked = ranked.dropna(subset=["instrument", "avg_score", "pos_ratio"]).copy()
    ranked["avg_score"] = pd.to_numeric(ranked["avg_score"], errors="coerce")
    ranked["pos_ratio"] = pd.to_numeric(ranked["pos_ratio"], errors="coerce")
    ranked = ranked.dropna(subset=["avg_score", "pos_ratio"])
    if ranked.empty: return ranked
    ranked = ranked.sort_values(by=["pos_ratio", "avg_score"], ascending=[False, False])
    return ranked.head(top_n)


# ──────────────────────────────────────────────
# 最终增强版：严格滚动回测
# ──────────────────────────────────────────────

def backtest_final(
    score_tables: dict[str, pd.DataFrame],
    top_n: int,
):
    predict_dates = list(score_tables.keys())
    if len(predict_dates) < 2:
        print("预测日期不足，无法回测")
        return [], []

    summary_rows: list[dict] =[]
    detail_rows: list[dict] =[]
    cum_profit = 0.0

    previous_positions: list[dict] =[]

    for i in range(1, len(predict_dates)):
        pred_day = predict_dates[i - 1]
        today = predict_dates[i]

        sell_instruments: list[str] =[]
        day_sell_total = 0.0
        day_sell_buy_cost = 0.0
        day_gross_profit = 0.0
        day_net_profit = 0.0
        day_total_fee = 0.0
        
        still_hold: list[dict] =[] # 记录今天无法卖出，需要继续持有的股票

        # 1) 卖出上一交易日持仓
        if previous_positions:
            sell_prices = get_close_prices([p["instrument"] for p in previous_positions], today)

            for pos in previous_positions:
                inst = pos["instrument"]
                bp = pos["buy_price"]
                bc = pos["buy_cost"]
                sp = sell_prices.get(inst)

                if sp is None or pd.isna(sp) or sp <= 0:
                    # 今天没有行情，继续持有
                    still_hold.append(pos)
                    continue
                
                sr = sell_revenue(sp, SHARES_PER_STOCK)
                buy_amount = bp * SHARES_PER_STOCK
                sell_amount = sp * SHARES_PER_STOCK
                
                buy_fee = round(bc - buy_amount, 2)
                sell_fee = round(sell_amount - sr, 2)
                
                gross = (sp - bp) * SHARES_PER_STOCK
                net = sr - bc
                fee = round(buy_fee + sell_fee, 2)

                sell_instruments.append(inst)
                day_sell_total += sr
                day_sell_buy_cost += bc
                day_gross_profit += gross
                day_net_profit += net
                day_total_fee += fee

                detail_rows.append({
                    "交易日期": today,
                    "股票代码": inst,
                    "操作": "卖出",
                    "价格": round(sp, 4),
                    "股数": SHARES_PER_STOCK,
                    "金额": round(sr, 2),
                    "手续费": sell_fee,
                    "净利润": round(net, 2),
                })

        # 2) 按前一个预测日的 top_n 买入
        buy_instruments: list[str] =[]
        buy_total = 0.0
        new_positions: list[dict] =[]

        today_buy_df = score_tables.get(pred_day)
        if today_buy_df is not None and not today_buy_df.empty:
            selected = select_trade_candidates(today_buy_df, top_n=top_n)
            buy_instruments = selected["instrument"].tolist()

            buy_prices = get_close_prices(buy_instruments, today)
            for inst in buy_instruments:
                bp = buy_prices.get(inst)
                if bp is None or pd.isna(bp) or bp <= 0:
                    continue

                bc = buy_cost(bp, SHARES_PER_STOCK)
                buy_amount = bp * SHARES_PER_STOCK
                buy_fee = round(bc - buy_amount, 2)

                new_positions.append({
                    "instrument": inst,
                    "buy_price": bp,
                    "buy_cost": bc,
                })
                buy_total += bc

                detail_rows.append({
                    "交易日期": today,
                    "股票代码": inst,
                    "操作": "买入",
                    "价格": round(bp, 4),
                    "股数": SHARES_PER_STOCK,
                    "金额": round(bc, 2),
                    "手续费": buy_fee,
                    "净利润": "",
                })

        # 【修复1：合并今天无法卖出的股票 + 今天新买入的股票】
        # 你的原代码只有 previous_positions = new_positions 会导致没卖出的股票直接从资金中消失！
        previous_positions = still_hold + new_positions

        cum_profit += day_net_profit
        return_pct = day_net_profit / day_sell_buy_cost * 100 if day_sell_buy_cost else 0.0

        summary_rows.append({
            "交易日期": today,
            "预测日期": pred_day,
            "买入股票数": len(buy_instruments),
            "买入总额": round(buy_total, 2),
            "卖出股票数": len(sell_instruments),
            "卖出总额": round(day_sell_total, 2),
            "卖出标的总买入成本": round(day_sell_buy_cost, 2), # 【修复4：加入此字段以便正确统计总收益率】
            "手续费": round(day_total_fee, 2),
            "毛利润": round(day_gross_profit, 2),
            "净利润": round(day_net_profit, 2),
            "收益率%": round(return_pct, 4),
            "累计净利润": round(cum_profit, 2),
            "买入股票": ",".join(buy_instruments) if buy_instruments else "",
            "卖出股票": ",".join(sell_instruments) if sell_instruments else "",
        })

        action_desc =[]
        if sell_instruments:
            action_desc.append(f"卖出{len(sell_instruments)}只")
        if buy_instruments:
            action_desc.append(f"买入{len(buy_instruments)}只")
        if still_hold:
            action_desc.append(f"因无行情滞留{len(still_hold)}只")
        if not action_desc:
            action_desc.append("无交易")

        print(
            f"[{today}] pred={pred_day} {'/'.join(action_desc)}  "
            f"净利润={day_net_profit:.2f}  累计={cum_profit:.2f}"
        )

    return summary_rows, detail_rows


def write_outputs(
    summary_rows: list[dict],
    detail_rows: list[dict],
    out_path: Path,
    detail_path: Path,
):
    df_summary = pd.DataFrame(summary_rows, columns=[
        "交易日期", "预测日期", "买入股票数", "买入总额",
        "卖出股票数", "卖出总额", "卖出标的总买入成本",
        "手续费", "毛利润", "净利润", "收益率%", "累计净利润","买入股票", "卖出股票", 
    ])
    df_summary.to_csv(out_path, index=False, encoding="utf-8-sig")

    df_detail = pd.DataFrame(detail_rows, columns=[
        "交易日期", "股票代码", "操作", "价格", "股数", "金额", "手续费", "净利润",
    ])
    df_detail.to_csv(detail_path, index=False, encoding="utf-8-sig")

    total_net = df_summary["净利润"].sum()
    
    # 【修复4】：计算累计投入成本。你之前的公式逻辑有误（卖出总额-毛利润 不等于 包含双边手续费的买入成本）
    total_sell_cost = df_summary["卖出标的总买入成本"].sum()
    
    # 3. 正确的总收益率：总净利润 / 总投入成本
    overall_return_pct = f"{(total_net / total_sell_cost * 100):.4f}%" if total_sell_cost > 0 else "0.00%"

    sell_days = int((df_summary["卖出股票数"] > 0).sum())
    total_days = len(df_summary)
    win_days = int((df_summary["净利润"] > 0).sum())
    win_pct = f"{win_days / sell_days * 100:.1f}%" if sell_days else "N/A"
    avg_net = f"{total_net / sell_days:.2f}" if sell_days else "N/A"

    return {
        "交易天数": total_days,
        "含卖出天数": sell_days,
        "盈利天数": win_days,
        "胜率": win_pct,
        "总净利润": round(total_net, 2),
        "总投入成本": round(total_sell_cost, 2),
        "平均日净利润": avg_net,
        "整体总收益率": overall_return_pct, 
    }


# ──────────────────────────────────────────────
# 主入口
# ──────────────────────────────────────────────

def main(
    provider_uri: str = "~/.qlib/qlib_data/cn_data",
    qlib_score_dir: str = "./qlib_score_csv",
    out: str = "./tests/sim_trade_result.csv",
    detail_out: str = "./tests/sim_trade_detail.csv",
):
    global SHARES_PER_STOCK
    for _nums in[300, 600, 1000]:
        _new_shuffix = f"-{_nums}"
        SHARES_PER_STOCK = _nums
        provider_uri = str(Path(provider_uri).expanduser())
        score_dir = Path(qlib_score_dir)
        if not score_dir.is_absolute():
            score_dir = Path.cwd() / score_dir

        print(f"\n====================================")
        print(f"初始化 qlib... 每次买入股数: {_nums}")
        print(f"====================================")
        init_qlib(provider_uri)

        score_tables = load_all_filter_tables(score_dir)
        if not score_tables:
            print("未找到任何 *filter_ret.csv，退出。")
            return

        top_n_list = [1, 3, 5, 10, 15]
        out_path = Path(out)
        detail_path = Path(detail_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        detail_path.parent.mkdir(parents=True, exist_ok=True)

        compare_rows: list[dict] =[]

        for n in top_n_list:
            print(f"\n========== 开始回测 top{n} ==========")
            summary_rows, detail_rows = backtest_final(score_tables, top_n=n)
            if not summary_rows:
                continue

            result_path = out_path.with_name(f"{out_path.stem}_top{n}{_new_shuffix}{out_path.suffix}")
            detail_result_path = detail_path.with_name(f"{detail_path.stem}_top{n}{_new_shuffix}{detail_path.suffix}")

            stats = write_outputs(summary_rows, detail_rows, result_path, detail_result_path)
            stats["top_n"] = n
            compare_rows.append(stats)

            
        if compare_rows:
            compare_df = pd.DataFrame(compare_rows, columns=[
                "top_n", "交易天数", "含卖出天数", "盈利天数", "胜率",
                "总净利润","总投入成本", "平均日净利润", "整体总收益率"
            ])

            compare_path = out_path.with_name(f"{out_path.stem}_compare{_new_shuffix}{out_path.suffix}")
            compare_df.to_csv(compare_path, index=False, encoding="utf-8-sig")
            print(f"\nTopN 对比汇总 ({_nums}股) 已保存: {compare_path}")
            print(compare_df.to_string(index=False))

if __name__ == "__main__":
    import fire
    fire.Fire(main)