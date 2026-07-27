# params 
 {'predict_dates': [{'start': '2026-07-27', 'end': '2026-07-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260727_14 980767635556148087 (Recorders: 5/6)

	Recorder: 4ad1c42903e34a9bb230e237b09ee47e

		Model: {'id': '4ad1c42903e34a9bb230e237b09ee47e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.345, 'Rank IC': 0.066, 'Rank ICIR': 0.42}, 'data_train_vec': ['2020-07-27', '2025-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.420', 'recency_weight': '0.122', 'weight': '0.043'}

	Recorder: b50773b62fd4473a8c325626d963c724

		Model: {'id': 'b50773b62fd4473a8c325626d963c724', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.185, 'Rank IC': 0.063, 'Rank ICIR': 0.373}, 'data_train_vec': ['2021-07-27', '2025-04-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.373', 'recency_weight': '0.172', 'weight': '0.048'}

	Recorder: 6a0f6078febb4676baa4ca99a7ee636f

		Model: {'id': '6a0f6078febb4676baa4ca99a7ee636f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.166, 'Rank IC': 0.059, 'Rank ICIR': 0.35}, 'data_train_vec': ['2022-07-27', '2025-07-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.350', 'recency_weight': '0.244', 'weight': '0.061'}

	Recorder: a8a550abb5b84d6da2c8472a98921952

		Model: {'id': 'a8a550abb5b84d6da2c8472a98921952', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.114, 'Rank IC': 0.067, 'Rank ICIR': 0.4}, 'data_train_vec': ['2023-07-27', '2025-10-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.400', 'recency_weight': '0.348', 'weight': '0.113'}

	Recorder: aa65c60831b24bfab74611cf1ff575d0

		Model: {'id': 'aa65c60831b24bfab74611cf1ff575d0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.098, 'Rank IC': 0.032, 'Rank ICIR': 0.171}, 'data_train_vec': ['2024-07-27', '2026-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.171', 'recency_weight': '0.496', 'weight': '0.029'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260727_14 739686777148129427 (Recorders: 5/6)

	Recorder: 3ecc8aabcd1c4c16b9823b9bf64bd05d

		Model: {'id': '3ecc8aabcd1c4c16b9823b9bf64bd05d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.322, 'Rank IC': 0.069, 'Rank ICIR': 0.428}, 'data_train_vec': ['2020-07-27', '2025-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.428', 'recency_weight': '0.122', 'weight': '0.045'}

	Recorder: 31164e61dee0466d9d44190a30ef5cb2

		Model: {'id': '31164e61dee0466d9d44190a30ef5cb2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.212, 'Rank IC': 0.06, 'Rank ICIR': 0.388}, 'data_train_vec': ['2021-07-27', '2025-04-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.388', 'recency_weight': '0.172', 'weight': '0.052'}

	Recorder: 1608e393f6b54bd4920c926151dbadf2

		Model: {'id': '1608e393f6b54bd4920c926151dbadf2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.164, 'Rank IC': 0.056, 'Rank ICIR': 0.352}, 'data_train_vec': ['2022-07-27', '2025-07-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.352', 'recency_weight': '0.244', 'weight': '0.061'}

	Recorder: b651708ff94d4a0b875d62eddb6bcd86

		Model: {'id': 'b651708ff94d4a0b875d62eddb6bcd86', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.253, 'Rank IC': 0.07, 'Rank ICIR': 0.437}, 'data_train_vec': ['2023-07-27', '2025-10-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.437', 'recency_weight': '0.348', 'weight': '0.135'}

	Recorder: f3485a9546bd4ed2a15c9336951d7abd

		Model: {'id': 'f3485a9546bd4ed2a15c9336951d7abd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.175, 'Rank IC': 0.03, 'Rank ICIR': 0.153}, 'data_train_vec': ['2024-07-27', '2026-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.153', 'recency_weight': '0.496', 'weight': '0.024'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260727_14 323285494788498309 (Recorders: 5/6)

	Recorder: e47ecf22ef9a436fa398e3964fa7d5d4

		Model: {'id': 'e47ecf22ef9a436fa398e3964fa7d5d4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.216, 'Rank IC': 0.054, 'Rank ICIR': 0.332}, 'data_train_vec': ['2020-07-27', '2025-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.332', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: bd375c134d1449b584a18c6b55360ec9

		Model: {'id': 'bd375c134d1449b584a18c6b55360ec9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.095, 'Rank IC': 0.045, 'Rank ICIR': 0.271}, 'data_train_vec': ['2021-07-27', '2025-04-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.271', 'recency_weight': '0.172', 'weight': '0.026'}

	Recorder: 4da7ffeba76b45f395251b9976f75470

		Model: {'id': '4da7ffeba76b45f395251b9976f75470', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.112, 'Rank IC': 0.048, 'Rank ICIR': 0.308}, 'data_train_vec': ['2022-07-27', '2025-07-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.308', 'recency_weight': '0.244', 'weight': '0.047'}

	Recorder: 6d6219862050466a98a99f9c009d69e0

		Model: {'id': '6d6219862050466a98a99f9c009d69e0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.227, 'Rank IC': 0.056, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-07-27', '2025-10-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.327', 'recency_weight': '0.348', 'weight': '0.075'}

	Recorder: 86e4de9a395b4543b87a20950284b40d

		Model: {'id': '86e4de9a395b4543b87a20950284b40d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.097, 'Rank IC': 0.016, 'Rank ICIR': 0.077}, 'data_train_vec': ['2024-07-27', '2026-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.077', 'recency_weight': '0.496', 'weight': '0.006'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260727_14 645219090327610512 (Recorders: 4/6)

	Recorder: 5623588085794fa2b3c0623478426cc3

		Model: {'id': '5623588085794fa2b3c0623478426cc3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.311, 'Rank IC': 0.07, 'Rank ICIR': 0.469}, 'data_train_vec': ['2020-07-27', '2025-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.469', 'recency_weight': '0.122', 'weight': '0.054'}

	Recorder: 74e6bbdc51b24b8d8a8f80121b8e31e4

		Model: {'id': '74e6bbdc51b24b8d8a8f80121b8e31e4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.151, 'Rank IC': 0.062, 'Rank ICIR': 0.386}, 'data_train_vec': ['2021-07-27', '2025-04-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.386', 'recency_weight': '0.172', 'weight': '0.052'}

	Recorder: 2809a33f3862498cac3f944dd392b0f4

		Model: {'id': '2809a33f3862498cac3f944dd392b0f4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.134, 'Rank IC': 0.058, 'Rank ICIR': 0.378}, 'data_train_vec': ['2022-07-27', '2025-07-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.378', 'recency_weight': '0.244', 'weight': '0.071'}

	Recorder: 7e3f17c37ff346eabb3256edd3dbc50f

		Model: {'id': '7e3f17c37ff346eabb3256edd3dbc50f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.099, 'Rank IC': 0.033, 'Rank ICIR': 0.173}, 'data_train_vec': ['2024-07-27', '2026-01-26'], 'train_time_vec': ['2026-07-27', '2026-07-27'], 'rank_icir': '0.173', 'recency_weight': '0.496', 'weight': '0.030'}
