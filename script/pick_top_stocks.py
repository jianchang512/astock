"""
pick_top_stocks.py
------------------
从每日预测数据 filter_ret.csv 中综合筛选出最推荐的 3~5 只股票。

不同于简单取 avg_score 最高的方式，本脚本从以下 5 个维度综合打分：
  1. 预测分数 (avg_score)           - 权重 35%
  2. 模型一致性 (pos_ratio)          - 权重 25%
  3. 低波动率 (STD5/STD20/STD60)    - 权重 15%
  4. 趋势动量 (ROC/MA 多头排列)       - 权重 15%
  5. 量价配合 (VWAP0 vs OPEN0)       - 权重 10%

使用方式:
    # 默认取最新数据，输出 Top 5
    python script/pick_top_stocks.py

    # 指定输出数量
    python script/pick_top_stocks.py --top 3

    # 指定数据目录
    python script/pick_top_stocks.py --data_dir ./qlib_score_csv/selection_20260413_15_31_02

    # 指定输出文件位置
    python script/pick_top_stocks.py --output ./my_picks.csv
"""

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from loguru import logger

# ── 权重配置 ──────────────────────────────────────────────────────────────────
WEIGHT_AVG_SCORE   = 0.35   # 预测分数权重
WEIGHT_POS_RATIO   = 0.25   # 模型一致性权重
WEIGHT_LOW_VOL     = 0.15   # 低波动率权重
WEIGHT_TREND       = 0.15   # 趋势动量权重
WEIGHT_VWAP        = 0.10   # 量价配合权重

# ── 基础过滤阈值 ──────────────────────────────────────────────────────────────
MIN_AVG_SCORE  = 0.0    # 模型预测看涨
MIN_POS_RATIO  = 0.5    # 至少一半模型看多


def _find_latest_selection_dir(base_dir: Path) -> Path:
    """
    扫描 qlib_score_csv/ 下所有 selection_YYYYMMDD_HH_MM_SS 子目录，
    按日期去重后返回最新的目录。

    同一日期可能存在多个目录（不同时间戳），只保留时间戳最大的那个。
    """
    pattern = re.compile(r"^selection_(\d{8})_(\d{2}_\d{2}_\d{2})$")
    # 按 (date, time) 两段分组，保留每日最大时间戳
    latest: dict[str, tuple[str, Path]] = {}
    for d in base_dir.iterdir():
        if not d.is_dir():
            continue
        m = pattern.match(d.name)
        if not m:
            continue
        date_str, time_str = m.group(1), m.group(2)
        if date_str not in latest or time_str > latest[date_str][0]:
            latest[date_str] = (time_str, d)

    if not latest:
        raise FileNotFoundError(f"在 {base_dir} 下未找到任何 selection_* 目录")

    # 返回日期最大的目录
    newest_date = max(latest.keys())
    return latest[newest_date][1]


def _find_filter_ret_csv(subdir: Path) -> tuple[Path, str]:
    """
    在给定 selection 子目录中找到 {date}_filter_ret.csv 文件，
    返回 (文件路径, 日期字符串)。
    """
    for f in subdir.glob("*_filter_ret.csv"):
        date_str = f.name.replace("_filter_ret.csv", "")
        return f, date_str
    raise FileNotFoundError(f"在 {subdir} 下未找到 *_filter_ret.csv 文件")


def _normalize_minmax(series: pd.Series) -> pd.Series:
    """Min-Max 归一化，范围 [0, 1]；若所有值相同则返回全 0.5。"""
    mn, mx = series.min(), series.max()
    if mx - mn < 1e-12:
        return pd.Series(0.5, index=series.index)
    return (series - mn) / (mx - mn)


def _score_volatility(df: pd.DataFrame) -> pd.Series:
    """
    低波动率得分：STD5、STD20、STD60 综合评估。
    波动率越低，得分越高（取平均后反转归一化）。
    """
    cols = [c for c in ["STD5", "STD20", "STD60"] if c in df.columns]
    if not cols:
        logger.warning("未找到 STD 波动率列，低波动率维度使用默认分 0.5")
        return pd.Series(0.5, index=df.index)
    avg_std = df[cols].mean(axis=1)
    # 波动率越低越好，故取反归一化
    return 1.0 - _normalize_minmax(avg_std)


def _score_trend(df: pd.DataFrame) -> pd.Series:
    """
    趋势动量得分：
      - ROC 短期大于长期 (ROC5 > ROC10, ROC10 > ROC20) 加分
      - 均线多头排列 (MA5 > MA10 > MA20) 加分
    每项满足得 1 分，总分 [0, 5]，再归一化到 [0, 1]。
    """
    scores = pd.Series(0.0, index=df.index)

    roc_pairs = [("ROC5", "ROC10"), ("ROC10", "ROC20"), ("ROC20", "ROC30")]
    for short, long_ in roc_pairs:
        if short in df.columns and long_ in df.columns:
            scores += (df[short] > df[long_]).astype(float)

    ma_pairs = [("MA5", "MA10"), ("MA10", "MA20")]
    for short, long_ in ma_pairs:
        if short in df.columns and long_ in df.columns:
            scores += (df[short] > df[long_]).astype(float)

    return _normalize_minmax(scores)


def _score_vwap(df: pd.DataFrame) -> pd.Series:
    """
    量价配合得分：VWAP0 >= OPEN0 时认为日内买方主导，得分高。
    用 (VWAP0 - OPEN0) / OPEN0 的归一化值作为得分。
    """
    if "VWAP0" not in df.columns or "OPEN0" not in df.columns:
        logger.warning("未找到 VWAP0/OPEN0 列，量价配合维度使用默认分 0.5")
        return pd.Series(0.5, index=df.index)
    open0 = df["OPEN0"].replace(0, np.nan)
    ratio = (df["VWAP0"] - open0) / open0.abs()
    return _normalize_minmax(ratio.fillna(0.0))


def compute_composite_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    计算综合评分，在 df 中新增以下列：
      score_avg_score  - 预测分数归一化得分
      score_pos_ratio  - 模型一致性归一化得分
      score_low_vol    - 低波动率得分
      score_trend      - 趋势动量得分
      score_vwap       - 量价配合得分
      composite_score  - 加权综合得分
    """
    result = df.copy()
    result["score_avg_score"] = _normalize_minmax(result["avg_score"])
    result["score_pos_ratio"] = _normalize_minmax(result["pos_ratio"])
    result["score_low_vol"]   = _score_volatility(result)
    result["score_trend"]     = _score_trend(result)
    result["score_vwap"]      = _score_vwap(result)

    result["composite_score"] = (
        result["score_avg_score"] * WEIGHT_AVG_SCORE
        + result["score_pos_ratio"] * WEIGHT_POS_RATIO
        + result["score_low_vol"]   * WEIGHT_LOW_VOL
        + result["score_trend"]     * WEIGHT_TREND
        + result["score_vwap"]      * WEIGHT_VWAP
    )
    return result


def pick_top_stocks(
    data_dir: str | None = None,
    top: int = 5,
    output: str | None = None,
) -> pd.DataFrame:
    """
    主函数：从 filter_ret.csv 中筛选最推荐股票。

    :param data_dir: 指定数据目录（selection_* 子目录），留空则自动找最新目录
    :param top:      输出 Top N（建议 3~5）
    :param output:   输出 CSV 路径，留空则保存到数据目录旁
    :return:         推荐股票 DataFrame
    """
    # ── 1. 确定数据目录 ──────────────────────────────────────────────────────
    # 兼容从项目根目录或 script/ 目录执行
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    if data_dir:
        subdir = Path(data_dir).resolve()
        if not subdir.exists():
            raise FileNotFoundError(f"指定目录不存在: {subdir}")
    else:
        # 优先尝试项目根目录下的 qlib_score_csv
        base_candidates = [
            project_root / "qlib_score_csv",
            script_dir / "qlib_score_csv",
            Path("qlib_score_csv").resolve(),
        ]
        base_dir = None
        for cand in base_candidates:
            if cand.exists() and cand.is_dir():
                base_dir = cand
                break
        if base_dir is None:
            raise FileNotFoundError("未找到 qlib_score_csv 目录，请通过 --data_dir 指定数据目录")
        logger.info(f"使用数据目录: {base_dir}")
        subdir = _find_latest_selection_dir(base_dir)

    logger.info(f"读取预测目录: {subdir}")

    # ── 2. 读取 filter_ret.csv ───────────────────────────────────────────────
    csv_path, date_str = _find_filter_ret_csv(subdir)
    logger.info(f"读取文件: {csv_path}")
    df = pd.read_csv(csv_path)
    logger.info(f"原始数据行数: {len(df)}")

    # ── 3. 基础列检查 ─────────────────────────────────────────────────────────
    required_cols = ["instrument", "avg_score", "pos_ratio"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"缺少必要列: {missing}")

    # 若 name 列缺失，补全为空
    if "name" not in df.columns:
        df["name"] = ""
    df["name"] = df["name"].fillna("")

    # ── 4. 基础过滤 ───────────────────────────────────────────────────────────
    df_filtered = df[
        (df["avg_score"] > MIN_AVG_SCORE) & (df["pos_ratio"] >= MIN_POS_RATIO)
    ].copy()
    logger.info(f"基础过滤后行数: {len(df_filtered)} (avg_score>{MIN_AVG_SCORE}, pos_ratio>={MIN_POS_RATIO})")

    if df_filtered.empty:
        logger.warning("过滤后无符合条件的股票，请检查数据或放宽过滤条件")
        return pd.DataFrame()

    # ── 5. 综合打分 ───────────────────────────────────────────────────────────
    df_scored = compute_composite_score(df_filtered)
    df_scored = df_scored.sort_values("composite_score", ascending=False)

    # ── 6. 取 Top N ──────────────────────────────────────────────────────────
    top_n = min(top, len(df_scored))
    df_top = df_scored.head(top_n).reset_index(drop=True)

    # ── 7. 整理输出列 ─────────────────────────────────────────────────────────
    display_cols = [
        "instrument", "name", "composite_score",
        "score_avg_score", "score_pos_ratio",
        "score_low_vol", "score_trend", "score_vwap",
        "avg_score", "pos_ratio",
    ]
    # 只保留存在的列
    display_cols = [c for c in display_cols if c in df_top.columns]
    df_display = df_top[display_cols].copy()

    # 四舍五入方便阅读
    score_cols = [c for c in display_cols if c.startswith("score_") or c == "composite_score"]
    df_display[score_cols] = df_display[score_cols].round(4)
    for col in ["avg_score", "pos_ratio"]:
        if col in df_display.columns:
            df_display[col] = df_display[col].round(4)

    # ── 8. 打印到终端 ─────────────────────────────────────────────────────────
    col_rename = {
        "instrument":     "股票代码",
        "name":           "股票名称",
        "composite_score":"综合评分",
        "score_avg_score":"预测分数",
        "score_pos_ratio":"模型一致性",
        "score_low_vol":  "低波动率",
        "score_trend":    "趋势动量",
        "score_vwap":     "量价配合",
        "avg_score":      "avg_score",
        "pos_ratio":      "pos_ratio",
    }
    df_print = df_display.rename(columns=col_rename)

    sep = "=" * 80
    print(f"\n{sep}")
    print(f"  📈 {date_str} 综合评分 Top {top_n} 推荐股票")
    print(f"  策略说明：预测分数(35%) + 模型一致性(25%) + 低波动率(15%) + 趋势动量(15%) + 量价配合(10%)")
    print(sep)
    try:
        from tabulate import tabulate
        print(tabulate(df_print, headers="keys", tablefmt="rounded_outline", showindex=True, floatfmt=".4f"))
    except ImportError:
        print(df_print.to_string(index=True))
    print(sep)
    print(f"  💡 提示：综合评分越高越推荐，各分项均为 [0,1] 归一化得分")
    print(f"{sep}\n")

    # ── 9. 保存 CSV ───────────────────────────────────────────────────────────
    if output:
        out_path = Path(output).resolve()
    else:
        out_path = subdir / f"top_picks_{date_str}.csv"

    df_display.to_csv(out_path, index=False, encoding="utf-8-sig")
    logger.info(f"推荐结果已保存到: {out_path}")

    return df_display


def _parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="从 filter_ret.csv 中综合筛选最推荐的 3~5 只 A 股",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python script/pick_top_stocks.py
  python script/pick_top_stocks.py --top 3
  python script/pick_top_stocks.py --data_dir ./qlib_score_csv/selection_20260413_15_31_02
  python script/pick_top_stocks.py --output ./my_picks.csv
        """,
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="输出推荐股票数量，默认 5（建议 3~5）",
    )
    parser.add_argument(
        "--data_dir",
        type=str,
        default=None,
        help="指定 selection_* 数据目录；留空则自动找最新目录",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="输出 CSV 路径；留空则保存到数据目录下 top_picks_{date}.csv",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = _parse_args()
    try:
        result = pick_top_stocks(
            data_dir=args.data_dir,
            top=args.top,
            output=args.output,
        )
        if result.empty:
            sys.exit(1)
    except FileNotFoundError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.exception(f"运行出错: {e}")
        sys.exit(1)
