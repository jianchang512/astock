# params 
 {'predict_dates': [{'start': '2026-04-10', 'end': '2026-04-10'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260410_15 198556301923151892 (Recorders: 3/5)

	Recorder: f1b69bc5f4b04d0d85dfd0befe7e37e2

		Model: {'id': 'f1b69bc5f4b04d0d85dfd0befe7e37e2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.202, 'Rank IC': 0.036, 'Rank ICIR': 0.222}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.222', 'weight': '0.080'}

	Recorder: 3b3995eedbb149ef8bbee1b42ddd666d

		Model: {'id': '3b3995eedbb149ef8bbee1b42ddd666d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.085, 'Rank IC': 0.028, 'Rank ICIR': 0.207}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.207', 'weight': '0.075'}

	Recorder: 796166c1067c40a5812133148ab7064f

		Model: {'id': '796166c1067c40a5812133148ab7064f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.097, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2025-04-10', '2026-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.025', 'weight': '0.009'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260410_15 783294842368601641 (Recorders: 1/5)

	Recorder: e44e9a11b624494e85de74158e207b2a

		Model: {'id': 'e44e9a11b624494e85de74158e207b2a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.326, 'Rank IC': 0.044, 'Rank ICIR': 0.391}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.391', 'weight': '0.142'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260410_12 510699725194099248 (Recorders: 3/5)

	Recorder: 528c1140ecee4c0b81a15cc8d835ec9b

		Model: {'id': '528c1140ecee4c0b81a15cc8d835ec9b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.036, 'Rank IC': 0.024, 'Rank ICIR': 0.138}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.138', 'weight': '0.050'}

	Recorder: 40edaf5422a44cf39f03c5287821dc2c

		Model: {'id': '40edaf5422a44cf39f03c5287821dc2c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.08, 'Rank IC': 0.046, 'Rank ICIR': 0.266}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.266', 'weight': '0.096'}

	Recorder: e1bf418e17574a0cbb1a6cdf064c7a42

		Model: {'id': 'e1bf418e17574a0cbb1a6cdf064c7a42', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.229, 'Rank IC': 0.023, 'Rank ICIR': 0.211}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.211', 'weight': '0.076'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260410_12 876865355325833767 (Recorders: 5/5)

	Recorder: e7d2a2a6b4414b0d9299188a9e459821

		Model: {'id': 'e7d2a2a6b4414b0d9299188a9e459821', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.088, 'Rank IC': 0.021, 'Rank ICIR': 0.17}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.170', 'weight': '0.062'}

	Recorder: f2bd2303fe784602bc32447448625d13

		Model: {'id': 'f2bd2303fe784602bc32447448625d13', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.019, 'Rank ICIR': 0.167}, 'data_train_vec': ['2022-04-10', '2025-04-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.167', 'weight': '0.060'}

	Recorder: e6ce899c4b2e4c5abf70db1f346f2e5d

		Model: {'id': 'e6ce899c4b2e4c5abf70db1f346f2e5d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.12, 'Rank IC': 0.038, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.327', 'weight': '0.118'}

	Recorder: 654501843f934ffa9ad90ef2b9c8ea00

		Model: {'id': '654501843f934ffa9ad90ef2b9c8ea00', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.055, 'Rank IC': 0.008, 'Rank ICIR': 0.064}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.064', 'weight': '0.023'}

	Recorder: f10e6a6c22714fc7a9ec617f5f9efec8

		Model: {'id': 'f10e6a6c22714fc7a9ec617f5f9efec8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.081, 'Rank IC': 0.003, 'Rank ICIR': 0.019}, 'data_train_vec': ['2025-04-10', '2026-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.019', 'weight': '0.007'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260410_12 162679621922897489 (Recorders: 3/5)

	Recorder: 7fdf9390335b4b499ed61ed780a4ef83

		Model: {'id': '7fdf9390335b4b499ed61ed780a4ef83', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.018, 'Rank ICIR': 0.097}, 'data_train_vec': ['2021-04-10', '2025-01-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.097', 'weight': '0.035'}

	Recorder: 6b32ceda04504446b7eb806cfb922de0

		Model: {'id': '6b32ceda04504446b7eb806cfb922de0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.031, 'Rank ICIR': 0.173}, 'data_train_vec': ['2023-04-10', '2025-07-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.173', 'weight': '0.063'}

	Recorder: 26624a42121c42c18fe4cbf0c8f18aa4

		Model: {'id': '26624a42121c42c18fe4cbf0c8f18aa4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.07, 'Rank IC': 0.034, 'Rank ICIR': 0.284}, 'data_train_vec': ['2024-04-10', '2025-10-09'], 'train_time_vec': ['2026-04-10', '2026-04-10'], 'rank_icir': '0.284', 'weight': '0.103'}
