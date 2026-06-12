# params 
 {'predict_dates': [{'start': '2026-06-12', 'end': '2026-06-12'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260612_11 560223127315146765 (Recorders: 6/6)

	Recorder: c43713107d9a4223bd3e4522c3be6807

		Model: {'id': 'c43713107d9a4223bd3e4522c3be6807', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.317, 'Rank IC': 0.058, 'Rank ICIR': 0.381}, 'data_train_vec': ['2020-06-12', '2024-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.381', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 1a17426feb614d4a8b19b0747faa88d9

		Model: {'id': '1a17426feb614d4a8b19b0747faa88d9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.295, 'Rank IC': 0.07, 'Rank ICIR': 0.46}, 'data_train_vec': ['2021-06-12', '2025-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.460', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: c9cfb16875cb497bbc828b9a5251d099

		Model: {'id': 'c9cfb16875cb497bbc828b9a5251d099', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.218, 'Rank IC': 0.072, 'Rank ICIR': 0.431}, 'data_train_vec': ['2022-06-12', '2025-06-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.431', 'recency_weight': '0.244', 'weight': '0.039'}

	Recorder: 42722c887d0c4ed5acb2655123e107b1

		Model: {'id': '42722c887d0c4ed5acb2655123e107b1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.27, 'Rank IC': 0.073, 'Rank ICIR': 0.431}, 'data_train_vec': ['2023-06-12', '2025-09-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.431', 'recency_weight': '0.348', 'weight': '0.055'}

	Recorder: c5b66b45b174494a877f349dafc34d88

		Model: {'id': 'c5b66b45b174494a877f349dafc34d88', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.23, 'Rank IC': 0.071, 'Rank ICIR': 0.511}, 'data_train_vec': ['2024-06-12', '2025-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.511', 'recency_weight': '0.494', 'weight': '0.110'}

	Recorder: 508449f074794aa5893c60eed4e11e44

		Model: {'id': '508449f074794aa5893c60eed4e11e44', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.351, 'Rank IC': 0.027, 'Rank ICIR': 0.135}, 'data_train_vec': ['2025-06-12', '2026-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.135', 'recency_weight': '0.699', 'weight': '0.011'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260612_11 459769051878631456 (Recorders: 6/6)

	Recorder: 8c440c898f6f452f872594b77165e22f

		Model: {'id': '8c440c898f6f452f872594b77165e22f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.312, 'Rank IC': 0.06, 'Rank ICIR': 0.376}, 'data_train_vec': ['2020-06-12', '2024-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.376', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 8f31cdb07698404a8ecdd0ecb8da843e

		Model: {'id': '8f31cdb07698404a8ecdd0ecb8da843e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.246, 'Rank IC': 0.061, 'Rank ICIR': 0.401}, 'data_train_vec': ['2021-06-12', '2025-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.401', 'recency_weight': '0.171', 'weight': '0.023'}

	Recorder: 336ba106e5d54c9a9d5e3c3a327e2c31

		Model: {'id': '336ba106e5d54c9a9d5e3c3a327e2c31', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.177, 'Rank IC': 0.069, 'Rank ICIR': 0.404}, 'data_train_vec': ['2022-06-12', '2025-06-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.404', 'recency_weight': '0.244', 'weight': '0.034'}

	Recorder: fa6b50dc827e4b7c95d174298a06dcf7

		Model: {'id': 'fa6b50dc827e4b7c95d174298a06dcf7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.247, 'Rank IC': 0.078, 'Rank ICIR': 0.462}, 'data_train_vec': ['2023-06-12', '2025-09-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.462', 'recency_weight': '0.348', 'weight': '0.063'}

	Recorder: 1fc8623495f04201bbe1da146119ded8

		Model: {'id': '1fc8623495f04201bbe1da146119ded8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.26, 'Rank IC': 0.07, 'Rank ICIR': 0.52}, 'data_train_vec': ['2024-06-12', '2025-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.520', 'recency_weight': '0.494', 'weight': '0.114'}

	Recorder: fe598b05af0d4a399ef94cf7b0513221

		Model: {'id': 'fe598b05af0d4a399ef94cf7b0513221', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.149, 'Rank IC': 0.011, 'Rank ICIR': 0.053}, 'data_train_vec': ['2025-06-12', '2026-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.053', 'recency_weight': '0.699', 'weight': '0.002'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260612_11 820185355462380518 (Recorders: 6/6)

	Recorder: c626ad4e149c4dcbb296e3e16f69f39b

		Model: {'id': 'c626ad4e149c4dcbb296e3e16f69f39b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.317, 'Rank IC': 0.063, 'Rank ICIR': 0.454}, 'data_train_vec': ['2020-06-12', '2024-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.454', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: d91ae9851d7b4285818eb698ff1a6cf5

		Model: {'id': 'd91ae9851d7b4285818eb698ff1a6cf5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.268, 'Rank IC': 0.067, 'Rank ICIR': 0.484}, 'data_train_vec': ['2021-06-12', '2025-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.484', 'recency_weight': '0.171', 'weight': '0.034'}

	Recorder: 890bd321f6e5443c8a839e5704a7ee5e

		Model: {'id': '890bd321f6e5443c8a839e5704a7ee5e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.113, 'Rank IC': 0.058, 'Rank ICIR': 0.381}, 'data_train_vec': ['2022-06-12', '2025-06-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.381', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: 86d3475f7219434ca44deecf77176117

		Model: {'id': '86d3475f7219434ca44deecf77176117', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.236, 'Rank IC': 0.062, 'Rank ICIR': 0.459}, 'data_train_vec': ['2023-06-12', '2025-09-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.459', 'recency_weight': '0.348', 'weight': '0.062'}

	Recorder: 30ac916edc6a41cebea3dd6162e314ab

		Model: {'id': '30ac916edc6a41cebea3dd6162e314ab', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.169, 'Rank IC': 0.044, 'Rank ICIR': 0.345}, 'data_train_vec': ['2024-06-12', '2025-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.345', 'recency_weight': '0.494', 'weight': '0.050'}

	Recorder: 73e92050ad3c47baa881917ce90ae65c

		Model: {'id': '73e92050ad3c47baa881917ce90ae65c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.227, 'Rank IC': 0.035, 'Rank ICIR': 0.16}, 'data_train_vec': ['2025-06-12', '2026-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.160', 'recency_weight': '0.699', 'weight': '0.015'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260612_11 535569336063901493 (Recorders: 6/6)

	Recorder: 30fed808764f4562ad3ce7bec9ae77da

		Model: {'id': '30fed808764f4562ad3ce7bec9ae77da', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.315, 'Rank IC': 0.055, 'Rank ICIR': 0.366}, 'data_train_vec': ['2020-06-12', '2024-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.366', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: c19271624f77450289008b6c8119aac0

		Model: {'id': 'c19271624f77450289008b6c8119aac0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.298, 'Rank IC': 0.064, 'Rank ICIR': 0.455}, 'data_train_vec': ['2021-06-12', '2025-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.455', 'recency_weight': '0.171', 'weight': '0.030'}

	Recorder: f1c1a93df0e2464ea3d31b56a4799021

		Model: {'id': 'f1c1a93df0e2464ea3d31b56a4799021', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.244, 'Rank IC': 0.072, 'Rank ICIR': 0.428}, 'data_train_vec': ['2022-06-12', '2025-06-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.428', 'recency_weight': '0.244', 'weight': '0.038'}

	Recorder: c2ff7149fae74f39a4a49680b35f5908

		Model: {'id': 'c2ff7149fae74f39a4a49680b35f5908', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.345, 'Rank IC': 0.078, 'Rank ICIR': 0.46}, 'data_train_vec': ['2023-06-12', '2025-09-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.460', 'recency_weight': '0.348', 'weight': '0.063'}

	Recorder: 1f31b0a86f764d7d9a93e753c02fb84e

		Model: {'id': '1f31b0a86f764d7d9a93e753c02fb84e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.288, 'Rank IC': 0.061, 'Rank ICIR': 0.498}, 'data_train_vec': ['2024-06-12', '2025-12-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.498', 'recency_weight': '0.494', 'weight': '0.104'}

	Recorder: 59962c116dec4faaa9669f8c23358935

		Model: {'id': '59962c116dec4faaa9669f8c23358935', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.375, 'Rank IC': 0.034, 'Rank ICIR': 0.212}, 'data_train_vec': ['2025-06-12', '2026-03-11'], 'train_time_vec': ['2026-06-12', '2026-06-12'], 'rank_icir': '0.212', 'recency_weight': '0.699', 'weight': '0.027'}
