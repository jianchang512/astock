# params 
 {'predict_dates': [{'start': '2026-04-30', 'end': '2026-04-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260430_12 997305124280137037 (Recorders: 6/6)

	Recorder: 7da9953abecc4d6085987c8161b2d40c

		Model: {'id': '7da9953abecc4d6085987c8161b2d40c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.44, 'Rank IC': 0.062, 'Rank ICIR': 0.391}, 'data_train_vec': ['2020-04-30', '2024-10-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.391', 'recency_weight': '0.121', 'weight': '0.017'}

	Recorder: b09b307795554a8595332dbc00f09e85

		Model: {'id': 'b09b307795554a8595332dbc00f09e85', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.248, 'Rank IC': 0.046, 'Rank ICIR': 0.315}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.315', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: 78d5723d8d1b420ca345a023d9e5372f

		Model: {'id': '78d5723d8d1b420ca345a023d9e5372f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.189, 'Rank IC': 0.042, 'Rank ICIR': 0.255}, 'data_train_vec': ['2022-04-30', '2025-04-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.255', 'recency_weight': '0.244', 'weight': '0.015'}

	Recorder: b895542cda994a5888d00a247b053274

		Model: {'id': 'b895542cda994a5888d00a247b053274', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.266, 'Rank IC': 0.054, 'Rank ICIR': 0.323}, 'data_train_vec': ['2023-04-30', '2025-07-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.323', 'recency_weight': '0.347', 'weight': '0.034'}

	Recorder: 241e84838ddc4da2b2fcdeb4bb8a0785

		Model: {'id': '241e84838ddc4da2b2fcdeb4bb8a0785', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.195, 'Rank IC': 0.028, 'Rank ICIR': 0.221}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.221', 'recency_weight': '0.490', 'weight': '0.022'}

	Recorder: 0e731182d0af4ad0b51b0d0b5b463d68

		Model: {'id': '0e731182d0af4ad0b51b0d0b5b463d68', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.539, 'Rank IC': 0.076, 'Rank ICIR': 0.481}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.481', 'recency_weight': '0.704', 'weight': '0.152'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260430_12 780529419496438874 (Recorders: 5/6)

	Recorder: 375f8c9a9f614e148c59a8762849d4d7

		Model: {'id': '375f8c9a9f614e148c59a8762849d4d7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.363, 'Rank IC': 0.057, 'Rank ICIR': 0.337}, 'data_train_vec': ['2020-04-30', '2024-10-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.337', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 0ca07c4bea7f4faab536f6679ae9b043

		Model: {'id': '0ca07c4bea7f4faab536f6679ae9b043', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.219, 'Rank IC': 0.048, 'Rank ICIR': 0.312}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.312', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: d1d5454c80704b98952817885f8f938b

		Model: {'id': 'd1d5454c80704b98952817885f8f938b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.099, 'Rank IC': 0.039, 'Rank ICIR': 0.239}, 'data_train_vec': ['2022-04-30', '2025-04-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.239', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: 7a523681320549a9a0da3e583ddf61b4

		Model: {'id': '7a523681320549a9a0da3e583ddf61b4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.093, 'Rank IC': 0.041, 'Rank ICIR': 0.253}, 'data_train_vec': ['2023-04-30', '2025-07-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.253', 'recency_weight': '0.347', 'weight': '0.021'}

	Recorder: 43378faf8eaa4d75a8c23fe547f2946f

		Model: {'id': '43378faf8eaa4d75a8c23fe547f2946f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.564, 'Rank IC': 0.073, 'Rank ICIR': 0.565}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.565', 'recency_weight': '0.704', 'weight': '0.210'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260430_11 498701024711419288 (Recorders: 4/6)

	Recorder: 66417afff06d45dda4a21a92c170c0f8

		Model: {'id': '66417afff06d45dda4a21a92c170c0f8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.375, 'Rank IC': 0.062, 'Rank ICIR': 0.481}, 'data_train_vec': ['2020-04-30', '2024-10-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.481', 'recency_weight': '0.121', 'weight': '0.026'}

	Recorder: 2f5e58c702064a3095246436cbf3cb1a

		Model: {'id': '2f5e58c702064a3095246436cbf3cb1a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.237, 'Rank IC': 0.05, 'Rank ICIR': 0.407}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.407', 'recency_weight': '0.173', 'weight': '0.027'}

	Recorder: 75049121ecb549ccb1978497743ad980

		Model: {'id': '75049121ecb549ccb1978497743ad980', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.16, 'Rank IC': 0.051, 'Rank ICIR': 0.356}, 'data_train_vec': ['2022-04-30', '2025-04-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.356', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 485e6cfefe1d40de81f16a2c54580412

		Model: {'id': '485e6cfefe1d40de81f16a2c54580412', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.44, 'Rank IC': 0.042, 'Rank ICIR': 0.315}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.315', 'recency_weight': '0.704', 'weight': '0.065'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260430_11 796143334572511587 (Recorders: 6/6)

	Recorder: a5f2375c94da4ce190171142e1b92f1b

		Model: {'id': 'a5f2375c94da4ce190171142e1b92f1b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.336, 'Rank IC': 0.055, 'Rank ICIR': 0.354}, 'data_train_vec': ['2020-04-30', '2024-10-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.354', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 7d2ab370e42445e2adfacd32d35f2a5b

		Model: {'id': '7d2ab370e42445e2adfacd32d35f2a5b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.221, 'Rank IC': 0.046, 'Rank ICIR': 0.328}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.328', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 8d227e7601e44b59905c6db4e39cbeaf

		Model: {'id': '8d227e7601e44b59905c6db4e39cbeaf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.255, 'Rank IC': 0.047, 'Rank ICIR': 0.292}, 'data_train_vec': ['2022-04-30', '2025-04-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.292', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: 79f59214ea374e50a3f9d60111a7b5dd

		Model: {'id': '79f59214ea374e50a3f9d60111a7b5dd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.324, 'Rank IC': 0.053, 'Rank ICIR': 0.343}, 'data_train_vec': ['2023-04-30', '2025-07-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.343', 'recency_weight': '0.347', 'weight': '0.038'}

	Recorder: d8b335cdf5b74cf796ad9e097d8d640a

		Model: {'id': 'd8b335cdf5b74cf796ad9e097d8d640a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.261, 'Rank IC': 0.042, 'Rank ICIR': 0.369}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.369', 'recency_weight': '0.490', 'weight': '0.062'}

	Recorder: 3587b992731a4520959e2627400662f2

		Model: {'id': '3587b992731a4520959e2627400662f2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.449, 'Rank IC': 0.079, 'Rank ICIR': 0.51}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.510', 'recency_weight': '0.704', 'weight': '0.171'}
