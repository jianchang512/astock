# params 
 {'predict_dates': [{'start': '2026-04-13', 'end': '2026-04-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260413_15 760712185588248346 (Recorders: 3/5)

	Recorder: 982ac944de8e4c029cae0369bbe85b9b

		Model: {'id': '982ac944de8e4c029cae0369bbe85b9b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.28, 'Rank IC': 0.046, 'Rank ICIR': 0.316}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.316', 'recency_weight': '0.347', 'weight': '0.080'}

	Recorder: 42d3d1b5e65b4ed3ab10e519b82a8fb4

		Model: {'id': '42d3d1b5e65b4ed3ab10e519b82a8fb4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.224, 'Rank IC': 0.051, 'Rank ICIR': 0.411}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.411', 'recency_weight': '0.494', 'weight': '0.194'}

	Recorder: 56918149cd93454d80b3b851c9ef6bc6

		Model: {'id': '56918149cd93454d80b3b851c9ef6bc6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.362, 'Rank IC': 0.043, 'Rank ICIR': 0.345}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.345', 'recency_weight': '0.704', 'weight': '0.194'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260413_14 743598124308725305 (Recorders: 1/5)

	Recorder: 23045fd1faa348e48f69cf53b596f964

		Model: {'id': '23045fd1faa348e48f69cf53b596f964', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.203, 'Rank IC': 0.036, 'Rank ICIR': 0.223}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.223', 'recency_weight': '0.704', 'weight': '0.081'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260413_12 717265142007781587 (Recorders: 2/5)

	Recorder: 4729658e3167454582a01c2139cdb096

		Model: {'id': '4729658e3167454582a01c2139cdb096', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.09, 'Rank IC': 0.048, 'Rank ICIR': 0.283}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.283', 'recency_weight': '0.347', 'weight': '0.064'}

	Recorder: 423c1863974f4d41badeffed1823f298

		Model: {'id': '423c1863974f4d41badeffed1823f298', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.141, 'Rank IC': 0.024, 'Rank ICIR': 0.202}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.202', 'recency_weight': '0.494', 'weight': '0.047'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260413_12 747818527580104306 (Recorders: 3/5)

	Recorder: 554438f2516749abb02843e8f498acd7

		Model: {'id': '554438f2516749abb02843e8f498acd7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.1, 'Rank IC': 0.037, 'Rank ICIR': 0.321}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.321', 'recency_weight': '0.347', 'weight': '0.083'}

	Recorder: 20b33d3602b4470dbfe063764db9370a

		Model: {'id': '20b33d3602b4470dbfe063764db9370a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.115, 'Rank IC': 0.02, 'Rank ICIR': 0.172}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.172', 'recency_weight': '0.494', 'weight': '0.034'}

	Recorder: ff80bd39d7334276afe959d2298c7ae2

		Model: {'id': 'ff80bd39d7334276afe959d2298c7ae2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.022, 'Rank ICIR': 0.138}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.138', 'recency_weight': '0.704', 'weight': '0.031'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260413_12 270524456778855248 (Recorders: 3/5)

	Recorder: 68aebf82a130465fb61fce01e12a8c30

		Model: {'id': '68aebf82a130465fb61fce01e12a8c30', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.124, 'Rank IC': 0.037, 'Rank ICIR': 0.226}, 'data_train_vec': ['2023-04-13', '2025-07-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.226', 'recency_weight': '0.347', 'weight': '0.041'}

	Recorder: 63974fcb4d654933b7d582d6484f57e2

		Model: {'id': '63974fcb4d654933b7d582d6484f57e2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.161, 'Rank IC': 0.041, 'Rank ICIR': 0.351}, 'data_train_vec': ['2024-04-13', '2025-10-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.351', 'recency_weight': '0.494', 'weight': '0.141'}

	Recorder: a8d75421652643ac96ad6dec766f9d87

		Model: {'id': 'a8d75421652643ac96ad6dec766f9d87', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.121, 'Rank IC': 0.012, 'Rank ICIR': 0.076}, 'data_train_vec': ['2025-04-13', '2026-01-12'], 'train_time_vec': ['2026-04-13', '2026-04-13'], 'rank_icir': '0.076', 'recency_weight': '0.704', 'weight': '0.009'}
