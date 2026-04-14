# params 
 {'predict_dates': [{'start': '2026-03-27', 'end': '2026-03-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260327_14 222777918030468882 (Recorders: 5/5)

	Recorder: d24f10915646429ea03e82db8903bd5b

		Model: {'id': 'd24f10915646429ea03e82db8903bd5b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.046, 'Rank IC': 0.021, 'Rank ICIR': 0.157}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.157', 'weight': '0.045'}

	Recorder: 30df075b02034f3f887becd5773d6d2c

		Model: {'id': '30df075b02034f3f887becd5773d6d2c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.058, 'Rank IC': 0.034, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-03-27', '2025-03-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.169', 'weight': '0.049'}

	Recorder: 8655eba77f5c4aa6be93aed08ffce344

		Model: {'id': '8655eba77f5c4aa6be93aed08ffce344', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.049, 'Rank ICIR': 0.324}, 'data_train_vec': ['2023-03-27', '2025-06-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.324', 'weight': '0.094'}

	Recorder: b1c7880de0dd415598d020b7ec1f880b

		Model: {'id': 'b1c7880de0dd415598d020b7ec1f880b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.093, 'Rank IC': 0.036, 'Rank ICIR': 0.249}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.249', 'weight': '0.072'}

	Recorder: bac1b32937b84b8dad16e89d68fcf715

		Model: {'id': 'bac1b32937b84b8dad16e89d68fcf715', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.019, 'Rank IC': 0.005, 'Rank ICIR': 0.036}, 'data_train_vec': ['2025-03-27', '2025-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.036', 'weight': '0.010'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260327_14 373675769200076254 (Recorders: 2/5)

	Recorder: 3f395c8b3a984cc1a5abf68f28ddd556

		Model: {'id': '3f395c8b3a984cc1a5abf68f28ddd556', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.045, 'Rank IC': 0.026, 'Rank ICIR': 0.162}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.162', 'weight': '0.047'}

	Recorder: acf9559a3c6d4382906152e0bd86d8fa

		Model: {'id': 'acf9559a3c6d4382906152e0bd86d8fa', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.285, 'Rank IC': 0.046, 'Rank ICIR': 0.36}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.360', 'weight': '0.104'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260327_12 604183670815729113 (Recorders: 3/5)

	Recorder: 0c6346dc31dd4b2da32312078fcb38da

		Model: {'id': '0c6346dc31dd4b2da32312078fcb38da', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.128, 'Rank IC': 0.04, 'Rank ICIR': 0.229}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.229', 'weight': '0.066'}

	Recorder: 53d5408fecd648bc9aad1be613bd2cba

		Model: {'id': '53d5408fecd648bc9aad1be613bd2cba', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.017, 'Rank IC': 0.037, 'Rank ICIR': 0.214}, 'data_train_vec': ['2023-03-27', '2025-06-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.214', 'weight': '0.062'}

	Recorder: 60f9e1149c714e7185387d04e1647b90

		Model: {'id': '60f9e1149c714e7185387d04e1647b90', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.293, 'Rank IC': 0.033, 'Rank ICIR': 0.287}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.287', 'weight': '0.083'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260327_11 736403191835532098 (Recorders: 5/5)

	Recorder: b15b1c4b9cef44d2a5c09f41e0150708

		Model: {'id': 'b15b1c4b9cef44d2a5c09f41e0150708', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.166, 'Rank IC': 0.028, 'Rank ICIR': 0.24}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.240', 'weight': '0.069'}

	Recorder: 7135b1f3dd804f87af9eda1cdb3fd394

		Model: {'id': '7135b1f3dd804f87af9eda1cdb3fd394', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.023, 'Rank ICIR': 0.199}, 'data_train_vec': ['2022-03-27', '2025-03-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.199', 'weight': '0.058'}

	Recorder: d8a06d8a83644e808954f2769526dd40

		Model: {'id': 'd8a06d8a83644e808954f2769526dd40', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.136, 'Rank IC': 0.039, 'Rank ICIR': 0.353}, 'data_train_vec': ['2023-03-27', '2025-06-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.353', 'weight': '0.102'}

	Recorder: 2d462927c0964935953875403799bc75

		Model: {'id': '2d462927c0964935953875403799bc75', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.127, 'Rank IC': 0.015, 'Rank ICIR': 0.121}, 'data_train_vec': ['2024-03-27', '2025-09-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.121', 'weight': '0.035'}

	Recorder: 83d4b3396871401b83310e77b6b71369

		Model: {'id': '83d4b3396871401b83310e77b6b71369', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.075, 'Rank IC': 0.017, 'Rank ICIR': 0.151}, 'data_train_vec': ['2025-03-27', '2025-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.151', 'weight': '0.044'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260327_11 367474550838297569 (Recorders: 1/5)

	Recorder: c7a6b9221dd848979bc8e579f181b52c

		Model: {'id': 'c7a6b9221dd848979bc8e579f181b52c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.067, 'Rank IC': 0.037, 'Rank ICIR': 0.205}, 'data_train_vec': ['2021-03-27', '2024-12-26'], 'train_time_vec': ['2026-03-27', '2026-03-27'], 'rank_icir': '0.205', 'weight': '0.059'}
