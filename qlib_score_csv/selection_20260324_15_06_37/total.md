# params 
 {'predict_dates': [{'start': '2026-03-24', 'end': '2026-03-24'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260324_14 380663602445105230 (Recorders: 3/5)

	Recorder: 0e8ff1ba78a1442e847c3a4f30c4a2ed

		Model: {'id': '0e8ff1ba78a1442e847c3a4f30c4a2ed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.035, 'Rank IC': 0.029, 'Rank ICIR': 0.172}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.172', 'weight': '0.040'}

	Recorder: abe6f678bbd146bc974f3f912eb5607f

		Model: {'id': 'abe6f678bbd146bc974f3f912eb5607f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.101, 'Rank IC': 0.04, 'Rank ICIR': 0.296}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.296', 'weight': '0.069'}

	Recorder: 9f9ab51ba65b409d9b8968f8373921ad

		Model: {'id': '9f9ab51ba65b409d9b8968f8373921ad', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.018, 'Rank IC': 0.031, 'Rank ICIR': 0.255}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.255', 'weight': '0.059'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260324_14 683255964614739181 (Recorders: 2/5)

	Recorder: d6472ddfa5dc4c55aaf3e408f3cb5d6f

		Model: {'id': 'd6472ddfa5dc4c55aaf3e408f3cb5d6f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.057, 'Rank IC': 0.024, 'Rank ICIR': 0.187}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.187', 'weight': '0.043'}

	Recorder: 61374aa5816c46a496824d8c5e8588c0

		Model: {'id': '61374aa5816c46a496824d8c5e8588c0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.348, 'Rank IC': 0.045, 'Rank ICIR': 0.413}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.413', 'weight': '0.096'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260324_12 302745819180652868 (Recorders: 3/5)

	Recorder: 6f9ee35d113d4ce09527f0fe702e46ef

		Model: {'id': '6f9ee35d113d4ce09527f0fe702e46ef', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.126, 'Rank IC': 0.036, 'Rank ICIR': 0.207}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.207', 'weight': '0.048'}

	Recorder: 17301409c03a4b728768a7d14ef0ffeb

		Model: {'id': '17301409c03a4b728768a7d14ef0ffeb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.308, 'Rank IC': 0.043, 'Rank ICIR': 0.369}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.369', 'weight': '0.086'}

	Recorder: e850b5f2a626482182f3b0e950e0f851

		Model: {'id': 'e850b5f2a626482182f3b0e950e0f851', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.058, 'Rank IC': 0.016, 'Rank ICIR': 0.175}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.175', 'weight': '0.041'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260324_11 869329394066339299 (Recorders: 5/5)

	Recorder: 42f59f276efb4ba3ad911e19e2db67fb

		Model: {'id': '42f59f276efb4ba3ad911e19e2db67fb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.168, 'Rank IC': 0.027, 'Rank ICIR': 0.235}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.235', 'weight': '0.054'}

	Recorder: b49d2be8e3824ae0aedf7a4815835bf2

		Model: {'id': 'b49d2be8e3824ae0aedf7a4815835bf2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.02, 'Rank ICIR': 0.178}, 'data_train_vec': ['2022-03-24', '2025-03-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.178', 'weight': '0.041'}

	Recorder: a13b88157b2f4bb685444fa568b88d54

		Model: {'id': 'a13b88157b2f4bb685444fa568b88d54', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.125, 'Rank IC': 0.039, 'Rank ICIR': 0.361}, 'data_train_vec': ['2023-03-24', '2025-06-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.361', 'weight': '0.084'}

	Recorder: 30008001fbf8453f921e2e9e3b8a9205

		Model: {'id': '30008001fbf8453f921e2e9e3b8a9205', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.141, 'Rank IC': 0.023, 'Rank ICIR': 0.181}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.181', 'weight': '0.042'}

	Recorder: 2c52089f88b74e1d96d986db7e7df42e

		Model: {'id': '2c52089f88b74e1d96d986db7e7df42e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.275, 'Rank IC': 0.036, 'Rank ICIR': 0.357}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.357', 'weight': '0.083'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260324_11 499086666321103216 (Recorders: 3/5)

	Recorder: ea10d36626f74c4bbaba0e50ba68f399

		Model: {'id': 'ea10d36626f74c4bbaba0e50ba68f399', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.09, 'Rank IC': 0.036, 'Rank ICIR': 0.197}, 'data_train_vec': ['2021-03-24', '2024-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.197', 'weight': '0.046'}

	Recorder: e3279db33cc248e39c247b4d9fca02de

		Model: {'id': 'e3279db33cc248e39c247b4d9fca02de', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.192, 'Rank IC': 0.041, 'Rank ICIR': 0.43}, 'data_train_vec': ['2024-03-24', '2025-09-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.430', 'weight': '0.100'}

	Recorder: ccc3da73cec14d5c936221ab706d5bd7

		Model: {'id': 'ccc3da73cec14d5c936221ab706d5bd7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.174, 'Rank IC': 0.026, 'Rank ICIR': 0.301}, 'data_train_vec': ['2025-03-24', '2025-12-23'], 'train_time_vec': ['2026-03-24', '2026-03-24'], 'rank_icir': '0.301', 'weight': '0.070'}
