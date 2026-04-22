# params 
 {'predict_dates': [{'start': '2026-04-22', 'end': '2026-04-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260422_12 418161340694875724 (Recorders: 6/6)

	Recorder: 8d73a8a5661e4e68aa33808f606f2bec

		Model: {'id': '8d73a8a5661e4e68aa33808f606f2bec', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.4, 'Rank IC': 0.055, 'Rank ICIR': 0.322}, 'data_train_vec': ['2020-04-22', '2024-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.322', 'recency_weight': '0.121', 'weight': '0.011'}

	Recorder: 955f1856bce74eda98fa7b68c48f3a2a

		Model: {'id': '955f1856bce74eda98fa7b68c48f3a2a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.283, 'Rank IC': 0.05, 'Rank ICIR': 0.327}, 'data_train_vec': ['2021-04-22', '2025-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.327', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: 95953b3ea638413da1a6ef10e67b7a78

		Model: {'id': '95953b3ea638413da1a6ef10e67b7a78', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.181, 'Rank IC': 0.041, 'Rank ICIR': 0.251}, 'data_train_vec': ['2022-04-22', '2025-04-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.251', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: ecf7dbf5ee98478da3e7e8a370e36281

		Model: {'id': 'ecf7dbf5ee98478da3e7e8a370e36281', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.252, 'Rank IC': 0.063, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-04-22', '2025-07-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.377', 'recency_weight': '0.347', 'weight': '0.044'}

	Recorder: 7f5b0837396046388d2b6508c54c9af5

		Model: {'id': '7f5b0837396046388d2b6508c54c9af5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.196, 'Rank IC': 0.035, 'Rank ICIR': 0.271}, 'data_train_vec': ['2024-04-22', '2025-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.271', 'recency_weight': '0.494', 'weight': '0.032'}

	Recorder: 05dc215a8fa9479c810b69c2d5e309a2

		Model: {'id': '05dc215a8fa9479c810b69c2d5e309a2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.081, 'ICIR': 0.504, 'Rank IC': 0.094, 'Rank ICIR': 0.566}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.566', 'recency_weight': '0.704', 'weight': '0.200'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260422_12 246120609231080705 (Recorders: 6/6)

	Recorder: d82c94699af24f188a98bbca19bd0eda

		Model: {'id': 'd82c94699af24f188a98bbca19bd0eda', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.33, 'Rank IC': 0.056, 'Rank ICIR': 0.32}, 'data_train_vec': ['2020-04-22', '2024-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.320', 'recency_weight': '0.121', 'weight': '0.011'}

	Recorder: 40b581928393491291235aced808b534

		Model: {'id': '40b581928393491291235aced808b534', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.215, 'Rank IC': 0.046, 'Rank ICIR': 0.304}, 'data_train_vec': ['2021-04-22', '2025-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.304', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 92af581bb58d4d1fb2130e4124e921b3

		Model: {'id': '92af581bb58d4d1fb2130e4124e921b3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.095, 'Rank IC': 0.036, 'Rank ICIR': 0.221}, 'data_train_vec': ['2022-04-22', '2025-04-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.221', 'recency_weight': '0.244', 'weight': '0.011'}

	Recorder: 6d9e43df0c7343cd96f9f185355e196f

		Model: {'id': '6d9e43df0c7343cd96f9f185355e196f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.176, 'Rank IC': 0.067, 'Rank ICIR': 0.411}, 'data_train_vec': ['2023-04-22', '2025-07-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.411', 'recency_weight': '0.347', 'weight': '0.052'}

	Recorder: 10a8bf9fa09b48db9214984d87a03d25

		Model: {'id': '10a8bf9fa09b48db9214984d87a03d25', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.105, 'Rank IC': 0.03, 'Rank ICIR': 0.212}, 'data_train_vec': ['2024-04-22', '2025-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.212', 'recency_weight': '0.494', 'weight': '0.020'}

	Recorder: 933651e31f6c409d8886350518dc2f73

		Model: {'id': '933651e31f6c409d8886350518dc2f73', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.594, 'Rank IC': 0.086, 'Rank ICIR': 0.551}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.551', 'recency_weight': '0.704', 'weight': '0.190'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260422_11 901630189126926889 (Recorders: 4/6)

	Recorder: 93159090b44c4007863c3f879208ec32

		Model: {'id': '93159090b44c4007863c3f879208ec32', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.347, 'Rank IC': 0.058, 'Rank ICIR': 0.429}, 'data_train_vec': ['2020-04-22', '2024-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.429', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: e4d55d55bd8d4206a87bf0aa259195cc

		Model: {'id': 'e4d55d55bd8d4206a87bf0aa259195cc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.253, 'Rank IC': 0.049, 'Rank ICIR': 0.413}, 'data_train_vec': ['2021-04-22', '2025-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.413', 'recency_weight': '0.173', 'weight': '0.026'}

	Recorder: 9a8a879a6e5a44b397f0effe62104017

		Model: {'id': '9a8a879a6e5a44b397f0effe62104017', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.171, 'Rank IC': 0.049, 'Rank ICIR': 0.337}, 'data_train_vec': ['2022-04-22', '2025-04-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.337', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 2227a379f11e42d09b25ed2683544f5b

		Model: {'id': '2227a379f11e42d09b25ed2683544f5b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.385, 'Rank IC': 0.055, 'Rank ICIR': 0.311}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.311', 'recency_weight': '0.704', 'weight': '0.061'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260422_11 514458813675400144 (Recorders: 6/6)

	Recorder: ec123c8435cb4b41b3e3082dbbcb6cdf

		Model: {'id': 'ec123c8435cb4b41b3e3082dbbcb6cdf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.358, 'Rank IC': 0.057, 'Rank ICIR': 0.337}, 'data_train_vec': ['2020-04-22', '2024-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.337', 'recency_weight': '0.121', 'weight': '0.012'}

	Recorder: b82e0f199be7419e9e2a177f00a7ebf1

		Model: {'id': 'b82e0f199be7419e9e2a177f00a7ebf1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.24, 'Rank IC': 0.047, 'Rank ICIR': 0.313}, 'data_train_vec': ['2021-04-22', '2025-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.313', 'recency_weight': '0.173', 'weight': '0.015'}

	Recorder: 8694f4fa1174481d8c45fa374aed4fcc

		Model: {'id': '8694f4fa1174481d8c45fa374aed4fcc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.136, 'Rank IC': 0.04, 'Rank ICIR': 0.258}, 'data_train_vec': ['2022-04-22', '2025-04-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.258', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: 17fe41edf1494a579a07a98354c68acc

		Model: {'id': '17fe41edf1494a579a07a98354c68acc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.227, 'Rank IC': 0.065, 'Rank ICIR': 0.404}, 'data_train_vec': ['2023-04-22', '2025-07-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.404', 'recency_weight': '0.347', 'weight': '0.050'}

	Recorder: 4658420679194e65a9a8000b880b23e3

		Model: {'id': '4658420679194e65a9a8000b880b23e3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.244, 'Rank IC': 0.036, 'Rank ICIR': 0.284}, 'data_train_vec': ['2024-04-22', '2025-10-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.284', 'recency_weight': '0.494', 'weight': '0.035'}

	Recorder: 48ce94893f0f4a0a996736e24ed129e8

		Model: {'id': '48ce94893f0f4a0a996736e24ed129e8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.375, 'Rank IC': 0.073, 'Rank ICIR': 0.449}, 'data_train_vec': ['2025-04-22', '2026-01-21'], 'train_time_vec': ['2026-04-22', '2026-04-22'], 'rank_icir': '0.449', 'recency_weight': '0.704', 'weight': '0.126'}
