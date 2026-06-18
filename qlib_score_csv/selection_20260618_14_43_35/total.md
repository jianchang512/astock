# params 
 {'predict_dates': [{'start': '2026-06-18', 'end': '2026-06-18'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260618_13 127547479317824312 (Recorders: 6/6)

	Recorder: 29a62f652ef940a5a59a8407e517a96c

		Model: {'id': '29a62f652ef940a5a59a8407e517a96c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.277, 'Rank IC': 0.053, 'Rank ICIR': 0.345}, 'data_train_vec': ['2020-06-18', '2024-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.345', 'recency_weight': '0.121', 'weight': '0.011'}

	Recorder: 9033ed0ffa6e493d96160c5e1fa1ff94

		Model: {'id': '9033ed0ffa6e493d96160c5e1fa1ff94', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.271, 'Rank IC': 0.066, 'Rank ICIR': 0.43}, 'data_train_vec': ['2021-06-18', '2025-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.430', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: 78daadd4477a4df3b830507003851d40

		Model: {'id': '78daadd4477a4df3b830507003851d40', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.173, 'Rank IC': 0.067, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-06-18', '2025-06-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.028'}

	Recorder: 70568110d5e642d0aa84b5e11c6b58b7

		Model: {'id': '70568110d5e642d0aa84b5e11c6b58b7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.287, 'Rank IC': 0.071, 'Rank ICIR': 0.417}, 'data_train_vec': ['2023-06-18', '2025-09-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.417', 'recency_weight': '0.348', 'weight': '0.046'}

	Recorder: 91be6ce604f34ec4885a32f6a9038e3b

		Model: {'id': '91be6ce604f34ec4885a32f6a9038e3b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.248, 'Rank IC': 0.069, 'Rank ICIR': 0.458}, 'data_train_vec': ['2024-06-18', '2025-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.458', 'recency_weight': '0.494', 'weight': '0.080'}

	Recorder: 4a6c7f8c785d4d9da191002498ea1d78

		Model: {'id': '4a6c7f8c785d4d9da191002498ea1d78', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.1, 'ICIR': 0.537, 'Rank IC': 0.063, 'Rank ICIR': 0.344}, 'data_train_vec': ['2025-06-18', '2026-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.344', 'recency_weight': '0.699', 'weight': '0.063'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260618_13 652945996927725296 (Recorders: 6/6)

	Recorder: dbda0afd316b4380930223336790bda8

		Model: {'id': 'dbda0afd316b4380930223336790bda8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.294, 'Rank IC': 0.059, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-06-18', '2024-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.379', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 22ce6331ca7e4e7f92d0def34127c8e5

		Model: {'id': '22ce6331ca7e4e7f92d0def34127c8e5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.24, 'Rank IC': 0.066, 'Rank ICIR': 0.42}, 'data_train_vec': ['2021-06-18', '2025-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.420', 'recency_weight': '0.171', 'weight': '0.023'}

	Recorder: 2fe3ef449dcb4ad19d388a163083a888

		Model: {'id': '2fe3ef449dcb4ad19d388a163083a888', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.099, 'Rank IC': 0.057, 'Rank ICIR': 0.337}, 'data_train_vec': ['2022-06-18', '2025-06-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.337', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 2897873fe9ff41349b5e86066ac56da9

		Model: {'id': '2897873fe9ff41349b5e86066ac56da9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.188, 'Rank IC': 0.066, 'Rank ICIR': 0.376}, 'data_train_vec': ['2023-06-18', '2025-09-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.376', 'recency_weight': '0.348', 'weight': '0.038'}

	Recorder: e163c311a1a9409abac4b99e2632a930

		Model: {'id': 'e163c311a1a9409abac4b99e2632a930', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.191, 'Rank IC': 0.063, 'Rank ICIR': 0.448}, 'data_train_vec': ['2024-06-18', '2025-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.448', 'recency_weight': '0.494', 'weight': '0.076'}

	Recorder: 11770a4b9b2a49d5b736234f03141aa5

		Model: {'id': '11770a4b9b2a49d5b736234f03141aa5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.355, 'Rank IC': 0.05, 'Rank ICIR': 0.227}, 'data_train_vec': ['2025-06-18', '2026-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.227', 'recency_weight': '0.699', 'weight': '0.028'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260618_13 836369181688398731 (Recorders: 6/6)

	Recorder: d1d37994749b4d6db36d249be2723fd6

		Model: {'id': 'd1d37994749b4d6db36d249be2723fd6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.322, 'Rank IC': 0.065, 'Rank ICIR': 0.472}, 'data_train_vec': ['2020-06-18', '2024-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.472', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: 57c1b60585e14fd89816550d2fb62bec

		Model: {'id': '57c1b60585e14fd89816550d2fb62bec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.237, 'Rank IC': 0.067, 'Rank ICIR': 0.472}, 'data_train_vec': ['2021-06-18', '2025-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.472', 'recency_weight': '0.171', 'weight': '0.029'}

	Recorder: 873e2b06a82d4711acb3b71dc9c127a7

		Model: {'id': '873e2b06a82d4711acb3b71dc9c127a7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.117, 'Rank IC': 0.06, 'Rank ICIR': 0.395}, 'data_train_vec': ['2022-06-18', '2025-06-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.395', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: c318c71c70e64324afc0f018122345ae

		Model: {'id': 'c318c71c70e64324afc0f018122345ae', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.17, 'Rank IC': 0.055, 'Rank ICIR': 0.41}, 'data_train_vec': ['2023-06-18', '2025-09-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.410', 'recency_weight': '0.348', 'weight': '0.045'}

	Recorder: a165f9fd646f45819348cff7559fb383

		Model: {'id': 'a165f9fd646f45819348cff7559fb383', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.273, 'Rank IC': 0.056, 'Rank ICIR': 0.418}, 'data_train_vec': ['2024-06-18', '2025-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.418', 'recency_weight': '0.494', 'weight': '0.066'}

	Recorder: ace9fa0ac1f24d848bae9b9ec685edc3

		Model: {'id': 'ace9fa0ac1f24d848bae9b9ec685edc3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.395, 'Rank IC': 0.074, 'Rank ICIR': 0.346}, 'data_train_vec': ['2025-06-18', '2026-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.346', 'recency_weight': '0.699', 'weight': '0.064'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260618_13 379162764586890257 (Recorders: 6/6)

	Recorder: ee7156505a534925a404c49587e52f3f

		Model: {'id': 'ee7156505a534925a404c49587e52f3f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.267, 'Rank IC': 0.055, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-06-18', '2024-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.370', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 67774da523204fae876b555d93f9f212

		Model: {'id': '67774da523204fae876b555d93f9f212', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.244, 'Rank IC': 0.066, 'Rank ICIR': 0.453}, 'data_train_vec': ['2021-06-18', '2025-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.453', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 05356950317f4ac48b7240a7780e3482

		Model: {'id': '05356950317f4ac48b7240a7780e3482', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.123, 'Rank IC': 0.066, 'Rank ICIR': 0.397}, 'data_train_vec': ['2022-06-18', '2025-06-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.397', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: 1bda472129e64f01a3317770ade6bed1

		Model: {'id': '1bda472129e64f01a3317770ade6bed1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.177, 'Rank IC': 0.06, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-06-18', '2025-09-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.377', 'recency_weight': '0.348', 'weight': '0.038'}

	Recorder: ed9e01bf6c684e959315040580193283

		Model: {'id': 'ed9e01bf6c684e959315040580193283', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.309, 'Rank IC': 0.07, 'Rank ICIR': 0.549}, 'data_train_vec': ['2024-06-18', '2025-12-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.549', 'recency_weight': '0.494', 'weight': '0.114'}

	Recorder: 1ecce71356204b8699cd21b5af530e0d

		Model: {'id': '1ecce71356204b8699cd21b5af530e0d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.535, 'Rank IC': 0.064, 'Rank ICIR': 0.365}, 'data_train_vec': ['2025-06-18', '2026-03-17'], 'train_time_vec': ['2026-06-18', '2026-06-18'], 'rank_icir': '0.365', 'recency_weight': '0.699', 'weight': '0.071'}
