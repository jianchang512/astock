# params 
 {'predict_dates': [{'start': '2026-07-14', 'end': '2026-07-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260714_16 511778332042549976 (Recorders: 6/6)

	Recorder: 423ccc01a25e4dc7acd396d993f458ed

		Model: {'id': '423ccc01a25e4dc7acd396d993f458ed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.365, 'Rank IC': 0.069, 'Rank ICIR': 0.462}, 'data_train_vec': ['2020-07-14', '2025-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.462', 'recency_weight': '0.122', 'weight': '0.037'}

	Recorder: 241de723fcfa4f729e2b4eac4e0371f0

		Model: {'id': '241de723fcfa4f729e2b4eac4e0371f0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.178, 'Rank IC': 0.065, 'Rank ICIR': 0.377}, 'data_train_vec': ['2021-07-14', '2025-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.377', 'recency_weight': '0.172', 'weight': '0.035'}

	Recorder: c6bfe7f79c1b464cb077ef4db7bb41a8

		Model: {'id': 'c6bfe7f79c1b464cb077ef4db7bb41a8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.154, 'Rank IC': 0.064, 'Rank ICIR': 0.383}, 'data_train_vec': ['2022-07-14', '2025-07-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.383', 'recency_weight': '0.244', 'weight': '0.052'}

	Recorder: 69b97c22fc144b628548b9c9fd61027f

		Model: {'id': '69b97c22fc144b628548b9c9fd61027f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.23, 'Rank IC': 0.065, 'Rank ICIR': 0.418}, 'data_train_vec': ['2023-07-14', '2025-10-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.418', 'recency_weight': '0.348', 'weight': '0.087'}

	Recorder: 095d868a0bd14f9890cadaba088bab9b

		Model: {'id': '095d868a0bd14f9890cadaba088bab9b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.219, 'Rank IC': 0.041, 'Rank ICIR': 0.277}, 'data_train_vec': ['2024-07-14', '2026-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.277', 'recency_weight': '0.496', 'weight': '0.055'}

	Recorder: 97c80c2b27d74834973c4e7c14d75bca

		Model: {'id': '97c80c2b27d74834973c4e7c14d75bca', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.173, 'Rank IC': 0.013, 'Rank ICIR': 0.066}, 'data_train_vec': ['2025-07-14', '2026-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.066', 'recency_weight': '0.702', 'weight': '0.004'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260714_16 473914208564591653 (Recorders: 6/6)

	Recorder: e6bbdd2acce14ba1bd0b1720a073becd

		Model: {'id': 'e6bbdd2acce14ba1bd0b1720a073becd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.323, 'Rank IC': 0.066, 'Rank ICIR': 0.431}, 'data_train_vec': ['2020-07-14', '2025-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.431', 'recency_weight': '0.122', 'weight': '0.033'}

	Recorder: d4494ed7322949fb9c38973af0d36e4c

		Model: {'id': 'd4494ed7322949fb9c38973af0d36e4c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.203, 'Rank IC': 0.059, 'Rank ICIR': 0.361}, 'data_train_vec': ['2021-07-14', '2025-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.361', 'recency_weight': '0.172', 'weight': '0.032'}

	Recorder: c4720129bf9140478abcb9f09137ffa3

		Model: {'id': 'c4720129bf9140478abcb9f09137ffa3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.166, 'Rank IC': 0.065, 'Rank ICIR': 0.424}, 'data_train_vec': ['2022-07-14', '2025-07-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.424', 'recency_weight': '0.244', 'weight': '0.063'}

	Recorder: 9f830d0b57b24e1694053d8363fee33c

		Model: {'id': '9f830d0b57b24e1694053d8363fee33c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.27, 'Rank IC': 0.069, 'Rank ICIR': 0.48}, 'data_train_vec': ['2023-07-14', '2025-10-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.480', 'recency_weight': '0.348', 'weight': '0.115'}

	Recorder: eadf2639aff64fe180b3231ad7179a67

		Model: {'id': 'eadf2639aff64fe180b3231ad7179a67', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.254, 'Rank IC': 0.032, 'Rank ICIR': 0.226}, 'data_train_vec': ['2024-07-14', '2026-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.226', 'recency_weight': '0.496', 'weight': '0.036'}

	Recorder: 74452a28d7da4dddaf5f7be49ba92047

		Model: {'id': '74452a28d7da4dddaf5f7be49ba92047', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.162, 'Rank IC': 0.02, 'Rank ICIR': 0.096}, 'data_train_vec': ['2025-07-14', '2026-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.096', 'recency_weight': '0.702', 'weight': '0.009'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260714_15 184382615933388608 (Recorders: 6/6)

	Recorder: babdc49a94d34970956b08b4b4e27b2a

		Model: {'id': 'babdc49a94d34970956b08b4b4e27b2a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.251, 'Rank IC': 0.057, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-07-14', '2025-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.383', 'recency_weight': '0.122', 'weight': '0.026'}

	Recorder: 1328819bcaa74c138d76faf1c5f4febc

		Model: {'id': '1328819bcaa74c138d76faf1c5f4febc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.085, 'Rank IC': 0.044, 'Rank ICIR': 0.276}, 'data_train_vec': ['2021-07-14', '2025-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.276', 'recency_weight': '0.172', 'weight': '0.019'}

	Recorder: 94c5444d0af8401481e7328606ab6a8d

		Model: {'id': '94c5444d0af8401481e7328606ab6a8d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.062, 'Rank IC': 0.045, 'Rank ICIR': 0.304}, 'data_train_vec': ['2022-07-14', '2025-07-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.304', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: 50d46a614b8542eab7ea8f50e05adb41

		Model: {'id': '50d46a614b8542eab7ea8f50e05adb41', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.202, 'Rank IC': 0.05, 'Rank ICIR': 0.359}, 'data_train_vec': ['2023-07-14', '2025-10-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.359', 'recency_weight': '0.348', 'weight': '0.065'}

	Recorder: 5a354da814db4b59bd41bbab4d94a604

		Model: {'id': '5a354da814db4b59bd41bbab4d94a604', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.14, 'Rank IC': 0.021, 'Rank ICIR': 0.129}, 'data_train_vec': ['2024-07-14', '2026-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.129', 'recency_weight': '0.496', 'weight': '0.012'}

	Recorder: 3bcbec5ba4fe42e2b7533fde5b9074ea

		Model: {'id': '3bcbec5ba4fe42e2b7533fde5b9074ea', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.192, 'Rank IC': 0.028, 'Rank ICIR': 0.148}, 'data_train_vec': ['2025-07-14', '2026-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.148', 'recency_weight': '0.702', 'weight': '0.022'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260714_15 463538514328106878 (Recorders: 6/6)

	Recorder: 8076437d85ac45fb81d5db032eb108b5

		Model: {'id': '8076437d85ac45fb81d5db032eb108b5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.331, 'Rank IC': 0.065, 'Rank ICIR': 0.451}, 'data_train_vec': ['2020-07-14', '2025-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.451', 'recency_weight': '0.122', 'weight': '0.036'}

	Recorder: 7e58698510cc41d291e9a67caa4fe958

		Model: {'id': '7e58698510cc41d291e9a67caa4fe958', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.144, 'Rank IC': 0.06, 'Rank ICIR': 0.375}, 'data_train_vec': ['2021-07-14', '2025-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.375', 'recency_weight': '0.172', 'weight': '0.035'}

	Recorder: 0f0d56687a8a46c49df6987b09a8a952

		Model: {'id': '0f0d56687a8a46c49df6987b09a8a952', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.177, 'Rank IC': 0.07, 'Rank ICIR': 0.439}, 'data_train_vec': ['2022-07-14', '2025-07-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.439', 'recency_weight': '0.244', 'weight': '0.068'}

	Recorder: 8161f1e088ae4e9a82e3cd5cde730f10

		Model: {'id': '8161f1e088ae4e9a82e3cd5cde730f10', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.18, 'Rank IC': 0.061, 'Rank ICIR': 0.412}, 'data_train_vec': ['2023-07-14', '2025-10-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.412', 'recency_weight': '0.348', 'weight': '0.085'}

	Recorder: 9a798dac6794479db4f04666bd8d44e5

		Model: {'id': '9a798dac6794479db4f04666bd8d44e5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.149, 'Rank IC': 0.026, 'Rank ICIR': 0.185}, 'data_train_vec': ['2024-07-14', '2026-01-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.185', 'recency_weight': '0.496', 'weight': '0.024'}

	Recorder: df3844f2a7f74b8f9f8891556df110d6

		Model: {'id': 'df3844f2a7f74b8f9f8891556df110d6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.179, 'Rank IC': 0.024, 'Rank ICIR': 0.131}, 'data_train_vec': ['2025-07-14', '2026-04-13'], 'train_time_vec': ['2026-07-14', '2026-07-14'], 'rank_icir': '0.131', 'recency_weight': '0.702', 'weight': '0.017'}
