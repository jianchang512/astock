# params 
 {'predict_dates': [{'start': '2026-05-26', 'end': '2026-05-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260526_13 874168107750645592 (Recorders: 6/6)

	Recorder: 21eeefd4ef51408b913924d477e793c8

		Model: {'id': '21eeefd4ef51408b913924d477e793c8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.338, 'Rank IC': 0.055, 'Rank ICIR': 0.38}, 'data_train_vec': ['2020-05-26', '2024-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.380', 'recency_weight': '0.122', 'weight': '0.023'}

	Recorder: 7d64ed304b094ebea3cc254453ae99f2

		Model: {'id': '7d64ed304b094ebea3cc254453ae99f2', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.224, 'Rank IC': 0.054, 'Rank ICIR': 0.375}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.375', 'recency_weight': '0.173', 'weight': '0.032'}

	Recorder: cfcc894981c34138877058125d0fe20b

		Model: {'id': 'cfcc894981c34138877058125d0fe20b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.228, 'Rank IC': 0.059, 'Rank ICIR': 0.366}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.366', 'recency_weight': '0.244', 'weight': '0.043'}

	Recorder: 193f0aec47c4405ca74abba3b46634a9

		Model: {'id': '193f0aec47c4405ca74abba3b46634a9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.257, 'Rank IC': 0.057, 'Rank ICIR': 0.378}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.378', 'recency_weight': '0.348', 'weight': '0.065'}

	Recorder: a5fac2d2df364296a5691d038d9f0252

		Model: {'id': 'a5fac2d2df364296a5691d038d9f0252', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.159, 'Rank IC': 0.047, 'Rank ICIR': 0.37}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.370', 'recency_weight': '0.496', 'weight': '0.089'}

	Recorder: ac1ea1e38ea04dc492ef22140a055944

		Model: {'id': 'ac1ea1e38ea04dc492ef22140a055944', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.518, 'Rank IC': 0.032, 'Rank ICIR': 0.215}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.215', 'recency_weight': '0.707', 'weight': '0.043'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260526_13 388449773951643279 (Recorders: 4/6)

	Recorder: 67c0a07792dd4761ba3e20190aa7e25b

		Model: {'id': '67c0a07792dd4761ba3e20190aa7e25b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.297, 'Rank IC': 0.054, 'Rank ICIR': 0.356}, 'data_train_vec': ['2020-05-26', '2024-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.356', 'recency_weight': '0.122', 'weight': '0.020'}

	Recorder: 1d1cd6d141eb49698d93d5f0cb9fd831

		Model: {'id': '1d1cd6d141eb49698d93d5f0cb9fd831', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.203, 'Rank IC': 0.053, 'Rank ICIR': 0.368}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.368', 'recency_weight': '0.173', 'weight': '0.031'}

	Recorder: fdb7906cbc464ca2b6a318f075fd1ab4

		Model: {'id': 'fdb7906cbc464ca2b6a318f075fd1ab4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.103, 'Rank IC': 0.055, 'Rank ICIR': 0.333}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.333', 'recency_weight': '0.244', 'weight': '0.035'}

	Recorder: d5783c21d83c4097a87946c1c817ec0d

		Model: {'id': 'd5783c21d83c4097a87946c1c817ec0d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.279, 'Rank IC': 0.012, 'Rank ICIR': 0.094}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.094', 'recency_weight': '0.707', 'weight': '0.008'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260526_12 554979387325219895 (Recorders: 4/6)

	Recorder: 46c1d237ced442548e43804a402e39f0

		Model: {'id': '46c1d237ced442548e43804a402e39f0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.298, 'Rank IC': 0.058, 'Rank ICIR': 0.444}, 'data_train_vec': ['2020-05-26', '2024-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.444', 'recency_weight': '0.122', 'weight': '0.031'}

	Recorder: ea194c8a786940f883604b63cb4ad2ea

		Model: {'id': 'ea194c8a786940f883604b63cb4ad2ea', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.23, 'Rank IC': 0.058, 'Rank ICIR': 0.441}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.441', 'recency_weight': '0.173', 'weight': '0.044'}

	Recorder: 5806c2b8e57d47cb8900fa6d2f60b63c

		Model: {'id': '5806c2b8e57d47cb8900fa6d2f60b63c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.135, 'Rank IC': 0.059, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.048'}

	Recorder: 1deee0610ae94965bb332666160fd593

		Model: {'id': '1deee0610ae94965bb332666160fd593', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.431, 'Rank IC': 0.081, 'Rank ICIR': 0.405}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.405', 'recency_weight': '0.707', 'weight': '0.152'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260526_12 456727672339233442 (Recorders: 6/6)

	Recorder: 10e2c46351c9493baff5b224db2cbf49

		Model: {'id': '10e2c46351c9493baff5b224db2cbf49', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.28, 'Rank IC': 0.055, 'Rank ICIR': 0.378}, 'data_train_vec': ['2020-05-26', '2024-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.378', 'recency_weight': '0.122', 'weight': '0.023'}

	Recorder: 9073183fbf2e40da8cf186f436d51302

		Model: {'id': '9073183fbf2e40da8cf186f436d51302', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.161, 'Rank IC': 0.048, 'Rank ICIR': 0.377}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.377', 'recency_weight': '0.173', 'weight': '0.032'}

	Recorder: d89efb7b1e9848ff9a8f2ff0e050adc1

		Model: {'id': 'd89efb7b1e9848ff9a8f2ff0e050adc1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.319, 'Rank IC': 0.066, 'Rank ICIR': 0.422}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.422', 'recency_weight': '0.244', 'weight': '0.057'}

	Recorder: 8217d7b73a474d99abdbb915759f8a2e

		Model: {'id': '8217d7b73a474d99abdbb915759f8a2e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.194, 'Rank IC': 0.054, 'Rank ICIR': 0.352}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.352', 'recency_weight': '0.348', 'weight': '0.056'}

	Recorder: d4d4f430533745f89d5d1ec07bec5225

		Model: {'id': 'd4d4f430533745f89d5d1ec07bec5225', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.188, 'Rank IC': 0.043, 'Rank ICIR': 0.364}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.364', 'recency_weight': '0.496', 'weight': '0.086'}

	Recorder: 0bb11bda8b6b4688ae1c71ac00e39b94

		Model: {'id': '0bb11bda8b6b4688ae1c71ac00e39b94', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.53, 'Rank IC': 0.045, 'Rank ICIR': 0.295}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.295', 'recency_weight': '0.707', 'weight': '0.081'}
