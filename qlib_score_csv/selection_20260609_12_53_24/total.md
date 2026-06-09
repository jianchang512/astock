# params 
 {'predict_dates': [{'start': '2026-06-09', 'end': '2026-06-09'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260609_12 507406302961340985 (Recorders: 6/6)

	Recorder: 416e2da349e3434fbd47bd23ec9d05de

		Model: {'id': '416e2da349e3434fbd47bd23ec9d05de', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.364, 'Rank IC': 0.063, 'Rank ICIR': 0.404}, 'data_train_vec': ['2020-06-09', '2024-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.404', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 7a6d6775aab34958b4b48358061695b1

		Model: {'id': '7a6d6775aab34958b4b48358061695b1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.317, 'Rank IC': 0.068, 'Rank ICIR': 0.46}, 'data_train_vec': ['2021-06-09', '2025-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.460', 'recency_weight': '0.171', 'weight': '0.035'}

	Recorder: 643e14bb466045d19c8fea562ad4f172

		Model: {'id': '643e14bb466045d19c8fea562ad4f172', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.243, 'Rank IC': 0.067, 'Rank ICIR': 0.405}, 'data_train_vec': ['2022-06-09', '2025-06-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.405', 'recency_weight': '0.244', 'weight': '0.038'}

	Recorder: 2a80c64c70ec4c11bf170a2ea927adbf

		Model: {'id': '2a80c64c70ec4c11bf170a2ea927adbf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.21, 'Rank IC': 0.065, 'Rank ICIR': 0.352}, 'data_train_vec': ['2023-06-09', '2025-09-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.352', 'recency_weight': '0.348', 'weight': '0.041'}

	Recorder: 4ccc74acd7d64a02950cfc4a7cec64c9

		Model: {'id': '4ccc74acd7d64a02950cfc4a7cec64c9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.257, 'Rank IC': 0.067, 'Rank ICIR': 0.447}, 'data_train_vec': ['2024-06-09', '2025-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.447', 'recency_weight': '0.494', 'weight': '0.094'}

	Recorder: 3efa90d0d0d84d51991efbf2952e10ce

		Model: {'id': '3efa90d0d0d84d51991efbf2952e10ce', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.417, 'Rank IC': 0.031, 'Rank ICIR': 0.155}, 'data_train_vec': ['2025-06-09', '2026-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.155', 'recency_weight': '0.699', 'weight': '0.016'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260609_12 758327085708345114 (Recorders: 6/6)

	Recorder: d3357071fce043c3aeec228a772575b2

		Model: {'id': 'd3357071fce043c3aeec228a772575b2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.33, 'Rank IC': 0.063, 'Rank ICIR': 0.39}, 'data_train_vec': ['2020-06-09', '2024-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.390', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: 7bcc2bad3f6349f499258980733f0d12

		Model: {'id': '7bcc2bad3f6349f499258980733f0d12', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.256, 'Rank IC': 0.064, 'Rank ICIR': 0.437}, 'data_train_vec': ['2021-06-09', '2025-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.437', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: 9665af96f9df4790b8c6ce9fd218545c

		Model: {'id': '9665af96f9df4790b8c6ce9fd218545c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.133, 'Rank IC': 0.062, 'Rank ICIR': 0.379}, 'data_train_vec': ['2022-06-09', '2025-06-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.379', 'recency_weight': '0.244', 'weight': '0.033'}

	Recorder: 625944c8a2e1415497500e5532550d32

		Model: {'id': '625944c8a2e1415497500e5532550d32', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.205, 'Rank IC': 0.069, 'Rank ICIR': 0.379}, 'data_train_vec': ['2023-06-09', '2025-09-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.379', 'recency_weight': '0.348', 'weight': '0.048'}

	Recorder: da5c724674b544a683d3d6a658da62b3

		Model: {'id': 'da5c724674b544a683d3d6a658da62b3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.211, 'Rank IC': 0.06, 'Rank ICIR': 0.456}, 'data_train_vec': ['2024-06-09', '2025-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.456', 'recency_weight': '0.494', 'weight': '0.098'}

	Recorder: 0742c25d9c9e40be805ce0661ef86153

		Model: {'id': '0742c25d9c9e40be805ce0661ef86153', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.201, 'Rank IC': 0.019, 'Rank ICIR': 0.105}, 'data_train_vec': ['2025-06-09', '2026-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.105', 'recency_weight': '0.699', 'weight': '0.007'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260609_11 335698973482201818 (Recorders: 6/6)

	Recorder: 56b04c8760eb453d89cf67dacd5f650b

		Model: {'id': '56b04c8760eb453d89cf67dacd5f650b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.327, 'Rank IC': 0.065, 'Rank ICIR': 0.473}, 'data_train_vec': ['2020-06-09', '2024-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.473', 'recency_weight': '0.121', 'weight': '0.026'}

	Recorder: 7dd1ebf95f8e4804b85b1604c833bcf8

		Model: {'id': '7dd1ebf95f8e4804b85b1604c833bcf8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.274, 'Rank IC': 0.067, 'Rank ICIR': 0.487}, 'data_train_vec': ['2021-06-09', '2025-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.487', 'recency_weight': '0.171', 'weight': '0.039'}

	Recorder: ef324611c763474482fbfa02747444fe

		Model: {'id': 'ef324611c763474482fbfa02747444fe', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.11, 'Rank IC': 0.056, 'Rank ICIR': 0.378}, 'data_train_vec': ['2022-06-09', '2025-06-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.378', 'recency_weight': '0.244', 'weight': '0.033'}

	Recorder: 79f3c2313797453495dd3a1adb912482

		Model: {'id': '79f3c2313797453495dd3a1adb912482', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.074, 'Rank IC': 0.042, 'Rank ICIR': 0.287}, 'data_train_vec': ['2023-06-09', '2025-09-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.287', 'recency_weight': '0.348', 'weight': '0.027'}

	Recorder: 55ec29b023f34154830bb7a27909dc50

		Model: {'id': '55ec29b023f34154830bb7a27909dc50', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.183, 'Rank IC': 0.045, 'Rank ICIR': 0.357}, 'data_train_vec': ['2024-06-09', '2025-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.357', 'recency_weight': '0.494', 'weight': '0.060'}

	Recorder: 4a0e8cb6f2f1455fbf7f7f23b1e33c69

		Model: {'id': '4a0e8cb6f2f1455fbf7f7f23b1e33c69', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.248, 'Rank IC': 0.045, 'Rank ICIR': 0.212}, 'data_train_vec': ['2025-06-09', '2026-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.212', 'recency_weight': '0.699', 'weight': '0.030'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260609_11 332786254070502638 (Recorders: 6/6)

	Recorder: a62ea6c8d6ff4648bac20b39ee5bfecd

		Model: {'id': 'a62ea6c8d6ff4648bac20b39ee5bfecd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.269, 'Rank IC': 0.054, 'Rank ICIR': 0.36}, 'data_train_vec': ['2020-06-09', '2024-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.360', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 0bec387a01ec4ef38b107015be667a92

		Model: {'id': '0bec387a01ec4ef38b107015be667a92', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.307, 'Rank IC': 0.07, 'Rank ICIR': 0.499}, 'data_train_vec': ['2021-06-09', '2025-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.499', 'recency_weight': '0.171', 'weight': '0.041'}

	Recorder: b1632d7ff16c4a3e9cb372231e46bdf4

		Model: {'id': 'b1632d7ff16c4a3e9cb372231e46bdf4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.251, 'Rank IC': 0.07, 'Rank ICIR': 0.453}, 'data_train_vec': ['2022-06-09', '2025-06-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.453', 'recency_weight': '0.244', 'weight': '0.048'}

	Recorder: 12ed26c92dd44a8480d43c7145ef32b0

		Model: {'id': '12ed26c92dd44a8480d43c7145ef32b0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.296, 'Rank IC': 0.066, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-06-09', '2025-09-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.377', 'recency_weight': '0.348', 'weight': '0.047'}

	Recorder: adab423683504e808f90ebc4360986d5

		Model: {'id': 'adab423683504e808f90ebc4360986d5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.348, 'Rank IC': 0.062, 'Rank ICIR': 0.514}, 'data_train_vec': ['2024-06-09', '2025-12-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.514', 'recency_weight': '0.494', 'weight': '0.124'}

	Recorder: 77ce8874f71f4c9c881cb05303cadf20

		Model: {'id': '77ce8874f71f4c9c881cb05303cadf20', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.429, 'Rank IC': 0.037, 'Rank ICIR': 0.218}, 'data_train_vec': ['2025-06-09', '2026-03-08'], 'train_time_vec': ['2026-06-09', '2026-06-09'], 'rank_icir': '0.218', 'recency_weight': '0.699', 'weight': '0.032'}
