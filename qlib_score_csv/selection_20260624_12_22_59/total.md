# params 
 {'predict_dates': [{'start': '2026-06-24', 'end': '2026-06-24'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260624_11 217756097520592436 (Recorders: 6/6)

	Recorder: 5214adf91ca84d08a5a7560219b0a223

		Model: {'id': '5214adf91ca84d08a5a7560219b0a223', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.354, 'Rank IC': 0.067, 'Rank ICIR': 0.447}, 'data_train_vec': ['2020-06-24', '2024-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.447', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 0bfdce9301154d2a988166f06fc9daaa

		Model: {'id': '0bfdce9301154d2a988166f06fc9daaa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.26, 'Rank IC': 0.072, 'Rank ICIR': 0.442}, 'data_train_vec': ['2021-06-24', '2025-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.442', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: e78b387b16554f4bb61dea2cd47ec7b9

		Model: {'id': 'e78b387b16554f4bb61dea2cd47ec7b9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.123, 'Rank IC': 0.058, 'Rank ICIR': 0.345}, 'data_train_vec': ['2022-06-24', '2025-06-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.345', 'recency_weight': '0.244', 'weight': '0.017'}

	Recorder: dc90c626b61e4e2098e5d5eb63b11ca8

		Model: {'id': 'dc90c626b61e4e2098e5d5eb63b11ca8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.297, 'Rank IC': 0.072, 'Rank ICIR': 0.445}, 'data_train_vec': ['2023-06-24', '2025-09-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.445', 'recency_weight': '0.348', 'weight': '0.040'}

	Recorder: ee97dee9ad2540daa115ff1955821594

		Model: {'id': 'ee97dee9ad2540daa115ff1955821594', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.407, 'Rank IC': 0.069, 'Rank ICIR': 0.536}, 'data_train_vec': ['2024-06-24', '2025-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.536', 'recency_weight': '0.494', 'weight': '0.083'}

	Recorder: 49ea047e3e9448da9b81dbd723d323cd

		Model: {'id': '49ea047e3e9448da9b81dbd723d323cd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.112, 'ICIR': 0.671, 'Rank IC': 0.086, 'Rank ICIR': 0.485}, 'data_train_vec': ['2025-06-24', '2026-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.485', 'recency_weight': '0.699', 'weight': '0.096'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260624_11 156668334241739814 (Recorders: 6/6)

	Recorder: fff06cfb58b44fd6a232c29a292048b7

		Model: {'id': 'fff06cfb58b44fd6a232c29a292048b7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.296, 'Rank IC': 0.063, 'Rank ICIR': 0.412}, 'data_train_vec': ['2020-06-24', '2024-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.412', 'recency_weight': '0.121', 'weight': '0.012'}

	Recorder: 52d86d6bb53e4d8589e481000f040824

		Model: {'id': '52d86d6bb53e4d8589e481000f040824', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.221, 'Rank IC': 0.064, 'Rank ICIR': 0.4}, 'data_train_vec': ['2021-06-24', '2025-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.400', 'recency_weight': '0.171', 'weight': '0.016'}

	Recorder: 00627665614f4c2999f096cef1c193a9

		Model: {'id': '00627665614f4c2999f096cef1c193a9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.115, 'Rank IC': 0.061, 'Rank ICIR': 0.365}, 'data_train_vec': ['2022-06-24', '2025-06-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.365', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: 149ff07bc954429f8a4a83fab4382c67

		Model: {'id': '149ff07bc954429f8a4a83fab4382c67', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.241, 'Rank IC': 0.066, 'Rank ICIR': 0.401}, 'data_train_vec': ['2023-06-24', '2025-09-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.401', 'recency_weight': '0.348', 'weight': '0.033'}

	Recorder: c3a02eca1a1c4352afd15b8c37c96872

		Model: {'id': 'c3a02eca1a1c4352afd15b8c37c96872', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.308, 'Rank IC': 0.067, 'Rank ICIR': 0.533}, 'data_train_vec': ['2024-06-24', '2025-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.533', 'recency_weight': '0.494', 'weight': '0.082'}

	Recorder: 62fc8b86cb6c4bd8ab6dd6bc96e59f61

		Model: {'id': '62fc8b86cb6c4bd8ab6dd6bc96e59f61', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.104, 'ICIR': 0.514, 'Rank IC': 0.076, 'Rank ICIR': 0.408}, 'data_train_vec': ['2025-06-24', '2026-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.408', 'recency_weight': '0.699', 'weight': '0.068'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260624_11 754884333156975334 (Recorders: 6/6)

	Recorder: 0425230100344862911ea978d4ec835a

		Model: {'id': '0425230100344862911ea978d4ec835a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.325, 'Rank IC': 0.068, 'Rank ICIR': 0.489}, 'data_train_vec': ['2020-06-24', '2024-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.489', 'recency_weight': '0.121', 'weight': '0.017'}

	Recorder: aa587c1b317849d3828d824df6390989

		Model: {'id': 'aa587c1b317849d3828d824df6390989', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.212, 'Rank IC': 0.066, 'Rank ICIR': 0.456}, 'data_train_vec': ['2021-06-24', '2025-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.456', 'recency_weight': '0.171', 'weight': '0.021'}

	Recorder: 44f136bcf6c4454b96334f365270705e

		Model: {'id': '44f136bcf6c4454b96334f365270705e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.108, 'Rank IC': 0.059, 'Rank ICIR': 0.375}, 'data_train_vec': ['2022-06-24', '2025-06-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.375', 'recency_weight': '0.244', 'weight': '0.020'}

	Recorder: 796aa2454a4e499cae1601fd843b3f84

		Model: {'id': '796aa2454a4e499cae1601fd843b3f84', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.184, 'Rank IC': 0.052, 'Rank ICIR': 0.363}, 'data_train_vec': ['2023-06-24', '2025-09-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.363', 'recency_weight': '0.348', 'weight': '0.027'}

	Recorder: daed845741f0410292ff233758b8a814

		Model: {'id': 'daed845741f0410292ff233758b8a814', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.277, 'Rank IC': 0.056, 'Rank ICIR': 0.401}, 'data_train_vec': ['2024-06-24', '2025-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.401', 'recency_weight': '0.494', 'weight': '0.046'}

	Recorder: 0b75102ccc84497b80954e82629a3403

		Model: {'id': '0b75102ccc84497b80954e82629a3403', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.091, 'ICIR': 0.411, 'Rank IC': 0.07, 'Rank ICIR': 0.354}, 'data_train_vec': ['2025-06-24', '2026-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.354', 'recency_weight': '0.699', 'weight': '0.051'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260624_11 641391322709004936 (Recorders: 6/6)

	Recorder: a476ee4bae604e03b784c36f121c79b7

		Model: {'id': 'a476ee4bae604e03b784c36f121c79b7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.313, 'Rank IC': 0.064, 'Rank ICIR': 0.43}, 'data_train_vec': ['2020-06-24', '2024-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.430', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: c5877aa9ebda4b4ba196076f4dacd7be

		Model: {'id': 'c5877aa9ebda4b4ba196076f4dacd7be', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.264, 'Rank IC': 0.071, 'Rank ICIR': 0.475}, 'data_train_vec': ['2021-06-24', '2025-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.475', 'recency_weight': '0.171', 'weight': '0.023'}

	Recorder: cb15978de01f4211a36c27362a626d96

		Model: {'id': 'cb15978de01f4211a36c27362a626d96', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.131, 'Rank IC': 0.067, 'Rank ICIR': 0.393}, 'data_train_vec': ['2022-06-24', '2025-06-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.393', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: 279916ae51734fc6a7015533ae76eb10

		Model: {'id': '279916ae51734fc6a7015533ae76eb10', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.189, 'Rank IC': 0.057, 'Rank ICIR': 0.369}, 'data_train_vec': ['2023-06-24', '2025-09-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.369', 'recency_weight': '0.348', 'weight': '0.028'}

	Recorder: 0e020dca67aa449a9caccc62206935d3

		Model: {'id': '0e020dca67aa449a9caccc62206935d3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.258, 'Rank IC': 0.067, 'Rank ICIR': 0.511}, 'data_train_vec': ['2024-06-24', '2025-12-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.511', 'recency_weight': '0.494', 'weight': '0.075'}

	Recorder: d4714ff7512142ab89760b80c12f9d17

		Model: {'id': 'd4714ff7512142ab89760b80c12f9d17', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.1, 'ICIR': 0.614, 'Rank IC': 0.089, 'Rank ICIR': 0.621}, 'data_train_vec': ['2025-06-24', '2026-03-23'], 'train_time_vec': ['2026-06-24', '2026-06-24'], 'rank_icir': '0.621', 'recency_weight': '0.699', 'weight': '0.157'}
