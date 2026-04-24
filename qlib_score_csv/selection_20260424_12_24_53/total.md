# params 
 {'predict_dates': [{'start': '2026-04-24', 'end': '2026-04-24'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260424_11 552730352422322703 (Recorders: 6/6)

	Recorder: 24705aacca4240b9a1833b4465240640

		Model: {'id': '24705aacca4240b9a1833b4465240640', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.414, 'Rank IC': 0.061, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-04-24', '2024-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: d7ef44795d7a4c38bcf845f2c3c1622e

		Model: {'id': 'd7ef44795d7a4c38bcf845f2c3c1622e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.299, 'Rank IC': 0.053, 'Rank ICIR': 0.36}, 'data_train_vec': ['2021-04-24', '2025-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.360', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 4779e227e972416e9ec0945a00eaa226

		Model: {'id': '4779e227e972416e9ec0945a00eaa226', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.159, 'Rank IC': 0.048, 'Rank ICIR': 0.295}, 'data_train_vec': ['2022-04-24', '2025-04-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.295', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: 0f242aacd0ee42708229422a3d71228b

		Model: {'id': '0f242aacd0ee42708229422a3d71228b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.274, 'Rank IC': 0.056, 'Rank ICIR': 0.328}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.328', 'recency_weight': '0.347', 'weight': '0.039'}

	Recorder: 326124fad5004cbfaadaa56570b8a038

		Model: {'id': '326124fad5004cbfaadaa56570b8a038', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.204, 'Rank IC': 0.031, 'Rank ICIR': 0.247}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.247', 'recency_weight': '0.494', 'weight': '0.032'}

	Recorder: 856c0bdf08f14f8e96db9e522e544c44

		Model: {'id': '856c0bdf08f14f8e96db9e522e544c44', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.4, 'Rank IC': 0.071, 'Rank ICIR': 0.4}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.400', 'recency_weight': '0.704', 'weight': '0.118'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260424_11 514043282495016329 (Recorders: 6/6)

	Recorder: b27201ab1f30418ebd55e3c381b554f8

		Model: {'id': 'b27201ab1f30418ebd55e3c381b554f8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.359, 'Rank IC': 0.058, 'Rank ICIR': 0.341}, 'data_train_vec': ['2020-04-24', '2024-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.341', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 5325a4be2ea2428ba1e6bea414f83a83

		Model: {'id': '5325a4be2ea2428ba1e6bea414f83a83', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.215, 'Rank IC': 0.045, 'Rank ICIR': 0.299}, 'data_train_vec': ['2021-04-24', '2025-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.299', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: a43e1d08f75145b4bbf571b786fd794b

		Model: {'id': 'a43e1d08f75145b4bbf571b786fd794b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.109, 'Rank IC': 0.044, 'Rank ICIR': 0.276}, 'data_train_vec': ['2022-04-24', '2025-04-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.276', 'recency_weight': '0.244', 'weight': '0.020'}

	Recorder: 7eb514aa07e14180a2f33e421ab85a80

		Model: {'id': '7eb514aa07e14180a2f33e421ab85a80', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.151, 'Rank IC': 0.064, 'Rank ICIR': 0.374}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.374', 'recency_weight': '0.347', 'weight': '0.051'}

	Recorder: 6b0cc05ebfe04a26a9a78b121fe6f146

		Model: {'id': '6b0cc05ebfe04a26a9a78b121fe6f146', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.097, 'Rank IC': 0.036, 'Rank ICIR': 0.255}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.255', 'recency_weight': '0.494', 'weight': '0.034'}

	Recorder: 53893a33a81b42a1b9ebff22b566881e

		Model: {'id': '53893a33a81b42a1b9ebff22b566881e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.07, 'ICIR': 0.487, 'Rank IC': 0.075, 'Rank ICIR': 0.466}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.466', 'recency_weight': '0.704', 'weight': '0.161'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260424_11 772477103953065294 (Recorders: 5/6)

	Recorder: 6d9a3f0ea0e34b8a8297709d0cacb629

		Model: {'id': '6d9a3f0ea0e34b8a8297709d0cacb629', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.388, 'Rank IC': 0.062, 'Rank ICIR': 0.48}, 'data_train_vec': ['2020-04-24', '2024-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.480', 'recency_weight': '0.121', 'weight': '0.029'}

	Recorder: 806afe11b115446fa2be9d87a6771b6e

		Model: {'id': '806afe11b115446fa2be9d87a6771b6e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.256, 'Rank IC': 0.049, 'Rank ICIR': 0.414}, 'data_train_vec': ['2021-04-24', '2025-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.414', 'recency_weight': '0.173', 'weight': '0.031'}

	Recorder: b2c156df29694750bbd282bfd9637328

		Model: {'id': 'b2c156df29694750bbd282bfd9637328', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.18, 'Rank IC': 0.05, 'Rank ICIR': 0.348}, 'data_train_vec': ['2022-04-24', '2025-04-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.348', 'recency_weight': '0.244', 'weight': '0.031'}

	Recorder: 9fdfea0a5fcf4c719e02f9eb303f4620

		Model: {'id': '9fdfea0a5fcf4c719e02f9eb303f4620', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.101, 'Rank IC': 0.039, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.290', 'recency_weight': '0.347', 'weight': '0.031'}

	Recorder: 76ec753c67fc4b1596aaec1ee8457de8

		Model: {'id': '76ec753c67fc4b1596aaec1ee8457de8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.377, 'Rank IC': 0.047, 'Rank ICIR': 0.288}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.288', 'recency_weight': '0.704', 'weight': '0.061'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260424_11 965147980474669960 (Recorders: 6/6)

	Recorder: 3dcf9414a9e145a0a9bf8fe60d6174e3

		Model: {'id': '3dcf9414a9e145a0a9bf8fe60d6174e3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.406, 'Rank IC': 0.061, 'Rank ICIR': 0.381}, 'data_train_vec': ['2020-04-24', '2024-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.381', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: e6984ce48f1e4479aeb70160b46d6116

		Model: {'id': 'e6984ce48f1e4479aeb70160b46d6116', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.248, 'Rank IC': 0.045, 'Rank ICIR': 0.308}, 'data_train_vec': ['2021-04-24', '2025-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.308', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 3a55d0da23f64a82b1ecdda9b99beac8

		Model: {'id': '3a55d0da23f64a82b1ecdda9b99beac8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.219, 'Rank IC': 0.053, 'Rank ICIR': 0.324}, 'data_train_vec': ['2022-04-24', '2025-04-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.324', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 8bb0cb415ae547c2bef4f6dc251a6600

		Model: {'id': '8bb0cb415ae547c2bef4f6dc251a6600', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.356, 'Rank IC': 0.074, 'Rank ICIR': 0.457}, 'data_train_vec': ['2023-04-24', '2025-07-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.457', 'recency_weight': '0.347', 'weight': '0.076'}

	Recorder: c1a2502f12f84ff18da0aabbf01e65b9

		Model: {'id': 'c1a2502f12f84ff18da0aabbf01e65b9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.176, 'Rank IC': 0.04, 'Rank ICIR': 0.303}, 'data_train_vec': ['2024-04-24', '2025-10-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.303', 'recency_weight': '0.494', 'weight': '0.048'}

	Recorder: c18a1297ae8f4e109ce2827c1785ecce

		Model: {'id': 'c18a1297ae8f4e109ce2827c1785ecce', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.386, 'Rank IC': 0.054, 'Rank ICIR': 0.331}, 'data_train_vec': ['2025-04-24', '2026-01-23'], 'train_time_vec': ['2026-04-24', '2026-04-24'], 'rank_icir': '0.331', 'recency_weight': '0.704', 'weight': '0.081'}
