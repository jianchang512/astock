# params 
 {'predict_dates': [{'start': '2026-05-07', 'end': '2026-05-07'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260507_11 793148664154597581 (Recorders: 6/6)

	Recorder: ad5dff154ac54a84aa326a1bd4b1e1ff

		Model: {'id': 'ad5dff154ac54a84aa326a1bd4b1e1ff', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.417, 'Rank IC': 0.055, 'Rank ICIR': 0.362}, 'data_train_vec': ['2020-05-07', '2024-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.362', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: 8b2035805f1a47d590de6fa74f1bd52d

		Model: {'id': '8b2035805f1a47d590de6fa74f1bd52d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.264, 'Rank IC': 0.049, 'Rank ICIR': 0.325}, 'data_train_vec': ['2021-05-07', '2025-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.325', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 9c9f883449fd402f8255edcd07e38138

		Model: {'id': '9c9f883449fd402f8255edcd07e38138', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.199, 'Rank IC': 0.046, 'Rank ICIR': 0.288}, 'data_train_vec': ['2022-05-07', '2025-05-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.288', 'recency_weight': '0.244', 'weight': '0.015'}

	Recorder: 1d3d702aa8ab4e83b64790074b9d8f70

		Model: {'id': '1d3d702aa8ab4e83b64790074b9d8f70', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.173, 'Rank IC': 0.04, 'Rank ICIR': 0.251}, 'data_train_vec': ['2023-05-07', '2025-08-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.251', 'recency_weight': '0.348', 'weight': '0.016'}

	Recorder: 64a3ad81adb348dc8a6f2440a0d9b7fa

		Model: {'id': '64a3ad81adb348dc8a6f2440a0d9b7fa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.182, 'Rank IC': 0.021, 'Rank ICIR': 0.15}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.150', 'recency_weight': '0.496', 'weight': '0.008'}

	Recorder: 247828bedcec45d78a7d0ffb5f4ea045

		Model: {'id': '247828bedcec45d78a7d0ffb5f4ea045', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.087, 'ICIR': 0.698, 'Rank IC': 0.084, 'Rank ICIR': 0.66}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.660', 'recency_weight': '0.707', 'weight': '0.231'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260507_11 356627248550501323 (Recorders: 4/6)

	Recorder: c6e0a05683c04c4cb668db7ca1c2247c

		Model: {'id': 'c6e0a05683c04c4cb668db7ca1c2247c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.377, 'Rank IC': 0.057, 'Rank ICIR': 0.375}, 'data_train_vec': ['2020-05-07', '2024-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.375', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: 4334749f99744407b7d3c662112248c4

		Model: {'id': '4334749f99744407b7d3c662112248c4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.21, 'Rank IC': 0.045, 'Rank ICIR': 0.296}, 'data_train_vec': ['2021-05-07', '2025-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.296', 'recency_weight': '0.173', 'weight': '0.011'}

	Recorder: 03aaefe329e647c2beb8ddca13c28c40

		Model: {'id': '03aaefe329e647c2beb8ddca13c28c40', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.119, 'Rank IC': 0.044, 'Rank ICIR': 0.271}, 'data_train_vec': ['2022-05-07', '2025-05-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.271', 'recency_weight': '0.244', 'weight': '0.013'}

	Recorder: 81b054254d474ce7b30e093cf1133898

		Model: {'id': '81b054254d474ce7b30e093cf1133898', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.538, 'Rank IC': 0.045, 'Rank ICIR': 0.494}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.494', 'recency_weight': '0.707', 'weight': '0.130'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260507_11 498636823845589386 (Recorders: 4/6)

	Recorder: 3b8f18a641fd42a2987124d2d59f2cad

		Model: {'id': '3b8f18a641fd42a2987124d2d59f2cad', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.355, 'Rank IC': 0.056, 'Rank ICIR': 0.439}, 'data_train_vec': ['2020-05-07', '2024-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.439', 'recency_weight': '0.122', 'weight': '0.018'}

	Recorder: 2dd347ca2adb47c7a7c33df1eb7f0bdc

		Model: {'id': '2dd347ca2adb47c7a7c33df1eb7f0bdc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.269, 'Rank IC': 0.051, 'Rank ICIR': 0.424}, 'data_train_vec': ['2021-05-07', '2025-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.424', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 7ba430b4369a49bc9533011303906715

		Model: {'id': '7ba430b4369a49bc9533011303906715', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.153, 'Rank IC': 0.052, 'Rank ICIR': 0.364}, 'data_train_vec': ['2022-05-07', '2025-05-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.364', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: 6cc17db437ff459b94152495a2e50b9a

		Model: {'id': '6cc17db437ff459b94152495a2e50b9a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.071, 'ICIR': 0.485, 'Rank IC': 0.06, 'Rank ICIR': 0.415}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.415', 'recency_weight': '0.707', 'weight': '0.092'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260507_11 542466547496010465 (Recorders: 6/6)

	Recorder: fdcf8261b77f4684a6ea8969cdc7f417

		Model: {'id': 'fdcf8261b77f4684a6ea8969cdc7f417', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.345, 'Rank IC': 0.053, 'Rank ICIR': 0.349}, 'data_train_vec': ['2020-05-07', '2024-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.349', 'recency_weight': '0.122', 'weight': '0.011'}

	Recorder: 11d657268f7148a39b0131c62a2c43cb

		Model: {'id': '11d657268f7148a39b0131c62a2c43cb', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.273, 'Rank IC': 0.048, 'Rank ICIR': 0.345}, 'data_train_vec': ['2021-05-07', '2025-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.345', 'recency_weight': '0.173', 'weight': '0.016'}

	Recorder: 28164ed3ad784d4fbcf6c5ff9d70fe50

		Model: {'id': '28164ed3ad784d4fbcf6c5ff9d70fe50', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.243, 'Rank IC': 0.053, 'Rank ICIR': 0.341}, 'data_train_vec': ['2022-05-07', '2025-05-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.341', 'recency_weight': '0.244', 'weight': '0.021'}

	Recorder: aa3b0d35a26b46698efd438c6157422e

		Model: {'id': 'aa3b0d35a26b46698efd438c6157422e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.206, 'Rank IC': 0.035, 'Rank ICIR': 0.234}, 'data_train_vec': ['2023-05-07', '2025-08-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.234', 'recency_weight': '0.348', 'weight': '0.014'}

	Recorder: b50c0d858e5b4c92a89f6c52171aea24

		Model: {'id': 'b50c0d858e5b4c92a89f6c52171aea24', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.164, 'Rank IC': 0.021, 'Rank ICIR': 0.171}, 'data_train_vec': ['2024-05-07', '2025-11-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.171', 'recency_weight': '0.496', 'weight': '0.011'}

	Recorder: 51891df982d145d8a82bc9d073b886ac

		Model: {'id': '51891df982d145d8a82bc9d073b886ac', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.07, 'ICIR': 0.577, 'Rank IC': 0.084, 'Rank ICIR': 0.758}, 'data_train_vec': ['2025-05-07', '2026-02-06'], 'train_time_vec': ['2026-05-07', '2026-05-07'], 'rank_icir': '0.758', 'recency_weight': '0.707', 'weight': '0.305'}
