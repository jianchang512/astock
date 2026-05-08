# params 
 {'predict_dates': [{'start': '2026-05-08', 'end': '2026-05-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260508_11 645236253924936451 (Recorders: 6/6)

	Recorder: 3a9ce06082764bf0bd9a1ff26bbf6f7d

		Model: {'id': '3a9ce06082764bf0bd9a1ff26bbf6f7d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.41, 'Rank IC': 0.054, 'Rank ICIR': 0.346}, 'data_train_vec': ['2020-05-08', '2024-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.346', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: 26b7344a064149e8b17a1a210e00f8d8

		Model: {'id': '26b7344a064149e8b17a1a210e00f8d8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.272, 'Rank IC': 0.05, 'Rank ICIR': 0.332}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.332', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: a1ed91ed8c9d4aa695c0c762f4a9c822

		Model: {'id': 'a1ed91ed8c9d4aa695c0c762f4a9c822', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.208, 'Rank IC': 0.045, 'Rank ICIR': 0.276}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.276', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: 799ad64d5ccc4311afd64a545b688d39

		Model: {'id': '799ad64d5ccc4311afd64a545b688d39', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.285, 'Rank IC': 0.043, 'Rank ICIR': 0.281}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.281', 'recency_weight': '0.348', 'weight': '0.023'}

	Recorder: 29990bdcf4bb4a3d893d6af302d552ce

		Model: {'id': '29990bdcf4bb4a3d893d6af302d552ce', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.182, 'Rank IC': 0.024, 'Rank ICIR': 0.175}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.175', 'recency_weight': '0.496', 'weight': '0.013'}

	Recorder: 8f1d338087784d65a9154209e970fef4

		Model: {'id': '8f1d338087784d65a9154209e970fef4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.065, 'ICIR': 0.526, 'Rank IC': 0.073, 'Rank ICIR': 0.643}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.643', 'recency_weight': '0.707', 'weight': '0.245'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260508_11 804862590520204365 (Recorders: 5/6)

	Recorder: 60a4d2980fbd49beb295ed39100c98de

		Model: {'id': '60a4d2980fbd49beb295ed39100c98de', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.366, 'Rank IC': 0.056, 'Rank ICIR': 0.35}, 'data_train_vec': ['2020-05-08', '2024-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.350', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: f68ad8587d47486f944ded9ea6179543

		Model: {'id': 'f68ad8587d47486f944ded9ea6179543', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.238, 'Rank IC': 0.049, 'Rank ICIR': 0.323}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.323', 'recency_weight': '0.173', 'weight': '0.015'}

	Recorder: 199151d6c1b74931832d2a93df2ba2ea

		Model: {'id': '199151d6c1b74931832d2a93df2ba2ea', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.114, 'Rank IC': 0.043, 'Rank ICIR': 0.258}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.258', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: d9fd21769be94b8b967dddd0ea6ce625

		Model: {'id': 'd9fd21769be94b8b967dddd0ea6ce625', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.102, 'Rank IC': 0.046, 'Rank ICIR': 0.352}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.352', 'recency_weight': '0.348', 'weight': '0.036'}

	Recorder: 117b12feb9e14a0d97840c02ab50d2ef

		Model: {'id': '117b12feb9e14a0d97840c02ab50d2ef', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.405, 'Rank IC': 0.044, 'Rank ICIR': 0.481}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.481', 'recency_weight': '0.707', 'weight': '0.137'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260508_11 330832444709694595 (Recorders: 4/6)

	Recorder: b97837deff9c497c843490bfe2ec1610

		Model: {'id': 'b97837deff9c497c843490bfe2ec1610', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.358, 'Rank IC': 0.057, 'Rank ICIR': 0.455}, 'data_train_vec': ['2020-05-08', '2024-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.455', 'recency_weight': '0.122', 'weight': '0.021'}

	Recorder: 8b273f4584504109a8f5ab8c176a14e0

		Model: {'id': '8b273f4584504109a8f5ab8c176a14e0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.276, 'Rank IC': 0.052, 'Rank ICIR': 0.434}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.434', 'recency_weight': '0.173', 'weight': '0.027'}

	Recorder: de00f6ca1db04b6aa1aee0a5c18d1c48

		Model: {'id': 'de00f6ca1db04b6aa1aee0a5c18d1c48', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.159, 'Rank IC': 0.053, 'Rank ICIR': 0.366}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.366', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 1edfa4c7b3204a1dbd9f718cb92e3127

		Model: {'id': '1edfa4c7b3204a1dbd9f718cb92e3127', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.475, 'Rank IC': 0.059, 'Rank ICIR': 0.445}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.445', 'recency_weight': '0.707', 'weight': '0.117'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260508_11 330518836695534421 (Recorders: 6/6)

	Recorder: f7bfa172a91548708afe1623062e788d

		Model: {'id': 'f7bfa172a91548708afe1623062e788d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.441, 'Rank IC': 0.055, 'Rank ICIR': 0.367}, 'data_train_vec': ['2020-05-08', '2024-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.367', 'recency_weight': '0.122', 'weight': '0.014'}

	Recorder: 9350bce7a19d44b4bf6095a7ef21fa8b

		Model: {'id': '9350bce7a19d44b4bf6095a7ef21fa8b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.259, 'Rank IC': 0.05, 'Rank ICIR': 0.346}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.346', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 9147e1f737a2464683b09dd3d9cc49d4

		Model: {'id': '9147e1f737a2464683b09dd3d9cc49d4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.24, 'Rank IC': 0.05, 'Rank ICIR': 0.322}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.322', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 9cedf86f57e745b38e9bc205c3050907

		Model: {'id': '9cedf86f57e745b38e9bc205c3050907', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.283, 'Rank IC': 0.047, 'Rank ICIR': 0.324}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.324', 'recency_weight': '0.348', 'weight': '0.031'}

	Recorder: 8e10eba93d8e4e3c82c54ec5a51d5874

		Model: {'id': '8e10eba93d8e4e3c82c54ec5a51d5874', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.211, 'Rank IC': 0.029, 'Rank ICIR': 0.245}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.245', 'recency_weight': '0.496', 'weight': '0.025'}

	Recorder: b98334353d7e48d99538cc43a9dba0c7

		Model: {'id': 'b98334353d7e48d99538cc43a9dba0c7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.434, 'Rank IC': 0.061, 'Rank ICIR': 0.519}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.519', 'recency_weight': '0.707', 'weight': '0.160'}
