# params 
 {'predict_dates': [{'end': '2026-05-11', 'start': '2026-05-11'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'analysis_folder': '~/.qlibAssistant/analysis/', 'dataset_name': 'Alpha158', 'model_filter': ['.*'], 'model_name': 'Linear', 'pfx_name': 'p', 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}], 'rolling_type': 'expanding', 'sfx_name': 's', 'step': 60, 'stock_pool': 'csi300', 'uri_folder': '~/.qlibAssistant/mlruns/'}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260512_11 700572644448500063 (Recorders: 6/6)

	Recorder: 0e93ca2267bf43bcb1e3835d6520aa00

		Model: {'id': '0e93ca2267bf43bcb1e3835d6520aa00', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.36, 'Rank IC': 0.054, 'Rank ICIR': 0.357}, 'data_train_vec': ['2020-05-12', '2024-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.357', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: 694266de9ca64a59afcc9611d89c7d65

		Model: {'id': '694266de9ca64a59afcc9611d89c7d65', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.222, 'Rank IC': 0.046, 'Rank ICIR': 0.301}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.301', 'recency_weight': '0.174', 'weight': '0.012'}

	Recorder: d613f477a96c43ed91138d37d66e67d4

		Model: {'id': 'd613f477a96c43ed91138d37d66e67d4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.242, 'Rank IC': 0.054, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.345', 'recency_weight': '0.245', 'weight': '0.022'}

	Recorder: d69a4296f4174c33a50d13ae4ed2b92b

		Model: {'id': 'd69a4296f4174c33a50d13ae4ed2b92b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.116, 'Rank IC': 0.037, 'Rank ICIR': 0.234}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.234', 'recency_weight': '0.349', 'weight': '0.014'}

	Recorder: 1421e655961e4da682354dc856972315

		Model: {'id': '1421e655961e4da682354dc856972315', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.192, 'Rank IC': 0.032, 'Rank ICIR': 0.267}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.267', 'recency_weight': '0.498', 'weight': '0.027'}

	Recorder: 045e06fbb2e140ac9d817d3277abb3fa

		Model: {'id': '045e06fbb2e140ac9d817d3277abb3fa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.61, 'Rank IC': 0.055, 'Rank ICIR': 0.505}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.505', 'recency_weight': '0.710', 'weight': '0.137'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260512_11 735675075810340014 (Recorders: 5/6)

	Recorder: de3a8302e78e4c408f9d0483e1a515a8

		Model: {'id': 'de3a8302e78e4c408f9d0483e1a515a8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.346, 'Rank IC': 0.055, 'Rank ICIR': 0.354}, 'data_train_vec': ['2020-05-12', '2024-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.354', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: 8f4d3fd9ec1d416a8ba5eb4218a13d7f

		Model: {'id': '8f4d3fd9ec1d416a8ba5eb4218a13d7f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.194, 'Rank IC': 0.045, 'Rank ICIR': 0.3}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.300', 'recency_weight': '0.174', 'weight': '0.012'}

	Recorder: 8c152c54d0d44e60a80d49fac2e0dcca

		Model: {'id': '8c152c54d0d44e60a80d49fac2e0dcca', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.148, 'Rank IC': 0.048, 'Rank ICIR': 0.287}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.287', 'recency_weight': '0.245', 'weight': '0.015'}

	Recorder: 1a07e40d4a474597b7e7c95fb13f2120

		Model: {'id': '1a07e40d4a474597b7e7c95fb13f2120', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.125, 'Rank IC': 0.039, 'Rank ICIR': 0.322}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.322', 'recency_weight': '0.498', 'weight': '0.039'}

	Recorder: 4ff1d4030e79438badc420705df7388e

		Model: {'id': '4ff1d4030e79438badc420705df7388e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.377, 'Rank IC': 0.044, 'Rank ICIR': 0.523}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.523', 'recency_weight': '0.710', 'weight': '0.147'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260512_11 870703443919126381 (Recorders: 4/6)

	Recorder: d0093f9410584942ab8ded4ee45290f7

		Model: {'id': 'd0093f9410584942ab8ded4ee45290f7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.33, 'Rank IC': 0.055, 'Rank ICIR': 0.438}, 'data_train_vec': ['2020-05-12', '2024-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.438', 'recency_weight': '0.122', 'weight': '0.018'}

	Recorder: f401bd97d8e840d3afacebed1f3cf545

		Model: {'id': 'f401bd97d8e840d3afacebed1f3cf545', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.234, 'Rank IC': 0.049, 'Rank ICIR': 0.402}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.402', 'recency_weight': '0.174', 'weight': '0.021'}

	Recorder: df0522dc4e5f4ec186441c8e15e38e78

		Model: {'id': 'df0522dc4e5f4ec186441c8e15e38e78', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.16, 'Rank IC': 0.055, 'Rank ICIR': 0.376}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.376', 'recency_weight': '0.245', 'weight': '0.026'}

	Recorder: fdd21e2935154a98a0bebfdb21533d58

		Model: {'id': 'fdd21e2935154a98a0bebfdb21533d58', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.39, 'Rank IC': 0.051, 'Rank ICIR': 0.421}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.421', 'recency_weight': '0.710', 'weight': '0.095'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260512_11 571763362449041142 (Recorders: 6/6)

	Recorder: 253e9f5fdeab46b0b0b40008bad4d96b

		Model: {'id': '253e9f5fdeab46b0b0b40008bad4d96b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.316, 'Rank IC': 0.052, 'Rank ICIR': 0.348}, 'data_train_vec': ['2020-05-12', '2024-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.348', 'recency_weight': '0.122', 'weight': '0.011'}

	Recorder: 8cdde68f325f4968aa06efd0d7381581

		Model: {'id': '8cdde68f325f4968aa06efd0d7381581', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.185, 'Rank IC': 0.043, 'Rank ICIR': 0.312}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.312', 'recency_weight': '0.174', 'weight': '0.013'}

	Recorder: c557b4765b9746589b1386eb722b0671

		Model: {'id': 'c557b4765b9746589b1386eb722b0671', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.229, 'Rank IC': 0.055, 'Rank ICIR': 0.344}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.344', 'recency_weight': '0.245', 'weight': '0.022'}

	Recorder: 542f454ce2334d94bfdf8db244a35aed

		Model: {'id': '542f454ce2334d94bfdf8db244a35aed', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.234, 'Rank IC': 0.046, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.304', 'recency_weight': '0.349', 'weight': '0.024'}

	Recorder: 8531ed6c3b4f4832af83af992431af8d

		Model: {'id': '8531ed6c3b4f4832af83af992431af8d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.17, 'Rank IC': 0.038, 'Rank ICIR': 0.346}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.346', 'recency_weight': '0.498', 'weight': '0.045'}

	Recorder: 26a2036e0fc04a959c96e1da66a05091

		Model: {'id': '26a2036e0fc04a959c96e1da66a05091', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.495, 'Rank IC': 0.065, 'Rank ICIR': 0.719}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.719', 'recency_weight': '0.710', 'weight': '0.277'}
