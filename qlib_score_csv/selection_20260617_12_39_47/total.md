# params 
 {'predict_dates': [{'start': '2026-06-17', 'end': '2026-06-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260617_11 152876793349210497 (Recorders: 6/6)

	Recorder: 15ab5626825b4557aee63fa950ba268d

		Model: {'id': '15ab5626825b4557aee63fa950ba268d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.3, 'Rank IC': 0.058, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-06-17', '2024-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.379', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 5cff01fad6934f5894f139637009dccf

		Model: {'id': '5cff01fad6934f5894f139637009dccf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.266, 'Rank IC': 0.071, 'Rank ICIR': 0.467}, 'data_train_vec': ['2021-06-17', '2025-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.467', 'recency_weight': '0.171', 'weight': '0.028'}

	Recorder: 0e8dedf7beb64b72a7640947f0a327aa

		Model: {'id': '0e8dedf7beb64b72a7640947f0a327aa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.175, 'Rank IC': 0.075, 'Rank ICIR': 0.44}, 'data_train_vec': ['2022-06-17', '2025-06-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.440', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 55d502cd491f49d58bad4c933344e870

		Model: {'id': '55d502cd491f49d58bad4c933344e870', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.29, 'Rank IC': 0.068, 'Rank ICIR': 0.4}, 'data_train_vec': ['2023-06-17', '2025-09-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.400', 'recency_weight': '0.348', 'weight': '0.042'}

	Recorder: 849237e09c274381a8b69198deeac1a4

		Model: {'id': '849237e09c274381a8b69198deeac1a4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.279, 'Rank IC': 0.066, 'Rank ICIR': 0.474}, 'data_train_vec': ['2024-06-17', '2025-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.474', 'recency_weight': '0.494', 'weight': '0.084'}

	Recorder: d23fa6456e2a4cd5b75937e12c5f4ccd

		Model: {'id': 'd23fa6456e2a4cd5b75937e12c5f4ccd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.089, 'ICIR': 0.488, 'Rank IC': 0.054, 'Rank ICIR': 0.276}, 'data_train_vec': ['2025-06-17', '2026-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.276', 'recency_weight': '0.699', 'weight': '0.040'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260617_11 424322836725280711 (Recorders: 6/6)

	Recorder: 2c1525ffcc0d4c5e8f77b2a83ca4d87c

		Model: {'id': '2c1525ffcc0d4c5e8f77b2a83ca4d87c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.291, 'Rank IC': 0.06, 'Rank ICIR': 0.376}, 'data_train_vec': ['2020-06-17', '2024-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.376', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 9813d9002d74491399c050f9a30ca7ff

		Model: {'id': '9813d9002d74491399c050f9a30ca7ff', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.257, 'Rank IC': 0.067, 'Rank ICIR': 0.441}, 'data_train_vec': ['2021-06-17', '2025-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.441', 'recency_weight': '0.171', 'weight': '0.025'}

	Recorder: 548519fa56e845e98d6bf06d92477850

		Model: {'id': '548519fa56e845e98d6bf06d92477850', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.127, 'Rank IC': 0.061, 'Rank ICIR': 0.361}, 'data_train_vec': ['2022-06-17', '2025-06-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.361', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: caa80c7c994d47538259e0b6d74fdc5f

		Model: {'id': 'caa80c7c994d47538259e0b6d74fdc5f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.207, 'Rank IC': 0.069, 'Rank ICIR': 0.395}, 'data_train_vec': ['2023-06-17', '2025-09-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.395', 'recency_weight': '0.348', 'weight': '0.041'}

	Recorder: 86c5a5955b364f4a916224956a581c9a

		Model: {'id': '86c5a5955b364f4a916224956a581c9a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.267, 'Rank IC': 0.072, 'Rank ICIR': 0.516}, 'data_train_vec': ['2024-06-17', '2025-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.516', 'recency_weight': '0.494', 'weight': '0.100'}

	Recorder: 01b75cb7d33b434da4da868bc8e8f874

		Model: {'id': '01b75cb7d33b434da4da868bc8e8f874', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.379, 'Rank IC': 0.05, 'Rank ICIR': 0.262}, 'data_train_vec': ['2025-06-17', '2026-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.262', 'recency_weight': '0.699', 'weight': '0.036'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260617_11 234248433898317408 (Recorders: 6/6)

	Recorder: 6156ff7e5f99415ca918ca016ec9918b

		Model: {'id': '6156ff7e5f99415ca918ca016ec9918b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.321, 'Rank IC': 0.066, 'Rank ICIR': 0.475}, 'data_train_vec': ['2020-06-17', '2024-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.475', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: 69151730bccd4129b73b6c99fc948163

		Model: {'id': '69151730bccd4129b73b6c99fc948163', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.237, 'Rank IC': 0.066, 'Rank ICIR': 0.469}, 'data_train_vec': ['2021-06-17', '2025-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.469', 'recency_weight': '0.171', 'weight': '0.029'}

	Recorder: f544df8b5ee741e093e61b9a228d3df1

		Model: {'id': 'f544df8b5ee741e093e61b9a228d3df1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.111, 'Rank IC': 0.059, 'Rank ICIR': 0.383}, 'data_train_vec': ['2022-06-17', '2025-06-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.383', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: c460f659586542919d84a2168ab2e5b5

		Model: {'id': 'c460f659586542919d84a2168ab2e5b5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.19, 'Rank IC': 0.059, 'Rank ICIR': 0.429}, 'data_train_vec': ['2023-06-17', '2025-09-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.429', 'recency_weight': '0.348', 'weight': '0.049'}

	Recorder: 77ec2b547bbe4632ba0a3edf25d5e76f

		Model: {'id': '77ec2b547bbe4632ba0a3edf25d5e76f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.27, 'Rank IC': 0.056, 'Rank ICIR': 0.424}, 'data_train_vec': ['2024-06-17', '2025-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.424', 'recency_weight': '0.494', 'weight': '0.067'}

	Recorder: ba76ea74f8fc4a0983d0614054592a9f

		Model: {'id': 'ba76ea74f8fc4a0983d0614054592a9f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.082, 'ICIR': 0.361, 'Rank IC': 0.062, 'Rank ICIR': 0.291}, 'data_train_vec': ['2025-06-17', '2026-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.291', 'recency_weight': '0.699', 'weight': '0.045'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260617_11 566835019678777417 (Recorders: 6/6)

	Recorder: 2e4288c897214d1d8c78bf181450142b

		Model: {'id': '2e4288c897214d1d8c78bf181450142b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.284, 'Rank IC': 0.056, 'Rank ICIR': 0.382}, 'data_train_vec': ['2020-06-17', '2024-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.382', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 072408688d9a41c3bd991ac797758378

		Model: {'id': '072408688d9a41c3bd991ac797758378', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.263, 'Rank IC': 0.068, 'Rank ICIR': 0.49}, 'data_train_vec': ['2021-06-17', '2025-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.490', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: 8fdf82f2e75d46be9719ee424be7e3e9

		Model: {'id': '8fdf82f2e75d46be9719ee424be7e3e9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.183, 'Rank IC': 0.066, 'Rank ICIR': 0.385}, 'data_train_vec': ['2022-06-17', '2025-06-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.385', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 36404f42a36c4a5cacc85286e63d51c6

		Model: {'id': '36404f42a36c4a5cacc85286e63d51c6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.245, 'Rank IC': 0.07, 'Rank ICIR': 0.421}, 'data_train_vec': ['2023-06-17', '2025-09-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.421', 'recency_weight': '0.348', 'weight': '0.047'}

	Recorder: 42ace401f99d48a7b4bcada48d70aed7

		Model: {'id': '42ace401f99d48a7b4bcada48d70aed7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.376, 'Rank IC': 0.073, 'Rank ICIR': 0.564}, 'data_train_vec': ['2024-06-17', '2025-12-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.564', 'recency_weight': '0.494', 'weight': '0.119'}

	Recorder: cf7751161b3e4a9d8d00df8dced0e8a5

		Model: {'id': 'cf7751161b3e4a9d8d00df8dced0e8a5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.44, 'Rank IC': 0.051, 'Rank ICIR': 0.282}, 'data_train_vec': ['2025-06-17', '2026-03-16'], 'train_time_vec': ['2026-06-17', '2026-06-17'], 'rank_icir': '0.282', 'recency_weight': '0.699', 'weight': '0.042'}
