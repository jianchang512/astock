# params 
 {'predict_dates': [{'start': '2026-04-29', 'end': '2026-04-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260429_12 878186363067046182 (Recorders: 6/6)

	Recorder: f7c1facec16947f7971724f1f2e8d1fb

		Model: {'id': 'f7c1facec16947f7971724f1f2e8d1fb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.471, 'Rank IC': 0.064, 'Rank ICIR': 0.404}, 'data_train_vec': ['2020-04-29', '2024-10-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.404', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: 2eca27e5cd744e458691e586baa148cf

		Model: {'id': '2eca27e5cd744e458691e586baa148cf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.242, 'Rank IC': 0.048, 'Rank ICIR': 0.315}, 'data_train_vec': ['2021-04-29', '2025-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.315', 'recency_weight': '0.173', 'weight': '0.015'}

	Recorder: 402865f3d3f54683ba2ec632c8c22326

		Model: {'id': '402865f3d3f54683ba2ec632c8c22326', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.196, 'Rank IC': 0.041, 'Rank ICIR': 0.26}, 'data_train_vec': ['2022-04-29', '2025-04-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.260', 'recency_weight': '0.244', 'weight': '0.015'}

	Recorder: e09cb8c89c7f4b988181c574c083c286

		Model: {'id': 'e09cb8c89c7f4b988181c574c083c286', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.338, 'Rank IC': 0.055, 'Rank ICIR': 0.332}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.332', 'recency_weight': '0.347', 'weight': '0.034'}

	Recorder: 17ad7689cb7d4ebbb14f43dcedbc6393

		Model: {'id': '17ad7689cb7d4ebbb14f43dcedbc6393', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.22, 'Rank IC': 0.031, 'Rank ICIR': 0.241}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.241', 'recency_weight': '0.492', 'weight': '0.025'}

	Recorder: 2db082259e004a9d9e22f8ef471be849

		Model: {'id': '2db082259e004a9d9e22f8ef471be849', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.514, 'Rank IC': 0.08, 'Rank ICIR': 0.52}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.520', 'recency_weight': '0.704', 'weight': '0.169'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260429_11 887449207237642639 (Recorders: 6/6)

	Recorder: 85e56711d11748579594b2af654f1378

		Model: {'id': '85e56711d11748579594b2af654f1378', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.387, 'Rank IC': 0.059, 'Rank ICIR': 0.356}, 'data_train_vec': ['2020-04-29', '2024-10-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.356', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 6fca8baad45e443da8cc5069fa0faaa1

		Model: {'id': '6fca8baad45e443da8cc5069fa0faaa1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.203, 'Rank IC': 0.046, 'Rank ICIR': 0.301}, 'data_train_vec': ['2021-04-29', '2025-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.301', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 7aabd09d711149dd8664817a419b4958

		Model: {'id': '7aabd09d711149dd8664817a419b4958', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.113, 'Rank IC': 0.042, 'Rank ICIR': 0.253}, 'data_train_vec': ['2022-04-29', '2025-04-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.253', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: f03ee17d0296425384be598f2b2ebe47

		Model: {'id': 'f03ee17d0296425384be598f2b2ebe47', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.162, 'Rank IC': 0.046, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.290', 'recency_weight': '0.347', 'weight': '0.026'}

	Recorder: 51f470d66b3e44878f02fa9fc2f93696

		Model: {'id': '51f470d66b3e44878f02fa9fc2f93696', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.098, 'Rank IC': 0.028, 'Rank ICIR': 0.209}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.209', 'recency_weight': '0.492', 'weight': '0.019'}

	Recorder: 37d47de5bcd34fc7806bc0aa34d89dad

		Model: {'id': '37d47de5bcd34fc7806bc0aa34d89dad', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.07, 'ICIR': 0.545, 'Rank IC': 0.067, 'Rank ICIR': 0.486}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.486', 'recency_weight': '0.704', 'weight': '0.147'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260429_11 461059329013030199 (Recorders: 5/6)

	Recorder: ac77199566f644639e2801adcf0505f7

		Model: {'id': 'ac77199566f644639e2801adcf0505f7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.398, 'Rank IC': 0.063, 'Rank ICIR': 0.494}, 'data_train_vec': ['2020-04-29', '2024-10-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.494', 'recency_weight': '0.121', 'weight': '0.026'}

	Recorder: 0ee13e233a3d4d6dbff2f137096c01b9

		Model: {'id': '0ee13e233a3d4d6dbff2f137096c01b9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.255, 'Rank IC': 0.051, 'Rank ICIR': 0.419}, 'data_train_vec': ['2021-04-29', '2025-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.419', 'recency_weight': '0.173', 'weight': '0.027'}

	Recorder: 686b9264f2aa4e158b5fb3f000b3063a

		Model: {'id': '686b9264f2aa4e158b5fb3f000b3063a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.17, 'Rank IC': 0.052, 'Rank ICIR': 0.362}, 'data_train_vec': ['2022-04-29', '2025-04-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.362', 'recency_weight': '0.244', 'weight': '0.028'}

	Recorder: 9ff23800d7a042d0829fdf675e27b997

		Model: {'id': '9ff23800d7a042d0829fdf675e27b997', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.111, 'Rank IC': 0.037, 'Rank ICIR': 0.279}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.279', 'recency_weight': '0.347', 'weight': '0.024'}

	Recorder: f143ecb771b54f079b04d30d48b42d3e

		Model: {'id': 'f143ecb771b54f079b04d30d48b42d3e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.065, 'ICIR': 0.471, 'Rank IC': 0.045, 'Rank ICIR': 0.307}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.307', 'recency_weight': '0.704', 'weight': '0.059'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260429_11 982075602267037155 (Recorders: 6/6)

	Recorder: 54acb3c369d84d74932b86d1e5fab0bc

		Model: {'id': '54acb3c369d84d74932b86d1e5fab0bc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.398, 'Rank IC': 0.059, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-04-29', '2024-10-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.379', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 6801a36aae474bdfbb51d26bff1ff621

		Model: {'id': '6801a36aae474bdfbb51d26bff1ff621', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.231, 'Rank IC': 0.047, 'Rank ICIR': 0.327}, 'data_train_vec': ['2021-04-29', '2025-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.327', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: 8338c648213f496fb49b8970aacc0472

		Model: {'id': '8338c648213f496fb49b8970aacc0472', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.162, 'Rank IC': 0.044, 'Rank ICIR': 0.284}, 'data_train_vec': ['2022-04-29', '2025-04-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.284', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: b0b2cc3b92644bbf9573ca791c6c8777

		Model: {'id': 'b0b2cc3b92644bbf9573ca791c6c8777', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.303, 'Rank IC': 0.057, 'Rank ICIR': 0.364}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.364', 'recency_weight': '0.347', 'weight': '0.041'}

	Recorder: df7caf03529c41b9adb58684230ecd03

		Model: {'id': 'df7caf03529c41b9adb58684230ecd03', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.281, 'Rank IC': 0.045, 'Rank ICIR': 0.391}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.391', 'recency_weight': '0.492', 'weight': '0.067'}

	Recorder: ced1b8ae49b24b6db1d909fc816df808

		Model: {'id': 'ced1b8ae49b24b6db1d909fc816df808', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.076, 'ICIR': 0.528, 'Rank IC': 0.081, 'Rank ICIR': 0.522}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.522', 'recency_weight': '0.704', 'weight': '0.170'}
