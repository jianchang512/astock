# params 
 {'predict_dates': [{'start': '2026-03-20', 'end': '2026-03-20'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260320_16 896026439015142642 (Recorders: 3/5)

	Recorder: 7d54a7d19fff43729d2a0e23053795a6

		Model: {'id': '7d54a7d19fff43729d2a0e23053795a6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.037, 'Rank ICIR': 0.184}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.184', 'weight': '0.050'}

	Recorder: 04f02f9f648547bf99c2a24dabc6a8fb

		Model: {'id': '04f02f9f648547bf99c2a24dabc6a8fb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.111, 'Rank IC': 0.037, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.251', 'weight': '0.069'}

	Recorder: 82df965be31c408598fac2588b0f3efe

		Model: {'id': '82df965be31c408598fac2588b0f3efe', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.206, 'Rank IC': 0.045, 'Rank ICIR': 0.358}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.358', 'weight': '0.098'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260320_15 767495318518439441 (Recorders: 1/5)

	Recorder: 64fb290e951a4ee3a8132dba9a211861

		Model: {'id': '64fb290e951a4ee3a8132dba9a211861', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.207, 'Rank IC': 0.038, 'Rank ICIR': 0.287}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.287', 'weight': '0.078'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260320_13 301834621140226065 (Recorders: 3/5)

	Recorder: fa629d20b6d24d089e277a1dbb2206ef

		Model: {'id': 'fa629d20b6d24d089e277a1dbb2206ef', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.073, 'Rank IC': 0.032, 'Rank ICIR': 0.186}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.186', 'weight': '0.051'}

	Recorder: 68c186b7260c4041b73764ce6ac0ec37

		Model: {'id': '68c186b7260c4041b73764ce6ac0ec37', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.295, 'Rank IC': 0.038, 'Rank ICIR': 0.35}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.350', 'weight': '0.096'}

	Recorder: 73071b919cbc4cb28cd681d303f4ed69

		Model: {'id': '73071b919cbc4cb28cd681d303f4ed69', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.066, 'Rank IC': 0.016, 'Rank ICIR': 0.176}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.176', 'weight': '0.048'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260320_13 421074577848224723 (Recorders: 5/5)

	Recorder: 912753ea96f946488be9ea0da87f2bca

		Model: {'id': '912753ea96f946488be9ea0da87f2bca', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.123, 'Rank IC': 0.022, 'Rank ICIR': 0.19}, 'data_train_vec': ['2021-03-20', '2024-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.190', 'weight': '0.052'}

	Recorder: 638bd7351c3d40ccbaa148c1727c3314

		Model: {'id': '638bd7351c3d40ccbaa148c1727c3314', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.019, 'Rank ICIR': 0.169}, 'data_train_vec': ['2022-03-20', '2025-03-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.169', 'weight': '0.046'}

	Recorder: 82a64722f6f7463ca8c316b9ec3a69ef

		Model: {'id': '82a64722f6f7463ca8c316b9ec3a69ef', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.108, 'Rank IC': 0.035, 'Rank ICIR': 0.308}, 'data_train_vec': ['2023-03-20', '2025-06-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.308', 'weight': '0.084'}

	Recorder: 4052e2df3a534953a8601ed597ca1697

		Model: {'id': '4052e2df3a534953a8601ed597ca1697', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.132, 'Rank IC': 0.013, 'Rank ICIR': 0.119}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.119', 'weight': '0.033'}

	Recorder: 860c8e8085bb4ea58f3ec854bdf745a1

		Model: {'id': '860c8e8085bb4ea58f3ec854bdf745a1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.163, 'Rank IC': 0.033, 'Rank ICIR': 0.313}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.313', 'weight': '0.086'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260320_13 718286857426159819 (Recorders: 2/5)

	Recorder: 8eb5cba1908e43b0b06c530eb654c64c

		Model: {'id': '8eb5cba1908e43b0b06c530eb654c64c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.103, 'Rank IC': 0.037, 'Rank ICIR': 0.28}, 'data_train_vec': ['2024-03-20', '2025-09-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.280', 'weight': '0.077'}

	Recorder: 15545fb263f54d1bb8c0174b2cdd32be

		Model: {'id': '15545fb263f54d1bb8c0174b2cdd32be', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.192, 'Rank IC': 0.041, 'Rank ICIR': 0.488}, 'data_train_vec': ['2025-03-20', '2025-12-19'], 'train_time_vec': ['2026-03-20', '2026-03-20'], 'rank_icir': '0.488', 'weight': '0.133'}
