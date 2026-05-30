# params 
 {'predict_dates': [{'start': '2026-05-29', 'end': '2026-05-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260530_14 723125553589087998 (Recorders: 6/6)

	Recorder: 1362b17cc2eb47d6a1a3e3eefe7b1211

		Model: {'id': '1362b17cc2eb47d6a1a3e3eefe7b1211', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.354, 'Rank IC': 0.06, 'Rank ICIR': 0.407}, 'data_train_vec': ['2020-05-30', '2024-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.407', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 556202fa8b6d411982e317ffdeb39a74

		Model: {'id': '556202fa8b6d411982e317ffdeb39a74', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.246, 'Rank IC': 0.058, 'Rank ICIR': 0.411}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.411', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 747a8cc4045443c2ad0d1ac2d5170d44

		Model: {'id': '747a8cc4045443c2ad0d1ac2d5170d44', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.219, 'Rank IC': 0.067, 'Rank ICIR': 0.392}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.392', 'recency_weight': '0.245', 'weight': '0.030'}

	Recorder: 619f8752ee6045339c2711c9cf4fa0f3

		Model: {'id': '619f8752ee6045339c2711c9cf4fa0f3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.268, 'Rank IC': 0.063, 'Rank ICIR': 0.388}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.388', 'recency_weight': '0.347', 'weight': '0.041'}

	Recorder: 23c09791921947508264aa0c3d9d0840

		Model: {'id': '23c09791921947508264aa0c3d9d0840', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.24, 'Rank IC': 0.068, 'Rank ICIR': 0.479}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.479', 'recency_weight': '0.498', 'weight': '0.091'}

	Recorder: d0839c5385a641b1955e543eb3052dbe

		Model: {'id': 'd0839c5385a641b1955e543eb3052dbe', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.065, 'ICIR': 0.517, 'Rank IC': 0.046, 'Rank ICIR': 0.273}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.273', 'recency_weight': '0.704', 'weight': '0.042'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260530_14 500891169457761604 (Recorders: 6/6)

	Recorder: 81863849cd1a4db3893e6a1fe10e37cd

		Model: {'id': '81863849cd1a4db3893e6a1fe10e37cd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.335, 'Rank IC': 0.06, 'Rank ICIR': 0.403}, 'data_train_vec': ['2020-05-30', '2024-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.403', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 8b4290f9455641b2af8fea0088476989

		Model: {'id': '8b4290f9455641b2af8fea0088476989', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.195, 'Rank IC': 0.055, 'Rank ICIR': 0.362}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.362', 'recency_weight': '0.173', 'weight': '0.018'}

	Recorder: 2287d41393734495a8fb11115c70511d

		Model: {'id': '2287d41393734495a8fb11115c70511d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.133, 'Rank IC': 0.063, 'Rank ICIR': 0.349}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.349', 'recency_weight': '0.245', 'weight': '0.024'}

	Recorder: 91451a85cb8a446d856cdc7b93a4b4b4

		Model: {'id': '91451a85cb8a446d856cdc7b93a4b4b4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.244, 'Rank IC': 0.067, 'Rank ICIR': 0.397}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.397', 'recency_weight': '0.347', 'weight': '0.043'}

	Recorder: fb7b52901020485789dd476ad1bbebc4

		Model: {'id': 'fb7b52901020485789dd476ad1bbebc4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.142, 'Rank IC': 0.055, 'Rank ICIR': 0.385}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.385', 'recency_weight': '0.498', 'weight': '0.059'}

	Recorder: 0cdf53f724f64c39a7b462fb1f31ff0b

		Model: {'id': '0cdf53f724f64c39a7b462fb1f31ff0b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.409, 'Rank IC': 0.043, 'Rank ICIR': 0.315}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.315', 'recency_weight': '0.704', 'weight': '0.056'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260530_14 362137214570227943 (Recorders: 6/6)

	Recorder: 01ac961aa2f44df2a4c864d5960949e2

		Model: {'id': '01ac961aa2f44df2a4c864d5960949e2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.33, 'Rank IC': 0.064, 'Rank ICIR': 0.468}, 'data_train_vec': ['2020-05-30', '2024-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.468', 'recency_weight': '0.122', 'weight': '0.021'}

	Recorder: 8f6340254117422cad3c1cfae7fbaec5

		Model: {'id': '8f6340254117422cad3c1cfae7fbaec5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.244, 'Rank IC': 0.064, 'Rank ICIR': 0.463}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.463', 'recency_weight': '0.173', 'weight': '0.029'}

	Recorder: 5001903f88e0480fa6db52e4568c821c

		Model: {'id': '5001903f88e0480fa6db52e4568c821c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.154, 'Rank IC': 0.066, 'Rank ICIR': 0.416}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.416', 'recency_weight': '0.245', 'weight': '0.034'}

	Recorder: 24570d173ff8448f985a9c31128744ce

		Model: {'id': '24570d173ff8448f985a9c31128744ce', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.081, 'Rank IC': 0.044, 'Rank ICIR': 0.312}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.312', 'recency_weight': '0.347', 'weight': '0.027'}

	Recorder: ceb7148860974ea18be6ee3a4c587bf7

		Model: {'id': 'ceb7148860974ea18be6ee3a4c587bf7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.131, 'Rank IC': 0.04, 'Rank ICIR': 0.31}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.310', 'recency_weight': '0.498', 'weight': '0.038'}

	Recorder: bda078bb2573453fa5661a259c8d9a36

		Model: {'id': 'bda078bb2573453fa5661a259c8d9a36', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.092, 'ICIR': 0.515, 'Rank IC': 0.094, 'Rank ICIR': 0.457}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.457', 'recency_weight': '0.704', 'weight': '0.117'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260530_14 987528833819608223 (Recorders: 6/6)

	Recorder: 9cb209d4188a4f189a5ff5a5d53e0862

		Model: {'id': '9cb209d4188a4f189a5ff5a5d53e0862', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.287, 'Rank IC': 0.055, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-05-30', '2024-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.370', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: 8e87635426aa431f9e7f4dd7bb75b600

		Model: {'id': '8e87635426aa431f9e7f4dd7bb75b600', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.206, 'Rank IC': 0.057, 'Rank ICIR': 0.395}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.395', 'recency_weight': '0.173', 'weight': '0.021'}

	Recorder: c6e3cf10daef4a3ea4c9d34b5abb4fae

		Model: {'id': 'c6e3cf10daef4a3ea4c9d34b5abb4fae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.272, 'Rank IC': 0.07, 'Rank ICIR': 0.425}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.425', 'recency_weight': '0.245', 'weight': '0.035'}

	Recorder: fa73623bf16e4d1aa25c86de81007f34

		Model: {'id': 'fa73623bf16e4d1aa25c86de81007f34', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.274, 'Rank IC': 0.065, 'Rank ICIR': 0.42}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.420', 'recency_weight': '0.347', 'weight': '0.049'}

	Recorder: dd8a8958b1c243619f458ca26142a0ad

		Model: {'id': 'dd8a8958b1c243619f458ca26142a0ad', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.166, 'Rank IC': 0.058, 'Rank ICIR': 0.459}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.459', 'recency_weight': '0.498', 'weight': '0.083'}

	Recorder: d2adb9a09e8548c9b508f3bdb931ec44

		Model: {'id': 'd2adb9a09e8548c9b508f3bdb931ec44', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.448, 'Rank IC': 0.062, 'Rank ICIR': 0.364}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.364', 'recency_weight': '0.704', 'weight': '0.074'}
