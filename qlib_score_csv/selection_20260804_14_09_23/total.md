# params 
 {'predict_dates': [{'start': '2026-08-04', 'end': '2026-08-04'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260804_13 778871986388620797 (Recorders: 5/6)

	Recorder: ae037e81eea14e3695f7e921f4d1b53d

		Model: {'id': 'ae037e81eea14e3695f7e921f4d1b53d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.308, 'Rank IC': 0.069, 'Rank ICIR': 0.437}, 'data_train_vec': ['2020-08-04', '2025-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.437', 'recency_weight': '0.122', 'weight': '0.054'}

	Recorder: 3deec92110ff41958445bbc6487b6f73

		Model: {'id': '3deec92110ff41958445bbc6487b6f73', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.163, 'Rank IC': 0.062, 'Rank ICIR': 0.37}, 'data_train_vec': ['2021-08-04', '2025-05-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.370', 'recency_weight': '0.171', 'weight': '0.055'}

	Recorder: 0349d3cafdf940b29c5ed3075cfef07b

		Model: {'id': '0349d3cafdf940b29c5ed3075cfef07b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.109, 'Rank IC': 0.06, 'Rank ICIR': 0.363}, 'data_train_vec': ['2022-08-04', '2025-08-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.363', 'recency_weight': '0.244', 'weight': '0.075'}

	Recorder: 23f099529c364e97800fd8fa5d39d87e

		Model: {'id': '23f099529c364e97800fd8fa5d39d87e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.103, 'Rank IC': 0.069, 'Rank ICIR': 0.394}, 'data_train_vec': ['2023-08-04', '2025-11-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.394', 'recency_weight': '0.348', 'weight': '0.126'}

	Recorder: 73119c8c471046dab8f976371686b419

		Model: {'id': '73119c8c471046dab8f976371686b419', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.043, 'Rank IC': 0.021, 'Rank ICIR': 0.102}, 'data_train_vec': ['2024-08-04', '2026-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.102', 'recency_weight': '0.496', 'weight': '0.012'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260804_13 960708610962058476 (Recorders: 5/6)

	Recorder: d6c44b5fcef44aecab369645204edecb

		Model: {'id': 'd6c44b5fcef44aecab369645204edecb', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.33, 'Rank IC': 0.068, 'Rank ICIR': 0.421}, 'data_train_vec': ['2020-08-04', '2025-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.421', 'recency_weight': '0.122', 'weight': '0.050'}

	Recorder: 31c50b901e0743c7962af29789ab020d

		Model: {'id': '31c50b901e0743c7962af29789ab020d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.223, 'Rank IC': 0.064, 'Rank ICIR': 0.405}, 'data_train_vec': ['2021-08-04', '2025-05-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.405', 'recency_weight': '0.171', 'weight': '0.066'}

	Recorder: dfd7cb9735bf49ec8f997d0ad3bd42c3

		Model: {'id': 'dfd7cb9735bf49ec8f997d0ad3bd42c3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.138, 'Rank IC': 0.052, 'Rank ICIR': 0.325}, 'data_train_vec': ['2022-08-04', '2025-08-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.325', 'recency_weight': '0.244', 'weight': '0.060'}

	Recorder: be51d03c4bc6488aa70403d01b63f857

		Model: {'id': 'be51d03c4bc6488aa70403d01b63f857', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.263, 'Rank IC': 0.072, 'Rank ICIR': 0.455}, 'data_train_vec': ['2023-08-04', '2025-11-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.455', 'recency_weight': '0.348', 'weight': '0.169'}

	Recorder: 35f43f4612934378afdc38604a39dbcf

		Model: {'id': '35f43f4612934378afdc38604a39dbcf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.126, 'Rank IC': 0.026, 'Rank ICIR': 0.133}, 'data_train_vec': ['2024-08-04', '2026-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.133', 'recency_weight': '0.496', 'weight': '0.021'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260804_13 530567173835656308 (Recorders: 5/6)

	Recorder: e169ee33670349319fb10fe1512956cf

		Model: {'id': 'e169ee33670349319fb10fe1512956cf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.195, 'Rank IC': 0.05, 'Rank ICIR': 0.308}, 'data_train_vec': ['2020-08-04', '2025-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.308', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: 40719a97577e469cb79222483a1b8655

		Model: {'id': '40719a97577e469cb79222483a1b8655', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.129, 'Rank IC': 0.047, 'Rank ICIR': 0.272}, 'data_train_vec': ['2021-08-04', '2025-05-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.272', 'recency_weight': '0.171', 'weight': '0.030'}

	Recorder: 9221dbfd58fb474799b4d51bebedeafd

		Model: {'id': '9221dbfd58fb474799b4d51bebedeafd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.128, 'Rank IC': 0.05, 'Rank ICIR': 0.305}, 'data_train_vec': ['2022-08-04', '2025-08-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.305', 'recency_weight': '0.244', 'weight': '0.053'}

	Recorder: 39827b517fe64240b148ba3bec089bde

		Model: {'id': '39827b517fe64240b148ba3bec089bde', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.239, 'Rank IC': 0.055, 'Rank ICIR': 0.309}, 'data_train_vec': ['2023-08-04', '2025-11-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.309', 'recency_weight': '0.348', 'weight': '0.078'}

	Recorder: 73b8b004d32746dc9ccde78373d323ab

		Model: {'id': '73b8b004d32746dc9ccde78373d323ab', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.081, 'Rank IC': 0.027, 'Rank ICIR': 0.122}, 'data_train_vec': ['2024-08-04', '2026-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.122', 'recency_weight': '0.496', 'weight': '0.017'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260804_13 699289773125903199 (Recorders: 2/6)

	Recorder: eef9fcfce9ae4b67938d36ea9e104f87

		Model: {'id': 'eef9fcfce9ae4b67938d36ea9e104f87', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.245, 'Rank IC': 0.064, 'Rank ICIR': 0.432}, 'data_train_vec': ['2020-08-04', '2025-02-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.432', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: 436b721059d14f41820f4a05812d9f6c

		Model: {'id': '436b721059d14f41820f4a05812d9f6c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.125, 'Rank IC': 0.058, 'Rank ICIR': 0.366}, 'data_train_vec': ['2021-08-04', '2025-05-03'], 'train_time_vec': ['2026-08-04', '2026-08-04'], 'rank_icir': '0.366', 'recency_weight': '0.171', 'weight': '0.054'}
