import importlib.util
import inspect
from pathlib import Path

import pandas as pd


MODULE_PATH = Path(__file__).with_name("sim_trade_ci.py")
SPEC = importlib.util.spec_from_file_location("sim_trade_ci", MODULE_PATH)
sim_trade_ci = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(sim_trade_ci)


def test_select_trade_candidates_uses_same_score_ranking_for_all_hold_days():
    df = pd.DataFrame(
        {
            "instrument": ["A", "B", "C", "D", "E"],
            "avg_score": [0.12, 0.11, 0.10, 0.09, 0.08],
            "pos_ratio": [0.20, 0.95, 0.10, 0.99, 0.30],
            "STD20": [0.50, 0.01, 0.80, 0.02, 0.60],
            "STD60": [0.40, 0.01, 0.70, 0.02, 0.50],
            "ROC10": [2.00, 1.01, 1.80, 1.02, 1.70],
            "ROC20": [2.10, 1.02, 1.90, 1.03, 1.80],
        }
    )

    for hold_days in (1, 3, 5):
        selected = sim_trade_ci.select_trade_candidates(df, top_n=3, hold_days=hold_days)
        assert selected["instrument"].tolist() == ["A", "B", "C"]


def test_select_trade_candidates_keeps_top_n_even_with_non_positive_scores():
    df = pd.DataFrame(
        {
            "instrument": ["A", "B", "C", "D"],
            "avg_score": [0.09, 0.01, -0.02, -0.10],
        }
    )

    selected = sim_trade_ci.select_trade_candidates(df, top_n=3, hold_days=5)

    assert selected["instrument"].tolist() == ["A", "B", "C"]


def test_main_top_n_default_is_3():
    assert inspect.signature(sim_trade_ci.main).parameters["top_n"].default == 3
