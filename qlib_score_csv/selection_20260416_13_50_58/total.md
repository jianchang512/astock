# params 
 {'predict_dates': [{'start': '2026-04-16', 'end': '2026-04-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260416_13 335004504266772468 (Recorders: 6/6)

	Recorder: f1ae16293eba42f392b0aa69d390edd9

		Model: {'id': 'f1ae16293eba42f392b0aa69d390edd9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.44, 'Rank IC': 0.064, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: 1d568bc063a149e4a60fefcce7f05d19

		Model: {'id': '1d568bc063a149e4a60fefcce7f05d19', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.346, 'Rank IC': 0.054, 'Rank ICIR': 0.354}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.354', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: 4bad18a39cbb4227969c038518afe078

		Model: {'id': '4bad18a39cbb4227969c038518afe078', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.205, 'Rank IC': 0.044, 'Rank ICIR': 0.251}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: b3d6c41ded3d4ca89b91a32994a711ab

		Model: {'id': 'b3d6c41ded3d4ca89b91a32994a711ab', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.395, 'Rank IC': 0.064, 'Rank ICIR': 0.419}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.347', 'weight': '0.067'}

	Recorder: 615a195e8cf249e088f8da052a86b613

		Model: {'id': '615a195e8cf249e088f8da052a86b613', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.205, 'Rank IC': 0.029, 'Rank ICIR': 0.212}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.212', 'recency_weight': '0.494', 'weight': '0.025'}

	Recorder: 5b53b1714fab4779b5848a90e522e99a

		Model: {'id': '5b53b1714fab4779b5848a90e522e99a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.351, 'Rank IC': 0.069, 'Rank ICIR': 0.352}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.352', 'recency_weight': '0.704', 'weight': '0.097'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260416_13 908813289248909373 (Recorders: 6/6)

	Recorder: ccb0b24199164f0a90b41abe2bc492d4

		Model: {'id': 'ccb0b24199164f0a90b41abe2bc492d4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.406, 'Rank IC': 0.061, 'Rank ICIR': 0.347}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.347', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 6df9b279dfaf4161bf63507e107b3901

		Model: {'id': '6df9b279dfaf4161bf63507e107b3901', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.284, 'Rank IC': 0.051, 'Rank ICIR': 0.319}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.319', 'recency_weight': '0.173', 'weight': '0.019'}

	Recorder: 01fc87b0539d4189a56cd2c2f3bbbcb2

		Model: {'id': '01fc87b0539d4189a56cd2c2f3bbbcb2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.134, 'Rank IC': 0.038, 'Rank ICIR': 0.22}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.220', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: b4e86df954754d98bc25451f4bcac9ab

		Model: {'id': 'b4e86df954754d98bc25451f4bcac9ab', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.169, 'Rank IC': 0.063, 'Rank ICIR': 0.4}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.400', 'recency_weight': '0.347', 'weight': '0.062'}

	Recorder: 42fecf14522b4344bb3c008351b487e6

		Model: {'id': '42fecf14522b4344bb3c008351b487e6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.227, 'Rank IC': 0.044, 'Rank ICIR': 0.331}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.331', 'recency_weight': '0.494', 'weight': '0.060'}

	Recorder: b0682676311244d397efed7cdba884c7

		Model: {'id': 'b0682676311244d397efed7cdba884c7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.299, 'Rank IC': 0.064, 'Rank ICIR': 0.329}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.329', 'recency_weight': '0.704', 'weight': '0.085'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260416_12 765197413588396966 (Recorders: 5/6)

	Recorder: ed1e6c8222d3476c92debeaa33590cd2

		Model: {'id': 'ed1e6c8222d3476c92debeaa33590cd2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.396, 'Rank IC': 0.063, 'Rank ICIR': 0.467}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.467', 'recency_weight': '0.121', 'weight': '0.029'}

	Recorder: 87fce26c8cf0418ab9c8c16c3cdc9147

		Model: {'id': '87fce26c8cf0418ab9c8c16c3cdc9147', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.342, 'Rank IC': 0.055, 'Rank ICIR': 0.474}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.474', 'recency_weight': '0.173', 'weight': '0.043'}

	Recorder: 353d457670904c1a845c65fd5524c218

		Model: {'id': '353d457670904c1a845c65fd5524c218', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.206, 'Rank IC': 0.051, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: 37d172d47ca347e890cb7c9a077cc772

		Model: {'id': '37d172d47ca347e890cb7c9a077cc772', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.181, 'Rank IC': 0.045, 'Rank ICIR': 0.332}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.332', 'recency_weight': '0.347', 'weight': '0.042'}

	Recorder: 0c642c716b494eaf978c52d58a51b4c3

		Model: {'id': '0c642c716b494eaf978c52d58a51b4c3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.267, 'Rank IC': 0.038, 'Rank ICIR': 0.184}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.184', 'recency_weight': '0.704', 'weight': '0.026'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260416_12 475413575709256999 (Recorders: 6/6)

	Recorder: 8cce2d582a6b451790585d5e2c04b2a6

		Model: {'id': '8cce2d582a6b451790585d5e2c04b2a6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.41, 'Rank IC': 0.06, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.370', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: b891271ef8e74c4fa4c0001920ca316b

		Model: {'id': 'b891271ef8e74c4fa4c0001920ca316b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.292, 'Rank IC': 0.053, 'Rank ICIR': 0.359}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.359', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: 1c6a5dad3a074ef2b80cb38c62f5478b

		Model: {'id': '1c6a5dad3a074ef2b80cb38c62f5478b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.242, 'Rank IC': 0.041, 'Rank ICIR': 0.255}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.255', 'recency_weight': '0.244', 'weight': '0.018'}

	Recorder: 60fe4ec90f5845f7801f90ca96c09db9

		Model: {'id': '60fe4ec90f5845f7801f90ca96c09db9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.45, 'Rank IC': 0.07, 'Rank ICIR': 0.483}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.483', 'recency_weight': '0.347', 'weight': '0.090'}

	Recorder: ea31283a44204236b8c811177cc7caac

		Model: {'id': 'ea31283a44204236b8c811177cc7caac', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.401, 'Rank IC': 0.033, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.494', 'weight': '0.035'}

	Recorder: f95af6fea1034222b53936edf338910b

		Model: {'id': 'f95af6fea1034222b53936edf338910b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.379, 'Rank IC': 0.066, 'Rank ICIR': 0.419}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.704', 'weight': '0.137'}
