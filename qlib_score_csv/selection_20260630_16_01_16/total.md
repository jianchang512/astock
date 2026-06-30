# params 
 {'predict_dates': [{'start': '2026-06-30', 'end': '2026-06-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260630_15 931242738107251229 (Recorders: 6/6)

	Recorder: 74621a58e1184942a2c10ff58b92b0dd

		Model: {'id': '74621a58e1184942a2c10ff58b92b0dd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.322, 'Rank IC': 0.065, 'Rank ICIR': 0.434}, 'data_train_vec': ['2020-06-30', '2024-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.434', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 2203fcd6ad4b4a7ca7bab61b2ba09ce4

		Model: {'id': '2203fcd6ad4b4a7ca7bab61b2ba09ce4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.222, 'Rank IC': 0.068, 'Rank ICIR': 0.407}, 'data_train_vec': ['2021-06-30', '2025-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.407', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: 7c1fb7e0922d474cbe23120b58454d62

		Model: {'id': '7c1fb7e0922d474cbe23120b58454d62', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.147, 'Rank IC': 0.064, 'Rank ICIR': 0.385}, 'data_train_vec': ['2022-06-28', '2025-06-27'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.385', 'recency_weight': '0.242', 'weight': '0.026'}

	Recorder: 59085078b00148a994937173314c2136

		Model: {'id': '59085078b00148a994937173314c2136', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.34, 'Rank IC': 0.073, 'Rank ICIR': 0.465}, 'data_train_vec': ['2023-06-30', '2025-09-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.465', 'recency_weight': '0.348', 'weight': '0.054'}

	Recorder: 8d43d797ab0848b9a4ddaf023f81a348

		Model: {'id': '8d43d797ab0848b9a4ddaf023f81a348', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.43, 'Rank IC': 0.063, 'Rank ICIR': 0.462}, 'data_train_vec': ['2024-06-30', '2025-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.462', 'recency_weight': '0.494', 'weight': '0.076'}

	Recorder: aae2323da9f14b8da983e2080e392ac3

		Model: {'id': 'aae2323da9f14b8da983e2080e392ac3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.112, 'ICIR': 0.61, 'Rank IC': 0.063, 'Rank ICIR': 0.363}, 'data_train_vec': ['2025-06-30', '2026-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.363', 'recency_weight': '0.699', 'weight': '0.066'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260630_15 261876153372976117 (Recorders: 6/6)

	Recorder: 3a5b64b3405c471dba78c61e5f02930e

		Model: {'id': '3a5b64b3405c471dba78c61e5f02930e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.315, 'Rank IC': 0.064, 'Rank ICIR': 0.431}, 'data_train_vec': ['2020-06-30', '2024-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.431', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: cfdb10f2a4484bdebe9089696d2e7a3b

		Model: {'id': 'cfdb10f2a4484bdebe9089696d2e7a3b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.195, 'Rank IC': 0.064, 'Rank ICIR': 0.387}, 'data_train_vec': ['2021-06-30', '2025-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.387', 'recency_weight': '0.171', 'weight': '0.018'}

	Recorder: 4bdbb30ca9ba4f1ebd2fbfb44be30c2e

		Model: {'id': '4bdbb30ca9ba4f1ebd2fbfb44be30c2e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.091, 'Rank IC': 0.059, 'Rank ICIR': 0.36}, 'data_train_vec': ['2022-06-28', '2025-06-27'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.360', 'recency_weight': '0.242', 'weight': '0.023'}

	Recorder: 9b91f320a0334cdab9aef02b9284fc2f

		Model: {'id': '9b91f320a0334cdab9aef02b9284fc2f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.288, 'Rank IC': 0.073, 'Rank ICIR': 0.458}, 'data_train_vec': ['2023-06-30', '2025-09-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.458', 'recency_weight': '0.348', 'weight': '0.053'}

	Recorder: 37bb2b49d2894d85be3afe7cb3d71ccf

		Model: {'id': '37bb2b49d2894d85be3afe7cb3d71ccf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.343, 'Rank IC': 0.064, 'Rank ICIR': 0.499}, 'data_train_vec': ['2024-06-30', '2025-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.499', 'recency_weight': '0.494', 'weight': '0.089'}

	Recorder: a853ff751f024b4caa76852ed529027d

		Model: {'id': 'a853ff751f024b4caa76852ed529027d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.125, 'ICIR': 0.607, 'Rank IC': 0.096, 'Rank ICIR': 0.49}, 'data_train_vec': ['2025-06-30', '2026-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.490', 'recency_weight': '0.699', 'weight': '0.121'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260630_15 160954989248680105 (Recorders: 5/6)

	Recorder: b2cada9bc94a4056ab1b5ad9f6315b67

		Model: {'id': 'b2cada9bc94a4056ab1b5ad9f6315b67', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.279, 'Rank IC': 0.063, 'Rank ICIR': 0.441}, 'data_train_vec': ['2020-06-30', '2024-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.441', 'recency_weight': '0.121', 'weight': '0.017'}

	Recorder: c58803e774514a258a8d2d93c266dd00

		Model: {'id': 'c58803e774514a258a8d2d93c266dd00', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.132, 'Rank IC': 0.057, 'Rank ICIR': 0.371}, 'data_train_vec': ['2021-06-30', '2025-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.371', 'recency_weight': '0.171', 'weight': '0.017'}

	Recorder: 610663ed2cd14fe79cdadf27df7af59c

		Model: {'id': '610663ed2cd14fe79cdadf27df7af59c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.238, 'Rank IC': 0.056, 'Rank ICIR': 0.42}, 'data_train_vec': ['2023-06-30', '2025-09-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.420', 'recency_weight': '0.348', 'weight': '0.044'}

	Recorder: 790169cd1f434016bab695ed09271998

		Model: {'id': '790169cd1f434016bab695ed09271998', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.217, 'Rank IC': 0.045, 'Rank ICIR': 0.316}, 'data_train_vec': ['2024-06-30', '2025-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.316', 'recency_weight': '0.494', 'weight': '0.036'}

	Recorder: 66b85c30c28c42f898c5d5de2eddfbc7

		Model: {'id': '66b85c30c28c42f898c5d5de2eddfbc7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.082, 'ICIR': 0.375, 'Rank IC': 0.069, 'Rank ICIR': 0.354}, 'data_train_vec': ['2025-06-30', '2026-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.354', 'recency_weight': '0.699', 'weight': '0.063'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260630_15 295347539227783316 (Recorders: 6/6)

	Recorder: dab40f50d9aa4a38946bbe5da3359355

		Model: {'id': 'dab40f50d9aa4a38946bbe5da3359355', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.319, 'Rank IC': 0.064, 'Rank ICIR': 0.452}, 'data_train_vec': ['2020-06-30', '2024-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.452', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: fc72a7dc2cfd42f7bdcf93678f8f986d

		Model: {'id': 'fc72a7dc2cfd42f7bdcf93678f8f986d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.181, 'Rank IC': 0.068, 'Rank ICIR': 0.444}, 'data_train_vec': ['2021-06-30', '2025-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.444', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: dc86d33ab4e843269f0f066b42c2390a

		Model: {'id': 'dc86d33ab4e843269f0f066b42c2390a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.087, 'Rank IC': 0.056, 'Rank ICIR': 0.35}, 'data_train_vec': ['2022-06-28', '2025-06-27'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.350', 'recency_weight': '0.242', 'weight': '0.021'}

	Recorder: 91c21e6636ab44cf9031d7004bae3494

		Model: {'id': '91c21e6636ab44cf9031d7004bae3494', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.296, 'Rank IC': 0.07, 'Rank ICIR': 0.502}, 'data_train_vec': ['2023-06-30', '2025-09-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.502', 'recency_weight': '0.348', 'weight': '0.063'}

	Recorder: ccbe425aa5e04110bc08c24a8f8085b3

		Model: {'id': 'ccbe425aa5e04110bc08c24a8f8085b3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.206, 'Rank IC': 0.055, 'Rank ICIR': 0.435}, 'data_train_vec': ['2024-06-30', '2025-12-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.435', 'recency_weight': '0.494', 'weight': '0.067'}

	Recorder: 24d1c97be97049629d194ce50616dd8d

		Model: {'id': '24d1c97be97049629d194ce50616dd8d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.419, 'Rank IC': 0.048, 'Rank ICIR': 0.316}, 'data_train_vec': ['2025-06-30', '2026-03-29'], 'train_time_vec': ['2026-06-30', '2026-06-30'], 'rank_icir': '0.316', 'recency_weight': '0.699', 'weight': '0.050'}
