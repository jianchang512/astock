# params 
 {'predict_dates': [{'start': '2026-07-17', 'end': '2026-07-17'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260720_13 113689088578345241 (Recorders: 5/6)

	Recorder: ad107fbc7c394e099bb4388c1608955d

		Model: {'id': 'ad107fbc7c394e099bb4388c1608955d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.292, 'Rank IC': 0.062, 'Rank ICIR': 0.389}, 'data_train_vec': ['2020-07-20', '2025-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.389', 'recency_weight': '0.123', 'weight': '0.038'}

	Recorder: 093dcb371eed46f99d1adfeee522f3fd

		Model: {'id': '093dcb371eed46f99d1adfeee522f3fd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.2, 'Rank IC': 0.062, 'Rank ICIR': 0.365}, 'data_train_vec': ['2021-07-20', '2025-04-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.365', 'recency_weight': '0.174', 'weight': '0.047'}

	Recorder: 77428ea971494174bdb0b02b47f854a4

		Model: {'id': '77428ea971494174bdb0b02b47f854a4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.08, 'Rank IC': 0.052, 'Rank ICIR': 0.326}, 'data_train_vec': ['2022-07-20', '2025-07-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.326', 'recency_weight': '0.247', 'weight': '0.053'}

	Recorder: c915ab7fbef947b9b08f94b9a473d21c

		Model: {'id': 'c915ab7fbef947b9b08f94b9a473d21c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.138, 'Rank IC': 0.068, 'Rank ICIR': 0.423}, 'data_train_vec': ['2023-07-20', '2025-10-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.423', 'recency_weight': '0.352', 'weight': '0.128'}

	Recorder: c90117b2ad514c958374ee652637cc50

		Model: {'id': 'c90117b2ad514c958374ee652637cc50', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.14, 'Rank IC': 0.034, 'Rank ICIR': 0.197}, 'data_train_vec': ['2024-07-20', '2026-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.197', 'recency_weight': '0.502', 'weight': '0.040'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260720_13 229552512976626232 (Recorders: 5/6)

	Recorder: 5e0720d244ad4bd0b0e32acc2ae41c7c

		Model: {'id': '5e0720d244ad4bd0b0e32acc2ae41c7c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.322, 'Rank IC': 0.064, 'Rank ICIR': 0.409}, 'data_train_vec': ['2020-07-20', '2025-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.409', 'recency_weight': '0.123', 'weight': '0.042'}

	Recorder: b6c0faf1cb15464a9f69b297fa4b428f

		Model: {'id': 'b6c0faf1cb15464a9f69b297fa4b428f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.206, 'Rank IC': 0.059, 'Rank ICIR': 0.37}, 'data_train_vec': ['2021-07-20', '2025-04-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.370', 'recency_weight': '0.174', 'weight': '0.048'}

	Recorder: 284e93ead57440018cd19cfe874baf0e

		Model: {'id': '284e93ead57440018cd19cfe874baf0e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.112, 'Rank IC': 0.049, 'Rank ICIR': 0.317}, 'data_train_vec': ['2022-07-20', '2025-07-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.317', 'recency_weight': '0.247', 'weight': '0.050'}

	Recorder: 0f20023b8e7542f184365a6dd316ec6f

		Model: {'id': '0f20023b8e7542f184365a6dd316ec6f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.241, 'Rank IC': 0.067, 'Rank ICIR': 0.445}, 'data_train_vec': ['2023-07-20', '2025-10-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.445', 'recency_weight': '0.352', 'weight': '0.142'}

	Recorder: 5a4e0d5286d54d899fe31b5a068872f1

		Model: {'id': '5a4e0d5286d54d899fe31b5a068872f1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.135, 'Rank IC': 0.02, 'Rank ICIR': 0.124}, 'data_train_vec': ['2024-07-20', '2026-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.124', 'recency_weight': '0.502', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260720_13 537320175281449790 (Recorders: 3/6)

	Recorder: 96f795892e37442da6052d0eaa4858b5

		Model: {'id': '96f795892e37442da6052d0eaa4858b5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.216, 'Rank IC': 0.051, 'Rank ICIR': 0.333}, 'data_train_vec': ['2020-07-20', '2025-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.333', 'recency_weight': '0.123', 'weight': '0.028'}

	Recorder: 4825669370d04b1dbfe0301a9dcd8e7b

		Model: {'id': '4825669370d04b1dbfe0301a9dcd8e7b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.08, 'Rank IC': 0.041, 'Rank ICIR': 0.261}, 'data_train_vec': ['2021-07-20', '2025-04-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.261', 'recency_weight': '0.174', 'weight': '0.024'}

	Recorder: 2cf9ecb0747f435f88b4c1940a0cbca4

		Model: {'id': '2cf9ecb0747f435f88b4c1940a0cbca4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.188, 'Rank IC': 0.049, 'Rank ICIR': 0.322}, 'data_train_vec': ['2023-07-20', '2025-10-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.322', 'recency_weight': '0.352', 'weight': '0.074'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260720_13 813201131733422665 (Recorders: 4/6)

	Recorder: bfcd6baf66ae4b61898633bc398b36b2

		Model: {'id': 'bfcd6baf66ae4b61898633bc398b36b2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.343, 'Rank IC': 0.066, 'Rank ICIR': 0.463}, 'data_train_vec': ['2020-07-20', '2025-01-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.463', 'recency_weight': '0.123', 'weight': '0.054'}

	Recorder: 4ed683538a0a46bb9f2596e6626ec6e4

		Model: {'id': '4ed683538a0a46bb9f2596e6626ec6e4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.096, 'Rank IC': 0.056, 'Rank ICIR': 0.351}, 'data_train_vec': ['2021-07-20', '2025-04-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.351', 'recency_weight': '0.174', 'weight': '0.044'}

	Recorder: 5c4642a4bddc4fb497cb2d2fcf54ebc2

		Model: {'id': '5c4642a4bddc4fb497cb2d2fcf54ebc2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.061, 'Rank IC': 0.057, 'Rank ICIR': 0.377}, 'data_train_vec': ['2022-07-20', '2025-07-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.377', 'recency_weight': '0.247', 'weight': '0.071'}

	Recorder: 8f5050e0b59d4bd9ad20f1638b81a939

		Model: {'id': '8f5050e0b59d4bd9ad20f1638b81a939', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.066, 'Rank IC': 0.059, 'Rank ICIR': 0.378}, 'data_train_vec': ['2023-07-20', '2025-10-19'], 'train_time_vec': ['2026-07-20', '2026-07-20'], 'rank_icir': '0.378', 'recency_weight': '0.352', 'weight': '0.102'}
