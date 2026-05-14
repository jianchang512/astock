# params 
 {'predict_dates': [{'start': '2026-05-14', 'end': '2026-05-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260514_11 642561679571124331 (Recorders: 6/6)

	Recorder: 5cb83123adfd419c8e4cba357233bbc4

		Model: {'id': '5cb83123adfd419c8e4cba357233bbc4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.364, 'Rank IC': 0.054, 'Rank ICIR': 0.351}, 'data_train_vec': ['2020-05-14', '2024-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.351', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: 693287438d184235978bec61ece95139

		Model: {'id': '693287438d184235978bec61ece95139', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.199, 'Rank IC': 0.045, 'Rank ICIR': 0.296}, 'data_train_vec': ['2021-05-14', '2025-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.296', 'recency_weight': '0.173', 'weight': '0.013'}

	Recorder: 9854dc26d23a4ab2ba727c8f345db4ed

		Model: {'id': '9854dc26d23a4ab2ba727c8f345db4ed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.256, 'Rank IC': 0.053, 'Rank ICIR': 0.326}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.326', 'recency_weight': '0.244', 'weight': '0.023'}

	Recorder: dea2c97dd3df4e73b2fadcc1d007aad4

		Model: {'id': 'dea2c97dd3df4e73b2fadcc1d007aad4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.216, 'Rank IC': 0.046, 'Rank ICIR': 0.28}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.280', 'recency_weight': '0.348', 'weight': '0.024'}

	Recorder: f40c49e255ba49db8fe0246d5de759b2

		Model: {'id': 'f40c49e255ba49db8fe0246d5de759b2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.215, 'Rank IC': 0.051, 'Rank ICIR': 0.375}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.375', 'recency_weight': '0.496', 'weight': '0.061'}

	Recorder: 52535a943c7349c08360a7191ff38e2d

		Model: {'id': '52535a943c7349c08360a7191ff38e2d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.07, 'ICIR': 0.648, 'Rank IC': 0.066, 'Rank ICIR': 0.561}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.561', 'recency_weight': '0.707', 'weight': '0.194'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260514_11 495677710573988446 (Recorders: 5/6)

	Recorder: f604c09b23ee4245a01e1d0c015e9a43

		Model: {'id': 'f604c09b23ee4245a01e1d0c015e9a43', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.329, 'Rank IC': 0.053, 'Rank ICIR': 0.346}, 'data_train_vec': ['2020-05-14', '2024-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.346', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: 283415dc34d04b8e952ef96e69307a2a

		Model: {'id': '283415dc34d04b8e952ef96e69307a2a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.143, 'Rank IC': 0.04, 'Rank ICIR': 0.261}, 'data_train_vec': ['2021-05-14', '2025-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.261', 'recency_weight': '0.173', 'weight': '0.010'}

	Recorder: 33760a78b9db4c6c8253146061f6bfae

		Model: {'id': '33760a78b9db4c6c8253146061f6bfae', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.112, 'Rank IC': 0.043, 'Rank ICIR': 0.256}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.256', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: 87b42486e24c4a0e90474eaddc3da05a

		Model: {'id': '87b42486e24c4a0e90474eaddc3da05a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.085, 'Rank IC': 0.043, 'Rank ICIR': 0.35}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.350', 'recency_weight': '0.496', 'weight': '0.053'}

	Recorder: ff655738bd48411eb90a77fb99e76725

		Model: {'id': 'ff655738bd48411eb90a77fb99e76725', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.331, 'Rank IC': 0.051, 'Rank ICIR': 0.498}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.498', 'recency_weight': '0.707', 'weight': '0.153'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260514_11 251275300626910380 (Recorders: 4/6)

	Recorder: a5ef1082ea4f48d3b9b0acb88c9ae075

		Model: {'id': 'a5ef1082ea4f48d3b9b0acb88c9ae075', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.334, 'Rank IC': 0.057, 'Rank ICIR': 0.451}, 'data_train_vec': ['2020-05-14', '2024-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.451', 'recency_weight': '0.122', 'weight': '0.022'}

	Recorder: 7fdbc56caa79450eadf394de243f641f

		Model: {'id': '7fdbc56caa79450eadf394de243f641f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.232, 'Rank IC': 0.051, 'Rank ICIR': 0.414}, 'data_train_vec': ['2021-05-14', '2025-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.414', 'recency_weight': '0.173', 'weight': '0.026'}

	Recorder: c110c3e1a5aa488a84e9125ed6c45e02

		Model: {'id': 'c110c3e1a5aa488a84e9125ed6c45e02', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.156, 'Rank IC': 0.056, 'Rank ICIR': 0.375}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.375', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: dced309e6e704a7c86846c36cea8efd0

		Model: {'id': 'dced309e6e704a7c86846c36cea8efd0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.388, 'Rank IC': 0.061, 'Rank ICIR': 0.419}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.419', 'recency_weight': '0.707', 'weight': '0.108'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260514_11 397265553557686021 (Recorders: 6/6)

	Recorder: 3272943be78f4e4391caf95c7b2b4dd6

		Model: {'id': '3272943be78f4e4391caf95c7b2b4dd6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.322, 'Rank IC': 0.05, 'Rank ICIR': 0.363}, 'data_train_vec': ['2020-05-14', '2024-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.363', 'recency_weight': '0.122', 'weight': '0.014'}

	Recorder: ae2b9b70b1ed43b2a23ff9072529c2a9

		Model: {'id': 'ae2b9b70b1ed43b2a23ff9072529c2a9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.164, 'Rank IC': 0.037, 'Rank ICIR': 0.264}, 'data_train_vec': ['2021-05-14', '2025-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.264', 'recency_weight': '0.173', 'weight': '0.011'}

	Recorder: bf957c3789b74eba8d4d9c76de269ae2

		Model: {'id': 'bf957c3789b74eba8d4d9c76de269ae2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.216, 'Rank IC': 0.05, 'Rank ICIR': 0.316}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.316', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 9ef7611924fa46fdbdbd0c6c6142cac0

		Model: {'id': '9ef7611924fa46fdbdbd0c6c6142cac0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.204, 'Rank IC': 0.049, 'Rank ICIR': 0.31}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.310', 'recency_weight': '0.348', 'weight': '0.029'}

	Recorder: b7063db41ead4c4b94f42bb130f09d54

		Model: {'id': 'b7063db41ead4c4b94f42bb130f09d54', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.227, 'Rank IC': 0.041, 'Rank ICIR': 0.317}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.317', 'recency_weight': '0.496', 'weight': '0.043'}

	Recorder: 39a941b55a9e4beca2584a9ed777781e

		Model: {'id': '39a941b55a9e4beca2584a9ed777781e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.486, 'Rank IC': 0.049, 'Rank ICIR': 0.454}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.454', 'recency_weight': '0.707', 'weight': '0.127'}
