# params 
 {'predict_dates': [{'start': '2026-05-18', 'end': '2026-05-18'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260518_11 529746504830492709 (Recorders: 6/6)

	Recorder: 2286d12d30644c2ca1fc3ded3e210797

		Model: {'id': '2286d12d30644c2ca1fc3ded3e210797', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.373, 'Rank IC': 0.056, 'Rank ICIR': 0.38}, 'data_train_vec': ['2020-05-18', '2024-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.380', 'recency_weight': '0.122', 'weight': '0.028'}

	Recorder: 468c7d11657a481cb741a8ae9495cf45

		Model: {'id': '468c7d11657a481cb741a8ae9495cf45', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.184, 'Rank IC': 0.042, 'Rank ICIR': 0.285}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.285', 'recency_weight': '0.173', 'weight': '0.022'}

	Recorder: a9db2806b9ac4f9f9a859007dcf40aa1

		Model: {'id': 'a9db2806b9ac4f9f9a859007dcf40aa1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.256, 'Rank IC': 0.061, 'Rank ICIR': 0.374}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.374', 'recency_weight': '0.244', 'weight': '0.054'}

	Recorder: 8eeb6c08a63245d0aa20d7dbc9f9a930

		Model: {'id': '8eeb6c08a63245d0aa20d7dbc9f9a930', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.097, 'Rank IC': 0.044, 'Rank ICIR': 0.274}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.274', 'recency_weight': '0.348', 'weight': '0.041'}

	Recorder: ebf2f6a2fdde4a02a97ada52c201585a

		Model: {'id': 'ebf2f6a2fdde4a02a97ada52c201585a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.124, 'Rank IC': 0.033, 'Rank ICIR': 0.27}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.270', 'recency_weight': '0.496', 'weight': '0.057'}

	Recorder: bc158039e5e446a6aa63375d83ea8ed7

		Model: {'id': 'bc158039e5e446a6aa63375d83ea8ed7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.37, 'Rank IC': 0.032, 'Rank ICIR': 0.261}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.261', 'recency_weight': '0.707', 'weight': '0.076'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260518_11 186782933549489138 (Recorders: 4/6)

	Recorder: 928b29f798ed46c2b86fbfba2c33d5f1

		Model: {'id': '928b29f798ed46c2b86fbfba2c33d5f1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.305, 'Rank IC': 0.054, 'Rank ICIR': 0.345}, 'data_train_vec': ['2020-05-18', '2024-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.345', 'recency_weight': '0.122', 'weight': '0.023'}

	Recorder: e33be6213d68440f9ee3526a2b531dcc

		Model: {'id': 'e33be6213d68440f9ee3526a2b531dcc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.136, 'Rank IC': 0.04, 'Rank ICIR': 0.269}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.269', 'recency_weight': '0.173', 'weight': '0.020'}

	Recorder: 4bfffe7496c84816be9f3b9e23fe0523

		Model: {'id': '4bfffe7496c84816be9f3b9e23fe0523', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.126, 'Rank IC': 0.053, 'Rank ICIR': 0.325}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.325', 'recency_weight': '0.244', 'weight': '0.041'}

	Recorder: 348789e8fa9147aab66031fcf030962b

		Model: {'id': '348789e8fa9147aab66031fcf030962b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.366, 'Rank IC': 0.027, 'Rank ICIR': 0.268}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.268', 'recency_weight': '0.707', 'weight': '0.080'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260518_11 821704032503557820 (Recorders: 4/6)

	Recorder: db1be7c86f8644c19d3f171a01409458

		Model: {'id': 'db1be7c86f8644c19d3f171a01409458', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.309, 'Rank IC': 0.057, 'Rank ICIR': 0.457}, 'data_train_vec': ['2020-05-18', '2024-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.457', 'recency_weight': '0.122', 'weight': '0.040'}

	Recorder: 3b639ff1226545e09c68b69ddd4bc0a0

		Model: {'id': '3b639ff1226545e09c68b69ddd4bc0a0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.21, 'Rank IC': 0.051, 'Rank ICIR': 0.407}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.407', 'recency_weight': '0.173', 'weight': '0.045'}

	Recorder: ce93e295289949a4ae57ca634ed63de2

		Model: {'id': 'ce93e295289949a4ae57ca634ed63de2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.118, 'Rank IC': 0.055, 'Rank ICIR': 0.364}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.364', 'recency_weight': '0.244', 'weight': '0.051'}

	Recorder: 69952b9035c5430592d5b4f0f440339e

		Model: {'id': '69952b9035c5430592d5b4f0f440339e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.274, 'Rank IC': 0.043, 'Rank ICIR': 0.262}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.262', 'recency_weight': '0.707', 'weight': '0.077'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260518_11 884969367007886099 (Recorders: 5/6)

	Recorder: 341f00c51f45409496e69e580210ed9e

		Model: {'id': '341f00c51f45409496e69e580210ed9e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.31, 'Rank IC': 0.055, 'Rank ICIR': 0.388}, 'data_train_vec': ['2020-05-18', '2024-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.388', 'recency_weight': '0.122', 'weight': '0.029'}

	Recorder: d17c08d583f04ffdbad311b8f65f0060

		Model: {'id': 'd17c08d583f04ffdbad311b8f65f0060', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.14, 'Rank IC': 0.041, 'Rank ICIR': 0.29}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.290', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 1f23904c28104676b26fadb006c217e8

		Model: {'id': '1f23904c28104676b26fadb006c217e8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.211, 'Rank IC': 0.055, 'Rank ICIR': 0.343}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.343', 'recency_weight': '0.244', 'weight': '0.045'}

	Recorder: 49e11a1cb5f0410faef590f7da418da4

		Model: {'id': '49e11a1cb5f0410faef590f7da418da4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.103, 'Rank IC': 0.041, 'Rank ICIR': 0.347}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.347', 'recency_weight': '0.496', 'weight': '0.094'}

	Recorder: 662c30c107fe4ba597db612ab1f252f8

		Model: {'id': '662c30c107fe4ba597db612ab1f252f8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.451, 'Rank IC': 0.046, 'Rank ICIR': 0.37}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.370', 'recency_weight': '0.707', 'weight': '0.153'}
