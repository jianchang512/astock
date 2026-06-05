# params 
 {'predict_dates': [{'start': '2026-06-05', 'end': '2026-06-05'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260605_15 659162247433375860 (Recorders: 6/6)

	Recorder: a69b51b3785a43e5a39ed17ab3a53f2c

		Model: {'id': 'a69b51b3785a43e5a39ed17ab3a53f2c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.368, 'Rank IC': 0.062, 'Rank ICIR': 0.415}, 'data_train_vec': ['2020-06-05', '2024-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.415', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 6981ebc0459a45b787ecd9a0e737ce15

		Model: {'id': '6981ebc0459a45b787ecd9a0e737ce15', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.275, 'Rank IC': 0.063, 'Rank ICIR': 0.444}, 'data_train_vec': ['2021-06-05', '2025-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.444', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: a7e07777ae7043e58beba515cc5deaa2

		Model: {'id': 'a7e07777ae7043e58beba515cc5deaa2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.177, 'Rank IC': 0.062, 'Rank ICIR': 0.366}, 'data_train_vec': ['2022-06-05', '2025-06-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.366', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: e5ba7b141ca64acba1441ced7e380578

		Model: {'id': 'e5ba7b141ca64acba1441ced7e380578', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.242, 'Rank IC': 0.069, 'Rank ICIR': 0.382}, 'data_train_vec': ['2023-06-05', '2025-09-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.382', 'recency_weight': '0.348', 'weight': '0.047'}

	Recorder: 23a6e63af4cd4fe8a96ba4d16e4e4e9c

		Model: {'id': '23a6e63af4cd4fe8a96ba4d16e4e4e9c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.209, 'Rank IC': 0.065, 'Rank ICIR': 0.489}, 'data_train_vec': ['2024-06-05', '2025-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.489', 'recency_weight': '0.494', 'weight': '0.109'}

	Recorder: 9ffcf4f6f6d54a61aa1bb37c42733dce

		Model: {'id': '9ffcf4f6f6d54a61aa1bb37c42733dce', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.088, 'ICIR': 0.539, 'Rank IC': 0.045, 'Rank ICIR': 0.246}, 'data_train_vec': ['2025-06-05', '2026-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.246', 'recency_weight': '0.699', 'weight': '0.039'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260605_14 108780910509150541 (Recorders: 6/6)

	Recorder: d3f5ba15c55542e7bf8c4202b0376525

		Model: {'id': 'd3f5ba15c55542e7bf8c4202b0376525', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.302, 'Rank IC': 0.059, 'Rank ICIR': 0.389}, 'data_train_vec': ['2020-06-05', '2024-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.389', 'recency_weight': '0.121', 'weight': '0.017'}

	Recorder: 2d1ae63f48b043b5ae122059b7a0007b

		Model: {'id': '2d1ae63f48b043b5ae122059b7a0007b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.221, 'Rank IC': 0.061, 'Rank ICIR': 0.411}, 'data_train_vec': ['2021-06-05', '2025-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.411', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 4b6b03a6d2594463881dae6254d26140

		Model: {'id': '4b6b03a6d2594463881dae6254d26140', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.119, 'Rank IC': 0.059, 'Rank ICIR': 0.34}, 'data_train_vec': ['2022-06-05', '2025-06-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.340', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: 18874bf2069e4835a4006035b13ea412

		Model: {'id': '18874bf2069e4835a4006035b13ea412', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.218, 'Rank IC': 0.065, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-06-05', '2025-09-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.377', 'recency_weight': '0.348', 'weight': '0.046'}

	Recorder: 7b6f475dd2cd4b75a4bc0016b0d6f50b

		Model: {'id': '7b6f475dd2cd4b75a4bc0016b0d6f50b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.145, 'Rank IC': 0.059, 'Rank ICIR': 0.403}, 'data_train_vec': ['2024-06-05', '2025-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.403', 'recency_weight': '0.494', 'weight': '0.074'}

	Recorder: d6b6e38c65eb47579f44c1c9eec23aaa

		Model: {'id': 'd6b6e38c65eb47579f44c1c9eec23aaa', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.287, 'Rank IC': 0.028, 'Rank ICIR': 0.194}, 'data_train_vec': ['2025-06-05', '2026-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.194', 'recency_weight': '0.699', 'weight': '0.024'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260605_14 655106759238511061 (Recorders: 6/6)

	Recorder: 112e313992c245eab94f9013f221345b

		Model: {'id': '112e313992c245eab94f9013f221345b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.32, 'Rank IC': 0.065, 'Rank ICIR': 0.473}, 'data_train_vec': ['2020-06-05', '2024-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.473', 'recency_weight': '0.121', 'weight': '0.025'}

	Recorder: 19225e5e2eec46738e7c013bfeb462ca

		Model: {'id': '19225e5e2eec46738e7c013bfeb462ca', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.237, 'Rank IC': 0.066, 'Rank ICIR': 0.477}, 'data_train_vec': ['2021-06-05', '2025-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.477', 'recency_weight': '0.171', 'weight': '0.036'}

	Recorder: b89e9fa274aa45dabe62fd66b6538fc2

		Model: {'id': 'b89e9fa274aa45dabe62fd66b6538fc2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.093, 'Rank IC': 0.056, 'Rank ICIR': 0.377}, 'data_train_vec': ['2022-06-05', '2025-06-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.377', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: 4d4f6e65087e4af99ac56efffe622213

		Model: {'id': '4d4f6e65087e4af99ac56efffe622213', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.072, 'Rank IC': 0.041, 'Rank ICIR': 0.282}, 'data_train_vec': ['2023-06-05', '2025-09-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.282', 'recency_weight': '0.348', 'weight': '0.026'}

	Recorder: 57666c8c5788451daee30eaa5fcc68f8

		Model: {'id': '57666c8c5788451daee30eaa5fcc68f8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.182, 'Rank IC': 0.049, 'Rank ICIR': 0.38}, 'data_train_vec': ['2024-06-05', '2025-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.380', 'recency_weight': '0.494', 'weight': '0.066'}

	Recorder: f53d9777fe8648ff9eac97ed80e5cc7a

		Model: {'id': 'f53d9777fe8648ff9eac97ed80e5cc7a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.323, 'Rank IC': 0.065, 'Rank ICIR': 0.32}, 'data_train_vec': ['2025-06-05', '2026-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.320', 'recency_weight': '0.699', 'weight': '0.066'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260605_14 439995167466687316 (Recorders: 6/6)

	Recorder: 95663dd0ebaa481e906429e770eca9ae

		Model: {'id': '95663dd0ebaa481e906429e770eca9ae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.324, 'Rank IC': 0.057, 'Rank ICIR': 0.381}, 'data_train_vec': ['2020-06-05', '2024-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.381', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 4e9993f5c1a74033a42c182d7d150df7

		Model: {'id': '4e9993f5c1a74033a42c182d7d150df7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.218, 'Rank IC': 0.06, 'Rank ICIR': 0.428}, 'data_train_vec': ['2021-06-05', '2025-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.428', 'recency_weight': '0.171', 'weight': '0.029'}

	Recorder: 1deb2222b0af4404b71ad20ec30e5904

		Model: {'id': '1deb2222b0af4404b71ad20ec30e5904', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.197, 'Rank IC': 0.065, 'Rank ICIR': 0.41}, 'data_train_vec': ['2022-06-05', '2025-06-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.410', 'recency_weight': '0.244', 'weight': '0.038'}

	Recorder: 9f00580a967a4af7bb29438a497ffc03

		Model: {'id': '9f00580a967a4af7bb29438a497ffc03', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.31, 'Rank IC': 0.066, 'Rank ICIR': 0.409}, 'data_train_vec': ['2023-06-05', '2025-09-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.409', 'recency_weight': '0.348', 'weight': '0.054'}

	Recorder: 37a9963416b243b291b7d7fb7346dfef

		Model: {'id': '37a9963416b243b291b7d7fb7346dfef', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.215, 'Rank IC': 0.05, 'Rank ICIR': 0.38}, 'data_train_vec': ['2024-06-05', '2025-12-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.380', 'recency_weight': '0.494', 'weight': '0.066'}

	Recorder: e3a0f314427a4054aec6c09281ea9a3d

		Model: {'id': 'e3a0f314427a4054aec6c09281ea9a3d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.083, 'ICIR': 0.575, 'Rank IC': 0.046, 'Rank ICIR': 0.289}, 'data_train_vec': ['2025-06-05', '2026-03-04'], 'train_time_vec': ['2026-06-05', '2026-06-05'], 'rank_icir': '0.289', 'recency_weight': '0.699', 'weight': '0.054'}
