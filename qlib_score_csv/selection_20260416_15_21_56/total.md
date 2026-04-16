# params 
 {'predict_dates': [{'start': '2026-04-16', 'end': '2026-04-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260416_14 357718317829884111 (Recorders: 6/6)

	Recorder: 50cf702314074bfea1110d7f6603fafc

		Model: {'id': '50cf702314074bfea1110d7f6603fafc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.44, 'Rank IC': 0.064, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: 1411d154606345c79eb624d863582564

		Model: {'id': '1411d154606345c79eb624d863582564', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.346, 'Rank IC': 0.054, 'Rank ICIR': 0.354}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.354', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: 949d823ba5764e6ab6db806ba7d67b5e

		Model: {'id': '949d823ba5764e6ab6db806ba7d67b5e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.205, 'Rank IC': 0.044, 'Rank ICIR': 0.251}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: 323252fb23b74543a5198afc50cb171f

		Model: {'id': '323252fb23b74543a5198afc50cb171f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.395, 'Rank IC': 0.064, 'Rank ICIR': 0.419}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.347', 'weight': '0.067'}

	Recorder: 5d2f412e93f34a15be50a9d6bd6b25d9

		Model: {'id': '5d2f412e93f34a15be50a9d6bd6b25d9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.205, 'Rank IC': 0.029, 'Rank ICIR': 0.212}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.212', 'recency_weight': '0.494', 'weight': '0.025'}

	Recorder: 58fd19262ace40428f50a4464bb56ff4

		Model: {'id': '58fd19262ace40428f50a4464bb56ff4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.351, 'Rank IC': 0.069, 'Rank ICIR': 0.352}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.352', 'recency_weight': '0.704', 'weight': '0.097'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260416_14 644208031398176694 (Recorders: 6/6)

	Recorder: 1b3327faf4ea4e07b729902ee97ad7e8

		Model: {'id': '1b3327faf4ea4e07b729902ee97ad7e8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.406, 'Rank IC': 0.061, 'Rank ICIR': 0.347}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.347', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 9a0dc7acfa544d7c8180d66195a17b83

		Model: {'id': '9a0dc7acfa544d7c8180d66195a17b83', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.284, 'Rank IC': 0.051, 'Rank ICIR': 0.319}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.319', 'recency_weight': '0.173', 'weight': '0.019'}

	Recorder: 573e9ddf6ed841118021ea5c0661d236

		Model: {'id': '573e9ddf6ed841118021ea5c0661d236', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.134, 'Rank IC': 0.038, 'Rank ICIR': 0.22}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.220', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: 4057fa00f8214b22af7ed4e9aa75322c

		Model: {'id': '4057fa00f8214b22af7ed4e9aa75322c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.169, 'Rank IC': 0.063, 'Rank ICIR': 0.4}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.400', 'recency_weight': '0.347', 'weight': '0.062'}

	Recorder: ff0d2dca3bd840939794017bbf3cab8c

		Model: {'id': 'ff0d2dca3bd840939794017bbf3cab8c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.227, 'Rank IC': 0.044, 'Rank ICIR': 0.331}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.331', 'recency_weight': '0.494', 'weight': '0.060'}

	Recorder: 4a4e53689d144f268cf4a3444c4c73e9

		Model: {'id': '4a4e53689d144f268cf4a3444c4c73e9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.299, 'Rank IC': 0.064, 'Rank ICIR': 0.329}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.329', 'recency_weight': '0.704', 'weight': '0.085'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260416_14 504629158673917386 (Recorders: 5/6)

	Recorder: f550f0eab49646a0af6a20dc22e43204

		Model: {'id': 'f550f0eab49646a0af6a20dc22e43204', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.396, 'Rank IC': 0.063, 'Rank ICIR': 0.467}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.467', 'recency_weight': '0.121', 'weight': '0.029'}

	Recorder: b8e7d6a2a2a6431fa4418c1595c94508

		Model: {'id': 'b8e7d6a2a2a6431fa4418c1595c94508', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.342, 'Rank IC': 0.055, 'Rank ICIR': 0.474}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.474', 'recency_weight': '0.173', 'weight': '0.043'}

	Recorder: b2edcc49edc24e0d8d72029de95ba631

		Model: {'id': 'b2edcc49edc24e0d8d72029de95ba631', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.206, 'Rank IC': 0.051, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: 7fbd5ca5de134abe890a0c1abb10feaf

		Model: {'id': '7fbd5ca5de134abe890a0c1abb10feaf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.181, 'Rank IC': 0.045, 'Rank ICIR': 0.332}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.332', 'recency_weight': '0.347', 'weight': '0.042'}

	Recorder: 4afca7993e89430a8ecf2376851b35d8

		Model: {'id': '4afca7993e89430a8ecf2376851b35d8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.267, 'Rank IC': 0.038, 'Rank ICIR': 0.184}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.184', 'recency_weight': '0.704', 'weight': '0.026'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260416_14 150577521430212130 (Recorders: 6/6)

	Recorder: b53e1a886be04cfc93fe009cf9f46e5d

		Model: {'id': 'b53e1a886be04cfc93fe009cf9f46e5d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.41, 'Rank IC': 0.06, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-04-16', '2024-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.370', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: e6274935f173473ab66e161d899f477a

		Model: {'id': 'e6274935f173473ab66e161d899f477a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.292, 'Rank IC': 0.053, 'Rank ICIR': 0.359}, 'data_train_vec': ['2021-04-16', '2025-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.359', 'recency_weight': '0.173', 'weight': '0.025'}

	Recorder: d5c1b15f6fbd468592cc85b630b2eeb9

		Model: {'id': 'd5c1b15f6fbd468592cc85b630b2eeb9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.242, 'Rank IC': 0.041, 'Rank ICIR': 0.255}, 'data_train_vec': ['2022-04-16', '2025-04-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.255', 'recency_weight': '0.244', 'weight': '0.018'}

	Recorder: a3934fe1fa7348c08a016f63c22c6175

		Model: {'id': 'a3934fe1fa7348c08a016f63c22c6175', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.45, 'Rank IC': 0.07, 'Rank ICIR': 0.483}, 'data_train_vec': ['2023-04-16', '2025-07-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.483', 'recency_weight': '0.347', 'weight': '0.090'}

	Recorder: 414efcf174864cc5b36484bf68667f6b

		Model: {'id': '414efcf174864cc5b36484bf68667f6b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.401, 'Rank IC': 0.033, 'Rank ICIR': 0.251}, 'data_train_vec': ['2024-04-16', '2025-10-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.251', 'recency_weight': '0.494', 'weight': '0.035'}

	Recorder: 0caf1f59f1b741cf9a44accf3ee570b1

		Model: {'id': '0caf1f59f1b741cf9a44accf3ee570b1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.379, 'Rank IC': 0.066, 'Rank ICIR': 0.419}, 'data_train_vec': ['2025-04-16', '2026-01-15'], 'train_time_vec': ['2026-04-16', '2026-04-16'], 'rank_icir': '0.419', 'recency_weight': '0.704', 'weight': '0.137'}
