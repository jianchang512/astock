# params 
 {'predict_dates': [{'start': '2026-07-20', 'end': '2026-07-20'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260721_13 754177919406572439 (Recorders: 5/6)

	Recorder: 2b2f5e844fc54c1182e4f2d5af9f5941

		Model: {'id': '2b2f5e844fc54c1182e4f2d5af9f5941', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.342, 'Rank IC': 0.06, 'Rank ICIR': 0.391}, 'data_train_vec': ['2020-07-21', '2025-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.391', 'recency_weight': '0.122', 'weight': '0.052'}

	Recorder: 0ecb67d9fde54da4abcfad1fdf3d6988

		Model: {'id': '0ecb67d9fde54da4abcfad1fdf3d6988', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.153, 'Rank IC': 0.057, 'Rank ICIR': 0.343}, 'data_train_vec': ['2021-07-21', '2025-04-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.343', 'recency_weight': '0.173', 'weight': '0.057'}

	Recorder: 78575abe02b548df80fe6a5d546b19ba

		Model: {'id': '78575abe02b548df80fe6a5d546b19ba', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.104, 'Rank IC': 0.051, 'Rank ICIR': 0.326}, 'data_train_vec': ['2022-07-21', '2025-07-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.326', 'recency_weight': '0.245', 'weight': '0.073'}

	Recorder: 94dfaa8b1aab45d8b53293dea2b8cc77

		Model: {'id': '94dfaa8b1aab45d8b53293dea2b8cc77', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.08, 'Rank IC': 0.059, 'Rank ICIR': 0.366}, 'data_train_vec': ['2023-07-21', '2025-10-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.366', 'recency_weight': '0.349', 'weight': '0.131'}

	Recorder: 9db19a0a33f248fa9b4ad1e3ed3ee7d3

		Model: {'id': '9db19a0a33f248fa9b4ad1e3ed3ee7d3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.111, 'Rank IC': 0.027, 'Rank ICIR': 0.162}, 'data_train_vec': ['2024-07-21', '2026-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.162', 'recency_weight': '0.498', 'weight': '0.037'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260721_12 527395661245264027 (Recorders: 5/6)

	Recorder: 77f3d0d0560347c49608e398f6f4ff63

		Model: {'id': '77f3d0d0560347c49608e398f6f4ff63', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.306, 'Rank IC': 0.062, 'Rank ICIR': 0.388}, 'data_train_vec': ['2020-07-21', '2025-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.388', 'recency_weight': '0.122', 'weight': '0.051'}

	Recorder: 53f693bf812449d8a03b2f40a548c4cb

		Model: {'id': '53f693bf812449d8a03b2f40a548c4cb', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.178, 'Rank IC': 0.056, 'Rank ICIR': 0.343}, 'data_train_vec': ['2021-07-21', '2025-04-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.343', 'recency_weight': '0.173', 'weight': '0.057'}

	Recorder: d83a3d075986451dbdcd48c4cd2aef8d

		Model: {'id': 'd83a3d075986451dbdcd48c4cd2aef8d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.111, 'Rank IC': 0.047, 'Rank ICIR': 0.301}, 'data_train_vec': ['2022-07-21', '2025-07-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.301', 'recency_weight': '0.245', 'weight': '0.062'}

	Recorder: ccb1523ee4774b18bcb5c51f3fa40db6

		Model: {'id': 'ccb1523ee4774b18bcb5c51f3fa40db6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.209, 'Rank IC': 0.062, 'Rank ICIR': 0.401}, 'data_train_vec': ['2023-07-21', '2025-10-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.401', 'recency_weight': '0.349', 'weight': '0.157'}

	Recorder: 166e7da0e9c4499c91f8279a476773ed

		Model: {'id': '166e7da0e9c4499c91f8279a476773ed', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.154, 'Rank IC': 0.017, 'Rank ICIR': 0.107}, 'data_train_vec': ['2024-07-21', '2026-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.107', 'recency_weight': '0.498', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260721_12 454477743017496212 (Recorders: 3/6)

	Recorder: ec7d111bff164662994cd2256f9ab3ff

		Model: {'id': 'ec7d111bff164662994cd2256f9ab3ff', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.2, 'Rank IC': 0.049, 'Rank ICIR': 0.308}, 'data_train_vec': ['2020-07-21', '2025-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.308', 'recency_weight': '0.122', 'weight': '0.032'}

	Recorder: 147062c0c09e48db809bff976c0782c3

		Model: {'id': '147062c0c09e48db809bff976c0782c3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.057, 'Rank IC': 0.038, 'Rank ICIR': 0.232}, 'data_train_vec': ['2021-07-21', '2025-04-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.232', 'recency_weight': '0.173', 'weight': '0.026'}

	Recorder: a5715c6be1c14c06b33efbfd20594612

		Model: {'id': 'a5715c6be1c14c06b33efbfd20594612', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.145, 'Rank IC': 0.043, 'Rank ICIR': 0.269}, 'data_train_vec': ['2023-07-21', '2025-10-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.269', 'recency_weight': '0.349', 'weight': '0.071'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260721_12 938298942950845821 (Recorders: 3/6)

	Recorder: 60dd84c287c8429599e57e9ddcec7403

		Model: {'id': '60dd84c287c8429599e57e9ddcec7403', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.324, 'Rank IC': 0.063, 'Rank ICIR': 0.428}, 'data_train_vec': ['2020-07-21', '2025-01-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.428', 'recency_weight': '0.122', 'weight': '0.062'}

	Recorder: 52ca9b5d52c34ca5a1d8412b85ff7e21

		Model: {'id': '52ca9b5d52c34ca5a1d8412b85ff7e21', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.119, 'Rank IC': 0.051, 'Rank ICIR': 0.312}, 'data_train_vec': ['2021-07-21', '2025-04-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.312', 'recency_weight': '0.173', 'weight': '0.047'}

	Recorder: 4a8ae87c317d4a788fcdaa8ffde15a37

		Model: {'id': '4a8ae87c317d4a788fcdaa8ffde15a37', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.074, 'Rank IC': 0.047, 'Rank ICIR': 0.319}, 'data_train_vec': ['2022-07-21', '2025-07-20'], 'train_time_vec': ['2026-07-21', '2026-07-21'], 'rank_icir': '0.319', 'recency_weight': '0.245', 'weight': '0.070'}
