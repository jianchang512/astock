# params 
 {'predict_dates': [{'start': '2026-04-01', 'end': '2026-04-01'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260401_15 479260349267403475 (Recorders: 3/5)

	Recorder: 19766ce76b924702bc16b5117cf1581e

		Model: {'id': '19766ce76b924702bc16b5117cf1581e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.208, 'Rank IC': 0.052, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.304', 'weight': '0.092'}

	Recorder: 491341b93b0c43ce967da3da30d67c29

		Model: {'id': '491341b93b0c43ce967da3da30d67c29', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.135, 'Rank IC': 0.05, 'Rank ICIR': 0.356}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.356', 'weight': '0.107'}

	Recorder: dbb0cf1396d143bbacbfc5c4107adf8c

		Model: {'id': 'dbb0cf1396d143bbacbfc5c4107adf8c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.14, 'Rank IC': 0.009, 'Rank ICIR': 0.069}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.069', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260401_14 491164610677239366 (Recorders: 3/5)

	Recorder: 691508983e7c4e638b8cb0a1d006b15a

		Model: {'id': '691508983e7c4e638b8cb0a1d006b15a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.039, 'Rank IC': 0.027, 'Rank ICIR': 0.158}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.158', 'weight': '0.048'}

	Recorder: 81dfd00a344b4e0ea14b2f0bba3d1c97

		Model: {'id': '81dfd00a344b4e0ea14b2f0bba3d1c97', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.007, 'Rank IC': 0.044, 'Rank ICIR': 0.228}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.228', 'weight': '0.069'}

	Recorder: bf4f56b5e37f44539255c826a71289ef

		Model: {'id': 'bf4f56b5e37f44539255c826a71289ef', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.142, 'Rank IC': 0.03, 'Rank ICIR': 0.256}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.256', 'weight': '0.077'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260401_12 430862945784326279 (Recorders: 4/5)

	Recorder: 498562cdef4d4674988157ce337db11c

		Model: {'id': '498562cdef4d4674988157ce337db11c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.092, 'Rank IC': 0.036, 'Rank ICIR': 0.199}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.199', 'weight': '0.060'}

	Recorder: 6b84fd1abbcf48ee9a3b9ea5ebd18b60

		Model: {'id': '6b84fd1abbcf48ee9a3b9ea5ebd18b60', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.097, 'Rank IC': 0.053, 'Rank ICIR': 0.295}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.295', 'weight': '0.089'}

	Recorder: 1433a5d1e09c4422a80e04e0f3e30a39

		Model: {'id': '1433a5d1e09c4422a80e04e0f3e30a39', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.284, 'Rank IC': 0.036, 'Rank ICIR': 0.351}, 'data_train_vec': ['2024-04-01', '2025-09-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.351', 'weight': '0.106'}

	Recorder: fec31ec2668c4607a5566345cb8bab1c

		Model: {'id': 'fec31ec2668c4607a5566345cb8bab1c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.006, 'Rank ICIR': 0.053}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.053', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260401_12 859367655774666025 (Recorders: 4/5)

	Recorder: 4f17d15f34024a6d879e721185290fba

		Model: {'id': '4f17d15f34024a6d879e721185290fba', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.101, 'Rank IC': 0.023, 'Rank ICIR': 0.185}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.185', 'weight': '0.056'}

	Recorder: 90c5c5cc5cbe48c8aca4957631734213

		Model: {'id': '90c5c5cc5cbe48c8aca4957631734213', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.02, 'Rank ICIR': 0.172}, 'data_train_vec': ['2022-04-01', '2025-03-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.172', 'weight': '0.052'}

	Recorder: 932d3205468c4e2fbec0389d5e2aec2e

		Model: {'id': '932d3205468c4e2fbec0389d5e2aec2e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.116, 'Rank IC': 0.039, 'Rank ICIR': 0.325}, 'data_train_vec': ['2023-04-01', '2025-06-30'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.325', 'weight': '0.098'}

	Recorder: 6368d89323ab40a49edaf1d27b70a08f

		Model: {'id': '6368d89323ab40a49edaf1d27b70a08f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.054, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.025', 'weight': '0.008'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260401_12 577855954737269401 (Recorders: 2/5)

	Recorder: 0e10b80346e442e4936089c4c6265201

		Model: {'id': '0e10b80346e442e4936089c4c6265201', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.118, 'Rank IC': 0.034, 'Rank ICIR': 0.181}, 'data_train_vec': ['2021-04-01', '2024-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.181', 'weight': '0.055'}

	Recorder: a448fa2b44fd46f6b35c2f934bffa899

		Model: {'id': 'a448fa2b44fd46f6b35c2f934bffa899', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.12, 'Rank IC': 0.014, 'Rank ICIR': 0.155}, 'data_train_vec': ['2025-04-01', '2025-12-31'], 'train_time_vec': ['2026-04-01', '2026-04-01'], 'rank_icir': '0.155', 'weight': '0.047'}
