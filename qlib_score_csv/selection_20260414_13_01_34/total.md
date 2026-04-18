# params 
 {'predict_dates': [{'start': '2026-04-14', 'end': '2026-04-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260415_12 615743728401174066 (Recorders: 6/6)

	Recorder: 1e89fe6bd28943ea8a6fe5f920dc3726

		Model: {'id': '1e89fe6bd28943ea8a6fe5f920dc3726', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.445, 'Rank IC': 0.065, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.383', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 2615b2264b0543c9a53f6f7d7cbb1879

		Model: {'id': '2615b2264b0543c9a53f6f7d7cbb1879', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.346, 'Rank IC': 0.052, 'Rank ICIR': 0.332}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.332', 'recency_weight': '0.173', 'weight': '0.020'}

	Recorder: a38d7b553a114740a98abd0cf04df22b

		Model: {'id': 'a38d7b553a114740a98abd0cf04df22b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.213, 'Rank IC': 0.04, 'Rank ICIR': 0.244}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.244', 'recency_weight': '0.245', 'weight': '0.015'}

	Recorder: bc48f4b7744f498fba40b40bea732917

		Model: {'id': 'bc48f4b7744f498fba40b40bea732917', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.4, 'Rank IC': 0.062, 'Rank ICIR': 0.411}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.411', 'recency_weight': '0.348', 'weight': '0.061'}

	Recorder: 29f5fb8ceec149dda3fe50721bcf7c8d

		Model: {'id': '29f5fb8ceec149dda3fe50721bcf7c8d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.215, 'Rank IC': 0.033, 'Rank ICIR': 0.28}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.280', 'recency_weight': '0.496', 'weight': '0.041'}

	Recorder: 82040246e92041b1b0fa321e52f4bcf0

		Model: {'id': '82040246e92041b1b0fa321e52f4bcf0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.272, 'Rank IC': 0.064, 'Rank ICIR': 0.353}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.353', 'recency_weight': '0.707', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260415_12 501517585073880777 (Recorders: 6/6)

	Recorder: 441fb1a558eb48cebdd9dc41c23a0832

		Model: {'id': '441fb1a558eb48cebdd9dc41c23a0832', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.365, 'Rank IC': 0.056, 'Rank ICIR': 0.319}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.319', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: f1acfbaf49a64986ba98cf4c98d671a1

		Model: {'id': 'f1acfbaf49a64986ba98cf4c98d671a1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.271, 'Rank IC': 0.05, 'Rank ICIR': 0.308}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.308', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 72b58e9c879040f18c427e0f8c0d4274

		Model: {'id': '72b58e9c879040f18c427e0f8c0d4274', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.106, 'Rank IC': 0.038, 'Rank ICIR': 0.225}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.225', 'recency_weight': '0.245', 'weight': '0.013'}

	Recorder: 6987ba7253a3499faf83509413f86f7c

		Model: {'id': '6987ba7253a3499faf83509413f86f7c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.19, 'Rank IC': 0.055, 'Rank ICIR': 0.381}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.381', 'recency_weight': '0.348', 'weight': '0.053'}

	Recorder: aa7cf355575147cb81234e7244ab0a70

		Model: {'id': 'aa7cf355575147cb81234e7244ab0a70', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.18, 'Rank IC': 0.035, 'Rank ICIR': 0.263}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.263', 'recency_weight': '0.496', 'weight': '0.036'}

	Recorder: d9673a36aa2e42699b9584b723f7d657

		Model: {'id': 'd9673a36aa2e42699b9584b723f7d657', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.37, 'Rank IC': 0.073, 'Rank ICIR': 0.457}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.457', 'recency_weight': '0.707', 'weight': '0.154'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260415_12 863867855111737880 (Recorders: 5/6)

	Recorder: 02167d4d4cfd4ea08fddfc973f121cde

		Model: {'id': '02167d4d4cfd4ea08fddfc973f121cde', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.392, 'Rank IC': 0.063, 'Rank ICIR': 0.461}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.461', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: 336d061b844e4447af41c62a13b2ca46

		Model: {'id': '336d061b844e4447af41c62a13b2ca46', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.352, 'Rank IC': 0.056, 'Rank ICIR': 0.481}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.481', 'recency_weight': '0.173', 'weight': '0.042'}

	Recorder: ad6b6aa6ca5447f5b883ff7172310a71

		Model: {'id': 'ad6b6aa6ca5447f5b883ff7172310a71', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.221, 'Rank IC': 0.051, 'Rank ICIR': 0.351}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.351', 'recency_weight': '0.245', 'weight': '0.032'}

	Recorder: 1dbeeabad490431284761f1394fa4226

		Model: {'id': '1dbeeabad490431284761f1394fa4226', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.206, 'Rank IC': 0.046, 'Rank ICIR': 0.344}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.344', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: 1f20d97067144df3a38d8f8859242ea7

		Model: {'id': '1f20d97067144df3a38d8f8859242ea7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.245, 'Rank IC': 0.035, 'Rank ICIR': 0.208}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.208', 'recency_weight': '0.707', 'weight': '0.032'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260415_11 381748506409994513 (Recorders: 6/6)

	Recorder: afd72cfbdbab4642b516d5052c5325af

		Model: {'id': 'afd72cfbdbab4642b516d5052c5325af', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.404, 'Rank IC': 0.063, 'Rank ICIR': 0.389}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.389', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 77ee6a382e52499eb1f3f8f378dfad5a

		Model: {'id': '77ee6a382e52499eb1f3f8f378dfad5a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.282, 'Rank IC': 0.052, 'Rank ICIR': 0.356}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.356', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 0a648ac690e742daadc5c98dcfcf3365

		Model: {'id': '0a648ac690e742daadc5c98dcfcf3365', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.045, 'Rank ICIR': 0.267}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.267', 'recency_weight': '0.245', 'weight': '0.018'}

	Recorder: 5f73a16d134444bb8bfd8c141b88f731

		Model: {'id': '5f73a16d134444bb8bfd8c141b88f731', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.367, 'Rank IC': 0.068, 'Rank ICIR': 0.477}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.477', 'recency_weight': '0.348', 'weight': '0.083'}

	Recorder: 0c1d5463cbf94fb9acbc34148b66461e

		Model: {'id': '0c1d5463cbf94fb9acbc34148b66461e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.179, 'Rank IC': 0.031, 'Rank ICIR': 0.254}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.254', 'recency_weight': '0.496', 'weight': '0.033'}

	Recorder: f819cf8255bb49aa93a9ae0f23fd3154

		Model: {'id': 'f819cf8255bb49aa93a9ae0f23fd3154', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.34, 'Rank IC': 0.065, 'Rank ICIR': 0.396}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.396', 'recency_weight': '0.707', 'weight': '0.116'}
