# params 
 {'predict_dates': [{'start': '2026-03-25', 'end': '2026-03-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260325_14 540476804393822471 (Recorders: 3/5)

	Recorder: 930aa8c6e81a4ea89a71600705b564ba

		Model: {'id': '930aa8c6e81a4ea89a71600705b564ba', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.045, 'Rank IC': 0.021, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.159', 'weight': '0.033'}

	Recorder: ac3f502ffcfc43418955159cc6243d6d

		Model: {'id': 'ac3f502ffcfc43418955159cc6243d6d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.106, 'Rank IC': 0.038, 'Rank ICIR': 0.304}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.304', 'weight': '0.064'}

	Recorder: be708240040344f480a491d69e54ef60

		Model: {'id': 'be708240040344f480a491d69e54ef60', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.169, 'Rank IC': 0.017, 'Rank ICIR': 0.115}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.115', 'weight': '0.024'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260325_14 935171173025564133 (Recorders: 2/5)

	Recorder: 8354897fca0742eab67d4a76acbbaf9f

		Model: {'id': '8354897fca0742eab67d4a76acbbaf9f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.06, 'Rank IC': 0.026, 'Rank ICIR': 0.189}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.189', 'weight': '0.040'}

	Recorder: c9fc54af3bb14c60b445a4509e19074a

		Model: {'id': 'c9fc54af3bb14c60b445a4509e19074a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.352, 'Rank IC': 0.051, 'Rank ICIR': 0.441}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.441', 'weight': '0.093'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260325_12 730489382803491483 (Recorders: 3/5)

	Recorder: 0796abdc09bc4508a38f6f00a3eca48a

		Model: {'id': '0796abdc09bc4508a38f6f00a3eca48a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.144, 'Rank IC': 0.042, 'Rank ICIR': 0.236}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.236', 'weight': '0.050'}

	Recorder: 82e617f9d4ba44dba2a357ca8127185f

		Model: {'id': '82e617f9d4ba44dba2a357ca8127185f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.378, 'Rank IC': 0.052, 'Rank ICIR': 0.468}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.468', 'weight': '0.099'}

	Recorder: a93dd4184d4f41009ed13e8234f59a4e

		Model: {'id': 'a93dd4184d4f41009ed13e8234f59a4e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.132, 'Rank IC': 0.024, 'Rank ICIR': 0.222}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.222', 'weight': '0.047'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260325_11 621268635037407911 (Recorders: 5/5)

	Recorder: 2c45c8833c3b4afe9dc3aa9683410c0c

		Model: {'id': '2c45c8833c3b4afe9dc3aa9683410c0c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.169, 'Rank IC': 0.027, 'Rank ICIR': 0.233}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.233', 'weight': '0.049'}

	Recorder: 1f2192ab1b864c9e890e7982de0df2d4

		Model: {'id': '1f2192ab1b864c9e890e7982de0df2d4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.019, 'Rank ICIR': 0.162}, 'data_train_vec': ['2022-03-25', '2025-03-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.162', 'weight': '0.034'}

	Recorder: e8f25c9d09524738b135cd3f0e9a7c32

		Model: {'id': 'e8f25c9d09524738b135cd3f0e9a7c32', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.127, 'Rank IC': 0.038, 'Rank ICIR': 0.341}, 'data_train_vec': ['2023-03-25', '2025-06-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.341', 'weight': '0.072'}

	Recorder: 513e3bc6c4e54ebe9eda2a06e558b5e5

		Model: {'id': '513e3bc6c4e54ebe9eda2a06e558b5e5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.148, 'Rank IC': 0.025, 'Rank ICIR': 0.214}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.214', 'weight': '0.045'}

	Recorder: 913279ed11bf4800bea40760456d1214

		Model: {'id': '913279ed11bf4800bea40760456d1214', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.173, 'Rank IC': 0.025, 'Rank ICIR': 0.242}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.242', 'weight': '0.051'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260325_11 617048761561443680 (Recorders: 5/5)

	Recorder: e160d7505c4c4914b99a6481a84f31f3

		Model: {'id': 'e160d7505c4c4914b99a6481a84f31f3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.102, 'Rank IC': 0.039, 'Rank ICIR': 0.216}, 'data_train_vec': ['2021-03-25', '2024-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.216', 'weight': '0.045'}

	Recorder: 07521212162042b5a840b6f248125565

		Model: {'id': '07521212162042b5a840b6f248125565', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.045, 'Rank IC': 0.014, 'Rank ICIR': 0.073}, 'data_train_vec': ['2022-03-25', '2025-03-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.073', 'weight': '0.015'}

	Recorder: 6ab4bb1becda4a40926d198c7fbcccfc

		Model: {'id': '6ab4bb1becda4a40926d198c7fbcccfc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.032, 'Rank ICIR': 0.185}, 'data_train_vec': ['2023-03-25', '2025-06-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.185', 'weight': '0.039'}

	Recorder: 0196fe06ffbe4ca0970fa59cfedb92bc

		Model: {'id': '0196fe06ffbe4ca0970fa59cfedb92bc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.041, 'Rank ICIR': 0.393}, 'data_train_vec': ['2024-03-25', '2025-09-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.393', 'weight': '0.083'}

	Recorder: 6d093633159849f0990d485b59e53d53

		Model: {'id': '6d093633159849f0990d485b59e53d53', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.252, 'Rank IC': 0.04, 'Rank ICIR': 0.556}, 'data_train_vec': ['2025-03-25', '2025-12-24'], 'train_time_vec': ['2026-03-25', '2026-03-25'], 'rank_icir': '0.556', 'weight': '0.117'}
