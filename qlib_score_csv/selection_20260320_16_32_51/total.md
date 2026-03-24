# params 
 {'predict_dates': [{'start': '2026-03-20', 'end': '2026-03-20'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260320_16 392273662023298498 (Recorders: 3/5)

	Recorder: 2437f2d24d44478f8557462892be8909

		Model: {'id': '2437f2d24d44478f8557462892be8909', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.037, 'Rank ICIR': 0.184}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.184', 'weight': '0.053'}

	Recorder: b6f8df78c3314fe991c10f47dc6eaacc

		Model: {'id': 'b6f8df78c3314fe991c10f47dc6eaacc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.111, 'Rank IC': 0.037, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.251', 'weight': '0.072'}

	Recorder: 457a0b80b6434585ba5b051c5433f606

		Model: {'id': '457a0b80b6434585ba5b051c5433f606', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.206, 'Rank IC': 0.045, 'Rank ICIR': 0.358}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.358', 'weight': '0.102'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260320_16 685004992375794522 (Recorders: 1/5)

	Recorder: 9f2bb8b0917e497a91446c663a2f6abb

		Model: {'id': '9f2bb8b0917e497a91446c663a2f6abb', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.207, 'Rank IC': 0.038, 'Rank ICIR': 0.287}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.287', 'weight': '0.082'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260320_13 923736447921815743 (Recorders: 2/5)

	Recorder: 49eb9b07ce6b45b99f51475a89086e35

		Model: {'id': '49eb9b07ce6b45b99f51475a89086e35', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.091, 'Rank IC': 0.033, 'Rank ICIR': 0.189}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.189', 'weight': '0.054'}

	Recorder: ffc62542047f4c07b5637d8be587554b

		Model: {'id': 'ffc62542047f4c07b5637d8be587554b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.38, 'Rank IC': 0.04, 'Rank ICIR': 0.362}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.362', 'weight': '0.103'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260320_13 222145423310636561 (Recorders: 5/5)

	Recorder: 9f81233894d04a16b06f6eb7f80db4b1

		Model: {'id': '9f81233894d04a16b06f6eb7f80db4b1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.123, 'Rank IC': 0.022, 'Rank ICIR': 0.19}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.190', 'weight': '0.054'}

	Recorder: 4a60fed1b8924c0194303d02466733cd

		Model: {'id': '4a60fed1b8924c0194303d02466733cd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.019, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-03-20', '2025-03-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.169', 'weight': '0.048'}

	Recorder: e7543f96b5324807a215226913b8c285

		Model: {'id': 'e7543f96b5324807a215226913b8c285', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.108, 'Rank IC': 0.035, 'Rank ICIR': 0.308}, 'data_train_vec': ['2023-03-20', '2025-06-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.308', 'weight': '0.088'}

	Recorder: 5cd8e9c5aeeb4626b276bf63ae3994e6

		Model: {'id': '5cd8e9c5aeeb4626b276bf63ae3994e6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.132, 'Rank IC': 0.013, 'Rank ICIR': 0.119}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.119', 'weight': '0.034'}

	Recorder: ffed2a5825344f488c0b7a824f9b5f27

		Model: {'id': 'ffed2a5825344f488c0b7a824f9b5f27', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.163, 'Rank IC': 0.033, 'Rank ICIR': 0.313}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.313', 'weight': '0.089'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260320_13 525533096851930186 (Recorders: 2/5)

	Recorder: f05cd072d6a745d9a8ad8fb1aaff966b

		Model: {'id': 'f05cd072d6a745d9a8ad8fb1aaff966b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.103, 'Rank IC': 0.037, 'Rank ICIR': 0.28}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.280', 'weight': '0.080'}

	Recorder: eabd49b710be4920b6b1ee015fd69c63

		Model: {'id': 'eabd49b710be4920b6b1ee015fd69c63', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.192, 'Rank IC': 0.041, 'Rank ICIR': 0.488}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.488', 'weight': '0.140'}
