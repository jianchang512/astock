# params 
 {'predict_dates': [{'start': '2026-06-16', 'end': '2026-06-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260616_11 950155411170577727 (Recorders: 6/6)

	Recorder: ebf6711afa6148c09d49ed77c9b753b4

		Model: {'id': 'ebf6711afa6148c09d49ed77c9b753b4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.306, 'Rank IC': 0.058, 'Rank ICIR': 0.372}, 'data_train_vec': ['2020-06-16', '2024-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.372', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: b3dc3de0d955494a9ab6990013231b9c

		Model: {'id': 'b3dc3de0d955494a9ab6990013231b9c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.374, 'Rank IC': 0.078, 'Rank ICIR': 0.498}, 'data_train_vec': ['2021-06-16', '2025-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.498', 'recency_weight': '0.171', 'weight': '0.032'}

	Recorder: f26ad8cd610e4931bb5d3dbcccd355e0

		Model: {'id': 'f26ad8cd610e4931bb5d3dbcccd355e0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.072, 'Rank ICIR': 0.407}, 'data_train_vec': ['2022-06-16', '2025-06-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.407', 'recency_weight': '0.244', 'weight': '0.031'}

	Recorder: 0ec56b4ac4044e84be6eebe89fc6b052

		Model: {'id': '0ec56b4ac4044e84be6eebe89fc6b052', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.337, 'Rank IC': 0.072, 'Rank ICIR': 0.437}, 'data_train_vec': ['2023-06-16', '2025-09-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.437', 'recency_weight': '0.348', 'weight': '0.051'}

	Recorder: 2f7e3dbc9d084c89a5c797f42465c592

		Model: {'id': '2f7e3dbc9d084c89a5c797f42465c592', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.219, 'Rank IC': 0.068, 'Rank ICIR': 0.485}, 'data_train_vec': ['2024-06-16', '2025-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.485', 'recency_weight': '0.494', 'weight': '0.088'}

	Recorder: 48abe44c04a74088a0caaee429f7c412

		Model: {'id': '48abe44c04a74088a0caaee429f7c412', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.094, 'ICIR': 0.528, 'Rank IC': 0.047, 'Rank ICIR': 0.239}, 'data_train_vec': ['2025-06-16', '2026-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.239', 'recency_weight': '0.699', 'weight': '0.030'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260616_11 275602396954417720 (Recorders: 6/6)

	Recorder: f379c7b1a727468c8b16aaf9ce9b22ca

		Model: {'id': 'f379c7b1a727468c8b16aaf9ce9b22ca', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.32, 'Rank IC': 0.06, 'Rank ICIR': 0.373}, 'data_train_vec': ['2020-06-16', '2024-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.373', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 33b26d9c30c343bf88c2b7fe28658b92

		Model: {'id': '33b26d9c30c343bf88c2b7fe28658b92', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.293, 'Rank IC': 0.069, 'Rank ICIR': 0.456}, 'data_train_vec': ['2021-06-16', '2025-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.456', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 2cb804445bf8418d9ab667c98f2ce0a9

		Model: {'id': '2cb804445bf8418d9ab667c98f2ce0a9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.142, 'Rank IC': 0.063, 'Rank ICIR': 0.374}, 'data_train_vec': ['2022-06-16', '2025-06-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.374', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: c49033fc86a7408aaf2cb388ee7ab74e

		Model: {'id': 'c49033fc86a7408aaf2cb388ee7ab74e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.249, 'Rank IC': 0.076, 'Rank ICIR': 0.44}, 'data_train_vec': ['2023-06-16', '2025-09-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.440', 'recency_weight': '0.348', 'weight': '0.051'}

	Recorder: 42de3d66ca8b47da91cc2e80b98e720b

		Model: {'id': '42de3d66ca8b47da91cc2e80b98e720b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.236, 'Rank IC': 0.069, 'Rank ICIR': 0.479}, 'data_train_vec': ['2024-06-16', '2025-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.479', 'recency_weight': '0.494', 'weight': '0.086'}

	Recorder: c3eb4e5c6fd44ce3bbbda8b1d557a872

		Model: {'id': 'c3eb4e5c6fd44ce3bbbda8b1d557a872', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.293, 'Rank IC': 0.037, 'Rank ICIR': 0.184}, 'data_train_vec': ['2025-06-16', '2026-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.184', 'recency_weight': '0.699', 'weight': '0.018'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260616_11 978946754895571727 (Recorders: 6/6)

	Recorder: 432ecfa5dc884d04b9c25dca7db87464

		Model: {'id': '432ecfa5dc884d04b9c25dca7db87464', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.335, 'Rank IC': 0.066, 'Rank ICIR': 0.48}, 'data_train_vec': ['2020-06-16', '2024-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.480', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: 5f448e4911e04f108a20fa7c25b12dba

		Model: {'id': '5f448e4911e04f108a20fa7c25b12dba', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.276, 'Rank IC': 0.07, 'Rank ICIR': 0.492}, 'data_train_vec': ['2021-06-16', '2025-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.492', 'recency_weight': '0.171', 'weight': '0.032'}

	Recorder: 06458578a73143efbfbbe3a3fa800b13

		Model: {'id': '06458578a73143efbfbbe3a3fa800b13', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.143, 'Rank IC': 0.062, 'Rank ICIR': 0.405}, 'data_train_vec': ['2022-06-16', '2025-06-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.405', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: ccca73f410374151b85d85453352120e

		Model: {'id': 'ccca73f410374151b85d85453352120e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.257, 'Rank IC': 0.065, 'Rank ICIR': 0.487}, 'data_train_vec': ['2023-06-16', '2025-09-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.487', 'recency_weight': '0.348', 'weight': '0.063'}

	Recorder: a7f7a52fa5b04bf9a3f9f9d7531b1353

		Model: {'id': 'a7f7a52fa5b04bf9a3f9f9d7531b1353', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.245, 'Rank IC': 0.055, 'Rank ICIR': 0.413}, 'data_train_vec': ['2024-06-16', '2025-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.413', 'recency_weight': '0.494', 'weight': '0.064'}

	Recorder: 0cc9df370e25433a841fc6c645a539e4

		Model: {'id': '0cc9df370e25433a841fc6c645a539e4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.312, 'Rank IC': 0.053, 'Rank ICIR': 0.244}, 'data_train_vec': ['2025-06-16', '2026-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.244', 'recency_weight': '0.699', 'weight': '0.032'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260616_11 950278472414570919 (Recorders: 6/6)

	Recorder: e71acc9581da4f38a17cec74cdfc2610

		Model: {'id': 'e71acc9581da4f38a17cec74cdfc2610', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.264, 'Rank IC': 0.057, 'Rank ICIR': 0.366}, 'data_train_vec': ['2020-06-16', '2024-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.366', 'recency_weight': '0.121', 'weight': '0.012'}

	Recorder: f7abad165c174dafbdcc0a47b6f060ed

		Model: {'id': 'f7abad165c174dafbdcc0a47b6f060ed', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.311, 'Rank IC': 0.073, 'Rank ICIR': 0.519}, 'data_train_vec': ['2021-06-16', '2025-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.519', 'recency_weight': '0.171', 'weight': '0.035'}

	Recorder: b6e92aac76b944fe853ab8357d3e3a15

		Model: {'id': 'b6e92aac76b944fe853ab8357d3e3a15', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.153, 'Rank IC': 0.069, 'Rank ICIR': 0.42}, 'data_train_vec': ['2022-06-16', '2025-06-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.420', 'recency_weight': '0.244', 'weight': '0.033'}

	Recorder: 88273750ad404fa480795e127f8868b3

		Model: {'id': '88273750ad404fa480795e127f8868b3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.355, 'Rank IC': 0.077, 'Rank ICIR': 0.462}, 'data_train_vec': ['2023-06-16', '2025-09-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.462', 'recency_weight': '0.348', 'weight': '0.057'}

	Recorder: 35a9508a51a9426e96f8a092bd4fc66b

		Model: {'id': '35a9508a51a9426e96f8a092bd4fc66b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.24, 'Rank IC': 0.064, 'Rank ICIR': 0.489}, 'data_train_vec': ['2024-06-16', '2025-12-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.489', 'recency_weight': '0.494', 'weight': '0.090'}

	Recorder: ea03e80266b649f3bb83daeadfad2b99

		Model: {'id': 'ea03e80266b649f3bb83daeadfad2b99', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.106, 'ICIR': 0.545, 'Rank IC': 0.064, 'Rank ICIR': 0.35}, 'data_train_vec': ['2025-06-16', '2026-03-15'], 'train_time_vec': ['2026-06-16', '2026-06-16'], 'rank_icir': '0.350', 'recency_weight': '0.699', 'weight': '0.065'}
