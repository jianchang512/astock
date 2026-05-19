# params 
 {'predict_dates': [{'start': '2026-05-19', 'end': '2026-05-19'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260519_11 724078878891872528 (Recorders: 6/6)

	Recorder: a22af701c88944789fea6b48650698c1

		Model: {'id': 'a22af701c88944789fea6b48650698c1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.373, 'Rank IC': 0.059, 'Rank ICIR': 0.41}, 'data_train_vec': ['2020-05-19', '2024-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.410', 'recency_weight': '0.122', 'weight': '0.032'}

	Recorder: 7260cefff7bb49a9ade5404f78d692c9

		Model: {'id': '7260cefff7bb49a9ade5404f78d692c9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.21, 'Rank IC': 0.047, 'Rank ICIR': 0.311}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.311', 'recency_weight': '0.173', 'weight': '0.026'}

	Recorder: 510fed589fdb4ba0b6ace927b79abe1c

		Model: {'id': '510fed589fdb4ba0b6ace927b79abe1c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.221, 'Rank IC': 0.053, 'Rank ICIR': 0.32}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.320', 'recency_weight': '0.244', 'weight': '0.039'}

	Recorder: 8c38d985a6634c888d29034c4f41d780

		Model: {'id': '8c38d985a6634c888d29034c4f41d780', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.15, 'Rank IC': 0.041, 'Rank ICIR': 0.255}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.255', 'recency_weight': '0.348', 'weight': '0.035'}

	Recorder: aa5e84311ed54f95b47d2fa30ffae5dc

		Model: {'id': 'aa5e84311ed54f95b47d2fa30ffae5dc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.158, 'Rank IC': 0.04, 'Rank ICIR': 0.323}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.323', 'recency_weight': '0.496', 'weight': '0.080'}

	Recorder: de34b3c65a494ec0aa09f80a2eff8e51

		Model: {'id': 'de34b3c65a494ec0aa09f80a2eff8e51', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.395, 'Rank IC': 0.03, 'Rank ICIR': 0.251}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.251', 'recency_weight': '0.707', 'weight': '0.069'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260519_11 183975245878043628 (Recorders: 4/6)

	Recorder: 77868601481544ab8f04f941d483286f

		Model: {'id': '77868601481544ab8f04f941d483286f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.299, 'Rank IC': 0.051, 'Rank ICIR': 0.342}, 'data_train_vec': ['2020-05-19', '2024-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.342', 'recency_weight': '0.122', 'weight': '0.022'}

	Recorder: f93b9206336c42a781bb85cafd9dea69

		Model: {'id': 'f93b9206336c42a781bb85cafd9dea69', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.146, 'Rank IC': 0.043, 'Rank ICIR': 0.287}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.287', 'recency_weight': '0.173', 'weight': '0.022'}

	Recorder: fec8f530c68b493a9b2dd5ffbbed5cdd

		Model: {'id': 'fec8f530c68b493a9b2dd5ffbbed5cdd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.123, 'Rank IC': 0.052, 'Rank ICIR': 0.32}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.320', 'recency_weight': '0.244', 'weight': '0.039'}

	Recorder: 079944d447ea46b18d04c5d5bec339ce

		Model: {'id': '079944d447ea46b18d04c5d5bec339ce', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.309, 'Rank IC': 0.02, 'Rank ICIR': 0.198}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.198', 'recency_weight': '0.707', 'weight': '0.043'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260519_11 108187504537882369 (Recorders: 4/6)

	Recorder: d214ba44ecde44e9b0d74c1aeb35e2d7

		Model: {'id': 'd214ba44ecde44e9b0d74c1aeb35e2d7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.303, 'Rank IC': 0.056, 'Rank ICIR': 0.45}, 'data_train_vec': ['2020-05-19', '2024-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.450', 'recency_weight': '0.122', 'weight': '0.038'}

	Recorder: 110cd5c8380f43a09a00eb603bcfe7fd

		Model: {'id': '110cd5c8380f43a09a00eb603bcfe7fd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.225, 'Rank IC': 0.053, 'Rank ICIR': 0.425}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.425', 'recency_weight': '0.173', 'weight': '0.048'}

	Recorder: 1c44746b8e484368acafc453457c196c

		Model: {'id': '1c44746b8e484368acafc453457c196c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.12, 'Rank IC': 0.056, 'Rank ICIR': 0.373}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.373', 'recency_weight': '0.244', 'weight': '0.053'}

	Recorder: 7e605071dead4bb582e7e7f22cc0164d

		Model: {'id': '7e605071dead4bb582e7e7f22cc0164d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.325, 'Rank IC': 0.049, 'Rank ICIR': 0.302}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.302', 'recency_weight': '0.707', 'weight': '0.100'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260519_11 149424265580955982 (Recorders: 6/6)

	Recorder: 8208db2b76854cc1b959cb46c2d4858b

		Model: {'id': '8208db2b76854cc1b959cb46c2d4858b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.308, 'Rank IC': 0.05, 'Rank ICIR': 0.34}, 'data_train_vec': ['2020-05-19', '2024-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.340', 'recency_weight': '0.122', 'weight': '0.022'}

	Recorder: 6a660f418d2b4bb2909e148dd4ce8d5c

		Model: {'id': '6a660f418d2b4bb2909e148dd4ce8d5c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.2, 'Rank IC': 0.046, 'Rank ICIR': 0.319}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.319', 'recency_weight': '0.173', 'weight': '0.027'}

	Recorder: 97d11c96d3b545c4949c8f1714a11b6c

		Model: {'id': '97d11c96d3b545c4949c8f1714a11b6c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.325, 'Rank IC': 0.064, 'Rank ICIR': 0.418}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.418', 'recency_weight': '0.244', 'weight': '0.066'}

	Recorder: 035f21cf3dfd4ccf8ae2397de6f9f461

		Model: {'id': '035f21cf3dfd4ccf8ae2397de6f9f461', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.188, 'Rank IC': 0.045, 'Rank ICIR': 0.282}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.282', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: 870c05efc5ba42208767df0c0680abf7

		Model: {'id': '870c05efc5ba42208767df0c0680abf7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.082, 'Rank IC': 0.034, 'Rank ICIR': 0.298}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.298', 'recency_weight': '0.496', 'weight': '0.068'}

	Recorder: e278f736496340c78c26c72ef3bd708f

		Model: {'id': 'e278f736496340c78c26c72ef3bd708f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.464, 'Rank IC': 0.042, 'Rank ICIR': 0.344}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.344', 'recency_weight': '0.707', 'weight': '0.129'}
