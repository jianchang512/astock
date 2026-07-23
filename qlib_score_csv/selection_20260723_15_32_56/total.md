# params 
 {'predict_dates': [{'start': '2026-07-23', 'end': '2026-07-23'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260723_15 673934968721949550 (Recorders: 5/6)

	Recorder: f2b51a231ab84e6b92ed8019728621e9

		Model: {'id': 'f2b51a231ab84e6b92ed8019728621e9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.321, 'Rank IC': 0.063, 'Rank ICIR': 0.403}, 'data_train_vec': ['2020-07-23', '2025-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.403', 'recency_weight': '0.122', 'weight': '0.046'}

	Recorder: cbfe84382bf64d2299dd7124c43b383a

		Model: {'id': 'cbfe84382bf64d2299dd7124c43b383a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.183, 'Rank IC': 0.06, 'Rank ICIR': 0.359}, 'data_train_vec': ['2021-07-23', '2025-04-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.359', 'recency_weight': '0.172', 'weight': '0.051'}

	Recorder: dabce16248264eb19723d489f2f1fab9

		Model: {'id': 'dabce16248264eb19723d489f2f1fab9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.134, 'Rank IC': 0.056, 'Rank ICIR': 0.331}, 'data_train_vec': ['2022-07-23', '2025-07-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.331', 'recency_weight': '0.244', 'weight': '0.062'}

	Recorder: 792271a101054898b4f28ad5fdee42f9

		Model: {'id': '792271a101054898b4f28ad5fdee42f9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.142, 'Rank IC': 0.065, 'Rank ICIR': 0.401}, 'data_train_vec': ['2023-07-23', '2025-10-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.401', 'recency_weight': '0.348', 'weight': '0.129'}

	Recorder: a973af1ea3e9475f94d0f97a350aa1de

		Model: {'id': 'a973af1ea3e9475f94d0f97a350aa1de', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.076, 'Rank IC': 0.023, 'Rank ICIR': 0.125}, 'data_train_vec': ['2024-07-23', '2026-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.125', 'recency_weight': '0.496', 'weight': '0.018'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260723_15 574958621592959988 (Recorders: 5/6)

	Recorder: bba4149ae04d44faaf887b2ed5b8172b

		Model: {'id': 'bba4149ae04d44faaf887b2ed5b8172b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.324, 'Rank IC': 0.066, 'Rank ICIR': 0.42}, 'data_train_vec': ['2020-07-23', '2025-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.420', 'recency_weight': '0.122', 'weight': '0.049'}

	Recorder: 59d7583bdb464caaaeeb37cba93a1203

		Model: {'id': '59d7583bdb464caaaeeb37cba93a1203', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.196, 'Rank IC': 0.058, 'Rank ICIR': 0.365}, 'data_train_vec': ['2021-07-23', '2025-04-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.365', 'recency_weight': '0.172', 'weight': '0.053'}

	Recorder: c74fc8f153034c948d2f25a64f7128d4

		Model: {'id': 'c74fc8f153034c948d2f25a64f7128d4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.12, 'Rank IC': 0.047, 'Rank ICIR': 0.3}, 'data_train_vec': ['2022-07-23', '2025-07-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.300', 'recency_weight': '0.244', 'weight': '0.051'}

	Recorder: 76eef75239534345a3872b924a00338f

		Model: {'id': '76eef75239534345a3872b924a00338f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.259, 'Rank IC': 0.069, 'Rank ICIR': 0.457}, 'data_train_vec': ['2023-07-23', '2025-10-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.457', 'recency_weight': '0.348', 'weight': '0.168'}

	Recorder: 27f5280ce2fa4769804bb1372f40aadd

		Model: {'id': '27f5280ce2fa4769804bb1372f40aadd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.153, 'Rank IC': 0.017, 'Rank ICIR': 0.096}, 'data_train_vec': ['2024-07-23', '2026-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.096', 'recency_weight': '0.496', 'weight': '0.011'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260723_14 126039726134584589 (Recorders: 4/6)

	Recorder: ea1d1dc105784a2d856968da0fe1ca0f

		Model: {'id': 'ea1d1dc105784a2d856968da0fe1ca0f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.205, 'Rank IC': 0.053, 'Rank ICIR': 0.329}, 'data_train_vec': ['2020-07-23', '2025-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.329', 'recency_weight': '0.122', 'weight': '0.030'}

	Recorder: f3d78807e0114d7e9d40522679c721bc

		Model: {'id': 'f3d78807e0114d7e9d40522679c721bc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.087, 'Rank IC': 0.042, 'Rank ICIR': 0.258}, 'data_train_vec': ['2021-07-23', '2025-04-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.258', 'recency_weight': '0.172', 'weight': '0.026'}

	Recorder: a5107e8ccd3d42e780878661ca216425

		Model: {'id': 'a5107e8ccd3d42e780878661ca216425', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.08, 'Rank IC': 0.043, 'Rank ICIR': 0.275}, 'data_train_vec': ['2022-07-23', '2025-07-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.275', 'recency_weight': '0.244', 'weight': '0.043'}

	Recorder: 97128097f18b464ab484da247d03d4b7

		Model: {'id': '97128097f18b464ab484da247d03d4b7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.21, 'Rank IC': 0.054, 'Rank ICIR': 0.328}, 'data_train_vec': ['2023-07-23', '2025-10-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.328', 'recency_weight': '0.348', 'weight': '0.086'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260723_14 485045127377284070 (Recorders: 3/6)

	Recorder: 81886f34668047b391b7f9a0a6f71325

		Model: {'id': '81886f34668047b391b7f9a0a6f71325', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.312, 'Rank IC': 0.065, 'Rank ICIR': 0.434}, 'data_train_vec': ['2020-07-23', '2025-01-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.434', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: f79d6882296e458184846dcd62cc11a5

		Model: {'id': 'f79d6882296e458184846dcd62cc11a5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.118, 'Rank IC': 0.06, 'Rank ICIR': 0.368}, 'data_train_vec': ['2021-07-23', '2025-04-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.368', 'recency_weight': '0.172', 'weight': '0.054'}

	Recorder: 5f1bd4be71714674b6f99ea034752292

		Model: {'id': '5f1bd4be71714674b6f99ea034752292', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.095, 'Rank IC': 0.053, 'Rank ICIR': 0.356}, 'data_train_vec': ['2022-07-23', '2025-07-22'], 'train_time_vec': ['2026-07-23', '2026-07-23'], 'rank_icir': '0.356', 'recency_weight': '0.244', 'weight': '0.071'}
