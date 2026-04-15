# params 
 {'predict_dates': [{'start': '2026-04-14', 'end': '2026-04-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260415_13 602840028531775355 (Recorders: 6/6)

	Recorder: c353aa64eeb44f9e89b3711928f4dceb

		Model: {'id': 'c353aa64eeb44f9e89b3711928f4dceb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.445, 'Rank IC': 0.065, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.383', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: ced4036df9ff4a809a64d72c37db011f

		Model: {'id': 'ced4036df9ff4a809a64d72c37db011f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.346, 'Rank IC': 0.052, 'Rank ICIR': 0.332}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.332', 'recency_weight': '0.173', 'weight': '0.020'}

	Recorder: 393163998fe34d2f88b33f5625dfefb6

		Model: {'id': '393163998fe34d2f88b33f5625dfefb6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.213, 'Rank IC': 0.04, 'Rank ICIR': 0.244}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.244', 'recency_weight': '0.245', 'weight': '0.015'}

	Recorder: bf3946a1c9df4846af594fe04c9ff165

		Model: {'id': 'bf3946a1c9df4846af594fe04c9ff165', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.4, 'Rank IC': 0.062, 'Rank ICIR': 0.411}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.411', 'recency_weight': '0.348', 'weight': '0.061'}

	Recorder: 3cecceda9e6042e1b146ebe5eed607b7

		Model: {'id': '3cecceda9e6042e1b146ebe5eed607b7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.215, 'Rank IC': 0.033, 'Rank ICIR': 0.28}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.280', 'recency_weight': '0.496', 'weight': '0.041'}

	Recorder: 87118b21622f4b2c9cb8b4653c7f64e8

		Model: {'id': '87118b21622f4b2c9cb8b4653c7f64e8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.272, 'Rank IC': 0.064, 'Rank ICIR': 0.353}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.353', 'recency_weight': '0.707', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260415_13 675141808854936160 (Recorders: 6/6)

	Recorder: 9812511bd78f4fecb34c8fe3b9720902

		Model: {'id': '9812511bd78f4fecb34c8fe3b9720902', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.365, 'Rank IC': 0.056, 'Rank ICIR': 0.319}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.319', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: 5614d1f9ef4742e292ac523030373f01

		Model: {'id': '5614d1f9ef4742e292ac523030373f01', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.271, 'Rank IC': 0.05, 'Rank ICIR': 0.308}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.308', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: ecc21ede34f14322946f799765da7efb

		Model: {'id': 'ecc21ede34f14322946f799765da7efb', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.106, 'Rank IC': 0.038, 'Rank ICIR': 0.225}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.225', 'recency_weight': '0.245', 'weight': '0.013'}

	Recorder: 3a95c49407be41db92013dea0fdcdc45

		Model: {'id': '3a95c49407be41db92013dea0fdcdc45', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.19, 'Rank IC': 0.055, 'Rank ICIR': 0.381}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.381', 'recency_weight': '0.348', 'weight': '0.053'}

	Recorder: 6938b7fcadb14c78bccb5780cce2314b

		Model: {'id': '6938b7fcadb14c78bccb5780cce2314b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.18, 'Rank IC': 0.035, 'Rank ICIR': 0.263}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.263', 'recency_weight': '0.496', 'weight': '0.036'}

	Recorder: 67a3fcf15cb1491783ff8bc424e2e7ee

		Model: {'id': '67a3fcf15cb1491783ff8bc424e2e7ee', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.37, 'Rank IC': 0.073, 'Rank ICIR': 0.457}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.457', 'recency_weight': '0.707', 'weight': '0.154'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260415_13 641382357931245633 (Recorders: 5/6)

	Recorder: 86d7a50563ff445eb3a610bdf06788fb

		Model: {'id': '86d7a50563ff445eb3a610bdf06788fb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.392, 'Rank IC': 0.063, 'Rank ICIR': 0.461}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.461', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: 89d36d0df5844e63a1e3a71796d8672a

		Model: {'id': '89d36d0df5844e63a1e3a71796d8672a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.352, 'Rank IC': 0.056, 'Rank ICIR': 0.481}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.481', 'recency_weight': '0.173', 'weight': '0.042'}

	Recorder: ac1a8b23d5c947f5a3867e33cab64234

		Model: {'id': 'ac1a8b23d5c947f5a3867e33cab64234', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.221, 'Rank IC': 0.051, 'Rank ICIR': 0.351}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.351', 'recency_weight': '0.245', 'weight': '0.032'}

	Recorder: ca2e86fb7a4c4c6294d95ba9a76958fe

		Model: {'id': 'ca2e86fb7a4c4c6294d95ba9a76958fe', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.206, 'Rank IC': 0.046, 'Rank ICIR': 0.344}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.344', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: 810a84ebcfba48578df0fc2e4e382843

		Model: {'id': '810a84ebcfba48578df0fc2e4e382843', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.245, 'Rank IC': 0.035, 'Rank ICIR': 0.208}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.208', 'recency_weight': '0.707', 'weight': '0.032'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260415_13 186261547442471083 (Recorders: 6/6)

	Recorder: ea69104ac3164d118bfeb96c8ed0ac5e

		Model: {'id': 'ea69104ac3164d118bfeb96c8ed0ac5e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.404, 'Rank IC': 0.063, 'Rank ICIR': 0.389}, 'data_train_vec': ['2020-04-15', '2024-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.389', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 8c786c0a7381443189722b914096ac4b

		Model: {'id': '8c786c0a7381443189722b914096ac4b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.282, 'Rank IC': 0.052, 'Rank ICIR': 0.356}, 'data_train_vec': ['2021-04-15', '2025-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.356', 'recency_weight': '0.173', 'weight': '0.023'}

	Recorder: 2dd90a521ab0463d94007eecb97dba00

		Model: {'id': '2dd90a521ab0463d94007eecb97dba00', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.2, 'Rank IC': 0.045, 'Rank ICIR': 0.267}, 'data_train_vec': ['2022-04-15', '2025-04-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.267', 'recency_weight': '0.245', 'weight': '0.018'}

	Recorder: 7d31fd8b7eac40dc81864277f42269f3

		Model: {'id': '7d31fd8b7eac40dc81864277f42269f3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.367, 'Rank IC': 0.068, 'Rank ICIR': 0.477}, 'data_train_vec': ['2023-04-15', '2025-07-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.477', 'recency_weight': '0.348', 'weight': '0.083'}

	Recorder: 36ea9873d2bb4baa866ba8fa2c00ea44

		Model: {'id': '36ea9873d2bb4baa866ba8fa2c00ea44', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.179, 'Rank IC': 0.031, 'Rank ICIR': 0.254}, 'data_train_vec': ['2024-04-15', '2025-10-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.254', 'recency_weight': '0.496', 'weight': '0.033'}

	Recorder: b67b6a0f4c844bd08d73655489e80e71

		Model: {'id': 'b67b6a0f4c844bd08d73655489e80e71', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.34, 'Rank IC': 0.065, 'Rank ICIR': 0.396}, 'data_train_vec': ['2025-04-15', '2026-01-14'], 'train_time_vec': ['2026-04-15', '2026-04-15'], 'rank_icir': '0.396', 'recency_weight': '0.707', 'weight': '0.116'}
