# params 
 {'predict_dates': [{'start': '2026-06-25', 'end': '2026-06-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260625_12 309312513393767465 (Recorders: 6/6)

	Recorder: 73cd2ba8d41242a4a03fc7f4df55a5af

		Model: {'id': '73cd2ba8d41242a4a03fc7f4df55a5af', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.328, 'Rank IC': 0.065, 'Rank ICIR': 0.429}, 'data_train_vec': ['2020-06-25', '2024-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.429', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 66b6f327c759438ca0ecd6a6deafa844

		Model: {'id': '66b6f327c759438ca0ecd6a6deafa844', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.235, 'Rank IC': 0.072, 'Rank ICIR': 0.431}, 'data_train_vec': ['2021-06-25', '2025-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.431', 'recency_weight': '0.171', 'weight': '0.022'}

	Recorder: 4500e3ecdbe442acb07ce4b0e8ccf9ce

		Model: {'id': '4500e3ecdbe442acb07ce4b0e8ccf9ce', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.061, 'Rank ICIR': 0.351}, 'data_train_vec': ['2022-06-25', '2025-06-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.351', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 12de8ad004934d60a49f878c52eab628

		Model: {'id': '12de8ad004934d60a49f878c52eab628', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.331, 'Rank IC': 0.071, 'Rank ICIR': 0.443}, 'data_train_vec': ['2023-06-25', '2025-09-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.443', 'recency_weight': '0.348', 'weight': '0.048'}

	Recorder: 32ab06bd67ce474fa0ab315358e57e1d

		Model: {'id': '32ab06bd67ce474fa0ab315358e57e1d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.408, 'Rank IC': 0.07, 'Rank ICIR': 0.541}, 'data_train_vec': ['2024-06-25', '2025-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.541', 'recency_weight': '0.494', 'weight': '0.101'}

	Recorder: 79a5d73595a640638597d368256522a1

		Model: {'id': '79a5d73595a640638597d368256522a1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.123, 'ICIR': 0.706, 'Rank IC': 0.065, 'Rank ICIR': 0.368}, 'data_train_vec': ['2025-06-25', '2026-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.368', 'recency_weight': '0.699', 'weight': '0.066'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260625_12 649976071051116915 (Recorders: 6/6)

	Recorder: 3a004daa5dfe46e193a24339b64e0ce4

		Model: {'id': '3a004daa5dfe46e193a24339b64e0ce4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.319, 'Rank IC': 0.065, 'Rank ICIR': 0.425}, 'data_train_vec': ['2020-06-25', '2024-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.425', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: d453e9dd48f14a0ab206718898dbffb7

		Model: {'id': 'd453e9dd48f14a0ab206718898dbffb7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.208, 'Rank IC': 0.064, 'Rank ICIR': 0.393}, 'data_train_vec': ['2021-06-25', '2025-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.393', 'recency_weight': '0.171', 'weight': '0.019'}

	Recorder: 7046f4deadb544008ab609895cb1005f

		Model: {'id': '7046f4deadb544008ab609895cb1005f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.115, 'Rank IC': 0.059, 'Rank ICIR': 0.35}, 'data_train_vec': ['2022-06-25', '2025-06-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.350', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: 8ff07e60f7474b079b0302f1071ef604

		Model: {'id': '8ff07e60f7474b079b0302f1071ef604', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.273, 'Rank IC': 0.068, 'Rank ICIR': 0.43}, 'data_train_vec': ['2023-06-25', '2025-09-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.430', 'recency_weight': '0.348', 'weight': '0.045'}

	Recorder: 81550c63344449b89fe6e0decc853a16

		Model: {'id': '81550c63344449b89fe6e0decc853a16', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.321, 'Rank IC': 0.065, 'Rank ICIR': 0.527}, 'data_train_vec': ['2024-06-25', '2025-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.527', 'recency_weight': '0.494', 'weight': '0.096'}

	Recorder: d216c9914b554e9bb985cfdee0ac6b46

		Model: {'id': 'd216c9914b554e9bb985cfdee0ac6b46', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.109, 'ICIR': 0.54, 'Rank IC': 0.073, 'Rank ICIR': 0.384}, 'data_train_vec': ['2025-06-25', '2026-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.384', 'recency_weight': '0.699', 'weight': '0.072'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260625_11 398005654591650431 (Recorders: 6/6)

	Recorder: 49e1420ac89545e2bba264b773630cff

		Model: {'id': '49e1420ac89545e2bba264b773630cff', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.307, 'Rank IC': 0.066, 'Rank ICIR': 0.469}, 'data_train_vec': ['2020-06-25', '2024-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.469', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: faff17c266a146abadc3191c0a1f2f99

		Model: {'id': 'faff17c266a146abadc3191c0a1f2f99', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.184, 'Rank IC': 0.063, 'Rank ICIR': 0.415}, 'data_train_vec': ['2021-06-25', '2025-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.415', 'recency_weight': '0.171', 'weight': '0.021'}

	Recorder: c07c34ef0d1841d89e124cad2a634970

		Model: {'id': 'c07c34ef0d1841d89e124cad2a634970', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.079, 'Rank IC': 0.057, 'Rank ICIR': 0.355}, 'data_train_vec': ['2022-06-25', '2025-06-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.355', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: 3af5f3a3f92a4a7ba5954a1e3133e476

		Model: {'id': '3af5f3a3f92a4a7ba5954a1e3133e476', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.205, 'Rank IC': 0.053, 'Rank ICIR': 0.374}, 'data_train_vec': ['2023-06-25', '2025-09-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.374', 'recency_weight': '0.348', 'weight': '0.034'}

	Recorder: b0677a58837f457492c698594143d14b

		Model: {'id': 'b0677a58837f457492c698594143d14b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.271, 'Rank IC': 0.055, 'Rank ICIR': 0.379}, 'data_train_vec': ['2024-06-25', '2025-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.379', 'recency_weight': '0.494', 'weight': '0.050'}

	Recorder: 4e36439e473544d4815f7b8b26177a86

		Model: {'id': '4e36439e473544d4815f7b8b26177a86', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.083, 'ICIR': 0.389, 'Rank IC': 0.061, 'Rank ICIR': 0.305}, 'data_train_vec': ['2025-06-25', '2026-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.305', 'recency_weight': '0.699', 'weight': '0.046'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260625_11 938482533492986085 (Recorders: 6/6)

	Recorder: 321ad084584148a6b73c1c4614f14bcd

		Model: {'id': '321ad084584148a6b73c1c4614f14bcd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.304, 'Rank IC': 0.064, 'Rank ICIR': 0.439}, 'data_train_vec': ['2020-06-25', '2024-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.439', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 838d13946f71412795b8e59de3c0b9d4

		Model: {'id': '838d13946f71412795b8e59de3c0b9d4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.213, 'Rank IC': 0.072, 'Rank ICIR': 0.451}, 'data_train_vec': ['2021-06-25', '2025-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.451', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: 689bea44c786485c8a7f47b66bdb86e6

		Model: {'id': '689bea44c786485c8a7f47b66bdb86e6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.097, 'Rank IC': 0.067, 'Rank ICIR': 0.4}, 'data_train_vec': ['2022-06-25', '2025-06-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.400', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 6c9329490ecf455eb7cc4f2df41a40e4

		Model: {'id': '6c9329490ecf455eb7cc4f2df41a40e4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.266, 'Rank IC': 0.07, 'Rank ICIR': 0.437}, 'data_train_vec': ['2023-06-25', '2025-09-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.437', 'recency_weight': '0.348', 'weight': '0.047'}

	Recorder: d9e9ca8f12fc40a6b8b700e883270b08

		Model: {'id': 'd9e9ca8f12fc40a6b8b700e883270b08', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.268, 'Rank IC': 0.056, 'Rank ICIR': 0.491}, 'data_train_vec': ['2024-06-25', '2025-12-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.491', 'recency_weight': '0.494', 'weight': '0.084'}

	Recorder: bca55584c58c4c0187c0c880749d3814

		Model: {'id': 'bca55584c58c4c0187c0c880749d3814', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.094, 'ICIR': 0.645, 'Rank IC': 0.057, 'Rank ICIR': 0.37}, 'data_train_vec': ['2025-06-25', '2026-03-24'], 'train_time_vec': ['2026-06-25', '2026-06-25'], 'rank_icir': '0.370', 'recency_weight': '0.699', 'weight': '0.067'}
