# params 
 {'predict_dates': [{'start': '2026-04-17', 'end': '2026-04-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260418_14 913140788957071809 (Recorders: 6/6)

	Recorder: 568bffd3add54f42bc0a2e395216d94e

		Model: {'id': '568bffd3add54f42bc0a2e395216d94e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.427, 'Rank IC': 0.062, 'Rank ICIR': 0.358}, 'data_train_vec': ['2020-04-18', '2024-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.358', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 9eac1e9617b941a58b60de77aa6fb9f2

		Model: {'id': '9eac1e9617b941a58b60de77aa6fb9f2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.307, 'Rank IC': 0.049, 'Rank ICIR': 0.319}, 'data_train_vec': ['2021-04-18', '2025-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.319', 'recency_weight': '0.173', 'weight': '0.021'}

	Recorder: 1b8d7ae3ee1f4ef9b31ac8f284ebf2dc

		Model: {'id': '1b8d7ae3ee1f4ef9b31ac8f284ebf2dc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.205, 'Rank IC': 0.036, 'Rank ICIR': 0.224}, 'data_train_vec': ['2022-04-18', '2025-04-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.224', 'recency_weight': '0.245', 'weight': '0.015'}

	Recorder: 97b68c15d522445caf37eb095f409b37

		Model: {'id': '97b68c15d522445caf37eb095f409b37', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.379, 'Rank IC': 0.071, 'Rank ICIR': 0.453}, 'data_train_vec': ['2023-04-18', '2025-07-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.453', 'recency_weight': '0.348', 'weight': '0.086'}

	Recorder: 58851c55c30a4bb1a4383e088ae9ae44

		Model: {'id': '58851c55c30a4bb1a4383e088ae9ae44', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.27, 'Rank IC': 0.034, 'Rank ICIR': 0.248}, 'data_train_vec': ['2024-04-18', '2025-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.248', 'recency_weight': '0.496', 'weight': '0.037'}

	Recorder: 24326c44e4d24609bd958766ca2e38e2

		Model: {'id': '24326c44e4d24609bd958766ca2e38e2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.379, 'Rank IC': 0.062, 'Rank ICIR': 0.331}, 'data_train_vec': ['2025-04-18', '2026-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.331', 'recency_weight': '0.707', 'weight': '0.093'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260418_13 575416186162685727 (Recorders: 6/6)

	Recorder: 98f749e80a174d0c9e041a8a657a7c2b

		Model: {'id': '98f749e80a174d0c9e041a8a657a7c2b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.369, 'Rank IC': 0.058, 'Rank ICIR': 0.329}, 'data_train_vec': ['2020-04-18', '2024-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.329', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 40089daac1b94aecbb4aa09dbfcc137c

		Model: {'id': '40089daac1b94aecbb4aa09dbfcc137c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.264, 'Rank IC': 0.05, 'Rank ICIR': 0.32}, 'data_train_vec': ['2021-04-18', '2025-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.320', 'recency_weight': '0.173', 'weight': '0.021'}

	Recorder: a2124184f7374035b06cd9a6c877d41b

		Model: {'id': 'a2124184f7374035b06cd9a6c877d41b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.102, 'Rank IC': 0.036, 'Rank ICIR': 0.211}, 'data_train_vec': ['2022-04-18', '2025-04-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.211', 'recency_weight': '0.245', 'weight': '0.013'}

	Recorder: 166fd8af42b447f08b7e1d84f5560b06

		Model: {'id': '166fd8af42b447f08b7e1d84f5560b06', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.184, 'Rank IC': 0.068, 'Rank ICIR': 0.431}, 'data_train_vec': ['2023-04-18', '2025-07-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.431', 'recency_weight': '0.348', 'weight': '0.078'}

	Recorder: 8ff8e9a58611496dafe20623abec5bad

		Model: {'id': '8ff8e9a58611496dafe20623abec5bad', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.169, 'Rank IC': 0.037, 'Rank ICIR': 0.285}, 'data_train_vec': ['2024-04-18', '2025-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.285', 'recency_weight': '0.496', 'weight': '0.049'}

	Recorder: 759801d96fca4515ae887933236e7df1

		Model: {'id': '759801d96fca4515ae887933236e7df1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.373, 'Rank IC': 0.061, 'Rank ICIR': 0.336}, 'data_train_vec': ['2025-04-18', '2026-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.336', 'recency_weight': '0.707', 'weight': '0.096'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260418_13 366576475066397522 (Recorders: 5/6)

	Recorder: 107cabf2f13a451c95ebea81386dac80

		Model: {'id': '107cabf2f13a451c95ebea81386dac80', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.366, 'Rank IC': 0.061, 'Rank ICIR': 0.446}, 'data_train_vec': ['2020-04-18', '2024-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.446', 'recency_weight': '0.122', 'weight': '0.029'}

	Recorder: 95e3573e090e4c0999de1df83df581ec

		Model: {'id': '95e3573e090e4c0999de1df83df581ec', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.299, 'Rank IC': 0.052, 'Rank ICIR': 0.447}, 'data_train_vec': ['2021-04-18', '2025-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.447', 'recency_weight': '0.173', 'weight': '0.042'}

	Recorder: ac28334f8b094148bfa9ae016fcc07ef

		Model: {'id': 'ac28334f8b094148bfa9ae016fcc07ef', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.175, 'Rank IC': 0.049, 'Rank ICIR': 0.329}, 'data_train_vec': ['2022-04-18', '2025-04-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.329', 'recency_weight': '0.245', 'weight': '0.032'}

	Recorder: 51b6aa16ed644359ba624d5be94da4f9

		Model: {'id': '51b6aa16ed644359ba624d5be94da4f9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.132, 'Rank IC': 0.039, 'Rank ICIR': 0.297}, 'data_train_vec': ['2023-04-18', '2025-07-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.297', 'recency_weight': '0.348', 'weight': '0.037'}

	Recorder: e05845122d10409a85e774e2f6a7a7cc

		Model: {'id': 'e05845122d10409a85e774e2f6a7a7cc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.238, 'Rank IC': 0.035, 'Rank ICIR': 0.187}, 'data_train_vec': ['2025-04-18', '2026-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.187', 'recency_weight': '0.707', 'weight': '0.030'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260418_13 679151333797904547 (Recorders: 6/6)

	Recorder: 0847ace834514e90bc8090612f4f7e5a

		Model: {'id': '0847ace834514e90bc8090612f4f7e5a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.394, 'Rank IC': 0.064, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-04-18', '2024-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.383', 'recency_weight': '0.122', 'weight': '0.022'}

	Recorder: d95477158e444c168728aebc51d6c32c

		Model: {'id': 'd95477158e444c168728aebc51d6c32c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.292, 'Rank IC': 0.05, 'Rank ICIR': 0.336}, 'data_train_vec': ['2021-04-18', '2025-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.336', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: 670e05f7f3954f1780baaa324c71a7b2

		Model: {'id': '670e05f7f3954f1780baaa324c71a7b2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.203, 'Rank IC': 0.043, 'Rank ICIR': 0.272}, 'data_train_vec': ['2022-04-18', '2025-04-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.272', 'recency_weight': '0.245', 'weight': '0.022'}

	Recorder: cd7d9403580b40d8927e90855bedb172

		Model: {'id': 'cd7d9403580b40d8927e90855bedb172', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.224, 'Rank IC': 0.065, 'Rank ICIR': 0.436}, 'data_train_vec': ['2023-04-18', '2025-07-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.436', 'recency_weight': '0.348', 'weight': '0.080'}

	Recorder: ca8fbd4d7484425981be57b08068b56b

		Model: {'id': 'ca8fbd4d7484425981be57b08068b56b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.195, 'Rank IC': 0.029, 'Rank ICIR': 0.241}, 'data_train_vec': ['2024-04-18', '2025-10-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.241', 'recency_weight': '0.496', 'weight': '0.035'}

	Recorder: 28bc841ae51444798d4102cff249e838

		Model: {'id': '28bc841ae51444798d4102cff249e838', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.288, 'Rank IC': 0.062, 'Rank ICIR': 0.35}, 'data_train_vec': ['2025-04-18', '2026-01-17'], 'train_time_vec': ['2026-04-18', '2026-04-18'], 'rank_icir': '0.350', 'recency_weight': '0.707', 'weight': '0.104'}
