# params 
 {'predict_dates': [{'start': '2026-07-01', 'end': '2026-07-01'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260701_12 994631688818705448 (Recorders: 6/6)

	Recorder: 777dc83c38af424d8259a18983b67401

		Model: {'id': '777dc83c38af424d8259a18983b67401', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.316, 'Rank IC': 0.065, 'Rank ICIR': 0.439}, 'data_train_vec': ['2020-07-01', '2024-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.439', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 88351341f802478c8c366eb431892ee0

		Model: {'id': '88351341f802478c8c366eb431892ee0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.205, 'Rank IC': 0.067, 'Rank ICIR': 0.396}, 'data_train_vec': ['2021-07-01', '2025-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.396', 'recency_weight': '0.172', 'weight': '0.018'}

	Recorder: d3290418f38849a8bd34f9d4942f9de8

		Model: {'id': 'd3290418f38849a8bd34f9d4942f9de8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.112, 'Rank IC': 0.062, 'Rank ICIR': 0.375}, 'data_train_vec': ['2022-07-01', '2025-06-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.375', 'recency_weight': '0.244', 'weight': '0.023'}

	Recorder: 0b7e8ffaf6df4f5ab84b0577d2044b5f

		Model: {'id': '0b7e8ffaf6df4f5ab84b0577d2044b5f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.412, 'Rank IC': 0.081, 'Rank ICIR': 0.518}, 'data_train_vec': ['2023-07-01', '2025-09-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.518', 'recency_weight': '0.348', 'weight': '0.063'}

	Recorder: cc19cb51df244019b37ae9fdf803ebb5

		Model: {'id': 'cc19cb51df244019b37ae9fdf803ebb5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.333, 'Rank IC': 0.069, 'Rank ICIR': 0.521}, 'data_train_vec': ['2024-07-01', '2025-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.521', 'recency_weight': '0.496', 'weight': '0.090'}

	Recorder: 68e93b194f734aeab8f0dce6f66bbe9f

		Model: {'id': '68e93b194f734aeab8f0dce6f66bbe9f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.114, 'ICIR': 0.662, 'Rank IC': 0.083, 'Rank ICIR': 0.441}, 'data_train_vec': ['2025-07-01', '2026-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.441', 'recency_weight': '0.702', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260701_12 461131369740768924 (Recorders: 6/6)

	Recorder: 0758ad53660d43c787d535d00d51d259

		Model: {'id': '0758ad53660d43c787d535d00d51d259', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.322, 'Rank IC': 0.065, 'Rank ICIR': 0.434}, 'data_train_vec': ['2020-07-01', '2024-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.434', 'recency_weight': '0.122', 'weight': '0.015'}

	Recorder: e997f29b251746fa82102176e1dd01df

		Model: {'id': 'e997f29b251746fa82102176e1dd01df', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.199, 'Rank IC': 0.065, 'Rank ICIR': 0.386}, 'data_train_vec': ['2021-07-01', '2025-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.386', 'recency_weight': '0.172', 'weight': '0.017'}

	Recorder: 40cb765a5b3d4ac7a8d99b65df7a6c39

		Model: {'id': '40cb765a5b3d4ac7a8d99b65df7a6c39', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.118, 'Rank IC': 0.063, 'Rank ICIR': 0.385}, 'data_train_vec': ['2022-07-01', '2025-06-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.385', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: ac2c077535744fc0b9d0cd2b4480e267

		Model: {'id': 'ac2c077535744fc0b9d0cd2b4480e267', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.298, 'Rank IC': 0.072, 'Rank ICIR': 0.46}, 'data_train_vec': ['2023-07-01', '2025-09-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.460', 'recency_weight': '0.348', 'weight': '0.049'}

	Recorder: a54880348dec407fbb9f8972f7b4fcbf

		Model: {'id': 'a54880348dec407fbb9f8972f7b4fcbf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.379, 'Rank IC': 0.064, 'Rank ICIR': 0.48}, 'data_train_vec': ['2024-07-01', '2025-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.480', 'recency_weight': '0.496', 'weight': '0.077'}

	Recorder: 2828bee82e824c9ca1c1c19bf9c671e5

		Model: {'id': '2828bee82e824c9ca1c1c19bf9c671e5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.111, 'ICIR': 0.576, 'Rank IC': 0.091, 'Rank ICIR': 0.487}, 'data_train_vec': ['2025-07-01', '2026-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.487', 'recency_weight': '0.702', 'weight': '0.112'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260701_12 777938871614994580 (Recorders: 5/6)

	Recorder: 5b482b0f31aa49e190cb3bb10a75fb3f

		Model: {'id': '5b482b0f31aa49e190cb3bb10a75fb3f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.262, 'Rank IC': 0.061, 'Rank ICIR': 0.433}, 'data_train_vec': ['2020-07-01', '2024-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.433', 'recency_weight': '0.122', 'weight': '0.015'}

	Recorder: 9653cf0f47aa4d90a09f2d8706469dfb

		Model: {'id': '9653cf0f47aa4d90a09f2d8706469dfb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.115, 'Rank IC': 0.052, 'Rank ICIR': 0.35}, 'data_train_vec': ['2021-07-01', '2025-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.350', 'recency_weight': '0.172', 'weight': '0.014'}

	Recorder: 75917ccaba6b4529978c9bf0bc3952b5

		Model: {'id': '75917ccaba6b4529978c9bf0bc3952b5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.24, 'Rank IC': 0.056, 'Rank ICIR': 0.414}, 'data_train_vec': ['2023-07-01', '2025-09-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.414', 'recency_weight': '0.348', 'weight': '0.040'}

	Recorder: 25ed9aa8473b4fd09c2a63919eef69ec

		Model: {'id': '25ed9aa8473b4fd09c2a63919eef69ec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.222, 'Rank IC': 0.042, 'Rank ICIR': 0.294}, 'data_train_vec': ['2024-07-01', '2025-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.294', 'recency_weight': '0.496', 'weight': '0.029'}

	Recorder: 2571012a813f4f84a260f1024014e1a3

		Model: {'id': '2571012a813f4f84a260f1024014e1a3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.084, 'ICIR': 0.396, 'Rank IC': 0.072, 'Rank ICIR': 0.378}, 'data_train_vec': ['2025-07-01', '2026-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.378', 'recency_weight': '0.702', 'weight': '0.067'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260701_11 740030294935038949 (Recorders: 6/6)

	Recorder: 108cb0eff45a48d5921edf8e34bea542

		Model: {'id': '108cb0eff45a48d5921edf8e34bea542', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.27, 'Rank IC': 0.065, 'Rank ICIR': 0.451}, 'data_train_vec': ['2020-07-01', '2024-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.451', 'recency_weight': '0.122', 'weight': '0.017'}

	Recorder: 5b8e651309ca4a7f85ed4fb4766fd68b

		Model: {'id': '5b8e651309ca4a7f85ed4fb4766fd68b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.186, 'Rank IC': 0.063, 'Rank ICIR': 0.399}, 'data_train_vec': ['2021-07-01', '2025-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.399', 'recency_weight': '0.172', 'weight': '0.018'}

	Recorder: fa5204304843425d9ddb559d1757df99

		Model: {'id': 'fa5204304843425d9ddb559d1757df99', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.108, 'Rank IC': 0.064, 'Rank ICIR': 0.395}, 'data_train_vec': ['2022-07-01', '2025-06-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.395', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: 26a78fc048be4c5a84ac65045e3e2736

		Model: {'id': '26a78fc048be4c5a84ac65045e3e2736', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.299, 'Rank IC': 0.061, 'Rank ICIR': 0.422}, 'data_train_vec': ['2023-07-01', '2025-09-30'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.422', 'recency_weight': '0.348', 'weight': '0.042'}

	Recorder: 6dc92b7e41214139abe480e0ea171d2d

		Model: {'id': '6dc92b7e41214139abe480e0ea171d2d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.272, 'Rank IC': 0.057, 'Rank ICIR': 0.498}, 'data_train_vec': ['2024-07-01', '2025-12-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.498', 'recency_weight': '0.496', 'weight': '0.083'}

	Recorder: 4b2b621bf5504b95868f952c239d9ddd

		Model: {'id': '4b2b621bf5504b95868f952c239d9ddd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.446, 'Rank IC': 0.053, 'Rank ICIR': 0.333}, 'data_train_vec': ['2025-07-01', '2026-03-31'], 'train_time_vec': ['2026-07-01', '2026-07-01'], 'rank_icir': '0.333', 'recency_weight': '0.702', 'weight': '0.052'}
