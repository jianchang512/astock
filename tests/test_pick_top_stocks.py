"""
tests/test_pick_top_stocks.py
测试 script/pick_top_stocks.py 的核心逻辑
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys

# 将 script/ 目录加入 sys.path
root_dir = Path(__file__).resolve().parent.parent
script_dir = os.path.join(root_dir, "script")
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from pick_top_stocks import (
    _find_latest_selection_dir,
    _find_filter_ret_csv,
    _normalize_minmax,
    _score_volatility,
    _score_trend,
    _score_vwap,
    compute_composite_score,
    pick_top_stocks,
)


# ── 测试辅助 fixture ───────────────────────────────────────────────────────────

def _make_sample_df(n=10):
    """构造含所有关键列的测试 DataFrame"""
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "instrument": [f"SH60{i:04d}" for i in range(n)],
        "name": [f"股票{i}" for i in range(n)],
        "avg_score": rng.uniform(0.01, 0.1, n),
        "pos_ratio": rng.uniform(0.5, 1.0, n),
        "STD5":  rng.uniform(0.005, 0.05, n),
        "STD20": rng.uniform(0.005, 0.05, n),
        "STD60": rng.uniform(0.005, 0.05, n),
        "ROC5":  rng.uniform(0.9, 1.1, n),
        "ROC10": rng.uniform(0.9, 1.1, n),
        "ROC20": rng.uniform(0.9, 1.1, n),
        "ROC30": rng.uniform(0.9, 1.1, n),
        "MA5":   rng.uniform(0.9, 1.1, n),
        "MA10":  rng.uniform(0.9, 1.1, n),
        "MA20":  rng.uniform(0.9, 1.1, n),
        "OPEN0": rng.uniform(0.95, 1.05, n),
        "VWAP0": rng.uniform(0.95, 1.05, n),
    })
    return df


# ── _find_latest_selection_dir ────────────────────────────────────────────────

def test_find_latest_selection_dir(tmp_path):
    """验证自动找到最新目录的逻辑，且同日期只保留时间戳最大的"""
    # 创建多个目录，包括同日期不同时间
    (tmp_path / "selection_20260408_10_00_00").mkdir()
    (tmp_path / "selection_20260409_08_00_00").mkdir()
    (tmp_path / "selection_20260409_15_30_00").mkdir()  # 同日最新
    (tmp_path / "selection_20260407_14_00_00").mkdir()

    latest = _find_latest_selection_dir(tmp_path)
    assert latest.name == "selection_20260409_15_30_00"


def test_find_latest_selection_dir_no_dirs(tmp_path):
    """验证空目录抛出 FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        _find_latest_selection_dir(tmp_path)


def test_find_latest_selection_dir_ignores_non_matching(tmp_path):
    """验证忽略不符合命名规则的目录"""
    (tmp_path / "selection_20260410_09_00_00").mkdir()
    (tmp_path / "other_dir").mkdir()
    (tmp_path / "selection_badname").mkdir()

    latest = _find_latest_selection_dir(tmp_path)
    assert latest.name == "selection_20260410_09_00_00"


# ── _find_filter_ret_csv ─────────────────────────────────────────────────────

def test_find_filter_ret_csv(tmp_path):
    """验证正确找到 *_filter_ret.csv 文件"""
    csv_file = tmp_path / "2026-04-13_filter_ret.csv"
    csv_file.write_text("a,b\n1,2\n")

    path, date_str = _find_filter_ret_csv(tmp_path)
    assert path == csv_file
    assert date_str == "2026-04-13"


def test_find_filter_ret_csv_missing(tmp_path):
    """验证找不到文件时抛出异常"""
    with pytest.raises(FileNotFoundError):
        _find_filter_ret_csv(tmp_path)


# ── _normalize_minmax ─────────────────────────────────────────────────────────

def test_normalize_minmax_normal():
    """验证 Min-Max 归一化结果在 [0, 1] 范围内"""
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = _normalize_minmax(s)
    assert result.min() == pytest.approx(0.0)
    assert result.max() == pytest.approx(1.0)


def test_normalize_minmax_constant():
    """验证全相同值时返回 0.5"""
    s = pd.Series([3.0, 3.0, 3.0])
    result = _normalize_minmax(s)
    assert (result == 0.5).all()


# ── _score_volatility ─────────────────────────────────────────────────────────

def test_score_volatility_range():
    """验证波动率得分在 [0, 1] 范围内"""
    df = _make_sample_df()
    scores = _score_volatility(df)
    assert scores.min() >= 0.0
    assert scores.max() <= 1.0


def test_score_volatility_missing_cols():
    """验证缺少 STD 列时使用默认分 0.5"""
    df = pd.DataFrame({"avg_score": [1.0, 2.0]})
    scores = _score_volatility(df)
    assert (scores == 0.5).all()


def test_score_volatility_lower_is_better():
    """验证波动率低的股票得分高"""
    df = pd.DataFrame({
        "STD5":  [0.01, 0.10],
        "STD20": [0.01, 0.10],
        "STD60": [0.01, 0.10],
    })
    scores = _score_volatility(df)
    # 第一行波动率低，得分应更高
    assert scores.iloc[0] > scores.iloc[1]


# ── _score_trend ──────────────────────────────────────────────────────────────

def test_score_trend_range():
    """验证趋势得分在 [0, 1] 范围内"""
    df = _make_sample_df()
    scores = _score_trend(df)
    assert scores.min() >= 0.0
    assert scores.max() <= 1.0


def test_score_trend_all_aligned():
    """多头完全排列时得分应为 1.0（相对最高）"""
    df = pd.DataFrame({
        "ROC5":  [1.05, 0.95],
        "ROC10": [1.03, 0.98],
        "ROC20": [1.01, 1.00],
        "ROC30": [0.99, 1.01],
        "MA5":   [1.05, 0.95],
        "MA10":  [1.03, 0.98],
        "MA20":  [1.01, 1.00],
    })
    scores = _score_trend(df)
    # 第一行完全符合多头排列，第二行完全不符，归一化后应差距最大
    assert scores.iloc[0] > scores.iloc[1]


# ── _score_vwap ───────────────────────────────────────────────────────────────

def test_score_vwap_range():
    """验证量价得分在 [0, 1] 范围内"""
    df = _make_sample_df()
    scores = _score_vwap(df)
    assert scores.min() >= 0.0
    assert scores.max() <= 1.0


def test_score_vwap_missing_cols():
    """验证缺少 VWAP0/OPEN0 列时使用默认分 0.5"""
    df = pd.DataFrame({"avg_score": [1.0, 2.0]})
    scores = _score_vwap(df)
    assert (scores == 0.5).all()


def test_score_vwap_above_open_is_better():
    """验证 VWAP0 > OPEN0 时得分更高"""
    df = pd.DataFrame({
        "OPEN0": [1.0, 1.0],
        "VWAP0": [1.05, 0.95],  # 第一行 VWAP > OPEN，第二行 VWAP < OPEN
    })
    scores = _score_vwap(df)
    assert scores.iloc[0] > scores.iloc[1]


# ── compute_composite_score ───────────────────────────────────────────────────

def test_composite_score_columns():
    """验证综合得分计算后新增了正确的列"""
    df = _make_sample_df()
    result = compute_composite_score(df)
    for col in ["score_avg_score", "score_pos_ratio", "score_low_vol",
                "score_trend", "score_vwap", "composite_score"]:
        assert col in result.columns


def test_composite_score_range():
    """验证综合得分在 [0, 1] 范围内（加权平均权重之和为 1）"""
    df = _make_sample_df()
    result = compute_composite_score(df)
    assert result["composite_score"].min() >= 0.0
    assert result["composite_score"].max() <= 1.0


def test_composite_score_weights_sum():
    """验证权重之和为 1"""
    from pick_top_stocks import (
        WEIGHT_AVG_SCORE, WEIGHT_POS_RATIO, WEIGHT_LOW_VOL,
        WEIGHT_TREND, WEIGHT_VWAP,
    )
    total = WEIGHT_AVG_SCORE + WEIGHT_POS_RATIO + WEIGHT_LOW_VOL + WEIGHT_TREND + WEIGHT_VWAP
    assert total == pytest.approx(1.0)


# ── pick_top_stocks（端到端）──────────────────────────────────────────────────

def _create_mock_data_dir(tmp_path, date_str="2026-04-13", n=20):
    """在 tmp_path 下创建模拟 selection 目录和 filter_ret.csv"""
    subdir = tmp_path / "qlib_score_csv" / f"selection_{date_str.replace('-', '')}_{date_str.replace('-', ''[:6])}_10_00_00"
    subdir.mkdir(parents=True)
    df = _make_sample_df(n)
    csv_path = subdir / f"{date_str}_filter_ret.csv"
    df.to_csv(csv_path, index=False)
    return subdir


def test_pick_top_stocks_returns_df(tmp_path):
    """验证 pick_top_stocks 返回 DataFrame，行数不超过 top"""
    subdir = _create_mock_data_dir(tmp_path)
    result = pick_top_stocks(data_dir=str(subdir), top=5)
    assert isinstance(result, pd.DataFrame)
    assert len(result) <= 5
    assert len(result) > 0


def test_pick_top_stocks_top_3(tmp_path):
    """验证指定 top=3 时结果最多 3 行"""
    subdir = _create_mock_data_dir(tmp_path)
    result = pick_top_stocks(data_dir=str(subdir), top=3)
    assert len(result) <= 3


def test_pick_top_stocks_sorted_desc(tmp_path):
    """验证结果按综合评分降序排列"""
    subdir = _create_mock_data_dir(tmp_path, n=15)
    result = pick_top_stocks(data_dir=str(subdir), top=5)
    if "composite_score" in result.columns:
        scores = result["composite_score"].tolist()
        assert scores == sorted(scores, reverse=True)


def test_pick_top_stocks_output_csv(tmp_path):
    """验证 CSV 文件被正确保存"""
    subdir = _create_mock_data_dir(tmp_path)
    out_path = tmp_path / "my_picks.csv"
    result = pick_top_stocks(data_dir=str(subdir), top=5, output=str(out_path))
    assert out_path.exists()
    df_saved = pd.read_csv(out_path)
    assert len(df_saved) == len(result)


def test_pick_top_stocks_missing_dir():
    """验证目录不存在时抛出 FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        pick_top_stocks(data_dir="/non/existent/path")


def test_pick_top_stocks_no_qualifying_stocks(tmp_path):
    """验证所有股票都被过滤掉时返回空 DataFrame"""
    subdir = tmp_path / "selection_20260413_10_00_00"
    subdir.mkdir(parents=True)
    # 所有股票 avg_score <= 0
    df = pd.DataFrame({
        "instrument": ["SH600001"],
        "avg_score": [-0.1],
        "pos_ratio": [0.9],
    })
    (subdir / "2026-04-13_filter_ret.csv").write_text(df.to_csv(index=False))
    result = pick_top_stocks(data_dir=str(subdir), top=5)
    assert result.empty


def test_pick_top_stocks_real_data():
    """使用仓库中真实数据进行集成测试"""
    real_dir = Path(__file__).resolve().parent.parent / "qlib_score_csv" / "selection_20260413_15_31_02"
    if not real_dir.exists():
        pytest.skip("真实数据目录不存在，跳过集成测试")
    result = pick_top_stocks(data_dir=str(real_dir), top=5)
    assert len(result) > 0
    assert "composite_score" in result.columns
