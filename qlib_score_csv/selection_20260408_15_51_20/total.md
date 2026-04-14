# params 
 {'predict_dates': [{'start': '2026-04-08', 'end': '2026-04-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260408_15 855644284712426144 (Recorders: 3/5)

	Recorder: 604f371262a94b1384a1f7a0699e5ed6

		Model: {'id': '604f371262a94b1384a1f7a0699e5ed6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.141, 'Rank IC': 0.045, 'Rank ICIR': 0.285}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.285', 'weight': '0.083'}

	Recorder: 3f326b2145f54a72a920cc3818a3c5ca

		Model: {'id': '3f326b2145f54a72a920cc3818a3c5ca', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.312, 'Rank IC': 0.035, 'Rank ICIR': 0.296}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.296', 'weight': '0.086'}

	Recorder: 5080eb3f50dc48aeae7fc34043f1cd0c

		Model: {'id': '5080eb3f50dc48aeae7fc34043f1cd0c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.144, 'Rank IC': 0.011, 'Rank ICIR': 0.071}, 'data_train_vec': ['2025-04-08', '2026-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.071', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260408_15 869514504280100029 (Recorders: 1/5)

	Recorder: 67a23c548c104666970b2859acde5249

		Model: {'id': '67a23c548c104666970b2859acde5249', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.322, 'Rank IC': 0.037, 'Rank ICIR': 0.311}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.311', 'weight': '0.091'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260408_12 140296784985495697 (Recorders: 4/5)

	Recorder: ba17d982d8194f209b4761b512a4c07b

		Model: {'id': 'ba17d982d8194f209b4761b512a4c07b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.056, 'Rank IC': 0.027, 'Rank ICIR': 0.152}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.152', 'weight': '0.044'}

	Recorder: 93eeb614bd764fe3872f37c13839a12a

		Model: {'id': '93eeb614bd764fe3872f37c13839a12a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.03, 'Rank IC': 0.031, 'Rank ICIR': 0.172}, 'data_train_vec': ['2022-04-08', '2025-04-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.172', 'weight': '0.050'}

	Recorder: 8cb371edc96341e79858e61ce0f3dcd6

		Model: {'id': '8cb371edc96341e79858e61ce0f3dcd6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.121, 'Rank IC': 0.054, 'Rank ICIR': 0.31}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.310', 'weight': '0.090'}

	Recorder: 56c1fe5b98f14f3bac477378912c6235

		Model: {'id': '56c1fe5b98f14f3bac477378912c6235', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.352, 'Rank IC': 0.035, 'Rank ICIR': 0.336}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.336', 'weight': '0.098'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260408_12 879606548474263451 (Recorders: 5/5)

	Recorder: 64ca87b17008433da10a6219a6a095d5

		Model: {'id': '64ca87b17008433da10a6219a6a095d5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.111, 'Rank IC': 0.022, 'Rank ICIR': 0.183}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.183', 'weight': '0.053'}

	Recorder: 2ca0f80bcd334b79900a5fa6eda7df33

		Model: {'id': '2ca0f80bcd334b79900a5fa6eda7df33', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.025, 'Rank ICIR': 0.212}, 'data_train_vec': ['2022-04-08', '2025-04-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.212', 'weight': '0.062'}

	Recorder: 5efef4938c2a4db08242582583f54452

		Model: {'id': '5efef4938c2a4db08242582583f54452', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.153, 'Rank IC': 0.044, 'Rank ICIR': 0.38}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.380', 'weight': '0.111'}

	Recorder: 7df80e4f822d480092cbc8205a14326f

		Model: {'id': '7df80e4f822d480092cbc8205a14326f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.067, 'Rank IC': 0.011, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.092', 'weight': '0.027'}

	Recorder: 86372c8a7ae64176bbd8ad0514b3cba1

		Model: {'id': '86372c8a7ae64176bbd8ad0514b3cba1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.072, 'Rank IC': 0.006, 'Rank ICIR': 0.036}, 'data_train_vec': ['2025-04-08', '2026-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.036', 'weight': '0.010'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260408_12 145019584625559182 (Recorders: 3/5)

	Recorder: 33d4bcddabd3406a9b0041d09875525a

		Model: {'id': '33d4bcddabd3406a9b0041d09875525a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.088, 'Rank IC': 0.025, 'Rank ICIR': 0.141}, 'data_train_vec': ['2021-04-08', '2025-01-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.141', 'weight': '0.041'}

	Recorder: 239a5470af52400e9b589a5114169b4e

		Model: {'id': '239a5470af52400e9b589a5114169b4e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.032, 'Rank ICIR': 0.189}, 'data_train_vec': ['2023-04-08', '2025-07-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.189', 'weight': '0.055'}

	Recorder: 10ced1342de44682bbe1a96991065ff0

		Model: {'id': '10ced1342de44682bbe1a96991065ff0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.301, 'Rank IC': 0.031, 'Rank ICIR': 0.27}, 'data_train_vec': ['2024-04-08', '2025-10-07'], 'train_time_vec': ['2026-04-08', '2026-04-08'], 'rank_icir': '0.270', 'weight': '0.079'}
