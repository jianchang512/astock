# params 
 {'predict_dates': [{'start': '2026-04-27', 'end': '2026-04-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260427_14 271855103801419886 (Recorders: 6/6)

	Recorder: 96e91fea945a4d78b42e25dec845dbe9

		Model: {'id': '96e91fea945a4d78b42e25dec845dbe9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.437, 'Rank IC': 0.062, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-04-27', '2024-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.383', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 6f4fd4105e9046ad905968da895efceb

		Model: {'id': '6f4fd4105e9046ad905968da895efceb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.22, 'Rank IC': 0.045, 'Rank ICIR': 0.299}, 'data_train_vec': ['2021-04-27', '2025-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.299', 'recency_weight': '0.173', 'weight': '0.013'}

	Recorder: 788b35bc48c24a53b11021c81c011a3a

		Model: {'id': '788b35bc48c24a53b11021c81c011a3a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.137, 'Rank IC': 0.045, 'Rank ICIR': 0.276}, 'data_train_vec': ['2022-04-27', '2025-04-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.276', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: db71fc414276493097666c5a8899e05a

		Model: {'id': 'db71fc414276493097666c5a8899e05a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.29, 'Rank IC': 0.053, 'Rank ICIR': 0.337}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.337', 'recency_weight': '0.347', 'weight': '0.034'}

	Recorder: 5ca1b8d3d7af4c01a8b5858c911aabcc

		Model: {'id': '5ca1b8d3d7af4c01a8b5858c911aabcc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.145, 'Rank IC': 0.03, 'Rank ICIR': 0.223}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.223', 'recency_weight': '0.494', 'weight': '0.021'}

	Recorder: 6a4641ba0ae146e1aa8fed7956e5957a

		Model: {'id': '6a4641ba0ae146e1aa8fed7956e5957a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.553, 'Rank IC': 0.095, 'Rank ICIR': 0.583}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.583', 'recency_weight': '0.704', 'weight': '0.206'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260427_14 837963731624334167 (Recorders: 5/6)

	Recorder: 21cf78e1e000407ab88fb07995378764

		Model: {'id': '21cf78e1e000407ab88fb07995378764', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.389, 'Rank IC': 0.06, 'Rank ICIR': 0.365}, 'data_train_vec': ['2020-04-27', '2024-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.365', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: bcf3b4c077d848499fc241ddca658e23

		Model: {'id': 'bcf3b4c077d848499fc241ddca658e23', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.189, 'Rank IC': 0.046, 'Rank ICIR': 0.296}, 'data_train_vec': ['2021-04-27', '2025-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.296', 'recency_weight': '0.173', 'weight': '0.013'}

	Recorder: b378bf93e7b9470f9e8cdacf6fdc4536

		Model: {'id': 'b378bf93e7b9470f9e8cdacf6fdc4536', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.139, 'Rank IC': 0.047, 'Rank ICIR': 0.285}, 'data_train_vec': ['2022-04-27', '2025-04-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.285', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: 7313af493afa4f7e99d8b02bf83b5f39

		Model: {'id': '7313af493afa4f7e99d8b02bf83b5f39', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.163, 'Rank IC': 0.05, 'Rank ICIR': 0.301}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.301', 'recency_weight': '0.347', 'weight': '0.027'}

	Recorder: dc6dbf7c6d9e4aee8deb603056718429

		Model: {'id': 'dc6dbf7c6d9e4aee8deb603056718429', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.58, 'Rank IC': 0.084, 'Rank ICIR': 0.565}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.565', 'recency_weight': '0.704', 'weight': '0.193'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260427_14 238191999110097718 (Recorders: 5/6)

	Recorder: b1832c364c1d49dcbbad6960a5790095

		Model: {'id': 'b1832c364c1d49dcbbad6960a5790095', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.383, 'Rank IC': 0.061, 'Rank ICIR': 0.469}, 'data_train_vec': ['2020-04-27', '2024-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.469', 'recency_weight': '0.121', 'weight': '0.023'}

	Recorder: bf4780362e714bd08c81bbf886936b0f

		Model: {'id': 'bf4780362e714bd08c81bbf886936b0f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.252, 'Rank IC': 0.05, 'Rank ICIR': 0.414}, 'data_train_vec': ['2021-04-27', '2025-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.414', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: da1b19164a6e4ebbba1bc030f6f96f66

		Model: {'id': 'da1b19164a6e4ebbba1bc030f6f96f66', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.16, 'Rank IC': 0.05, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-04-27', '2025-04-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 6f5f0031aa2c42369ec4925051dd9490

		Model: {'id': '6f5f0031aa2c42369ec4925051dd9490', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.097, 'Rank IC': 0.036, 'Rank ICIR': 0.275}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.275', 'recency_weight': '0.347', 'weight': '0.023'}

	Recorder: 707ca570caa54b0da89779c5d562b444

		Model: {'id': '707ca570caa54b0da89779c5d562b444', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.48, 'Rank IC': 0.047, 'Rank ICIR': 0.32}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.320', 'recency_weight': '0.704', 'weight': '0.062'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260427_14 767593644818184183 (Recorders: 6/6)

	Recorder: 9da5e71baab84f5ab31ad95373adf1f8

		Model: {'id': '9da5e71baab84f5ab31ad95373adf1f8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.386, 'Rank IC': 0.062, 'Rank ICIR': 0.395}, 'data_train_vec': ['2020-04-27', '2024-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.395', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: c93d0661aca3408ca8ba1a7555c4bbc0

		Model: {'id': 'c93d0661aca3408ca8ba1a7555c4bbc0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.205, 'Rank IC': 0.041, 'Rank ICIR': 0.282}, 'data_train_vec': ['2021-04-27', '2025-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.282', 'recency_weight': '0.173', 'weight': '0.012'}

	Recorder: 8248fe7c59004999bd9c565fd67d6b77

		Model: {'id': '8248fe7c59004999bd9c565fd67d6b77', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.166, 'Rank IC': 0.047, 'Rank ICIR': 0.292}, 'data_train_vec': ['2022-04-27', '2025-04-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.292', 'recency_weight': '0.244', 'weight': '0.018'}

	Recorder: cd31e2d866d14875a8de0f4d74466f46

		Model: {'id': 'cd31e2d866d14875a8de0f4d74466f46', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.334, 'Rank IC': 0.066, 'Rank ICIR': 0.435}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.435', 'recency_weight': '0.347', 'weight': '0.056'}

	Recorder: e4527e88959d478c99fc1b95bde9de15

		Model: {'id': 'e4527e88959d478c99fc1b95bde9de15', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.181, 'Rank IC': 0.035, 'Rank ICIR': 0.307}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.307', 'recency_weight': '0.494', 'weight': '0.040'}

	Recorder: bcb6e46fae66447c9358b7722613c4a8

		Model: {'id': 'bcb6e46fae66447c9358b7722613c4a8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.544, 'Rank IC': 0.077, 'Rank ICIR': 0.465}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.465', 'recency_weight': '0.704', 'weight': '0.131'}
