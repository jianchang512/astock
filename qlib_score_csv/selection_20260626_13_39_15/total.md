# params 
 {'predict_dates': [{'start': '2026-06-26', 'end': '2026-06-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260626_13 391893039239175467 (Recorders: 6/6)

	Recorder: 3e8e8db094694c7396cbd441b5715835

		Model: {'id': '3e8e8db094694c7396cbd441b5715835', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.332, 'Rank IC': 0.064, 'Rank ICIR': 0.424}, 'data_train_vec': ['2020-06-26', '2024-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.424', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 178d1ecd7bc14ccb81a8c432744b9a9a

		Model: {'id': '178d1ecd7bc14ccb81a8c432744b9a9a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.243, 'Rank IC': 0.07, 'Rank ICIR': 0.441}, 'data_train_vec': ['2021-06-26', '2025-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.441', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: 7a861145184040098416d37bac2e3072

		Model: {'id': '7a861145184040098416d37bac2e3072', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.179, 'Rank IC': 0.07, 'Rank ICIR': 0.408}, 'data_train_vec': ['2022-06-26', '2025-06-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.408', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 1d7fa79abb24419888a69af7f46f9d84

		Model: {'id': '1d7fa79abb24419888a69af7f46f9d84', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.345, 'Rank IC': 0.071, 'Rank ICIR': 0.438}, 'data_train_vec': ['2023-06-26', '2025-09-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.438', 'recency_weight': '0.348', 'weight': '0.048'}

	Recorder: 3be1fb5775444342a06e6e0eeb2e8479

		Model: {'id': '3be1fb5775444342a06e6e0eeb2e8479', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.393, 'Rank IC': 0.069, 'Rank ICIR': 0.535}, 'data_train_vec': ['2024-06-26', '2025-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.535', 'recency_weight': '0.494', 'weight': '0.102'}

	Recorder: f9b36583794d4570acd6f251deb7a985

		Model: {'id': 'f9b36583794d4570acd6f251deb7a985', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.106, 'ICIR': 0.701, 'Rank IC': 0.047, 'Rank ICIR': 0.278}, 'data_train_vec': ['2025-06-26', '2026-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.278', 'recency_weight': '0.699', 'weight': '0.039'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260626_12 442284337882621640 (Recorders: 6/6)

	Recorder: e7f5a7146a5d4c9a911ae93411d76688

		Model: {'id': 'e7f5a7146a5d4c9a911ae93411d76688', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.336, 'Rank IC': 0.065, 'Rank ICIR': 0.421}, 'data_train_vec': ['2020-06-26', '2024-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.421', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: cadb6901c14e4c548e3bf09feaff9657

		Model: {'id': 'cadb6901c14e4c548e3bf09feaff9657', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.23, 'Rank IC': 0.066, 'Rank ICIR': 0.403}, 'data_train_vec': ['2021-06-26', '2025-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.403', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: 7b2e247f45fe4feda46200a5b2ff8a73

		Model: {'id': '7b2e247f45fe4feda46200a5b2ff8a73', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.113, 'Rank IC': 0.063, 'Rank ICIR': 0.373}, 'data_train_vec': ['2022-06-26', '2025-06-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.373', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 8286d6bae2b14441a590b27f712335dc

		Model: {'id': '8286d6bae2b14441a590b27f712335dc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.247, 'Rank IC': 0.07, 'Rank ICIR': 0.425}, 'data_train_vec': ['2023-06-26', '2025-09-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.425', 'recency_weight': '0.348', 'weight': '0.046'}

	Recorder: 2f6b8592163145229d07b0a82de61add

		Model: {'id': '2f6b8592163145229d07b0a82de61add', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.369, 'Rank IC': 0.072, 'Rank ICIR': 0.57}, 'data_train_vec': ['2024-06-26', '2025-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.570', 'recency_weight': '0.494', 'weight': '0.116'}

	Recorder: 488e5a7db4334ff5a2fb53e5eba88122

		Model: {'id': '488e5a7db4334ff5a2fb53e5eba88122', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.449, 'Rank IC': 0.053, 'Rank ICIR': 0.29}, 'data_train_vec': ['2025-06-26', '2026-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.290', 'recency_weight': '0.699', 'weight': '0.043'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260626_12 726312743849224776 (Recorders: 6/6)

	Recorder: 398d7c76654d4a1887973005bc1499ec

		Model: {'id': '398d7c76654d4a1887973005bc1499ec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.308, 'Rank IC': 0.065, 'Rank ICIR': 0.462}, 'data_train_vec': ['2020-06-26', '2024-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.462', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 645635a3e81745e4a177ef8feb9b6e84

		Model: {'id': '645635a3e81745e4a177ef8feb9b6e84', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.168, 'Rank IC': 0.06, 'Rank ICIR': 0.401}, 'data_train_vec': ['2021-06-26', '2025-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.401', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: a88454262cfb438a9a3874a4dd46525e

		Model: {'id': 'a88454262cfb438a9a3874a4dd46525e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.055, 'Rank ICIR': 0.347}, 'data_train_vec': ['2022-06-26', '2025-06-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.347', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 39cdb6c63ec5423682505dfc74ed36f3

		Model: {'id': '39cdb6c63ec5423682505dfc74ed36f3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.211, 'Rank IC': 0.056, 'Rank ICIR': 0.415}, 'data_train_vec': ['2023-06-26', '2025-09-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.415', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: 3c86c0ddbe664547b243790a5e6f658c

		Model: {'id': '3c86c0ddbe664547b243790a5e6f658c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.27, 'Rank IC': 0.053, 'Rank ICIR': 0.389}, 'data_train_vec': ['2024-06-26', '2025-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.389', 'recency_weight': '0.494', 'weight': '0.054'}

	Recorder: 9cc4e74de6a346e6853450645d332344

		Model: {'id': '9cc4e74de6a346e6853450645d332344', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.345, 'Rank IC': 0.055, 'Rank ICIR': 0.272}, 'data_train_vec': ['2025-06-26', '2026-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.272', 'recency_weight': '0.699', 'weight': '0.037'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260626_12 537257246827950515 (Recorders: 6/6)

	Recorder: 47bb597b8bb84dd1bdf2c14400f62881

		Model: {'id': '47bb597b8bb84dd1bdf2c14400f62881', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.343, 'Rank IC': 0.066, 'Rank ICIR': 0.457}, 'data_train_vec': ['2020-06-26', '2024-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.457', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: 6cc0de0c55a3414dbb588099186ef658

		Model: {'id': '6cc0de0c55a3414dbb588099186ef658', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.21, 'Rank IC': 0.065, 'Rank ICIR': 0.411}, 'data_train_vec': ['2021-06-26', '2025-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.411', 'recency_weight': '0.171', 'weight': '0.021'}

	Recorder: f4d96c6532fb42d1a2ae2c70504437ac

		Model: {'id': 'f4d96c6532fb42d1a2ae2c70504437ac', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.117, 'Rank IC': 0.059, 'Rank ICIR': 0.371}, 'data_train_vec': ['2022-06-26', '2025-06-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.371', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: 6d2a932ec3ff46d1bba06f7c05904665

		Model: {'id': '6d2a932ec3ff46d1bba06f7c05904665', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.222, 'Rank IC': 0.067, 'Rank ICIR': 0.418}, 'data_train_vec': ['2023-06-26', '2025-09-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.418', 'recency_weight': '0.348', 'weight': '0.044'}

	Recorder: f0c1713f78694da7b168d54652f854af

		Model: {'id': 'f0c1713f78694da7b168d54652f854af', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.388, 'Rank IC': 0.066, 'Rank ICIR': 0.541}, 'data_train_vec': ['2024-06-26', '2025-12-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.541', 'recency_weight': '0.494', 'weight': '0.105'}

	Recorder: 8b5f3f5baf37478abb108641de822b61

		Model: {'id': '8b5f3f5baf37478abb108641de822b61', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.101, 'ICIR': 0.681, 'Rank IC': 0.057, 'Rank ICIR': 0.37}, 'data_train_vec': ['2025-06-26', '2026-03-25'], 'train_time_vec': ['2026-06-26', '2026-06-26'], 'rank_icir': '0.370', 'recency_weight': '0.699', 'weight': '0.069'}
