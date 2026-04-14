import importlib.util
from pathlib import Path

import pandas as pd


MODULE_PATH = Path(__file__).with_name("sim_trade_ci.py")
SPEC = importlib.util.spec_from_file_location("sim_trade_ci", MODULE_PATH)
sim_trade_ci = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(sim_trade_ci)


def test_select_trade_candidates_filters_low_confidence_and_negative_scores():
    df = pd.DataFrame(
        {
            "instrument": ["A", "B", "C", "D", "E", "F"],
            "avg_score": [0.12, 0.11, 0.08, 0.07, 0.06, -0.02],
            "pos_ratio": [1.0, 0.50, 0.95, 0.90, 0.80, 1.0],
            "STD20": [0.01, 0.01, 0.01, 0.04, 0.01, 0.01],
            "STD60": [0.01, 0.01, 0.01, 0.03, 0.01, 0.01],
            "ROC10": [1.02, 1.01, 1.03, 1.10, 1.20, 1.01],
            "ROC20": [1.03, 1.02, 1.04, 1.12, 1.18, 1.02],
        }
    )

    selected = sim_trade_ci.select_trade_candidates(df, top_n=5, hold_days=1)

    assert selected["instrument"].tolist() == ["A", "C"]


def test_select_trade_candidates_reduces_position_count_for_longer_holds():
    df = pd.DataFrame(
        {
            "instrument": [f"S{i}" for i in range(10)],
            "avg_score": [0.12, 0.11, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03],
            "pos_ratio": [1.0, 1.0, 0.95, 0.95, 0.90, 0.90, 0.85, 0.85, 0.80, 0.80],
            "STD20": [0.01] * 10,
            "STD60": [0.01] * 10,
            "ROC10": [1.02] * 10,
            "ROC20": [1.03] * 10,
        }
    )

    selected = sim_trade_ci.select_trade_candidates(df, top_n=10, hold_days=5)

    assert len(selected) == 4
    assert selected["instrument"].tolist() == ["S0", "S1", "S2", "S3"]


def test_select_trade_candidates_works_without_optional_factor_columns():
    df = pd.DataFrame(
        {
            "instrument": ["A", "B", "C", "D"],
            "avg_score": [0.09, 0.05, 0.04, 0.01],
            "pos_ratio": [1.0, 0.8, 0.7, 0.6],
        }
    )

    selected = sim_trade_ci.select_trade_candidates(df, top_n=3, hold_days=3)

    assert selected["instrument"].tolist() == ["A", "B"]
