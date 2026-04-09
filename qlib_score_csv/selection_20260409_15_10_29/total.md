# params 
 {'predict_dates': [{'start': '2026-04-09', 'end': '2026-04-09'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260409_14 726600458984089917 (Recorders: 1/5)

	Recorder: 3f393251bae4467f954002cfd7ebc7b7

		Model: {'id': '3f393251bae4467f954002cfd7ebc7b7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.233, 'Rank IC': 0.045, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.290', 'weight': '0.128'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260409_14 766124070339226390 (Recorders: 1/5)

	Recorder: c8c2320182464d5f85e8391b85803ec3

		Model: {'id': 'c8c2320182464d5f85e8391b85803ec3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.251, 'Rank IC': 0.036, 'Rank ICIR': 0.313}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.313', 'weight': '0.139'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260409_12 265527896849703367 (Recorders: 3/5)

	Recorder: 84c4d6f5ac70445c897afc59f508f17c

		Model: {'id': '84c4d6f5ac70445c897afc59f508f17c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.046, 'Rank IC': 0.024, 'Rank ICIR': 0.135}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.135', 'weight': '0.060'}

	Recorder: ab8fe7c24f9f491685146d99338c2481

		Model: {'id': 'ab8fe7c24f9f491685146d99338c2481', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.115, 'Rank IC': 0.052, 'Rank ICIR': 0.299}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.299', 'weight': '0.132'}

	Recorder: 94582a6af19441c2b2ffaeb7139e6182

		Model: {'id': '94582a6af19441c2b2ffaeb7139e6182', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.265, 'Rank IC': 0.032, 'Rank ICIR': 0.312}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.312', 'weight': '0.138'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260409_12 523009332322633344 (Recorders: 5/5)

	Recorder: d15fac4a77cd4535a799c1f788dbcc7d

		Model: {'id': 'd15fac4a77cd4535a799c1f788dbcc7d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.088, 'Rank IC': 0.019, 'Rank ICIR': 0.156}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.156', 'weight': '0.069'}

	Recorder: a9f45bbef3c74bc0800cb89e4c250057

		Model: {'id': 'a9f45bbef3c74bc0800cb89e4c250057', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.017, 'Rank ICIR': 0.147}, 'data_train_vec': ['2022-04-09', '2025-04-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.147', 'weight': '0.065'}

	Recorder: ea7edc429d374121a420a608890b694f

		Model: {'id': 'ea7edc429d374121a420a608890b694f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.149, 'Rank IC': 0.042, 'Rank ICIR': 0.36}, 'data_train_vec': ['2023-04-09', '2025-07-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.360', 'weight': '0.160'}

	Recorder: c524d4e03763475ca113336c7b41c086

		Model: {'id': 'c524d4e03763475ca113336c7b41c086', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.052, 'Rank IC': 0.011, 'Rank ICIR': 0.087}, 'data_train_vec': ['2024-04-09', '2025-10-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.087', 'weight': '0.039'}

	Recorder: b8b5b70042bc4f508c2c10f27ef8fe76

		Model: {'id': 'b8b5b70042bc4f508c2c10f27ef8fe76', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.078, 'Rank IC': 0.006, 'Rank ICIR': 0.046}, 'data_train_vec': ['2025-04-09', '2026-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.046', 'weight': '0.020'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260409_12 529041242244446488 (Recorders: 1/5)

	Recorder: c6fe2e42083546a3a2038a3506807a0d

		Model: {'id': 'c6fe2e42083546a3a2038a3506807a0d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.032, 'Rank IC': 0.021, 'Rank ICIR': 0.112}, 'data_train_vec': ['2021-04-09', '2025-01-08'], 'train_time_vec': ['2026-04-09', '2026-04-09'], 'rank_icir': '0.112', 'weight': '0.050'}
