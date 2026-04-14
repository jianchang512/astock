# params 
 {'predict_dates': [{'start': '2026-03-19', 'end': '2026-03-19'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260319_14 683882663747188280 (Recorders: 3/5)

	Recorder: 70ca8f9f68c84f33bf18e0e150c0e19b

		Model: {'id': '70ca8f9f68c84f33bf18e0e150c0e19b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.038, 'Rank IC': 0.029, 'Rank ICIR': 0.145}, 'data_train_vec': ['2021-03-19', '2024-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.145', 'weight': '0.037'}

	Recorder: b3e58b7fc66241b39f2c6473303195e9

		Model: {'id': 'b3e58b7fc66241b39f2c6473303195e9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.314, 'Rank IC': 0.051, 'Rank ICIR': 0.417}, 'data_train_vec': ['2024-03-19', '2025-09-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.417', 'weight': '0.105'}

	Recorder: d73f0b38dd7b4a67b9fc329188f3bd0d

		Model: {'id': 'd73f0b38dd7b4a67b9fc329188f3bd0d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.101, 'Rank IC': 0.05, 'Rank ICIR': 0.32}, 'data_train_vec': ['2025-03-19', '2025-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.320', 'weight': '0.081'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260319_14 784777676147630775 (Recorders: 2/5)

	Recorder: 9cffa15f8b174f87bb4885255c919088

		Model: {'id': '9cffa15f8b174f87bb4885255c919088', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.228, 'Rank IC': 0.042, 'Rank ICIR': 0.308}, 'data_train_vec': ['2024-03-19', '2025-09-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.308', 'weight': '0.078'}

	Recorder: d9d2251b70a0479f91b512fafe2aa8dd

		Model: {'id': 'd9d2251b70a0479f91b512fafe2aa8dd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.041, 'Rank IC': 0.024, 'Rank ICIR': 0.192}, 'data_train_vec': ['2025-03-19', '2025-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.192', 'weight': '0.048'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260319_11 570641430314999528 (Recorders: 4/5)

	Recorder: 856320e5df0445a1b32d8e159041a1d7

		Model: {'id': '856320e5df0445a1b32d8e159041a1d7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.086, 'Rank IC': 0.033, 'Rank ICIR': 0.195}, 'data_train_vec': ['2021-03-19', '2024-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.195', 'weight': '0.049'}

	Recorder: e6ebe95ca73c4a8f963dcadbcc62cbf5

		Model: {'id': 'e6ebe95ca73c4a8f963dcadbcc62cbf5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.023, 'Rank ICIR': 0.125}, 'data_train_vec': ['2022-03-19', '2025-03-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.125', 'weight': '0.032'}

	Recorder: 5fbf40f021b145618431a97c41b90122

		Model: {'id': '5fbf40f021b145618431a97c41b90122', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.303, 'Rank IC': 0.034, 'Rank ICIR': 0.323}, 'data_train_vec': ['2024-03-19', '2025-09-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.323', 'weight': '0.082'}

	Recorder: 76b32b21ae894d2dbdba3e91c0794bde

		Model: {'id': '76b32b21ae894d2dbdba3e91c0794bde', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.091, 'Rank IC': 0.027, 'Rank ICIR': 0.296}, 'data_train_vec': ['2025-03-19', '2025-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.296', 'weight': '0.075'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260319_11 510292688464660649 (Recorders: 5/5)

	Recorder: 21d5133439214700b8ee74d05dc48205

		Model: {'id': '21d5133439214700b8ee74d05dc48205', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.115, 'Rank IC': 0.02, 'Rank ICIR': 0.176}, 'data_train_vec': ['2021-03-19', '2024-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.176', 'weight': '0.044'}

	Recorder: d9db4a5e061442f19239c999433fc2df

		Model: {'id': 'd9db4a5e061442f19239c999433fc2df', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.099, 'Rank IC': 0.022, 'Rank ICIR': 0.185}, 'data_train_vec': ['2022-03-19', '2025-03-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.185', 'weight': '0.047'}

	Recorder: 11cf2a20578141668d965ddcab634a55

		Model: {'id': '11cf2a20578141668d965ddcab634a55', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.118, 'Rank IC': 0.037, 'Rank ICIR': 0.315}, 'data_train_vec': ['2023-03-19', '2025-06-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.315', 'weight': '0.080'}

	Recorder: 0ac94680c22447f9aff800ac588b4c2c

		Model: {'id': '0ac94680c22447f9aff800ac588b4c2c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.146, 'Rank IC': 0.015, 'Rank ICIR': 0.138}, 'data_train_vec': ['2024-03-19', '2025-09-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.138', 'weight': '0.035'}

	Recorder: ca40789cd50a4aab977fac942c5dbb9a

		Model: {'id': 'ca40789cd50a4aab977fac942c5dbb9a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.31, 'Rank IC': 0.044, 'Rank ICIR': 0.435}, 'data_train_vec': ['2025-03-19', '2025-12-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.435', 'weight': '0.110'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260319_11 414803361424184789 (Recorders: 1/5)

	Recorder: 35fac831ba684d3bb6d550df44fcd8d1

		Model: {'id': '35fac831ba684d3bb6d550df44fcd8d1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.223, 'Rank IC': 0.043, 'Rank ICIR': 0.389}, 'data_train_vec': ['2024-03-19', '2025-09-18'], 'train_time_vec': ['2026-03-19', '2026-03-19'], 'rank_icir': '0.389', 'weight': '0.098'}
