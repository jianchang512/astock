# params 
 {'predict_dates': [{'start': '2026-06-22', 'end': '2026-06-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260622_11 229610256901505611 (Recorders: 6/6)

	Recorder: 81c38cbca97d424ca41d3b3d9be1aa51

		Model: {'id': '81c38cbca97d424ca41d3b3d9be1aa51', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.325, 'Rank IC': 0.063, 'Rank ICIR': 0.418}, 'data_train_vec': ['2020-06-22', '2024-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.418', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 8ec1de6b59e3466f8fd86192c12ea863

		Model: {'id': '8ec1de6b59e3466f8fd86192c12ea863', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.245, 'Rank IC': 0.069, 'Rank ICIR': 0.421}, 'data_train_vec': ['2021-06-22', '2025-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.421', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: 52d87358341f44bb892925b1d279c1dd

		Model: {'id': '52d87358341f44bb892925b1d279c1dd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.166, 'Rank IC': 0.066, 'Rank ICIR': 0.376}, 'data_train_vec': ['2022-06-22', '2025-06-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.376', 'recency_weight': '0.244', 'weight': '0.023'}

	Recorder: 5b1491ba9e4c4fe89cc6649a428212f6

		Model: {'id': '5b1491ba9e4c4fe89cc6649a428212f6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.257, 'Rank IC': 0.064, 'Rank ICIR': 0.391}, 'data_train_vec': ['2023-06-22', '2025-09-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.391', 'recency_weight': '0.348', 'weight': '0.035'}

	Recorder: d0fa4bf0893f460aa93e3afecbfb7846

		Model: {'id': 'd0fa4bf0893f460aa93e3afecbfb7846', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.316, 'Rank IC': 0.07, 'Rank ICIR': 0.508}, 'data_train_vec': ['2024-06-22', '2025-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.508', 'recency_weight': '0.494', 'weight': '0.083'}

	Recorder: 686d8b7d8b434be3aaf43436ecc7bb2a

		Model: {'id': '686d8b7d8b434be3aaf43436ecc7bb2a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.105, 'ICIR': 0.653, 'Rank IC': 0.088, 'Rank ICIR': 0.521}, 'data_train_vec': ['2025-06-22', '2026-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.521', 'recency_weight': '0.699', 'weight': '0.124'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260622_11 792935701107637293 (Recorders: 6/6)

	Recorder: 7d8fdb6d30c349198c65f094b6a9411f

		Model: {'id': '7d8fdb6d30c349198c65f094b6a9411f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.31, 'Rank IC': 0.063, 'Rank ICIR': 0.412}, 'data_train_vec': ['2020-06-22', '2024-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.412', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 7e75978eb4bf475c80965e469d17d506

		Model: {'id': '7e75978eb4bf475c80965e469d17d506', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.218, 'Rank IC': 0.065, 'Rank ICIR': 0.406}, 'data_train_vec': ['2021-06-22', '2025-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.406', 'recency_weight': '0.171', 'weight': '0.018'}

	Recorder: 72e0092195a542b1b3ba1f53f19f90c7

		Model: {'id': '72e0092195a542b1b3ba1f53f19f90c7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.13, 'Rank IC': 0.06, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-06-22', '2025-06-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: 865ad42bdc5c47d8b8887d440d23c9bd

		Model: {'id': '865ad42bdc5c47d8b8887d440d23c9bd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.211, 'Rank IC': 0.061, 'Rank ICIR': 0.366}, 'data_train_vec': ['2023-06-22', '2025-09-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.366', 'recency_weight': '0.348', 'weight': '0.030'}

	Recorder: 119f1319942c47fbac5fdf701ea5723c

		Model: {'id': '119f1319942c47fbac5fdf701ea5723c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.293, 'Rank IC': 0.064, 'Rank ICIR': 0.467}, 'data_train_vec': ['2024-06-22', '2025-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.467', 'recency_weight': '0.494', 'weight': '0.070'}

	Recorder: 7b3cd01872e24c1cbe9513ada3ad9c25

		Model: {'id': '7b3cd01872e24c1cbe9513ada3ad9c25', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.11, 'ICIR': 0.525, 'Rank IC': 0.086, 'Rank ICIR': 0.456}, 'data_train_vec': ['2025-06-22', '2026-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.456', 'recency_weight': '0.699', 'weight': '0.095'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260622_11 262320540346780112 (Recorders: 6/6)

	Recorder: 2a4898288a8e43538343ae82c95bd099

		Model: {'id': '2a4898288a8e43538343ae82c95bd099', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.338, 'Rank IC': 0.068, 'Rank ICIR': 0.497}, 'data_train_vec': ['2020-06-22', '2024-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.497', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: c6e639ac6de74bb19b901173bc9b8cb1

		Model: {'id': 'c6e639ac6de74bb19b901173bc9b8cb1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.22, 'Rank IC': 0.067, 'Rank ICIR': 0.462}, 'data_train_vec': ['2021-06-22', '2025-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.462', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: b7636674dc2d4c01a073f29689065c68

		Model: {'id': 'b7636674dc2d4c01a073f29689065c68', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.118, 'Rank IC': 0.06, 'Rank ICIR': 0.383}, 'data_train_vec': ['2022-06-22', '2025-06-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.383', 'recency_weight': '0.244', 'weight': '0.023'}

	Recorder: a5ef3319b969487e91721990de8ab466

		Model: {'id': 'a5ef3319b969487e91721990de8ab466', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.196, 'Rank IC': 0.055, 'Rank ICIR': 0.382}, 'data_train_vec': ['2023-06-22', '2025-09-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.382', 'recency_weight': '0.348', 'weight': '0.033'}

	Recorder: d89e0e7461e447e79c60fec1977ba329

		Model: {'id': 'd89e0e7461e447e79c60fec1977ba329', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.349, 'Rank IC': 0.06, 'Rank ICIR': 0.445}, 'data_train_vec': ['2024-06-22', '2025-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.445', 'recency_weight': '0.494', 'weight': '0.064'}

	Recorder: dd246e35c11648889b24b2a7526a2783

		Model: {'id': 'dd246e35c11648889b24b2a7526a2783', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.403, 'Rank IC': 0.067, 'Rank ICIR': 0.335}, 'data_train_vec': ['2025-06-22', '2026-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.335', 'recency_weight': '0.699', 'weight': '0.051'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260622_11 254826979087542757 (Recorders: 6/6)

	Recorder: 927d02587f1d436386bde3429227c347

		Model: {'id': '927d02587f1d436386bde3429227c347', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.341, 'Rank IC': 0.059, 'Rank ICIR': 0.423}, 'data_train_vec': ['2020-06-22', '2024-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.423', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: d82f8605da45409cb253e11c75142d1b

		Model: {'id': 'd82f8605da45409cb253e11c75142d1b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.226, 'Rank IC': 0.07, 'Rank ICIR': 0.461}, 'data_train_vec': ['2021-06-22', '2025-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.461', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: 672d7323f10f41caaa209cf7bf2e09a8

		Model: {'id': '672d7323f10f41caaa209cf7bf2e09a8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.145, 'Rank IC': 0.065, 'Rank ICIR': 0.393}, 'data_train_vec': ['2022-06-22', '2025-06-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.393', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: fdbdbab2412e4ff0acc77142695e9cb0

		Model: {'id': 'fdbdbab2412e4ff0acc77142695e9cb0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.274, 'Rank IC': 0.065, 'Rank ICIR': 0.412}, 'data_train_vec': ['2023-06-22', '2025-09-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.412', 'recency_weight': '0.348', 'weight': '0.039'}

	Recorder: e75cb6ca9b6d44bd846d13c6101a7ed1

		Model: {'id': 'e75cb6ca9b6d44bd846d13c6101a7ed1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.249, 'Rank IC': 0.06, 'Rank ICIR': 0.482}, 'data_train_vec': ['2024-06-22', '2025-12-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.482', 'recency_weight': '0.494', 'weight': '0.075'}

	Recorder: 9dd11e5df36f4051844de0bc76c115ce

		Model: {'id': '9dd11e5df36f4051844de0bc76c115ce', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.086, 'ICIR': 0.507, 'Rank IC': 0.06, 'Rank ICIR': 0.371}, 'data_train_vec': ['2025-06-22', '2026-03-21'], 'train_time_vec': ['2026-06-22', '2026-06-22'], 'rank_icir': '0.371', 'recency_weight': '0.699', 'weight': '0.063'}
