# params 
 {'predict_dates': [{'start': '2026-05-15', 'end': '2026-05-15'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260515_11 957156653529755883 (Recorders: 6/6)

	Recorder: f2f4b18cf793431ebf52ec8fdf3b3cca

		Model: {'id': 'f2f4b18cf793431ebf52ec8fdf3b3cca', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.372, 'Rank IC': 0.06, 'Rank ICIR': 0.399}, 'data_train_vec': ['2020-05-15', '2024-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.399', 'recency_weight': '0.122', 'weight': '0.021'}

	Recorder: 79a28c68d37c4858a6883562c6709639

		Model: {'id': '79a28c68d37c4858a6883562c6709639', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.193, 'Rank IC': 0.043, 'Rank ICIR': 0.285}, 'data_train_vec': ['2021-05-15', '2025-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.285', 'recency_weight': '0.173', 'weight': '0.015'}

	Recorder: adbdd9533c8c478394bb702178099111

		Model: {'id': 'adbdd9533c8c478394bb702178099111', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.236, 'Rank IC': 0.054, 'Rank ICIR': 0.334}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.334', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 5fdbe753167e48d997ac9a75e4c7f2d7

		Model: {'id': '5fdbe753167e48d997ac9a75e4c7f2d7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.252, 'Rank IC': 0.045, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.290', 'recency_weight': '0.348', 'weight': '0.031'}

	Recorder: 1ffc5fc79c764d44a6e7c89e4e4212aa

		Model: {'id': '1ffc5fc79c764d44a6e7c89e4e4212aa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.2, 'Rank IC': 0.049, 'Rank ICIR': 0.383}, 'data_train_vec': ['2024-05-15', '2025-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.383', 'recency_weight': '0.496', 'weight': '0.078'}

	Recorder: f999cd6ad9a44ae0bdd5ae3164a13a7c

		Model: {'id': 'f999cd6ad9a44ae0bdd5ae3164a13a7c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.468, 'Rank IC': 0.047, 'Rank ICIR': 0.331}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.331', 'recency_weight': '0.707', 'weight': '0.083'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260515_11 366925095207465342 (Recorders: 5/6)

	Recorder: 13527b12c85e4c259e4e825ec3d489ea

		Model: {'id': '13527b12c85e4c259e4e825ec3d489ea', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.315, 'Rank IC': 0.053, 'Rank ICIR': 0.339}, 'data_train_vec': ['2020-05-15', '2024-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.339', 'recency_weight': '0.122', 'weight': '0.015'}

	Recorder: c6f3af06c08945db976b2b89347e0364

		Model: {'id': 'c6f3af06c08945db976b2b89347e0364', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.148, 'Rank IC': 0.04, 'Rank ICIR': 0.261}, 'data_train_vec': ['2021-05-15', '2025-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.261', 'recency_weight': '0.173', 'weight': '0.013'}

	Recorder: 6615d1e4bf2b4b188cb6fa64ce49e33f

		Model: {'id': '6615d1e4bf2b4b188cb6fa64ce49e33f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.092, 'Rank IC': 0.044, 'Rank ICIR': 0.273}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.273', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: 9da6bf0e6b7848ada8714c917c0a241c

		Model: {'id': '9da6bf0e6b7848ada8714c917c0a241c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.081, 'Rank IC': 0.043, 'Rank ICIR': 0.346}, 'data_train_vec': ['2024-05-15', '2025-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.346', 'recency_weight': '0.496', 'weight': '0.063'}

	Recorder: 205be69eac0d433b9ac3cbf77a47fe00

		Model: {'id': '205be69eac0d433b9ac3cbf77a47fe00', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.498, 'Rank IC': 0.04, 'Rank ICIR': 0.371}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.371', 'recency_weight': '0.707', 'weight': '0.104'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260515_11 181587879423392213 (Recorders: 4/6)

	Recorder: 61e2bdc39b0f40cdb2525d1ab785b2f3

		Model: {'id': '61e2bdc39b0f40cdb2525d1ab785b2f3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.336, 'Rank IC': 0.058, 'Rank ICIR': 0.462}, 'data_train_vec': ['2020-05-15', '2024-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.462', 'recency_weight': '0.122', 'weight': '0.028'}

	Recorder: 6a32266b38bc4ebfb2940c3cee595752

		Model: {'id': '6a32266b38bc4ebfb2940c3cee595752', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.237, 'Rank IC': 0.052, 'Rank ICIR': 0.419}, 'data_train_vec': ['2021-05-15', '2025-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.419', 'recency_weight': '0.173', 'weight': '0.033'}

	Recorder: b3826e808d764398b95c1e62260509d5

		Model: {'id': 'b3826e808d764398b95c1e62260509d5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.157, 'Rank IC': 0.057, 'Rank ICIR': 0.376}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.376', 'recency_weight': '0.244', 'weight': '0.037'}

	Recorder: a8b98411066949f298fbc451bd5775cc

		Model: {'id': 'a8b98411066949f298fbc451bd5775cc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.432, 'Rank IC': 0.064, 'Rank ICIR': 0.394}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.394', 'recency_weight': '0.707', 'weight': '0.117'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260515_11 733549285704841875 (Recorders: 6/6)

	Recorder: 3e3edf05893f43ecbd367a0372a052d9

		Model: {'id': '3e3edf05893f43ecbd367a0372a052d9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.357, 'Rank IC': 0.055, 'Rank ICIR': 0.377}, 'data_train_vec': ['2020-05-15', '2024-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.377', 'recency_weight': '0.122', 'weight': '0.018'}

	Recorder: cfd300e464ab44fda520ab73a42176b7

		Model: {'id': 'cfd300e464ab44fda520ab73a42176b7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.112, 'Rank IC': 0.039, 'Rank ICIR': 0.275}, 'data_train_vec': ['2021-05-15', '2025-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.275', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 60e7c5a3a8d94527b9db2ffb9cd3fd6b

		Model: {'id': '60e7c5a3a8d94527b9db2ffb9cd3fd6b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.236, 'Rank IC': 0.06, 'Rank ICIR': 0.371}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.371', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 521bc26088eb4c5eb49ea928e9b5ea5e

		Model: {'id': '521bc26088eb4c5eb49ea928e9b5ea5e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.222, 'Rank IC': 0.047, 'Rank ICIR': 0.295}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.295', 'recency_weight': '0.348', 'weight': '0.032'}

	Recorder: 6940c31e3f0c4f1f92090d97bfdeb175

		Model: {'id': '6940c31e3f0c4f1f92090d97bfdeb175', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.226, 'Rank IC': 0.045, 'Rank ICIR': 0.412}, 'data_train_vec': ['2024-05-15', '2025-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.412', 'recency_weight': '0.496', 'weight': '0.090'}

	Recorder: 10d94426325442b98051b93c6078a506

		Model: {'id': '10d94426325442b98051b93c6078a506', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.611, 'Rank IC': 0.052, 'Rank ICIR': 0.405}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.405', 'recency_weight': '0.707', 'weight': '0.124'}
