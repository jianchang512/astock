# params 
 {'predict_dates': [{'start': '2026-06-10', 'end': '2026-06-10'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260610_16 699281826089667463 (Recorders: 6/6)

	Recorder: 69eaa64101a94d8f8b0d248c1dd14bad

		Model: {'id': '69eaa64101a94d8f8b0d248c1dd14bad', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.353, 'Rank IC': 0.062, 'Rank ICIR': 0.405}, 'data_train_vec': ['2020-06-10', '2024-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.405', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: 58bef5289717404fba618fb2326a7e37

		Model: {'id': '58bef5289717404fba618fb2326a7e37', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.351, 'Rank IC': 0.075, 'Rank ICIR': 0.5}, 'data_train_vec': ['2021-06-10', '2025-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.500', 'recency_weight': '0.171', 'weight': '0.039'}

	Recorder: 456ee5ec704a4e798766ced9053459ed

		Model: {'id': '456ee5ec704a4e798766ced9053459ed', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.226, 'Rank IC': 0.07, 'Rank ICIR': 0.402}, 'data_train_vec': ['2022-06-10', '2025-06-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.402', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 7bfe23309475476bbee241873a8564e8

		Model: {'id': '7bfe23309475476bbee241873a8564e8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.3, 'Rank IC': 0.073, 'Rank ICIR': 0.422}, 'data_train_vec': ['2023-06-10', '2025-09-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.422', 'recency_weight': '0.348', 'weight': '0.057'}

	Recorder: 96cd6a3239c84f08a774583f6c4e1266

		Model: {'id': '96cd6a3239c84f08a774583f6c4e1266', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.281, 'Rank IC': 0.065, 'Rank ICIR': 0.461}, 'data_train_vec': ['2024-06-10', '2025-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.461', 'recency_weight': '0.494', 'weight': '0.096'}

	Recorder: 4924cca7770b41189773c971ef88dd2a

		Model: {'id': '4924cca7770b41189773c971ef88dd2a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.413, 'Rank IC': 0.027, 'Rank ICIR': 0.142}, 'data_train_vec': ['2025-06-10', '2026-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.142', 'recency_weight': '0.699', 'weight': '0.013'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260610_16 969019384485511624 (Recorders: 5/6)

	Recorder: 437687e3311045d49895fb768529c849

		Model: {'id': '437687e3311045d49895fb768529c849', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.339, 'Rank IC': 0.065, 'Rank ICIR': 0.416}, 'data_train_vec': ['2020-06-10', '2024-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.416', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 5ad1c05e1c474f799a5ffe6a272264f2

		Model: {'id': '5ad1c05e1c474f799a5ffe6a272264f2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.277, 'Rank IC': 0.069, 'Rank ICIR': 0.458}, 'data_train_vec': ['2021-06-10', '2025-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.458', 'recency_weight': '0.171', 'weight': '0.033'}

	Recorder: 2d2e955df9944252a35ea5cb584bcda5

		Model: {'id': '2d2e955df9944252a35ea5cb584bcda5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.177, 'Rank IC': 0.071, 'Rank ICIR': 0.406}, 'data_train_vec': ['2022-06-10', '2025-06-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.406', 'recency_weight': '0.244', 'weight': '0.037'}

	Recorder: df9c8c23d3cd49a6b62ba25787a117d8

		Model: {'id': 'df9c8c23d3cd49a6b62ba25787a117d8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.239, 'Rank IC': 0.082, 'Rank ICIR': 0.462}, 'data_train_vec': ['2023-06-10', '2025-09-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.462', 'recency_weight': '0.348', 'weight': '0.068'}

	Recorder: ce6fe452394d471587ca5d5783a32927

		Model: {'id': 'ce6fe452394d471587ca5d5783a32927', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.23, 'Rank IC': 0.066, 'Rank ICIR': 0.493}, 'data_train_vec': ['2024-06-10', '2025-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.493', 'recency_weight': '0.494', 'weight': '0.110'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260610_16 261880158794613437 (Recorders: 6/6)

	Recorder: 5c9628bbc2ee480592df6615f6c2408f

		Model: {'id': '5c9628bbc2ee480592df6615f6c2408f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.33, 'Rank IC': 0.066, 'Rank ICIR': 0.48}, 'data_train_vec': ['2020-06-10', '2024-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.480', 'recency_weight': '0.121', 'weight': '0.026'}

	Recorder: ba8873df60274440827709fe883dbd8b

		Model: {'id': 'ba8873df60274440827709fe883dbd8b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.271, 'Rank IC': 0.069, 'Rank ICIR': 0.497}, 'data_train_vec': ['2021-06-10', '2025-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.497', 'recency_weight': '0.171', 'weight': '0.039'}

	Recorder: e946fea8b7894ac88ffcaccd356c9ac9

		Model: {'id': 'e946fea8b7894ac88ffcaccd356c9ac9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.122, 'Rank IC': 0.059, 'Rank ICIR': 0.387}, 'data_train_vec': ['2022-06-10', '2025-06-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.387', 'recency_weight': '0.244', 'weight': '0.033'}

	Recorder: 9389ccb8018547b9b30aa67bf0fc3c5c

		Model: {'id': '9389ccb8018547b9b30aa67bf0fc3c5c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.163, 'Rank IC': 0.056, 'Rank ICIR': 0.403}, 'data_train_vec': ['2023-06-10', '2025-09-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.403', 'recency_weight': '0.348', 'weight': '0.052'}

	Recorder: f985707f77ca4720a709368850dd226f

		Model: {'id': 'f985707f77ca4720a709368850dd226f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.185, 'Rank IC': 0.044, 'Rank ICIR': 0.353}, 'data_train_vec': ['2024-06-10', '2025-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.353', 'recency_weight': '0.494', 'weight': '0.056'}

	Recorder: b2377d326a9041cfa48c3726751f8158

		Model: {'id': 'b2377d326a9041cfa48c3726751f8158', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.228, 'Rank IC': 0.035, 'Rank ICIR': 0.163}, 'data_train_vec': ['2025-06-10', '2026-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.163', 'recency_weight': '0.699', 'weight': '0.017'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260610_16 909697729710473512 (Recorders: 6/6)

	Recorder: 4ad060335e9b476f88dd2aea85fbaead

		Model: {'id': '4ad060335e9b476f88dd2aea85fbaead', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.302, 'Rank IC': 0.064, 'Rank ICIR': 0.418}, 'data_train_vec': ['2020-06-10', '2024-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.418', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: 2bddb24dd88a427dae6160828bc66d7c

		Model: {'id': '2bddb24dd88a427dae6160828bc66d7c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.299, 'Rank IC': 0.069, 'Rank ICIR': 0.494}, 'data_train_vec': ['2021-06-10', '2025-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.494', 'recency_weight': '0.171', 'weight': '0.038'}

	Recorder: fe5ac062e2094bceaac57bf06cc89ac5

		Model: {'id': 'fe5ac062e2094bceaac57bf06cc89ac5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.239, 'Rank IC': 0.072, 'Rank ICIR': 0.426}, 'data_train_vec': ['2022-06-10', '2025-06-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.426', 'recency_weight': '0.244', 'weight': '0.041'}

	Recorder: d71367d4704a4fb886d4b46cad5ae71b

		Model: {'id': 'd71367d4704a4fb886d4b46cad5ae71b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.329, 'Rank IC': 0.073, 'Rank ICIR': 0.441}, 'data_train_vec': ['2023-06-10', '2025-09-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.441', 'recency_weight': '0.348', 'weight': '0.062'}

	Recorder: 164d55af2c5d4152a2353d8c6509ee7e

		Model: {'id': '164d55af2c5d4152a2353d8c6509ee7e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.164, 'Rank IC': 0.055, 'Rank ICIR': 0.435}, 'data_train_vec': ['2024-06-10', '2025-12-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.435', 'recency_weight': '0.494', 'weight': '0.085'}

	Recorder: 5bee1b3e16fa41e4ab99912f9e4726cf

		Model: {'id': '5bee1b3e16fa41e4ab99912f9e4726cf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.351, 'Rank IC': 0.017, 'Rank ICIR': 0.102}, 'data_train_vec': ['2025-06-10', '2026-03-09'], 'train_time_vec': ['2026-06-10', '2026-06-10'], 'rank_icir': '0.102', 'recency_weight': '0.699', 'weight': '0.007'}
