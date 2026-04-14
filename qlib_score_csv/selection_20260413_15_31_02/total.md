# params 
 {'predict_dates': [{'start': '2026-04-13', 'end': '2026-04-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260413_15 760712185588248346 (Recorders: 3/5)

	Recorder: 982ac944de8e4c029cae0369bbe85b9b

		Model: {'id': '982ac944de8e4c029cae0369bbe85b9b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.28, 'Rank IC': 0.046, 'Rank ICIR': 0.316}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.316', 'weight': '0.089'}

	Recorder: 42d3d1b5e65b4ed3ab10e519b82a8fb4

		Model: {'id': '42d3d1b5e65b4ed3ab10e519b82a8fb4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.224, 'Rank IC': 0.051, 'Rank ICIR': 0.411}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.411', 'weight': '0.115'}

	Recorder: 56918149cd93454d80b3b851c9ef6bc6

		Model: {'id': '56918149cd93454d80b3b851c9ef6bc6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.362, 'Rank IC': 0.043, 'Rank ICIR': 0.345}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.345', 'weight': '0.097'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260413_14 743598124308725305 (Recorders: 2/5)

	Recorder: fb5a0509a69c498ea4fdc87839b57114

		Model: {'id': 'fb5a0509a69c498ea4fdc87839b57114', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.108, 'Rank IC': 0.017, 'Rank ICIR': 0.141}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.141', 'weight': '0.040'}

	Recorder: 23045fd1faa348e48f69cf53b596f964

		Model: {'id': '23045fd1faa348e48f69cf53b596f964', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.203, 'Rank IC': 0.036, 'Rank ICIR': 0.223}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.223', 'weight': '0.063'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260413_12 717265142007781587 (Recorders: 4/5)

	Recorder: 941ccd7ca72748429d93c5c1ca9720bb

		Model: {'id': '941ccd7ca72748429d93c5c1ca9720bb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.042, 'Rank IC': 0.024, 'Rank ICIR': 0.141}, 'data_train_vec': ['2021-04-13', '2025-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.141', 'weight': '0.040'}

	Recorder: 4729658e3167454582a01c2139cdb096

		Model: {'id': '4729658e3167454582a01c2139cdb096', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.09, 'Rank IC': 0.048, 'Rank ICIR': 0.283}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.283', 'weight': '0.079'}

	Recorder: 423c1863974f4d41badeffed1823f298

		Model: {'id': '423c1863974f4d41badeffed1823f298', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.141, 'Rank IC': 0.024, 'Rank ICIR': 0.202}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.202', 'weight': '0.057'}

	Recorder: f13a0c77ba0848388649bfbb3675901f

		Model: {'id': 'f13a0c77ba0848388649bfbb3675901f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.073, 'Rank IC': 0.01, 'Rank ICIR': 0.058}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.058', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260413_12 747818527580104306 (Recorders: 4/5)

	Recorder: 3303cb2b53ca4b31837380b63cadf154

		Model: {'id': '3303cb2b53ca4b31837380b63cadf154', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.018, 'Rank ICIR': 0.16}, 'data_train_vec': ['2021-04-13', '2025-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.160', 'weight': '0.045'}

	Recorder: 554438f2516749abb02843e8f498acd7

		Model: {'id': '554438f2516749abb02843e8f498acd7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.1, 'Rank IC': 0.037, 'Rank ICIR': 0.321}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.321', 'weight': '0.090'}

	Recorder: 20b33d3602b4470dbfe063764db9370a

		Model: {'id': '20b33d3602b4470dbfe063764db9370a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.115, 'Rank IC': 0.02, 'Rank ICIR': 0.172}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.172', 'weight': '0.048'}

	Recorder: ff80bd39d7334276afe959d2298c7ae2

		Model: {'id': 'ff80bd39d7334276afe959d2298c7ae2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.022, 'Rank ICIR': 0.138}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.138', 'weight': '0.039'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260413_12 270524456778855248 (Recorders: 3/5)

	Recorder: 68aebf82a130465fb61fce01e12a8c30

		Model: {'id': '68aebf82a130465fb61fce01e12a8c30', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.124, 'Rank IC': 0.037, 'Rank ICIR': 0.226}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.226', 'weight': '0.063'}

	Recorder: 63974fcb4d654933b7d582d6484f57e2

		Model: {'id': '63974fcb4d654933b7d582d6484f57e2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.161, 'Rank IC': 0.041, 'Rank ICIR': 0.351}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.351', 'weight': '0.098'}

	Recorder: a8d75421652643ac96ad6dec766f9d87

		Model: {'id': 'a8d75421652643ac96ad6dec766f9d87', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.121, 'Rank IC': 0.012, 'Rank ICIR': 0.076}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.076', 'weight': '0.021'}
