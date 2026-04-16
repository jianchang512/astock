# params 
 {'predict_dates': [{'start': '2026-04-16', 'end': '2026-04-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260416_12 376548625562987440 (Recorders: 6/6)

	Recorder: 213c2ff2256045148ef7e75915d3e51a

		Model: {'id': '213c2ff2256045148ef7e75915d3e51a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.44, 'Rank IC': 0.064, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: a331b0f304a34c3a83e43872bfb2f419

		Model: {'id': 'a331b0f304a34c3a83e43872bfb2f419', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.346, 'Rank IC': 0.054, 'Rank ICIR': 0.354}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.354', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: 36900c1864a449349538264cd57fa111

		Model: {'id': '36900c1864a449349538264cd57fa111', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.205, 'Rank IC': 0.044, 'Rank ICIR': 0.251}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: c47d90f0188d4426938190154476a159

		Model: {'id': 'c47d90f0188d4426938190154476a159', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.395, 'Rank IC': 0.064, 'Rank ICIR': 0.419}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.347', 'weight': '0.067'}

	Recorder: 5622005af8a04e56a85e197dd1e0a215

		Model: {'id': '5622005af8a04e56a85e197dd1e0a215', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.205, 'Rank IC': 0.029, 'Rank ICIR': 0.212}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.212', 'recency_weight': '0.494', 'weight': '0.025'}

	Recorder: fdad04bd42b44b8e90c3c52f9c22290c

		Model: {'id': 'fdad04bd42b44b8e90c3c52f9c22290c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.351, 'Rank IC': 0.069, 'Rank ICIR': 0.352}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.352', 'recency_weight': '0.704', 'weight': '0.097'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260416_12 615374535272986987 (Recorders: 6/6)

	Recorder: 7a8a8895e9ee451c87771ef8d3b490a0

		Model: {'id': '7a8a8895e9ee451c87771ef8d3b490a0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.406, 'Rank IC': 0.061, 'Rank ICIR': 0.347}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.347', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 160aaaf27a03414e8e41c52279029d28

		Model: {'id': '160aaaf27a03414e8e41c52279029d28', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.284, 'Rank IC': 0.051, 'Rank ICIR': 0.319}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.319', 'recency_weight': '0.173', 'weight': '0.019'}

	Recorder: b8b99d8d95c14c449e598760ea1841ca

		Model: {'id': 'b8b99d8d95c14c449e598760ea1841ca', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.134, 'Rank IC': 0.038, 'Rank ICIR': 0.22}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.220', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: 078328b635374070bee2080990a58c8a

		Model: {'id': '078328b635374070bee2080990a58c8a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.169, 'Rank IC': 0.063, 'Rank ICIR': 0.4}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.400', 'recency_weight': '0.347', 'weight': '0.062'}

	Recorder: b15505e45ad44cca86b0211c9980d079

		Model: {'id': 'b15505e45ad44cca86b0211c9980d079', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.227, 'Rank IC': 0.044, 'Rank ICIR': 0.331}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.331', 'recency_weight': '0.494', 'weight': '0.060'}

	Recorder: 582ab9553d0643698a0b1d3707c3051f

		Model: {'id': '582ab9553d0643698a0b1d3707c3051f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.299, 'Rank IC': 0.064, 'Rank ICIR': 0.329}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.329', 'recency_weight': '0.704', 'weight': '0.085'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260416_11 867483191204464156 (Recorders: 5/6)

	Recorder: 14181f213e8e4d3aa11bfd6cd07927d3

		Model: {'id': '14181f213e8e4d3aa11bfd6cd07927d3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.396, 'Rank IC': 0.063, 'Rank ICIR': 0.467}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.467', 'recency_weight': '0.121', 'weight': '0.029'}

	Recorder: 566a4b1e748b4cf581f5065ba10d2f80

		Model: {'id': '566a4b1e748b4cf581f5065ba10d2f80', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.342, 'Rank IC': 0.055, 'Rank ICIR': 0.474}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.474', 'recency_weight': '0.173', 'weight': '0.043'}

	Recorder: 009e7e79a27e41ea9ea6538e89489102

		Model: {'id': '009e7e79a27e41ea9ea6538e89489102', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.206, 'Rank IC': 0.051, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: 6e1e10799860460391bdafcba7e6e57a

		Model: {'id': '6e1e10799860460391bdafcba7e6e57a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.181, 'Rank IC': 0.045, 'Rank ICIR': 0.332}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.332', 'recency_weight': '0.347', 'weight': '0.042'}

	Recorder: 6b65513f05b0483182efe16c2311b38e

		Model: {'id': '6b65513f05b0483182efe16c2311b38e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.267, 'Rank IC': 0.038, 'Rank ICIR': 0.184}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.184', 'recency_weight': '0.704', 'weight': '0.026'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260416_11 180260524597879029 (Recorders: 6/6)

	Recorder: 5d69dbf51af54d10aca36c4aa37600b6

		Model: {'id': '5d69dbf51af54d10aca36c4aa37600b6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.41, 'Rank IC': 0.06, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.370', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: fe8af1d22b7f4a94bfba0b7b4122c79e

		Model: {'id': 'fe8af1d22b7f4a94bfba0b7b4122c79e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.292, 'Rank IC': 0.053, 'Rank ICIR': 0.359}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.359', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: 2fa83e4b17054f5987d37423452a222e

		Model: {'id': '2fa83e4b17054f5987d37423452a222e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.242, 'Rank IC': 0.041, 'Rank ICIR': 0.255}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.255', 'recency_weight': '0.244', 'weight': '0.018'}

	Recorder: 7d88b16ec1624f3e88b2b2f0b5bd64ef

		Model: {'id': '7d88b16ec1624f3e88b2b2f0b5bd64ef', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.45, 'Rank IC': 0.07, 'Rank ICIR': 0.483}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.483', 'recency_weight': '0.347', 'weight': '0.090'}

	Recorder: 2001109cd7ed455f807942268ce50024

		Model: {'id': '2001109cd7ed455f807942268ce50024', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.401, 'Rank IC': 0.033, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.494', 'weight': '0.035'}

	Recorder: 02d60578bc4b4d96ae5daf463e108025

		Model: {'id': '02d60578bc4b4d96ae5daf463e108025', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.379, 'Rank IC': 0.066, 'Rank ICIR': 0.419}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.704', 'weight': '0.137'}
