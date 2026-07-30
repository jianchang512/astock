# params 
 {'predict_dates': [{'start': '2026-07-30', 'end': '2026-07-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260730_13 818322736548138229 (Recorders: 4/6)

	Recorder: 04762b2d17ab4fa4aaf38d3d7e120457

		Model: {'id': '04762b2d17ab4fa4aaf38d3d7e120457', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.31, 'Rank IC': 0.066, 'Rank ICIR': 0.445}, 'data_train_vec': ['2020-07-30', '2025-01-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.445', 'recency_weight': '0.122', 'weight': '0.058'}

	Recorder: 3b04611cb2ff4d76899364702ef63813

		Model: {'id': '3b04611cb2ff4d76899364702ef63813', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.185, 'Rank IC': 0.066, 'Rank ICIR': 0.383}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.383', 'recency_weight': '0.171', 'weight': '0.060'}

	Recorder: e6eb3fb6a3464b2cbe77cbb809b17105

		Model: {'id': 'e6eb3fb6a3464b2cbe77cbb809b17105', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.135, 'Rank IC': 0.056, 'Rank ICIR': 0.346}, 'data_train_vec': ['2022-07-30', '2025-07-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.346', 'recency_weight': '0.244', 'weight': '0.070'}

	Recorder: 13a23e3fc44b48b5ae2367e8dd668cfc

		Model: {'id': '13a23e3fc44b48b5ae2367e8dd668cfc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.098, 'Rank IC': 0.065, 'Rank ICIR': 0.374}, 'data_train_vec': ['2023-07-30', '2025-10-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.374', 'recency_weight': '0.348', 'weight': '0.117'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260730_13 144700974063503122 (Recorders: 4/6)

	Recorder: b8f9e0f5bb5544ff8c6185c165b368c6

		Model: {'id': 'b8f9e0f5bb5544ff8c6185c165b368c6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.334, 'Rank IC': 0.069, 'Rank ICIR': 0.424}, 'data_train_vec': ['2020-07-30', '2025-01-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.424', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: 5640cdca89254b5888ca7e3acae3948c

		Model: {'id': '5640cdca89254b5888ca7e3acae3948c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.233, 'Rank IC': 0.064, 'Rank ICIR': 0.392}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.392', 'recency_weight': '0.171', 'weight': '0.063'}

	Recorder: dc8bbbd0436341ee9165d9e5588003f8

		Model: {'id': 'dc8bbbd0436341ee9165d9e5588003f8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.146, 'Rank IC': 0.053, 'Rank ICIR': 0.334}, 'data_train_vec': ['2022-07-30', '2025-07-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.334', 'recency_weight': '0.244', 'weight': '0.065'}

	Recorder: dfef11c9cd9a459a8fcc610d1817cc80

		Model: {'id': 'dfef11c9cd9a459a8fcc610d1817cc80', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.197, 'Rank IC': 0.06, 'Rank ICIR': 0.364}, 'data_train_vec': ['2023-07-30', '2025-10-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.364', 'recency_weight': '0.348', 'weight': '0.111'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260730_13 318479864101076058 (Recorders: 5/6)

	Recorder: c5587be3555a47ea9a074605e4546b76

		Model: {'id': 'c5587be3555a47ea9a074605e4546b76', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.225, 'Rank IC': 0.056, 'Rank ICIR': 0.337}, 'data_train_vec': ['2020-07-30', '2025-01-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.337', 'recency_weight': '0.122', 'weight': '0.033'}

	Recorder: 70b9de5ef2924f79988a299985054741

		Model: {'id': '70b9de5ef2924f79988a299985054741', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.128, 'Rank IC': 0.049, 'Rank ICIR': 0.285}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.285', 'recency_weight': '0.171', 'weight': '0.033'}

	Recorder: e380b2cee20d4a7498cc722ece230e67

		Model: {'id': 'e380b2cee20d4a7498cc722ece230e67', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.122, 'Rank IC': 0.049, 'Rank ICIR': 0.31}, 'data_train_vec': ['2022-07-30', '2025-07-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.310', 'recency_weight': '0.244', 'weight': '0.056'}

	Recorder: d94d8c991a42435e957a072c6c5e3a45

		Model: {'id': 'd94d8c991a42435e957a072c6c5e3a45', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.222, 'Rank IC': 0.054, 'Rank ICIR': 0.299}, 'data_train_vec': ['2023-07-30', '2025-10-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.299', 'recency_weight': '0.348', 'weight': '0.075'}

	Recorder: f40144b73df348d1a6f939158b22a318

		Model: {'id': 'f40144b73df348d1a6f939158b22a318', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.069, 'Rank IC': 0.019, 'Rank ICIR': 0.091}, 'data_train_vec': ['2024-07-30', '2026-01-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.091', 'recency_weight': '0.496', 'weight': '0.010'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260730_12 418253707003634525 (Recorders: 3/6)

	Recorder: edbba4c7f22f49bd90585a7b31965866

		Model: {'id': 'edbba4c7f22f49bd90585a7b31965866', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.282, 'Rank IC': 0.065, 'Rank ICIR': 0.452}, 'data_train_vec': ['2020-07-30', '2025-01-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.452', 'recency_weight': '0.122', 'weight': '0.060'}

	Recorder: 26a4d7bcbc8647ec8a10934a4f2c64f7

		Model: {'id': '26a4d7bcbc8647ec8a10934a4f2c64f7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.151, 'Rank IC': 0.059, 'Rank ICIR': 0.367}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.367', 'recency_weight': '0.171', 'weight': '0.055'}

	Recorder: 35df9c33fb40484896506dac169f736b

		Model: {'id': '35df9c33fb40484896506dac169f736b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.064, 'Rank IC': 0.058, 'Rank ICIR': 0.369}, 'data_train_vec': ['2022-07-30', '2025-07-29'], 'train_time_vec': ['2026-07-30', '2026-07-30'], 'rank_icir': '0.369', 'recency_weight': '0.244', 'weight': '0.080'}
