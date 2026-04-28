# params 
 {'predict_dates': [{'start': '2026-04-28', 'end': '2026-04-28'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260428_13 538202707613146520 (Recorders: 6/6)

	Recorder: 6e5e937e61594771be7d22c9a8c298f3

		Model: {'id': '6e5e937e61594771be7d22c9a8c298f3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.403, 'Rank IC': 0.06, 'Rank ICIR': 0.366}, 'data_train_vec': ['2020-04-28', '2024-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.366', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: d5e317d827c2446e9fa594c262ad45a8

		Model: {'id': 'd5e317d827c2446e9fa594c262ad45a8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.207, 'Rank IC': 0.042, 'Rank ICIR': 0.275}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.275', 'recency_weight': '0.173', 'weight': '0.011'}

	Recorder: f27c8f4285ef47b3a0d481c36cbe4eb8

		Model: {'id': 'f27c8f4285ef47b3a0d481c36cbe4eb8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.236, 'Rank IC': 0.048, 'Rank ICIR': 0.303}, 'data_train_vec': ['2022-04-28', '2025-04-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.303', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: 65c05fcd907348c0aac59dd0f6871914

		Model: {'id': '65c05fcd907348c0aac59dd0f6871914', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.25, 'Rank IC': 0.059, 'Rank ICIR': 0.333}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.333', 'recency_weight': '0.347', 'weight': '0.032'}

	Recorder: 74e60a98ccc84c68bc67f92b20aae08d

		Model: {'id': '74e60a98ccc84c68bc67f92b20aae08d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.215, 'Rank IC': 0.032, 'Rank ICIR': 0.243}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.243', 'recency_weight': '0.494', 'weight': '0.024'}

	Recorder: ff1dcf5155f44b1eb1e8294d75749905

		Model: {'id': 'ff1dcf5155f44b1eb1e8294d75749905', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.525, 'Rank IC': 0.084, 'Rank ICIR': 0.523}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.523', 'recency_weight': '0.704', 'weight': '0.160'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260428_13 363253233104616870 (Recorders: 6/6)

	Recorder: 2df7f5514d2b4dd897b8464cb815ae54

		Model: {'id': '2df7f5514d2b4dd897b8464cb815ae54', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.378, 'Rank IC': 0.061, 'Rank ICIR': 0.373}, 'data_train_vec': ['2020-04-28', '2024-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.373', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: f07cf2d7a78f43feb924c1b82fcaab06

		Model: {'id': 'f07cf2d7a78f43feb924c1b82fcaab06', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.208, 'Rank IC': 0.048, 'Rank ICIR': 0.312}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.312', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 2b1aeba96d9f4444b51aa561785803f1

		Model: {'id': '2b1aeba96d9f4444b51aa561785803f1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.113, 'Rank IC': 0.042, 'Rank ICIR': 0.26}, 'data_train_vec': ['2022-04-28', '2025-04-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.260', 'recency_weight': '0.244', 'weight': '0.014'}

	Recorder: 0491c3625470453aae346f40a75e77b8

		Model: {'id': '0491c3625470453aae346f40a75e77b8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.247, 'Rank IC': 0.058, 'Rank ICIR': 0.419}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.419', 'recency_weight': '0.347', 'weight': '0.051'}

	Recorder: 7cf288afaa9d44ad89ae4e231675de6f

		Model: {'id': '7cf288afaa9d44ad89ae4e231675de6f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.084, 'Rank IC': 0.028, 'Rank ICIR': 0.213}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.213', 'recency_weight': '0.494', 'weight': '0.019'}

	Recorder: 6f92ccbd2d1749bdb5105cec2985c934

		Model: {'id': '6f92ccbd2d1749bdb5105cec2985c934', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.545, 'Rank IC': 0.075, 'Rank ICIR': 0.503}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.503', 'recency_weight': '0.704', 'weight': '0.148'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260428_13 540475166294539464 (Recorders: 5/6)

	Recorder: 1d97b5e4a1a34d56b8d35903ce2a1362

		Model: {'id': '1d97b5e4a1a34d56b8d35903ce2a1362', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.397, 'Rank IC': 0.063, 'Rank ICIR': 0.49}, 'data_train_vec': ['2020-04-28', '2024-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.490', 'recency_weight': '0.121', 'weight': '0.024'}

	Recorder: 6ed1f022bc2941c092d880ef184e8f85

		Model: {'id': '6ed1f022bc2941c092d880ef184e8f85', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.252, 'Rank IC': 0.05, 'Rank ICIR': 0.414}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.414', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: 023c9076bc914ca1aacbf2b6b2dfe22f

		Model: {'id': '023c9076bc914ca1aacbf2b6b2dfe22f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.172, 'Rank IC': 0.053, 'Rank ICIR': 0.361}, 'data_train_vec': ['2022-04-28', '2025-04-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.361', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: df74be2162054d5d8b3f0ed5014be926

		Model: {'id': 'df74be2162054d5d8b3f0ed5014be926', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.112, 'Rank IC': 0.039, 'Rank ICIR': 0.287}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.287', 'recency_weight': '0.347', 'weight': '0.024'}

	Recorder: 9f18a92a471249c9853d444bab8e6dce

		Model: {'id': '9f18a92a471249c9853d444bab8e6dce', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.468, 'Rank IC': 0.043, 'Rank ICIR': 0.296}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.296', 'recency_weight': '0.704', 'weight': '0.051'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260428_12 318386424915561419 (Recorders: 6/6)

	Recorder: 3a59e2c508054050886ce23aaa32d781

		Model: {'id': '3a59e2c508054050886ce23aaa32d781', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.362, 'Rank IC': 0.06, 'Rank ICIR': 0.373}, 'data_train_vec': ['2020-04-28', '2024-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.373', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 8c0ae77abd574c5f91fe8c5f0205b12d

		Model: {'id': '8c0ae77abd574c5f91fe8c5f0205b12d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.199, 'Rank IC': 0.045, 'Rank ICIR': 0.313}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.313', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: b6cbbb81a8e34858bb86a8452a411d76

		Model: {'id': 'b6cbbb81a8e34858bb86a8452a411d76', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.186, 'Rank IC': 0.052, 'Rank ICIR': 0.327}, 'data_train_vec': ['2022-04-28', '2025-04-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.327', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: 89b0b5154d8947ae9c67f47c13263536

		Model: {'id': '89b0b5154d8947ae9c67f47c13263536', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.233, 'Rank IC': 0.061, 'Rank ICIR': 0.385}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.385', 'recency_weight': '0.347', 'weight': '0.043'}

	Recorder: e9398b8faf2f4f7290d71032d0ce2c8f

		Model: {'id': 'e9398b8faf2f4f7290d71032d0ce2c8f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.27, 'Rank IC': 0.045, 'Rank ICIR': 0.39}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.390', 'recency_weight': '0.494', 'weight': '0.062'}

	Recorder: a0da7b8332db4350bae3e82480a01bcb

		Model: {'id': 'a0da7b8332db4350bae3e82480a01bcb', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.568, 'Rank IC': 0.085, 'Rank ICIR': 0.55}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.550', 'recency_weight': '0.704', 'weight': '0.177'}
