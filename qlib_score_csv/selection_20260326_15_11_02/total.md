# params 
 {'predict_dates': [{'start': '2026-03-26', 'end': '2026-03-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260326_14 440952601026580805 (Recorders: 3/5)

	Recorder: 67eabbbe5ef746e9ab4b9d0f8eb840f4

		Model: {'id': '67eabbbe5ef746e9ab4b9d0f8eb840f4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.124, 'Rank IC': 0.026, 'Rank ICIR': 0.215}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.215', 'weight': '0.047'}

	Recorder: e66c410e736f44f59bc2a60946e02fdc

		Model: {'id': 'e66c410e736f44f59bc2a60946e02fdc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.213, 'Rank IC': 0.022, 'Rank ICIR': 0.183}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.183', 'weight': '0.040'}

	Recorder: 2549fa87e72d43bcb610836cd10c0ec7

		Model: {'id': '2549fa87e72d43bcb610836cd10c0ec7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.215, 'Rank IC': 0.045, 'Rank ICIR': 0.352}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.352', 'weight': '0.077'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260326_14 704823153244544792 (Recorders: 2/5)

	Recorder: 44e3a0d076234fc0902a2fb679f445b8

		Model: {'id': '44e3a0d076234fc0902a2fb679f445b8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.059, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.196', 'weight': '0.043'}

	Recorder: d6a1e6bc422b4e5ab9905cff391e4653

		Model: {'id': 'd6a1e6bc422b4e5ab9905cff391e4653', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.391, 'Rank IC': 0.057, 'Rank ICIR': 0.482}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.482', 'weight': '0.106'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260326_12 332393681253000548 (Recorders: 3/5)

	Recorder: e23eef70e0c54562b86d64e46239067d

		Model: {'id': 'e23eef70e0c54562b86d64e46239067d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.132, 'Rank IC': 0.041, 'Rank ICIR': 0.236}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.236', 'weight': '0.052'}

	Recorder: 04e1083f86684234bdb0b9143ef5b99f

		Model: {'id': '04e1083f86684234bdb0b9143ef5b99f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.339, 'Rank IC': 0.043, 'Rank ICIR': 0.361}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.361', 'weight': '0.079'}

	Recorder: 99c73e019b77485e963dfd0ba6962f6b

		Model: {'id': '99c73e019b77485e963dfd0ba6962f6b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.133, 'Rank IC': 0.024, 'Rank ICIR': 0.214}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.214', 'weight': '0.047'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260326_12 603295009399826776 (Recorders: 5/5)

	Recorder: 2bd5dafff03c450f8b96a8efa7e138c6

		Model: {'id': '2bd5dafff03c450f8b96a8efa7e138c6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.183, 'Rank IC': 0.029, 'Rank ICIR': 0.251}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.251', 'weight': '0.055'}

	Recorder: c2a4fd10cc0345b1acbb62845136f586

		Model: {'id': 'c2a4fd10cc0345b1acbb62845136f586', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.047, 'Rank IC': 0.021, 'Rank ICIR': 0.181}, 'data_train_vec': ['2022-03-26', '2025-03-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.181', 'weight': '0.040'}

	Recorder: 5ddeb0269f254903b976a9dfa7aa191c

		Model: {'id': '5ddeb0269f254903b976a9dfa7aa191c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.149, 'Rank IC': 0.04, 'Rank ICIR': 0.362}, 'data_train_vec': ['2023-03-26', '2025-06-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.362', 'weight': '0.080'}

	Recorder: 8e2b7a5e09f54a12ae6bccc8e5533af0

		Model: {'id': '8e2b7a5e09f54a12ae6bccc8e5533af0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.118, 'Rank IC': 0.022, 'Rank ICIR': 0.174}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.174', 'weight': '0.038'}

	Recorder: cc8fe20e2e1a4f4cb5307ef457bb3ac7

		Model: {'id': 'cc8fe20e2e1a4f4cb5307ef457bb3ac7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.151, 'Rank IC': 0.026, 'Rank ICIR': 0.246}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.246', 'weight': '0.054'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260326_11 247834683213220880 (Recorders: 3/5)

	Recorder: 44674ae4a76c4845b9c6ab8f6174b3c0

		Model: {'id': '44674ae4a76c4845b9c6ab8f6174b3c0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.03, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-03-26', '2024-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.159', 'weight': '0.035'}

	Recorder: 6e18c235661a4ce3b816ac5c147f0042

		Model: {'id': '6e18c235661a4ce3b816ac5c147f0042', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.051, 'Rank ICIR': 0.424}, 'data_train_vec': ['2024-03-26', '2025-09-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.424', 'weight': '0.093'}

	Recorder: 4a0a8bd8b938469792255fd028f8e975

		Model: {'id': '4a0a8bd8b938469792255fd028f8e975', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.257, 'Rank IC': 0.046, 'Rank ICIR': 0.514}, 'data_train_vec': ['2025-03-26', '2025-12-25'], 'train_time_vec': ['2026-03-26', '2026-03-26'], 'rank_icir': '0.514', 'weight': '0.113'}
