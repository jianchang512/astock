# params 
 {'predict_dates': [{'end': '2026-07-09', 'start': '2026-07-04'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'analysis_folder': '~/.qlibAssistant/analysis/', 'dataset_name': 'Alpha158', 'model_filter': ['.*'], 'model_name': 'Linear', 'pfx_name': 'p', 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}], 'rolling_type': 'expanding', 'sfx_name': 's', 'step': 60, 'stock_pool': 'csi300', 'uri_folder': '~/.qlibAssistant/mlruns/'}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260712_14 754546108666542800 (Recorders: 6/6)

	Recorder: a7bf867573cb4097b2578ec5a1003f94

		Model: {'id': 'a7bf867573cb4097b2578ec5a1003f94', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.331, 'Rank IC': 0.065, 'Rank ICIR': 0.448}, 'data_train_vec': ['2020-07-12', '2025-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.448', 'recency_weight': '0.125', 'weight': '0.024'}

	Recorder: 6bede71a55134b5798209144f45d1da7

		Model: {'id': '6bede71a55134b5798209144f45d1da7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.191, 'Rank IC': 0.064, 'Rank ICIR': 0.378}, 'data_train_vec': ['2021-07-12', '2025-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.378', 'recency_weight': '0.177', 'weight': '0.024'}

	Recorder: b02f4d72d67f453f985c1c10c97ec5b9

		Model: {'id': 'b02f4d72d67f453f985c1c10c97ec5b9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.157, 'Rank IC': 0.062, 'Rank ICIR': 0.392}, 'data_train_vec': ['2022-07-12', '2025-07-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.392', 'recency_weight': '0.252', 'weight': '0.036'}

	Recorder: 9c7292d3be3b40138e2e98cc8f2a5aec

		Model: {'id': '9c7292d3be3b40138e2e98cc8f2a5aec', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.257, 'Rank IC': 0.067, 'Rank ICIR': 0.438}, 'data_train_vec': ['2023-07-12', '2025-10-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.438', 'recency_weight': '0.359', 'weight': '0.065'}

	Recorder: bed9df61ca6645d6af620bdc39f81152

		Model: {'id': 'bed9df61ca6645d6af620bdc39f81152', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.225, 'Rank IC': 0.048, 'Rank ICIR': 0.34}, 'data_train_vec': ['2024-07-12', '2026-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.340', 'recency_weight': '0.512', 'weight': '0.055'}

	Recorder: 95db16cefe044b25b327362977f819ce

		Model: {'id': '95db16cefe044b25b327362977f819ce', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.337, 'Rank IC': 0.035, 'Rank ICIR': 0.178}, 'data_train_vec': ['2025-07-12', '2026-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.178', 'recency_weight': '0.724', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260712_14 476785472344051870 (Recorders: 6/6)

	Recorder: b8bceab17438487fab3467842463ae8a

		Model: {'id': 'b8bceab17438487fab3467842463ae8a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.333, 'Rank IC': 0.068, 'Rank ICIR': 0.447}, 'data_train_vec': ['2020-07-12', '2025-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.447', 'recency_weight': '0.125', 'weight': '0.024'}

	Recorder: 5c25cebca9b949ef89085b056d4c5e23

		Model: {'id': '5c25cebca9b949ef89085b056d4c5e23', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.207, 'Rank IC': 0.061, 'Rank ICIR': 0.388}, 'data_train_vec': ['2021-07-12', '2025-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.388', 'recency_weight': '0.177', 'weight': '0.025'}

	Recorder: eb29e750a63a46b5a16b5fb3d9acc9d3

		Model: {'id': 'eb29e750a63a46b5a16b5fb3d9acc9d3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.163, 'Rank IC': 0.067, 'Rank ICIR': 0.424}, 'data_train_vec': ['2022-07-12', '2025-07-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.424', 'recency_weight': '0.252', 'weight': '0.042'}

	Recorder: 544338cb0e384e648c8195ea856a7dcd

		Model: {'id': '544338cb0e384e648c8195ea856a7dcd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.286, 'Rank IC': 0.069, 'Rank ICIR': 0.465}, 'data_train_vec': ['2023-07-12', '2025-10-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.465', 'recency_weight': '0.359', 'weight': '0.073'}

	Recorder: 7deb0d3b8f714a23aa25469fae5d4618

		Model: {'id': '7deb0d3b8f714a23aa25469fae5d4618', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.273, 'Rank IC': 0.039, 'Rank ICIR': 0.298}, 'data_train_vec': ['2024-07-12', '2026-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.298', 'recency_weight': '0.512', 'weight': '0.043'}

	Recorder: 83029536cae642e68104d459c2d766ea

		Model: {'id': '83029536cae642e68104d459c2d766ea', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.371, 'Rank IC': 0.061, 'Rank ICIR': 0.309}, 'data_train_vec': ['2025-07-12', '2026-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.309', 'recency_weight': '0.724', 'weight': '0.065'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260712_14 755079687110511087 (Recorders: 6/6)

	Recorder: 129f0e2c025a4f7abc81fdd638c200e1

		Model: {'id': '129f0e2c025a4f7abc81fdd638c200e1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.265, 'Rank IC': 0.06, 'Rank ICIR': 0.418}, 'data_train_vec': ['2020-07-12', '2025-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.418', 'recency_weight': '0.125', 'weight': '0.021'}

	Recorder: 056b9fa20f45477fbcfb7ecd766f9b7e

		Model: {'id': '056b9fa20f45477fbcfb7ecd766f9b7e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.076, 'Rank IC': 0.045, 'Rank ICIR': 0.297}, 'data_train_vec': ['2021-07-12', '2025-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.297', 'recency_weight': '0.177', 'weight': '0.015'}

	Recorder: 680677bc73ce402cbbecca7cb50b6a5b

		Model: {'id': '680677bc73ce402cbbecca7cb50b6a5b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.071, 'Rank IC': 0.046, 'Rank ICIR': 0.329}, 'data_train_vec': ['2022-07-12', '2025-07-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.329', 'recency_weight': '0.252', 'weight': '0.026'}

	Recorder: 65f92eefd0554f008d4b76fc2c9b0ddf

		Model: {'id': '65f92eefd0554f008d4b76fc2c9b0ddf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.232, 'Rank IC': 0.05, 'Rank ICIR': 0.379}, 'data_train_vec': ['2023-07-12', '2025-10-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.379', 'recency_weight': '0.359', 'weight': '0.048'}

	Recorder: 491a8e704aed4b05af097312b02b2936

		Model: {'id': '491a8e704aed4b05af097312b02b2936', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.21, 'Rank IC': 0.028, 'Rank ICIR': 0.2}, 'data_train_vec': ['2024-07-12', '2026-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.200', 'recency_weight': '0.512', 'weight': '0.019'}

	Recorder: 8113d0cdb3e04b21b4da7e921986af4f

		Model: {'id': '8113d0cdb3e04b21b4da7e921986af4f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.433, 'Rank IC': 0.072, 'Rank ICIR': 0.44}, 'data_train_vec': ['2025-07-12', '2026-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.440', 'recency_weight': '0.724', 'weight': '0.131'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260712_14 317272975187970729 (Recorders: 6/6)

	Recorder: fb1d3e87d2b04509aa4dfc5c247944cc

		Model: {'id': 'fb1d3e87d2b04509aa4dfc5c247944cc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.257, 'Rank IC': 0.064, 'Rank ICIR': 0.439}, 'data_train_vec': ['2020-07-12', '2025-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.439', 'recency_weight': '0.125', 'weight': '0.023'}

	Recorder: 4f337e2e01044cffa00349f29d4406ab

		Model: {'id': '4f337e2e01044cffa00349f29d4406ab', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.169, 'Rank IC': 0.06, 'Rank ICIR': 0.376}, 'data_train_vec': ['2021-07-12', '2025-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.376', 'recency_weight': '0.177', 'weight': '0.024'}

	Recorder: d21941fd11664994ae9140c49032af01

		Model: {'id': 'd21941fd11664994ae9140c49032af01', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.138, 'Rank IC': 0.063, 'Rank ICIR': 0.418}, 'data_train_vec': ['2022-07-12', '2025-07-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.418', 'recency_weight': '0.252', 'weight': '0.041'}

	Recorder: feed3d6345e14318af1822ceaf7d7ac1

		Model: {'id': 'feed3d6345e14318af1822ceaf7d7ac1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.205, 'Rank IC': 0.057, 'Rank ICIR': 0.398}, 'data_train_vec': ['2023-07-12', '2025-10-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.398', 'recency_weight': '0.359', 'weight': '0.053'}

	Recorder: 9c7bf01da669477388c530ef04c738b1

		Model: {'id': '9c7bf01da669477388c530ef04c738b1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.18, 'Rank IC': 0.036, 'Rank ICIR': 0.285}, 'data_train_vec': ['2024-07-12', '2026-01-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.285', 'recency_weight': '0.512', 'weight': '0.039'}

	Recorder: eb6210f9fb8c4bb6ada0fe3ecf8923bb

		Model: {'id': 'eb6210f9fb8c4bb6ada0fe3ecf8923bb', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.348, 'Rank IC': 0.046, 'Rank ICIR': 0.308}, 'data_train_vec': ['2025-07-12', '2026-04-11'], 'train_time_vec': ['2026-07-12', '2026-07-12'], 'rank_icir': '0.308', 'recency_weight': '0.724', 'weight': '0.064'}
