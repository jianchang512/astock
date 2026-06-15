# params 
 {'predict_dates': [{'start': '2026-06-15', 'end': '2026-06-15'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260615_13 282458493585649713 (Recorders: 6/6)

	Recorder: 3db3918c1a954dcb954b700190c52550

		Model: {'id': '3db3918c1a954dcb954b700190c52550', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.317, 'Rank IC': 0.058, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-06-15', '2024-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.379', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 58acf485b1e44d34ae7fe66fe4cbd0e7

		Model: {'id': '58acf485b1e44d34ae7fe66fe4cbd0e7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.327, 'Rank IC': 0.074, 'Rank ICIR': 0.483}, 'data_train_vec': ['2021-06-15', '2025-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.483', 'recency_weight': '0.171', 'weight': '0.032'}

	Recorder: 3eedc789a88e42c1823ca3ee00784898

		Model: {'id': '3eedc789a88e42c1823ca3ee00784898', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.256, 'Rank IC': 0.074, 'Rank ICIR': 0.446}, 'data_train_vec': ['2022-06-15', '2025-06-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.446', 'recency_weight': '0.244', 'weight': '0.038'}

	Recorder: cb457232f60a4061bdfe596389e3ed4a

		Model: {'id': 'cb457232f60a4061bdfe596389e3ed4a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.332, 'Rank IC': 0.074, 'Rank ICIR': 0.424}, 'data_train_vec': ['2023-06-15', '2025-09-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.424', 'recency_weight': '0.348', 'weight': '0.049'}

	Recorder: 110492c1aed34818bf184ec6633dd942

		Model: {'id': '110492c1aed34818bf184ec6633dd942', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.241, 'Rank IC': 0.074, 'Rank ICIR': 0.515}, 'data_train_vec': ['2024-06-15', '2025-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.515', 'recency_weight': '0.494', 'weight': '0.104'}

	Recorder: c80a52cbdd144873b8d84a28c7d3b65e

		Model: {'id': 'c80a52cbdd144873b8d84a28c7d3b65e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.092, 'ICIR': 0.517, 'Rank IC': 0.045, 'Rank ICIR': 0.225}, 'data_train_vec': ['2025-06-15', '2026-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.225', 'recency_weight': '0.699', 'weight': '0.028'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260615_13 884327387681185572 (Recorders: 6/6)

	Recorder: edfea2ad29ae4c18b25e8b59b8d54d83

		Model: {'id': 'edfea2ad29ae4c18b25e8b59b8d54d83', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.307, 'Rank IC': 0.059, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-06-15', '2024-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.379', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 5eff26ca72344f739377ee6f4bfa1ee1

		Model: {'id': '5eff26ca72344f739377ee6f4bfa1ee1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.287, 'Rank IC': 0.068, 'Rank ICIR': 0.449}, 'data_train_vec': ['2021-06-15', '2025-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.449', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 3bf635ec77754bbb9c3b0a9ab9b5a671

		Model: {'id': '3bf635ec77754bbb9c3b0a9ab9b5a671', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.168, 'Rank IC': 0.067, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-06-15', '2025-06-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 17238c1b9f1c45efbbeb8234ea55f7a4

		Model: {'id': '17238c1b9f1c45efbbeb8234ea55f7a4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.268, 'Rank IC': 0.08, 'Rank ICIR': 0.464}, 'data_train_vec': ['2023-06-15', '2025-09-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.464', 'recency_weight': '0.348', 'weight': '0.059'}

	Recorder: bd7a038ecd95451fb04994dd36ec5439

		Model: {'id': 'bd7a038ecd95451fb04994dd36ec5439', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.257, 'Rank IC': 0.073, 'Rank ICIR': 0.5}, 'data_train_vec': ['2024-06-15', '2025-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.500', 'recency_weight': '0.494', 'weight': '0.098'}

	Recorder: 367c980d4fed4a179b3f2637b609a739

		Model: {'id': '367c980d4fed4a179b3f2637b609a739', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.268, 'Rank IC': 0.032, 'Rank ICIR': 0.158}, 'data_train_vec': ['2025-06-15', '2026-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.158', 'recency_weight': '0.699', 'weight': '0.014'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260615_13 367882004434035830 (Recorders: 6/6)

	Recorder: 40c55c077e594bbf80d0f7dd454a2f3f

		Model: {'id': '40c55c077e594bbf80d0f7dd454a2f3f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.329, 'Rank IC': 0.065, 'Rank ICIR': 0.467}, 'data_train_vec': ['2020-06-15', '2024-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.467', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: 80fa3fe43bfb4ec5abf7d6aa5f5bd4a6

		Model: {'id': '80fa3fe43bfb4ec5abf7d6aa5f5bd4a6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.271, 'Rank IC': 0.068, 'Rank ICIR': 0.481}, 'data_train_vec': ['2021-06-15', '2025-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.481', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: f83b4f025f48437dbddf26b075e3560e

		Model: {'id': 'f83b4f025f48437dbddf26b075e3560e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.145, 'Rank IC': 0.062, 'Rank ICIR': 0.406}, 'data_train_vec': ['2022-06-15', '2025-06-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.406', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: dc927b8712d44614a2e7258ff1276b16

		Model: {'id': 'dc927b8712d44614a2e7258ff1276b16', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.258, 'Rank IC': 0.065, 'Rank ICIR': 0.483}, 'data_train_vec': ['2023-06-15', '2025-09-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.483', 'recency_weight': '0.348', 'weight': '0.064'}

	Recorder: af5faeb253a445f09a7c9bf2a8bec166

		Model: {'id': 'af5faeb253a445f09a7c9bf2a8bec166', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.208, 'Rank IC': 0.052, 'Rank ICIR': 0.38}, 'data_train_vec': ['2024-06-15', '2025-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.380', 'recency_weight': '0.494', 'weight': '0.056'}

	Recorder: 894864c34fcc432cb200279d397edcd6

		Model: {'id': '894864c34fcc432cb200279d397edcd6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.071, 'ICIR': 0.306, 'Rank IC': 0.053, 'Rank ICIR': 0.242}, 'data_train_vec': ['2025-06-15', '2026-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.242', 'recency_weight': '0.699', 'weight': '0.032'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260615_13 829287868296815180 (Recorders: 6/6)

	Recorder: 91e95a3d719d4c538ce69228beb81d72

		Model: {'id': '91e95a3d719d4c538ce69228beb81d72', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.282, 'Rank IC': 0.053, 'Rank ICIR': 0.35}, 'data_train_vec': ['2020-06-15', '2024-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.350', 'recency_weight': '0.121', 'weight': '0.012'}

	Recorder: c07c241bb6e04a8eb5c28755d944fe0d

		Model: {'id': 'c07c241bb6e04a8eb5c28755d944fe0d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.29, 'Rank IC': 0.062, 'Rank ICIR': 0.431}, 'data_train_vec': ['2021-06-15', '2025-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.431', 'recency_weight': '0.171', 'weight': '0.025'}

	Recorder: b3976e4ff55a4e1996c1634d0a35595b

		Model: {'id': 'b3976e4ff55a4e1996c1634d0a35595b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.254, 'Rank IC': 0.076, 'Rank ICIR': 0.464}, 'data_train_vec': ['2022-06-15', '2025-06-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.464', 'recency_weight': '0.244', 'weight': '0.042'}

	Recorder: 0fab0ec8e4ea46dc861b6d14f861b564

		Model: {'id': '0fab0ec8e4ea46dc861b6d14f861b564', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.271, 'Rank IC': 0.073, 'Rank ICIR': 0.444}, 'data_train_vec': ['2023-06-15', '2025-09-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.444', 'recency_weight': '0.348', 'weight': '0.054'}

	Recorder: 468accf9eff141519a056b8835489223

		Model: {'id': '468accf9eff141519a056b8835489223', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.262, 'Rank IC': 0.061, 'Rank ICIR': 0.458}, 'data_train_vec': ['2024-06-15', '2025-12-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.458', 'recency_weight': '0.494', 'weight': '0.082'}

	Recorder: e6e392dfaee84c018abb952bd9dd9c21

		Model: {'id': 'e6e392dfaee84c018abb952bd9dd9c21', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.089, 'ICIR': 0.457, 'Rank IC': 0.052, 'Rank ICIR': 0.279}, 'data_train_vec': ['2025-06-15', '2026-03-14'], 'train_time_vec': ['2026-06-15', '2026-06-15'], 'rank_icir': '0.279', 'recency_weight': '0.699', 'weight': '0.043'}
