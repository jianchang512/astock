# params 
 {'predict_dates': [{'start': '2026-04-20', 'end': '2026-04-20'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260420_12 863303756039498230 (Recorders: 6/6)

	Recorder: 10168c9c3f7e416a90f5777d099b1662

		Model: {'id': '10168c9c3f7e416a90f5777d099b1662', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.435, 'Rank IC': 0.058, 'Rank ICIR': 0.343}, 'data_train_vec': ['2020-04-20', '2024-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.343', 'recency_weight': '0.121', 'weight': '0.017'}

	Recorder: 41eeafb1e0b34cddb359a9dde563506d

		Model: {'id': '41eeafb1e0b34cddb359a9dde563506d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.295, 'Rank IC': 0.046, 'Rank ICIR': 0.308}, 'data_train_vec': ['2021-04-20', '2025-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.308', 'recency_weight': '0.173', 'weight': '0.019'}

	Recorder: 5fd03d51db864681ba7bb27bbdf7a75f

		Model: {'id': '5fd03d51db864681ba7bb27bbdf7a75f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.182, 'Rank IC': 0.044, 'Rank ICIR': 0.271}, 'data_train_vec': ['2022-04-20', '2025-04-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.271', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 4aa90458c00f474a894d411d2f525716

		Model: {'id': '4aa90458c00f474a894d411d2f525716', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.344, 'Rank IC': 0.062, 'Rank ICIR': 0.373}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.373', 'recency_weight': '0.347', 'weight': '0.056'}

	Recorder: 82041d8d6a4b4606982af355def7afff

		Model: {'id': '82041d8d6a4b4606982af355def7afff', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.215, 'Rank IC': 0.028, 'Rank ICIR': 0.223}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.223', 'recency_weight': '0.494', 'weight': '0.029'}

	Recorder: c080ea6d46044ca68540f8af6f23d4f9

		Model: {'id': 'c080ea6d46044ca68540f8af6f23d4f9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.379, 'Rank IC': 0.067, 'Rank ICIR': 0.355}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.355', 'recency_weight': '0.704', 'weight': '0.103'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260420_12 272683149383357719 (Recorders: 6/6)

	Recorder: 58cc858c8c82481e83d26ae9e33bcfc5

		Model: {'id': '58cc858c8c82481e83d26ae9e33bcfc5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.36, 'Rank IC': 0.056, 'Rank ICIR': 0.321}, 'data_train_vec': ['2020-04-20', '2024-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.321', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: c7da8ae7c8e240958db7906f70d57cee

		Model: {'id': 'c7da8ae7c8e240958db7906f70d57cee', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.239, 'Rank IC': 0.046, 'Rank ICIR': 0.295}, 'data_train_vec': ['2021-04-20', '2025-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.295', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 3dc930103dc44ffe856cf9d1ef11916b

		Model: {'id': '3dc930103dc44ffe856cf9d1ef11916b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.106, 'Rank IC': 0.039, 'Rank ICIR': 0.239}, 'data_train_vec': ['2022-04-20', '2025-04-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.239', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: 15aca0c49ff74a80b43663eee428d667

		Model: {'id': '15aca0c49ff74a80b43663eee428d667', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.147, 'Rank IC': 0.056, 'Rank ICIR': 0.374}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.374', 'recency_weight': '0.347', 'weight': '0.056'}

	Recorder: 5be41dd2d72842529b803cdfe663e3f9

		Model: {'id': '5be41dd2d72842529b803cdfe663e3f9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.109, 'Rank IC': 0.028, 'Rank ICIR': 0.202}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.202', 'recency_weight': '0.494', 'weight': '0.023'}

	Recorder: b9096f0f09e64b6bb087753a77251287

		Model: {'id': 'b9096f0f09e64b6bb087753a77251287', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.401, 'Rank IC': 0.072, 'Rank ICIR': 0.439}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.439', 'recency_weight': '0.704', 'weight': '0.158'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260420_12 850775071027156856 (Recorders: 5/6)

	Recorder: 81ca2bd806004d839818794b653ed310

		Model: {'id': '81ca2bd806004d839818794b653ed310', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.363, 'Rank IC': 0.06, 'Rank ICIR': 0.445}, 'data_train_vec': ['2020-04-20', '2024-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.445', 'recency_weight': '0.121', 'weight': '0.028'}

	Recorder: 65a90149cfce4ad19b0c2ea55a7418e5

		Model: {'id': '65a90149cfce4ad19b0c2ea55a7418e5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.286, 'Rank IC': 0.051, 'Rank ICIR': 0.434}, 'data_train_vec': ['2021-04-20', '2025-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.434', 'recency_weight': '0.173', 'weight': '0.038'}

	Recorder: 288df51fa0e54a3cbed444cdfb51d652

		Model: {'id': '288df51fa0e54a3cbed444cdfb51d652', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.197, 'Rank IC': 0.051, 'Rank ICIR': 0.357}, 'data_train_vec': ['2022-04-20', '2025-04-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.357', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 1d79b437d9fa492582d98d8442937594

		Model: {'id': '1d79b437d9fa492582d98d8442937594', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.091, 'Rank IC': 0.036, 'Rank ICIR': 0.266}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.266', 'recency_weight': '0.347', 'weight': '0.029'}

	Recorder: 9e337589139c4234b10e3f173f495274

		Model: {'id': '9e337589139c4234b10e3f173f495274', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.369, 'Rank IC': 0.05, 'Rank ICIR': 0.301}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.301', 'recency_weight': '0.704', 'weight': '0.074'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260420_12 611360761565380044 (Recorders: 6/6)

	Recorder: 412386fb2d804f99a30456316172272c

		Model: {'id': '412386fb2d804f99a30456316172272c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.328, 'Rank IC': 0.061, 'Rank ICIR': 0.374}, 'data_train_vec': ['2020-04-20', '2024-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.374', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: 1f06714132ff4635b314e1e66502a755

		Model: {'id': '1f06714132ff4635b314e1e66502a755', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.242, 'Rank IC': 0.047, 'Rank ICIR': 0.323}, 'data_train_vec': ['2021-04-20', '2025-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.323', 'recency_weight': '0.173', 'weight': '0.021'}

	Recorder: 36ff2d045ced4c559d5587c47a9a2c79

		Model: {'id': '36ff2d045ced4c559d5587c47a9a2c79', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.166, 'Rank IC': 0.041, 'Rank ICIR': 0.273}, 'data_train_vec': ['2022-04-20', '2025-04-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.273', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 580644a131c843e19edd650b5f591fd0

		Model: {'id': '580644a131c843e19edd650b5f591fd0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.289, 'Rank IC': 0.065, 'Rank ICIR': 0.425}, 'data_train_vec': ['2023-04-20', '2025-07-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.425', 'recency_weight': '0.347', 'weight': '0.073'}

	Recorder: 24a2a292319b494795ebe2e319adea2f

		Model: {'id': '24a2a292319b494795ebe2e319adea2f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.232, 'Rank IC': 0.031, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-04-20', '2025-10-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.251', 'recency_weight': '0.494', 'weight': '0.036'}

	Recorder: 00d225416a7d47b3b0cbc1f2f1bf1eae

		Model: {'id': '00d225416a7d47b3b0cbc1f2f1bf1eae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.318, 'Rank IC': 0.055, 'Rank ICIR': 0.337}, 'data_train_vec': ['2025-04-20', '2026-01-19'], 'train_time_vec': ['2026-04-20', '2026-04-20'], 'rank_icir': '0.337', 'recency_weight': '0.704', 'weight': '0.093'}
