# params 
 {'predict_dates': [{'start': '2026-04-07', 'end': '2026-04-07'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260407_14 524426194399064099 (Recorders: 4/5)

	Recorder: bd1ac0092a5b40cfaf8878fafe0f4b14

		Model: {'id': 'bd1ac0092a5b40cfaf8878fafe0f4b14', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.048, 'Rank IC': 0.025, 'Rank ICIR': 0.135}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.135', 'weight': '0.036'}

	Recorder: 2ace07476c904aa3a3a6ec01ac96060e

		Model: {'id': '2ace07476c904aa3a3a6ec01ac96060e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.034, 'Rank ICIR': 0.182}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.182', 'weight': '0.048'}

	Recorder: 0ee7ad51426e41d78c1475593481f1b9

		Model: {'id': '0ee7ad51426e41d78c1475593481f1b9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.072, 'Rank IC': 0.048, 'Rank ICIR': 0.364}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.364', 'weight': '0.097'}

	Recorder: 82d84ec4c7c84f63be848256ca6cb5e5

		Model: {'id': '82d84ec4c7c84f63be848256ca6cb5e5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.322, 'Rank IC': 0.039, 'Rank ICIR': 0.336}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.336', 'weight': '0.090'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260407_14 335770828686225827 (Recorders: 1/5)

	Recorder: df161349b8494a5fabb5c4c42b582d71

		Model: {'id': 'df161349b8494a5fabb5c4c42b582d71', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.302, 'Rank IC': 0.037, 'Rank ICIR': 0.312}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.312', 'weight': '0.083'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260407_12 637561553885865850 (Recorders: 4/5)

	Recorder: c926fcc158a04884b7f49eccbb86014c

		Model: {'id': 'c926fcc158a04884b7f49eccbb86014c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.091, 'Rank IC': 0.034, 'Rank ICIR': 0.19}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.190', 'weight': '0.051'}

	Recorder: fa7643e24d00440c8562c9d15f5c0caa

		Model: {'id': 'fa7643e24d00440c8562c9d15f5c0caa', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.021, 'Rank IC': 0.032, 'Rank ICIR': 0.179}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.179', 'weight': '0.048'}

	Recorder: 6ae901a4aa194f6fbf225bf7ffc665b5

		Model: {'id': '6ae901a4aa194f6fbf225bf7ffc665b5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.134, 'Rank IC': 0.056, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.327', 'weight': '0.087'}

	Recorder: b1b9447a3d4d401d9d84709d375d8a01

		Model: {'id': 'b1b9447a3d4d401d9d84709d375d8a01', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.294, 'Rank IC': 0.031, 'Rank ICIR': 0.289}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.289', 'weight': '0.077'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260407_12 741644944022969351 (Recorders: 3/5)

	Recorder: 418cca962fa84d47b2652e06a3110f0a

		Model: {'id': '418cca962fa84d47b2652e06a3110f0a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.11, 'Rank IC': 0.023, 'Rank ICIR': 0.187}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.187', 'weight': '0.050'}

	Recorder: faaea31186fe43f5af5b88fd55b25686

		Model: {'id': 'faaea31186fe43f5af5b88fd55b25686', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.024, 'Rank ICIR': 0.204}, 'data_train_vec': ['2022-04-07', '2025-04-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.204', 'weight': '0.054'}

	Recorder: 5af658d5018e4a9b90b9dcad9ede88aa

		Model: {'id': '5af658d5018e4a9b90b9dcad9ede88aa', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.101, 'Rank IC': 0.039, 'Rank ICIR': 0.338}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.338', 'weight': '0.090'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260407_11 783371896040037512 (Recorders: 3/5)

	Recorder: 27ed874812c145aa956bc1c0699534d2

		Model: {'id': '27ed874812c145aa956bc1c0699534d2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.048, 'Rank IC': 0.028, 'Rank ICIR': 0.151}, 'data_train_vec': ['2021-04-07', '2025-01-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.151', 'weight': '0.040'}

	Recorder: 1e33da2d73e14c7ab57725c8041b7b15

		Model: {'id': '1e33da2d73e14c7ab57725c8041b7b15', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.087, 'Rank IC': 0.048, 'Rank ICIR': 0.286}, 'data_train_vec': ['2023-04-07', '2025-07-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.286', 'weight': '0.076'}

	Recorder: 495ab8667dcf4a72989fbc17e691b9db

		Model: {'id': '495ab8667dcf4a72989fbc17e691b9db', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.287, 'Rank IC': 0.032, 'Rank ICIR': 0.273}, 'data_train_vec': ['2024-04-07', '2025-10-06'], 'train_time_vec': ['2026-04-07', '2026-04-07'], 'rank_icir': '0.273', 'weight': '0.073'}
