# params 
 {'predict_dates': [{'start': '2026-03-23', 'end': '2026-03-23'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260323_16 762299663363952332 (Recorders: 3/5)

	Recorder: ff5ac5f565404286aa0d508cf4b3ec6a

		Model: {'id': 'ff5ac5f565404286aa0d508cf4b3ec6a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.055, 'Rank IC': 0.023, 'Rank ICIR': 0.152}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.152', 'weight': '0.035'}

	Recorder: 2e378709df23418ca51ee5c5c84e2431

		Model: {'id': '2e378709df23418ca51ee5c5c84e2431', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.165, 'Rank IC': 0.058, 'Rank ICIR': 0.37}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.370', 'weight': '0.085'}

	Recorder: 881c704af0e3421191cb96749649c30d

		Model: {'id': '881c704af0e3421191cb96749649c30d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.137, 'Rank IC': 0.038, 'Rank ICIR': 0.285}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.285', 'weight': '0.066'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260323_16 387761463091792861 (Recorders: 2/5)

	Recorder: f32f2f124b4a4d18b83b39092b0ee32c

		Model: {'id': 'f32f2f124b4a4d18b83b39092b0ee32c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.067, 'Rank IC': 0.031, 'Rank ICIR': 0.192}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.192', 'weight': '0.044'}

	Recorder: cafae6c186b34668a90b6a5bf1f28ee9

		Model: {'id': 'cafae6c186b34668a90b6a5bf1f28ee9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.268, 'Rank IC': 0.044, 'Rank ICIR': 0.383}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.383', 'weight': '0.088'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260323_13 119829996181832742 (Recorders: 3/5)

	Recorder: eabc6392d2fc4f178cb7b01a822df390

		Model: {'id': 'eabc6392d2fc4f178cb7b01a822df390', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.118, 'Rank IC': 0.037, 'Rank ICIR': 0.212}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.212', 'weight': '0.049'}

	Recorder: 092e7d20e27c457693affe92417530d5

		Model: {'id': '092e7d20e27c457693affe92417530d5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.295, 'Rank IC': 0.044, 'Rank ICIR': 0.381}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.381', 'weight': '0.088'}

	Recorder: ee4bc44122854011b2ce9c62d8f48de3

		Model: {'id': 'ee4bc44122854011b2ce9c62d8f48de3', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.016, 'Rank IC': 0.013, 'Rank ICIR': 0.147}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.147', 'weight': '0.034'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260323_13 721472964338721456 (Recorders: 5/5)

	Recorder: 82b16ae79f12435b98491919ddc71192

		Model: {'id': '82b16ae79f12435b98491919ddc71192', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.16, 'Rank IC': 0.026, 'Rank ICIR': 0.231}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.231', 'weight': '0.053'}

	Recorder: 47f5d6d017be405bad8d85507d1374df

		Model: {'id': '47f5d6d017be405bad8d85507d1374df', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.061, 'Rank IC': 0.02, 'Rank ICIR': 0.174}, 'data_train_vec': ['2022-03-23', '2025-03-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.174', 'weight': '0.040'}

	Recorder: f24e00152bb342718371ec59a2ef938a

		Model: {'id': 'f24e00152bb342718371ec59a2ef938a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.122, 'Rank IC': 0.038, 'Rank ICIR': 0.344}, 'data_train_vec': ['2023-03-23', '2025-06-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.344', 'weight': '0.079'}

	Recorder: 28b28eaade8d45a78da7d7bb4d8d69c2

		Model: {'id': '28b28eaade8d45a78da7d7bb4d8d69c2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.126, 'Rank IC': 0.021, 'Rank ICIR': 0.18}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.180', 'weight': '0.042'}

	Recorder: 5393a7347b364dcbb4a45e05da3dc2ac

		Model: {'id': '5393a7347b364dcbb4a45e05da3dc2ac', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.152, 'Rank IC': 0.026, 'Rank ICIR': 0.262}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.262', 'weight': '0.061'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260323_13 340893289053726656 (Recorders: 3/5)

	Recorder: b03f2ec0aac84d11a3476550b29ddf3a

		Model: {'id': 'b03f2ec0aac84d11a3476550b29ddf3a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.067, 'Rank IC': 0.033, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-03-23', '2024-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.196', 'weight': '0.045'}

	Recorder: d737e897e22144958071283818d91807

		Model: {'id': 'd737e897e22144958071283818d91807', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.251, 'Rank IC': 0.048, 'Rank ICIR': 0.454}, 'data_train_vec': ['2024-03-23', '2025-09-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.454', 'weight': '0.105'}

	Recorder: ada7be43fdb54f6f95570414a356e193

		Model: {'id': 'ada7be43fdb54f6f95570414a356e193', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.251, 'Rank IC': 0.022, 'Rank ICIR': 0.365}, 'data_train_vec': ['2025-03-23', '2025-12-22'], 'train_time_vec': ['2026-03-23', '2026-03-23'], 'rank_icir': '0.365', 'weight': '0.084'}
