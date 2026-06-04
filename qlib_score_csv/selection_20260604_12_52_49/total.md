# params 
 {'predict_dates': [{'start': '2026-06-04', 'end': '2026-06-04'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260604_12 587775687816493107 (Recorders: 6/6)

	Recorder: 8a158b61c7424c13b3b67499367cd8cf

		Model: {'id': '8a158b61c7424c13b3b67499367cd8cf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.327, 'Rank IC': 0.059, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-06-04', '2024-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 4c6ab5c0af1649968860eca682999f73

		Model: {'id': '4c6ab5c0af1649968860eca682999f73', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.208, 'Rank IC': 0.06, 'Rank ICIR': 0.396}, 'data_train_vec': ['2021-06-04', '2025-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.396', 'recency_weight': '0.171', 'weight': '0.023'}

	Recorder: b002bb1ced01462f977934c69aea2166

		Model: {'id': 'b002bb1ced01462f977934c69aea2166', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.205, 'Rank IC': 0.064, 'Rank ICIR': 0.375}, 'data_train_vec': ['2022-06-04', '2025-06-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.375', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 4f60696cfef8477aa61b65eeb75f74ea

		Model: {'id': '4f60696cfef8477aa61b65eeb75f74ea', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.261, 'Rank IC': 0.065, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-06-04', '2025-09-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.377', 'recency_weight': '0.348', 'weight': '0.042'}

	Recorder: 79c43d289bbf414aba1dbf38368219c8

		Model: {'id': '79c43d289bbf414aba1dbf38368219c8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.251, 'Rank IC': 0.072, 'Rank ICIR': 0.507}, 'data_train_vec': ['2024-06-04', '2025-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.507', 'recency_weight': '0.494', 'weight': '0.109'}

	Recorder: 468808dd9bb2433692f77c0b9c7a923a

		Model: {'id': '468808dd9bb2433692f77c0b9c7a923a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.083, 'ICIR': 0.487, 'Rank IC': 0.057, 'Rank ICIR': 0.321}, 'data_train_vec': ['2025-06-04', '2026-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.321', 'recency_weight': '0.699', 'weight': '0.062'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260604_12 654556548037327529 (Recorders: 6/6)

	Recorder: a4d830dd60cc4f40adec18b4f6181b20

		Model: {'id': 'a4d830dd60cc4f40adec18b4f6181b20', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.31, 'Rank IC': 0.058, 'Rank ICIR': 0.375}, 'data_train_vec': ['2020-06-04', '2024-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.375', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: c21aed9173f44f22a8e4c13325c3b487

		Model: {'id': 'c21aed9173f44f22a8e4c13325c3b487', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.202, 'Rank IC': 0.058, 'Rank ICIR': 0.389}, 'data_train_vec': ['2021-06-04', '2025-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.389', 'recency_weight': '0.171', 'weight': '0.022'}

	Recorder: 99afe605e87744b5b1eb2bac70bafe4a

		Model: {'id': '99afe605e87744b5b1eb2bac70bafe4a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.095, 'Rank IC': 0.057, 'Rank ICIR': 0.322}, 'data_train_vec': ['2022-06-04', '2025-06-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.322', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: d0a173b14e7f42caa5e7870afa58749f

		Model: {'id': 'd0a173b14e7f42caa5e7870afa58749f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.213, 'Rank IC': 0.066, 'Rank ICIR': 0.391}, 'data_train_vec': ['2023-06-04', '2025-09-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.391', 'recency_weight': '0.348', 'weight': '0.046'}

	Recorder: 495c357886404378b3dd7a38731cab2e

		Model: {'id': '495c357886404378b3dd7a38731cab2e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.132, 'Rank IC': 0.054, 'Rank ICIR': 0.38}, 'data_train_vec': ['2024-06-04', '2025-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.380', 'recency_weight': '0.494', 'weight': '0.061'}

	Recorder: 884fae4c086b47e486b84c33020efe60

		Model: {'id': '884fae4c086b47e486b84c33020efe60', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.341, 'Rank IC': 0.036, 'Rank ICIR': 0.244}, 'data_train_vec': ['2025-06-04', '2026-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.244', 'recency_weight': '0.699', 'weight': '0.036'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260604_12 263118647268102918 (Recorders: 6/6)

	Recorder: b0c562962cbe48b6ad90b1d940b3a55e

		Model: {'id': 'b0c562962cbe48b6ad90b1d940b3a55e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.329, 'Rank IC': 0.064, 'Rank ICIR': 0.465}, 'data_train_vec': ['2020-06-04', '2024-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.465', 'recency_weight': '0.121', 'weight': '0.022'}

	Recorder: 12ee8ddb4ce944d5bc537ff6a2e8d984

		Model: {'id': '12ee8ddb4ce944d5bc537ff6a2e8d984', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.242, 'Rank IC': 0.066, 'Rank ICIR': 0.479}, 'data_train_vec': ['2021-06-04', '2025-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.479', 'recency_weight': '0.171', 'weight': '0.034'}

	Recorder: 5277295255804d89a1874c1c588c0689

		Model: {'id': '5277295255804d89a1874c1c588c0689', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.096, 'Rank IC': 0.056, 'Rank ICIR': 0.372}, 'data_train_vec': ['2022-06-04', '2025-06-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.372', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: cae6c95219ec43239cc31e7c560857a9

		Model: {'id': 'cae6c95219ec43239cc31e7c560857a9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.099, 'Rank IC': 0.045, 'Rank ICIR': 0.308}, 'data_train_vec': ['2023-06-04', '2025-09-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.308', 'recency_weight': '0.348', 'weight': '0.028'}

	Recorder: eebee009cba7457584322da955fe2243

		Model: {'id': 'eebee009cba7457584322da955fe2243', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.216, 'Rank IC': 0.052, 'Rank ICIR': 0.408}, 'data_train_vec': ['2024-06-04', '2025-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.408', 'recency_weight': '0.494', 'weight': '0.071'}

	Recorder: 38772465639841a6b9efdd30d43869c4

		Model: {'id': '38772465639841a6b9efdd30d43869c4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.408, 'Rank IC': 0.074, 'Rank ICIR': 0.376}, 'data_train_vec': ['2025-06-04', '2026-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.376', 'recency_weight': '0.699', 'weight': '0.085'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260604_11 864187676594804493 (Recorders: 6/6)

	Recorder: d65d8023aba24a11aa8ab5ece76023f9

		Model: {'id': 'd65d8023aba24a11aa8ab5ece76023f9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.279, 'Rank IC': 0.055, 'Rank ICIR': 0.362}, 'data_train_vec': ['2020-06-04', '2024-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.362', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 4c57f1b50dbc42cdbe6f198adde3a8e6

		Model: {'id': '4c57f1b50dbc42cdbe6f198adde3a8e6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.17, 'Rank IC': 0.055, 'Rank ICIR': 0.394}, 'data_train_vec': ['2021-06-04', '2025-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.394', 'recency_weight': '0.171', 'weight': '0.023'}

	Recorder: 2be66cc19c224ff5a2d6d5a7ee445b54

		Model: {'id': '2be66cc19c224ff5a2d6d5a7ee445b54', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.195, 'Rank IC': 0.066, 'Rank ICIR': 0.402}, 'data_train_vec': ['2022-06-04', '2025-06-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.402', 'recency_weight': '0.244', 'weight': '0.034'}

	Recorder: 1ced1166786d4c04af3fa1527b9ddcaa

		Model: {'id': '1ced1166786d4c04af3fa1527b9ddcaa', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.272, 'Rank IC': 0.062, 'Rank ICIR': 0.384}, 'data_train_vec': ['2023-06-04', '2025-09-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.384', 'recency_weight': '0.348', 'weight': '0.044'}

	Recorder: 0d9b9e4a23884f13b51d0ed1eba8ba8c

		Model: {'id': '0d9b9e4a23884f13b51d0ed1eba8ba8c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.24, 'Rank IC': 0.057, 'Rank ICIR': 0.417}, 'data_train_vec': ['2024-06-04', '2025-12-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.417', 'recency_weight': '0.494', 'weight': '0.074'}

	Recorder: 89081fdc371249a6884cc5f8ee277255

		Model: {'id': '89081fdc371249a6884cc5f8ee277255', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.549, 'Rank IC': 0.047, 'Rank ICIR': 0.317}, 'data_train_vec': ['2025-06-04', '2026-03-03'], 'train_time_vec': ['2026-06-04', '2026-06-04'], 'rank_icir': '0.317', 'recency_weight': '0.699', 'weight': '0.060'}
