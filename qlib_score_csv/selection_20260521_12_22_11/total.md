# params 
 {'predict_dates': [{'start': '2026-05-21', 'end': '2026-05-21'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260521_11 632630747155898858 (Recorders: 6/6)

	Recorder: 010c2c17fc144558b93a403875851d41

		Model: {'id': '010c2c17fc144558b93a403875851d41', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.306, 'Rank IC': 0.05, 'Rank ICIR': 0.342}, 'data_train_vec': ['2020-05-21', '2024-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.342', 'recency_weight': '0.122', 'weight': '0.024'}

	Recorder: abd91751ce6547c89d1f4959a04c4aaf

		Model: {'id': 'abd91751ce6547c89d1f4959a04c4aaf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.186, 'Rank IC': 0.05, 'Rank ICIR': 0.353}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.353', 'recency_weight': '0.173', 'weight': '0.036'}

	Recorder: 031609f10e054e97add30d389dfb15c8

		Model: {'id': '031609f10e054e97add30d389dfb15c8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.216, 'Rank IC': 0.061, 'Rank ICIR': 0.358}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.358', 'recency_weight': '0.244', 'weight': '0.052'}

	Recorder: d2c85636e01f478cba04e0410172ce49

		Model: {'id': 'd2c85636e01f478cba04e0410172ce49', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.158, 'Rank IC': 0.047, 'Rank ICIR': 0.31}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.310', 'recency_weight': '0.348', 'weight': '0.056'}

	Recorder: ce51285f1f2547c0a29b6967342cfbf4

		Model: {'id': 'ce51285f1f2547c0a29b6967342cfbf4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.086, 'Rank IC': 0.032, 'Rank ICIR': 0.25}, 'data_train_vec': ['2024-05-21', '2025-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.250', 'recency_weight': '0.496', 'weight': '0.052'}

	Recorder: dfd3ae0f2b9747fa99fb89fad2f29961

		Model: {'id': 'dfd3ae0f2b9747fa99fb89fad2f29961', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.445, 'Rank IC': 0.021, 'Rank ICIR': 0.215}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.215', 'recency_weight': '0.707', 'weight': '0.055'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260521_11 772143568836060650 (Recorders: 3/6)

	Recorder: 08b904db09ec4575826b119f5f326193

		Model: {'id': '08b904db09ec4575826b119f5f326193', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.303, 'Rank IC': 0.053, 'Rank ICIR': 0.377}, 'data_train_vec': ['2020-05-21', '2024-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.377', 'recency_weight': '0.122', 'weight': '0.029'}

	Recorder: ea31006afdd446ceb175f2f355f1a511

		Model: {'id': 'ea31006afdd446ceb175f2f355f1a511', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.166, 'Rank IC': 0.047, 'Rank ICIR': 0.335}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.335', 'recency_weight': '0.173', 'weight': '0.033'}

	Recorder: fa0c2d3fed124193ac9c791c1d6bbf34

		Model: {'id': 'fa0c2d3fed124193ac9c791c1d6bbf34', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.144, 'Rank IC': 0.057, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.049'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260521_11 179978328412331375 (Recorders: 4/6)

	Recorder: 936d76456b8a48f190d8527f0b27f6a7

		Model: {'id': '936d76456b8a48f190d8527f0b27f6a7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.282, 'Rank IC': 0.054, 'Rank ICIR': 0.435}, 'data_train_vec': ['2020-05-21', '2024-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.435', 'recency_weight': '0.122', 'weight': '0.039'}

	Recorder: fa62ce67f8864793a8bef3885e539fa8

		Model: {'id': 'fa62ce67f8864793a8bef3885e539fa8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.225, 'Rank IC': 0.054, 'Rank ICIR': 0.434}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.434', 'recency_weight': '0.173', 'weight': '0.055'}

	Recorder: dc1d6dd733394dfbbc6c855ffec25d9e

		Model: {'id': 'dc1d6dd733394dfbbc6c855ffec25d9e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.124, 'Rank IC': 0.056, 'Rank ICIR': 0.378}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.378', 'recency_weight': '0.244', 'weight': '0.058'}

	Recorder: 20feabec65d84887bc7b60fd9724dbe3

		Model: {'id': '20feabec65d84887bc7b60fd9724dbe3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.256, 'Rank IC': 0.047, 'Rank ICIR': 0.311}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.311', 'recency_weight': '0.707', 'weight': '0.114'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260521_11 525597425479771872 (Recorders: 6/6)

	Recorder: 66e5c9a624fd41c1926307faf87dce88

		Model: {'id': '66e5c9a624fd41c1926307faf87dce88', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.287, 'Rank IC': 0.047, 'Rank ICIR': 0.33}, 'data_train_vec': ['2020-05-21', '2024-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.330', 'recency_weight': '0.122', 'weight': '0.022'}

	Recorder: 07eef3dd789b4106b85503923f598d91

		Model: {'id': '07eef3dd789b4106b85503923f598d91', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.119, 'Rank IC': 0.044, 'Rank ICIR': 0.33}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.330', 'recency_weight': '0.173', 'weight': '0.032'}

	Recorder: 04af9268fc394e66a9df0469388a26ad

		Model: {'id': '04af9268fc394e66a9df0469388a26ad', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.268, 'Rank IC': 0.065, 'Rank ICIR': 0.415}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.415', 'recency_weight': '0.244', 'weight': '0.070'}

	Recorder: a1b6cf9d2535438a800a1c77b6b50fae

		Model: {'id': 'a1b6cf9d2535438a800a1c77b6b50fae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.17, 'Rank IC': 0.053, 'Rank ICIR': 0.343}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.343', 'recency_weight': '0.348', 'weight': '0.069'}

	Recorder: 661e70302efe42d0927dd9d7b34b285e

		Model: {'id': '661e70302efe42d0927dd9d7b34b285e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.144, 'Rank IC': 0.033, 'Rank ICIR': 0.283}, 'data_train_vec': ['2024-05-21', '2025-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.283', 'recency_weight': '0.496', 'weight': '0.066'}

	Recorder: 36c003461ebf4bd1a960f140a2d804c4

		Model: {'id': '36c003461ebf4bd1a960f140a2d804c4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.277, 'Rank IC': 0.034, 'Rank ICIR': 0.276}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.276', 'recency_weight': '0.707', 'weight': '0.090'}
