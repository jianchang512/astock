# params 
 {'predict_dates': [{'start': '2026-04-23', 'end': '2026-04-23'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260423_14 375896224480390406 (Recorders: 6/6)

	Recorder: 7320c53328ce4bbaaa184fd26bb19dd1

		Model: {'id': '7320c53328ce4bbaaa184fd26bb19dd1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.396, 'Rank IC': 0.059, 'Rank ICIR': 0.359}, 'data_train_vec': ['2020-04-23', '2024-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.359', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 57185fe2e3114af592b5dde7eaad3080

		Model: {'id': '57185fe2e3114af592b5dde7eaad3080', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.264, 'Rank IC': 0.048, 'Rank ICIR': 0.314}, 'data_train_vec': ['2021-04-23', '2025-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.314', 'recency_weight': '0.173', 'weight': '0.015'}

	Recorder: 588dd32b90f34ff2ab22ef305eb58503

		Model: {'id': '588dd32b90f34ff2ab22ef305eb58503', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.171, 'Rank IC': 0.044, 'Rank ICIR': 0.27}, 'data_train_vec': ['2022-04-23', '2025-04-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.270', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: a7a995c25d5f4b10bff1fdaebc8880f6

		Model: {'id': 'a7a995c25d5f4b10bff1fdaebc8880f6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.263, 'Rank IC': 0.056, 'Rank ICIR': 0.333}, 'data_train_vec': ['2023-04-23', '2025-07-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.333', 'recency_weight': '0.347', 'weight': '0.035'}

	Recorder: 9ba0df9b5159456099a29f26aef5d874

		Model: {'id': '9ba0df9b5159456099a29f26aef5d874', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.099, 'Rank IC': 0.026, 'Rank ICIR': 0.19}, 'data_train_vec': ['2024-04-23', '2025-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.190', 'recency_weight': '0.494', 'weight': '0.016'}

	Recorder: 06f2a51113f74c3f8295a498b7fb1af5

		Model: {'id': '06f2a51113f74c3f8295a498b7fb1af5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.079, 'ICIR': 0.545, 'Rank IC': 0.094, 'Rank ICIR': 0.593}, 'data_train_vec': ['2025-04-23', '2026-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.593', 'recency_weight': '0.704', 'weight': '0.223'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260423_14 270076199811670954 (Recorders: 6/6)

	Recorder: 334584bad12c4dfbb528d7ffd521280c

		Model: {'id': '334584bad12c4dfbb528d7ffd521280c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.322, 'Rank IC': 0.053, 'Rank ICIR': 0.304}, 'data_train_vec': ['2020-04-23', '2024-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.304', 'recency_weight': '0.121', 'weight': '0.010'}

	Recorder: 6f99f9057d0b4f009143330d59858af2

		Model: {'id': '6f99f9057d0b4f009143330d59858af2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.217, 'Rank IC': 0.046, 'Rank ICIR': 0.295}, 'data_train_vec': ['2021-04-23', '2025-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.295', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: b7f1ce57c3c445ff8032c840b58d296a

		Model: {'id': 'b7f1ce57c3c445ff8032c840b58d296a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.082, 'Rank IC': 0.039, 'Rank ICIR': 0.244}, 'data_train_vec': ['2022-04-23', '2025-04-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.244', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: fb73b5741ede421ba26a20975bfaef80

		Model: {'id': 'fb73b5741ede421ba26a20975bfaef80', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.136, 'Rank IC': 0.063, 'Rank ICIR': 0.374}, 'data_train_vec': ['2023-04-23', '2025-07-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.374', 'recency_weight': '0.347', 'weight': '0.044'}

	Recorder: a96123ff0e664678aadb87813abbdce2

		Model: {'id': 'a96123ff0e664678aadb87813abbdce2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.1, 'Rank IC': 0.03, 'Rank ICIR': 0.22}, 'data_train_vec': ['2024-04-23', '2025-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.220', 'recency_weight': '0.494', 'weight': '0.022'}

	Recorder: 92b213b6c7744ea3aa97cbce1f0ef87d

		Model: {'id': '92b213b6c7744ea3aa97cbce1f0ef87d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.575, 'Rank IC': 0.086, 'Rank ICIR': 0.565}, 'data_train_vec': ['2025-04-23', '2026-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.565', 'recency_weight': '0.704', 'weight': '0.202'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260423_14 321318253197958168 (Recorders: 5/6)

	Recorder: 67afb3988a3a49e7837f7ba29d7a7bc1

		Model: {'id': '67afb3988a3a49e7837f7ba29d7a7bc1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.355, 'Rank IC': 0.059, 'Rank ICIR': 0.435}, 'data_train_vec': ['2020-04-23', '2024-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.435', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: cccaf112a6a64a058ef68a36942226c8

		Model: {'id': 'cccaf112a6a64a058ef68a36942226c8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.247, 'Rank IC': 0.049, 'Rank ICIR': 0.411}, 'data_train_vec': ['2021-04-23', '2025-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.411', 'recency_weight': '0.173', 'weight': '0.026'}

	Recorder: eda93ced935047c397d62e0c2bb97f34

		Model: {'id': 'eda93ced935047c397d62e0c2bb97f34', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.18, 'Rank IC': 0.05, 'Rank ICIR': 0.353}, 'data_train_vec': ['2022-04-23', '2025-04-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.353', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 216a2ddcf9a749debc807036d159e155

		Model: {'id': '216a2ddcf9a749debc807036d159e155', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.096, 'Rank IC': 0.042, 'Rank ICIR': 0.312}, 'data_train_vec': ['2023-04-23', '2025-07-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.312', 'recency_weight': '0.347', 'weight': '0.030'}

	Recorder: 78ef3b7f29bf44dc816f0b005de4daf3

		Model: {'id': '78ef3b7f29bf44dc816f0b005de4daf3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.377, 'Rank IC': 0.05, 'Rank ICIR': 0.314}, 'data_train_vec': ['2025-04-23', '2026-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.314', 'recency_weight': '0.704', 'weight': '0.062'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260423_14 887011854681363430 (Recorders: 6/6)

	Recorder: 42ce05291c1e43418e6356981de019bc

		Model: {'id': '42ce05291c1e43418e6356981de019bc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.344, 'Rank IC': 0.053, 'Rank ICIR': 0.322}, 'data_train_vec': ['2020-04-23', '2024-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.322', 'recency_weight': '0.121', 'weight': '0.011'}

	Recorder: 73bdc9571fbb4af9ad7e0154515b371d

		Model: {'id': '73bdc9571fbb4af9ad7e0154515b371d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.194, 'Rank IC': 0.045, 'Rank ICIR': 0.3}, 'data_train_vec': ['2021-04-23', '2025-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.300', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 941a26f5ad504362b67e2742c1b6ebdc

		Model: {'id': '941a26f5ad504362b67e2742c1b6ebdc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.19, 'Rank IC': 0.045, 'Rank ICIR': 0.278}, 'data_train_vec': ['2022-04-23', '2025-04-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.278', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: 05d30ea93780473db4bcb74f02e02cbc

		Model: {'id': '05d30ea93780473db4bcb74f02e02cbc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.264, 'Rank IC': 0.068, 'Rank ICIR': 0.41}, 'data_train_vec': ['2023-04-23', '2025-07-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.410', 'recency_weight': '0.347', 'weight': '0.052'}

	Recorder: d220e97045b84b7c85ac5ba34499820a

		Model: {'id': 'd220e97045b84b7c85ac5ba34499820a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.232, 'Rank IC': 0.028, 'Rank ICIR': 0.222}, 'data_train_vec': ['2024-04-23', '2025-10-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.222', 'recency_weight': '0.494', 'weight': '0.022'}

	Recorder: e59b79b077bf42bbbb2a6302f0ab07a9

		Model: {'id': 'e59b79b077bf42bbbb2a6302f0ab07a9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.319, 'Rank IC': 0.062, 'Rank ICIR': 0.385}, 'data_train_vec': ['2025-04-23', '2026-01-22'], 'train_time_vec': ['2026-04-23', '2026-04-23'], 'rank_icir': '0.385', 'recency_weight': '0.704', 'weight': '0.094'}
