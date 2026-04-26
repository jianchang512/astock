#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
模拟交易 CI 版 —— 真实资金流 + 复权因子等效股数版
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
# 费用计算 (注意：股数可能会因为复权变成浮点数，将类型改为 float)
# ──────────────────────────────────────────────

def _commission(amount: float) -> float:
    return max(amount * COMMISSION_RATE, MIN_COMMISSION)

def _transfer_fee(amount: float) -> float:
    return amount * TRANSFER_RATE

def buy_cost(price: float, shares: float) -> float:
    amount = price * shares
    return amount + _commission(amount) + _transfer_fee(amount)

def sell_revenue(price: float, shares: float) -> float:
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


def get_price_info(instruments: list[str], date: str) -> dict[str, dict]:
    """
    同时获取复权价(close)和复权因子(factor)，并还原出【真实不复权价格】
    """
    from qlib.data import D

    if not instruments:
        return {}

    # 在 Qlib 中，默认的 $close 是复权价
    df = D.features(
        instruments, ["$close", "$factor"],
        start_time=date,
        end_time=date,
        freq="day",
    )
    if df is None or df.empty:
        return {}

    df.columns =["close", "factor"]
    df = df.reset_index()
    df = df.dropna(subset=["close"])

    result: dict[str, dict] = {}
    for _, row in df.iterrows():
        adj_close = float(row["close"])
        # 防止 factor 为空或 0 导致除以 0 报错
        factor = float(row["factor"]) if not pd.isna(row["factor"]) and float(row["factor"]) != 0 else 1.0
        
        # ⭐ 核心修复：真实现价 = 复权价 / 复权因子
        real_price = adj_close / factor

        result[row["instrument"]] = {
            "real_price": real_price,
            "factor": factor
        }
    return result
# ──────────────────────────────────────────────
# 预测数据扫描与去重 (省略不变的辅助函数, 与原版一致)
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
        if date_key: date_to_subdir[date_key] = d
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


def backtest_final(
    score_tables: dict[str, pd.DataFrame],
    top_n: int,
):
    predict_dates = list(score_tables.keys())
    if len(predict_dates) < 2:
        return [],[]

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
        
        still_hold: list[dict] =[]

        # 1) 卖出上一交易日持仓
        if previous_positions:
            sell_info = get_price_info([p["instrument"] for p in previous_positions], today)

            for pos in previous_positions:
                inst = pos["instrument"]
                bp = pos["buy_price"]
                bc = pos["buy_cost"]
                bfactor = pos["buy_factor"]
                old_shares = pos["shares"]

                info = sell_info.get(inst)

                # 使用 real_price 判定行情
                if not info or pd.isna(info["real_price"]) or info["real_price"] <= 0:
                    still_hold.append(pos)
                    continue
                
                sp = info["real_price"]   # 这里拿到的就是真实的 8 块钱了
                sfactor = info["factor"]

                # 等效股数：自动处理分红和拆股
                equiv_shares = old_shares * (sfactor / bfactor) if bfactor else old_shares
                
                sr = sell_revenue(sp, equiv_shares)
                buy_amount = bp * old_shares
                sell_amount = sp * equiv_shares
                
                buy_fee = round(bc - buy_amount, 2)
                sell_fee = round(sell_amount - sr, 2)
                
                gross = sell_amount - buy_amount
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
                    "真实价格": round(sp, 4),
                    "股数": round(equiv_shares, 2), 
                    "金额(真金)": round(sr, 2),
                    "手续费": sell_fee,
                    "净利润": round(net, 2),
                })

        # 2) 买入新股票
        buy_instruments: list[str] =[]
        buy_total = 0.0
        new_positions: list[dict] =[]

        today_buy_df = score_tables.get(pred_day)
        if today_buy_df is not None and not today_buy_df.empty:
            selected = select_trade_candidates(today_buy_df, top_n=top_n)
            buy_instruments = selected["instrument"].tolist()

            buy_info = get_price_info(buy_instruments, today)
            for inst in buy_instruments:
                info = buy_info.get(inst)
                if not info or pd.isna(info["real_price"]) or info["real_price"] <= 0:
                    continue

                bp = info["real_price"]  # 这里也是 8 块钱
                bfactor = info["factor"]

                bc = buy_cost(bp, SHARES_PER_STOCK)
                buy_amount = bp * SHARES_PER_STOCK
                buy_fee = round(bc - buy_amount, 2)

                new_positions.append({
                    "instrument": inst,
                    "buy_price": bp,
                    "buy_cost": bc,
                    "buy_factor": bfactor,
                    "shares": SHARES_PER_STOCK
                })
                buy_total += bc

                detail_rows.append({
                    "交易日期": today,
                    "股票代码": inst,
                    "操作": "买入",
                    "真实价格": round(bp, 4),
                    "股数": SHARES_PER_STOCK,
                    "金额(真金)": round(bc, 2),
                    "手续费": buy_fee,
                    "净利润": "",
                })

        previous_positions = still_hold + new_positions

        cum_profit += day_net_profit
        return_pct = day_net_profit / day_sell_buy_cost * 100 if day_sell_buy_cost else 0.0

        summary_rows.append({
            "交易日期": today,
            "预测日期": pred_day,
            "买入股票数": len(buy_instruments),
            "买入总额(真金)": round(buy_total, 2),
            "卖出股票数": len(sell_instruments),
            "卖出总额(真金)": round(day_sell_total, 2),
            "卖出标的总买入成本": round(day_sell_buy_cost, 2),
            "手续费": round(day_total_fee, 2),
            "毛利润": round(day_gross_profit, 2),
            "净利润": round(day_net_profit, 2),
            "收益率%": round(return_pct, 4),
            "累计净利润": round(cum_profit, 2),
            "买入股票": ",".join(buy_instruments) if buy_instruments else "",
            "卖出股票": ",".join(sell_instruments) if sell_instruments else "",
        })

        action_desc =[]
        if sell_instruments: action_desc.append(f"卖出{len(sell_instruments)}只")
        if buy_instruments: action_desc.append(f"买入{len(buy_instruments)}只")
        if still_hold: action_desc.append(f"滞留{len(still_hold)}只")
        if not action_desc: action_desc.append("无交易")

        print(
            f"[{today}] pred={pred_day} {'/'.join(action_desc)}  "
            f"净利={day_net_profit:.2f}  累计={cum_profit:.2f}"
        )

    return summary_rows, detail_rows

def write_outputs(
    summary_rows: list[dict],
    detail_rows: list[dict],
    out_path: Path,
    detail_path: Path,
):
    df_summary = pd.DataFrame(summary_rows, columns=[
        "交易日期", "预测日期", "买入股票数", "买入总额(真金)",
        "卖出股票数", "卖出总额(真金)", "卖出标的总买入成本",
        "手续费", "毛利润", "净利润", "收益率%", "累计净利润","买入股票", "卖出股票", 
    ])
    df_summary.to_csv(out_path, index=False, encoding="utf-8-sig")

    df_detail = pd.DataFrame(detail_rows, columns=[
        "交易日期", "股票代码", "操作", "真实价格", "股数", "金额(真金)", "手续费", "净利润",
    ])
    df_detail.to_csv(detail_path, index=False, encoding="utf-8-sig")

    total_net = df_summary["净利润"].sum()
    total_sell_cost = df_summary["卖出标的总买入成本"].sum()
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
        "总净利(真金)": round(total_net, 2),
        "总投入本金": round(total_sell_cost, 2),
        "平均日净利": avg_net,
        "真实总收益率": overall_return_pct, 
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
    for _nums in [300, 600, 1000]:
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
        if not score_tables: return

        top_n_list =[1, 3, 5, 10, 15]
        out_path = Path(out)
        detail_path = Path(detail_out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        detail_path.parent.mkdir(parents=True, exist_ok=True)

        compare_rows: list[dict] =[]

        for n in top_n_list:
            print(f"\n========== 开始回测 top{n} ==========")
            summary_rows, detail_rows = backtest_final(score_tables, top_n=n)
            if not summary_rows: continue

            result_path = out_path.with_name(f"{out_path.stem}_top{n}{_new_shuffix}{out_path.suffix}")
            detail_result_path = detail_path.with_name(f"{detail_path.stem}_top{n}{_new_shuffix}{detail_path.suffix}")

            stats = write_outputs(summary_rows, detail_rows, result_path, detail_result_path)
            stats["top_n"] = n
            compare_rows.append(stats)
            
        if compare_rows:
            compare_df = pd.DataFrame(compare_rows, columns=[
                "top_n", "交易天数", "含卖出天数", "盈利天数", "胜率",
                "总净利(真金)","总投入本金", "平均日净利", "真实总收益率"
            ])
            compare_path = out_path.with_name(f"{out_path.stem}_compare{_new_shuffix}{out_path.suffix}")
            compare_df.to_csv(compare_path, index=False, encoding="utf-8-sig")
            print(f"\nTopN 对比汇总 ({_nums}股) 已保存: {compare_path}")
            print(compare_df.to_string(index=False))

if __name__ == "__main__":
    import fire
    fire.Fire(main)