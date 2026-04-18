# params 
 {'predict_dates': [{'start': '2026-04-17', 'end': '2026-04-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260417_14 585795715846562893 (Recorders: 6/6)

	Recorder: c8002c80b7de4c4c96621a9862992558

		Model: {'id': 'c8002c80b7de4c4c96621a9862992558', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.45, 'Rank IC': 0.064, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-04-17', '2024-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: 2f1a88ea83884b04af68c24673c59fed

		Model: {'id': '2f1a88ea83884b04af68c24673c59fed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.308, 'Rank IC': 0.054, 'Rank ICIR': 0.35}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.350', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: c9156a895d114bbd8a72ad1a2d5e9ec6

		Model: {'id': 'c9156a895d114bbd8a72ad1a2d5e9ec6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.255, 'Rank IC': 0.045, 'Rank ICIR': 0.264}, 'data_train_vec': ['2022-04-17', '2025-04-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.264', 'recency_weight': '0.244', 'weight': '0.020'}

	Recorder: b3f678adc2fc42108b6480d6e4b8b2c2

		Model: {'id': 'b3f678adc2fc42108b6480d6e4b8b2c2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.364, 'Rank IC': 0.067, 'Rank ICIR': 0.434}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.434', 'recency_weight': '0.347', 'weight': '0.077'}

	Recorder: f84a6da04dbc4111a3b7846f777e1f65

		Model: {'id': 'f84a6da04dbc4111a3b7846f777e1f65', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.168, 'Rank IC': 0.026, 'Rank ICIR': 0.208}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.208', 'recency_weight': '0.494', 'weight': '0.025'}

	Recorder: 4bfef3b38cae43ceb4b78c68d434f1a0

		Model: {'id': '4bfef3b38cae43ceb4b78c68d434f1a0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.445, 'Rank IC': 0.074, 'Rank ICIR': 0.405}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.405', 'recency_weight': '0.704', 'weight': '0.137'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260417_14 279757960655049497 (Recorders: 6/6)

	Recorder: 0232ee0dfb464904a78c6661ad38bc68

		Model: {'id': '0232ee0dfb464904a78c6661ad38bc68', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.369, 'Rank IC': 0.059, 'Rank ICIR': 0.336}, 'data_train_vec': ['2020-04-17', '2024-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.336', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: d59549e7569b480ab02b77360c57a6a7

		Model: {'id': 'd59549e7569b480ab02b77360c57a6a7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.264, 'Rank IC': 0.05, 'Rank ICIR': 0.318}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.318', 'recency_weight': '0.173', 'weight': '0.021'}

	Recorder: 4b86507fcda74cabb139963e936747b7

		Model: {'id': '4b86507fcda74cabb139963e936747b7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.132, 'Rank IC': 0.042, 'Rank ICIR': 0.24}, 'data_train_vec': ['2022-04-17', '2025-04-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.240', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: 58c3cf5d72264476b59e60b10ed84625

		Model: {'id': '58c3cf5d72264476b59e60b10ed84625', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.149, 'Rank IC': 0.057, 'Rank ICIR': 0.359}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.359', 'recency_weight': '0.347', 'weight': '0.053'}

	Recorder: 1e4d696f10e54bbd89758129b1ce38c1

		Model: {'id': '1e4d696f10e54bbd89758129b1ce38c1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.134, 'Rank IC': 0.034, 'Rank ICIR': 0.246}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.246', 'recency_weight': '0.494', 'weight': '0.035'}

	Recorder: 19f324eed2d249aaaa6ba5b416daccaa

		Model: {'id': '19f324eed2d249aaaa6ba5b416daccaa', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.316, 'Rank IC': 0.056, 'Rank ICIR': 0.277}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.277', 'recency_weight': '0.704', 'weight': '0.064'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260417_14 568891344557493940 (Recorders: 5/6)

	Recorder: 58a00d6a17124d13bed8882a6656802f

		Model: {'id': '58a00d6a17124d13bed8882a6656802f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.38, 'Rank IC': 0.062, 'Rank ICIR': 0.458}, 'data_train_vec': ['2020-04-17', '2024-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.458', 'recency_weight': '0.121', 'weight': '0.030'}

	Recorder: 9a91bb3e389549e29c482b9f129799e3

		Model: {'id': '9a91bb3e389549e29c482b9f129799e3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.311, 'Rank IC': 0.053, 'Rank ICIR': 0.453}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.453', 'recency_weight': '0.173', 'weight': '0.042'}

	Recorder: c08b34395ee94c488623e4dbd4fbc27a

		Model: {'id': 'c08b34395ee94c488623e4dbd4fbc27a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.178, 'Rank IC': 0.049, 'Rank ICIR': 0.332}, 'data_train_vec': ['2022-04-17', '2025-04-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.332', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: e53b4a02622f47999570021df0ece216

		Model: {'id': 'e53b4a02622f47999570021df0ece216', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.132, 'Rank IC': 0.039, 'Rank ICIR': 0.295}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.295', 'recency_weight': '0.347', 'weight': '0.036'}

	Recorder: 43bf925016a54634b817cc8842303555

		Model: {'id': '43bf925016a54634b817cc8842303555', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.316, 'Rank IC': 0.049, 'Rank ICIR': 0.237}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.237', 'recency_weight': '0.704', 'weight': '0.047'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260417_14 419235306502205227 (Recorders: 6/6)

	Recorder: 291ee1a45295413282c8159ce93b5c79

		Model: {'id': '291ee1a45295413282c8159ce93b5c79', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.376, 'Rank IC': 0.06, 'Rank ICIR': 0.365}, 'data_train_vec': ['2020-04-17', '2024-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.365', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 951861aa777a4efdad1907cf500ad3d8

		Model: {'id': '951861aa777a4efdad1907cf500ad3d8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.306, 'Rank IC': 0.051, 'Rank ICIR': 0.345}, 'data_train_vec': ['2021-04-17', '2025-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.345', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: a0e0f06a82b44697957ff68dec6cb20e

		Model: {'id': 'a0e0f06a82b44697957ff68dec6cb20e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.211, 'Rank IC': 0.042, 'Rank ICIR': 0.261}, 'data_train_vec': ['2022-04-17', '2025-04-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.261', 'recency_weight': '0.244', 'weight': '0.020'}

	Recorder: debf74aa5de24100982ff4ec04fe5852

		Model: {'id': 'debf74aa5de24100982ff4ec04fe5852', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.338, 'Rank IC': 0.063, 'Rank ICIR': 0.424}, 'data_train_vec': ['2023-04-17', '2025-07-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.424', 'recency_weight': '0.347', 'weight': '0.074'}

	Recorder: 41b2195a09e1459eb68b8556006971a0

		Model: {'id': '41b2195a09e1459eb68b8556006971a0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.269, 'Rank IC': 0.034, 'Rank ICIR': 0.274}, 'data_train_vec': ['2024-04-17', '2025-10-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.274', 'recency_weight': '0.494', 'weight': '0.044'}

	Recorder: eb9d5fd1444d49cdb1187ed6977505c8

		Model: {'id': 'eb9d5fd1444d49cdb1187ed6977505c8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.076, 'ICIR': 0.498, 'Rank IC': 0.067, 'Rank ICIR': 0.379}, 'data_train_vec': ['2025-04-17', '2026-01-16'], 'train_time_vec': ['2026-04-17', '2026-04-17'], 'rank_icir': '0.379', 'recency_weight': '0.704', 'weight': '0.120'}
