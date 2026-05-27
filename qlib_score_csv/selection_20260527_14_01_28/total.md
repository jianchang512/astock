# params 
 {'predict_dates': [{'start': '2026-05-27', 'end': '2026-05-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260527_13 178119671454655091 (Recorders: 6/6)

	Recorder: 65a5e7d8dab74e7b9ec501af09d7848c

		Model: {'id': '65a5e7d8dab74e7b9ec501af09d7848c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.328, 'Rank IC': 0.055, 'Rank ICIR': 0.378}, 'data_train_vec': ['2020-05-27', '2024-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.378', 'recency_weight': '0.122', 'weight': '0.020'}

	Recorder: 4726eba3045046f5bcfda51c92846b5a

		Model: {'id': '4726eba3045046f5bcfda51c92846b5a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.216, 'Rank IC': 0.054, 'Rank ICIR': 0.389}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.389', 'recency_weight': '0.173', 'weight': '0.030'}

	Recorder: aead3c17b02948328424875c3f6a1ae1

		Model: {'id': 'aead3c17b02948328424875c3f6a1ae1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.2, 'Rank IC': 0.064, 'Rank ICIR': 0.384}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.384', 'recency_weight': '0.244', 'weight': '0.042'}

	Recorder: 040d4adfee5e48f9913b5261f7dbb9a1

		Model: {'id': '040d4adfee5e48f9913b5261f7dbb9a1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.217, 'Rank IC': 0.058, 'Rank ICIR': 0.373}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.373', 'recency_weight': '0.348', 'weight': '0.056'}

	Recorder: 36430ec03e3e4a4ba9efd824d1e6ae56

		Model: {'id': '36430ec03e3e4a4ba9efd824d1e6ae56', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.225, 'Rank IC': 0.06, 'Rank ICIR': 0.501}, 'data_train_vec': ['2024-05-27', '2025-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.501', 'recency_weight': '0.496', 'weight': '0.144'}

	Recorder: 78e4b908beca45b1aa769348ac64a784

		Model: {'id': '78e4b908beca45b1aa769348ac64a784', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.476, 'Rank IC': 0.032, 'Rank ICIR': 0.196}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.196', 'recency_weight': '0.707', 'weight': '0.032'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260527_13 884004329858073140 (Recorders: 5/6)

	Recorder: 67777879b7284e53b7e373c2d5eb1681

		Model: {'id': '67777879b7284e53b7e373c2d5eb1681', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.295, 'Rank IC': 0.054, 'Rank ICIR': 0.365}, 'data_train_vec': ['2020-05-27', '2024-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.365', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 39cf3af37d2e4c23bbd419c2205f086f

		Model: {'id': '39cf3af37d2e4c23bbd419c2205f086f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.185, 'Rank IC': 0.052, 'Rank ICIR': 0.356}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.356', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: c6fd99dcb29743baa504bc765dc2e7a1

		Model: {'id': 'c6fd99dcb29743baa504bc765dc2e7a1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.116, 'Rank IC': 0.06, 'Rank ICIR': 0.355}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.355', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 5c244ab896bf49a8963c315dc61b4154

		Model: {'id': '5c244ab896bf49a8963c315dc61b4154', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.172, 'Rank IC': 0.059, 'Rank ICIR': 0.368}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.368', 'recency_weight': '0.348', 'weight': '0.055'}

	Recorder: 83345ea842314e98874ab865d537ce43

		Model: {'id': '83345ea842314e98874ab865d537ce43', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.265, 'Rank IC': 0.025, 'Rank ICIR': 0.194}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.194', 'recency_weight': '0.707', 'weight': '0.031'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260527_13 879379278711747033 (Recorders: 4/6)

	Recorder: 3c3cc38949ad4946b893f1c95b06ebb4

		Model: {'id': '3c3cc38949ad4946b893f1c95b06ebb4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.316, 'Rank IC': 0.06, 'Rank ICIR': 0.455}, 'data_train_vec': ['2020-05-27', '2024-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.455', 'recency_weight': '0.122', 'weight': '0.029'}

	Recorder: 1acf3c07ac1e48fea02bbe1e37a42664

		Model: {'id': '1acf3c07ac1e48fea02bbe1e37a42664', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.225, 'Rank IC': 0.058, 'Rank ICIR': 0.439}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.439', 'recency_weight': '0.173', 'weight': '0.039'}

	Recorder: 84da2a9d960c4ce2a464329e28048842

		Model: {'id': '84da2a9d960c4ce2a464329e28048842', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.15, 'Rank IC': 0.061, 'Rank ICIR': 0.402}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.402', 'recency_weight': '0.244', 'weight': '0.046'}

	Recorder: f2598c94ce6b41c299105ed4f38bf1a3

		Model: {'id': 'f2598c94ce6b41c299105ed4f38bf1a3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.07, 'ICIR': 0.391, 'Rank IC': 0.07, 'Rank ICIR': 0.346}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.346', 'recency_weight': '0.707', 'weight': '0.098'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260527_12 342576900289448264 (Recorders: 6/6)

	Recorder: f900737e0a164662b1b89f0e96f3ee32

		Model: {'id': 'f900737e0a164662b1b89f0e96f3ee32', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.329, 'Rank IC': 0.055, 'Rank ICIR': 0.387}, 'data_train_vec': ['2020-05-27', '2024-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.387', 'recency_weight': '0.122', 'weight': '0.021'}

	Recorder: 3a9bcbd8a1ed4b56afa16085a2a9da1f

		Model: {'id': '3a9bcbd8a1ed4b56afa16085a2a9da1f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.217, 'Rank IC': 0.053, 'Rank ICIR': 0.392}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.392', 'recency_weight': '0.173', 'weight': '0.031'}

	Recorder: 73f474b328e249b699b2daa05f9e5522

		Model: {'id': '73f474b328e249b699b2daa05f9e5522', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.277, 'Rank IC': 0.068, 'Rank ICIR': 0.406}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.406', 'recency_weight': '0.244', 'weight': '0.047'}

	Recorder: aac42659c4f64f73bff012f063ff38f9

		Model: {'id': 'aac42659c4f64f73bff012f063ff38f9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.221, 'Rank IC': 0.063, 'Rank ICIR': 0.419}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.419', 'recency_weight': '0.348', 'weight': '0.071'}

	Recorder: a11b6f7edd9f48e2baed214009620686

		Model: {'id': 'a11b6f7edd9f48e2baed214009620686', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.142, 'Rank IC': 0.038, 'Rank ICIR': 0.334}, 'data_train_vec': ['2024-05-27', '2025-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.334', 'recency_weight': '0.496', 'weight': '0.064'}

	Recorder: f4b969e32be942b9a8987710a2fcdb30

		Model: {'id': 'f4b969e32be942b9a8987710a2fcdb30', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.427, 'Rank IC': 0.04, 'Rank ICIR': 0.279}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.279', 'recency_weight': '0.707', 'weight': '0.064'}
