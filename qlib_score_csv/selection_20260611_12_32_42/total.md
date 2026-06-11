# params 
 {'predict_dates': [{'start': '2026-06-11', 'end': '2026-06-11'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260611_11 544427636527286787 (Recorders: 6/6)

	Recorder: 9e1ba33cce4948228e96f2073b2c974d

		Model: {'id': '9e1ba33cce4948228e96f2073b2c974d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.357, 'Rank IC': 0.063, 'Rank ICIR': 0.413}, 'data_train_vec': ['2020-06-11', '2024-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.413', 'recency_weight': '0.121', 'weight': '0.018'}

	Recorder: c1a23ddfb042465da5eba368f4473120

		Model: {'id': 'c1a23ddfb042465da5eba368f4473120', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.304, 'Rank IC': 0.072, 'Rank ICIR': 0.469}, 'data_train_vec': ['2021-06-11', '2025-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.469', 'recency_weight': '0.171', 'weight': '0.032'}

	Recorder: 2de79bb767d840158077de796639581c

		Model: {'id': '2de79bb767d840158077de796639581c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.205, 'Rank IC': 0.073, 'Rank ICIR': 0.424}, 'data_train_vec': ['2022-06-11', '2025-06-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.424', 'recency_weight': '0.244', 'weight': '0.038'}

	Recorder: 23ffe3f47ef1426d8685758da0f18ae1

		Model: {'id': '23ffe3f47ef1426d8685758da0f18ae1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.335, 'Rank IC': 0.079, 'Rank ICIR': 0.465}, 'data_train_vec': ['2023-06-11', '2025-09-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.465', 'recency_weight': '0.348', 'weight': '0.065'}

	Recorder: 7a8a306d205e428992b97cf2a757c3f1

		Model: {'id': '7a8a306d205e428992b97cf2a757c3f1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.254, 'Rank IC': 0.07, 'Rank ICIR': 0.495}, 'data_train_vec': ['2024-06-11', '2025-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.495', 'recency_weight': '0.494', 'weight': '0.104'}

	Recorder: 215344c73feb4378adc28c09a56a4638

		Model: {'id': '215344c73feb4378adc28c09a56a4638', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.312, 'Rank IC': 0.011, 'Rank ICIR': 0.056}, 'data_train_vec': ['2025-06-11', '2026-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.056', 'recency_weight': '0.699', 'weight': '0.002'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260611_11 644564817022509044 (Recorders: 5/6)

	Recorder: a37f351fb0db4f3d932c5af676aa4bde

		Model: {'id': 'a37f351fb0db4f3d932c5af676aa4bde', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.321, 'Rank IC': 0.062, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-06-11', '2024-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: c540175c2ecb4e99a7d0d1f69363d540

		Model: {'id': 'c540175c2ecb4e99a7d0d1f69363d540', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.266, 'Rank IC': 0.066, 'Rank ICIR': 0.442}, 'data_train_vec': ['2021-06-11', '2025-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.442', 'recency_weight': '0.171', 'weight': '0.029'}

	Recorder: c840586669794973b52072562dfb255f

		Model: {'id': 'c840586669794973b52072562dfb255f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.146, 'Rank IC': 0.063, 'Rank ICIR': 0.37}, 'data_train_vec': ['2022-06-11', '2025-06-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.370', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 00682c71c75b41628cd3eee3f4ba27e0

		Model: {'id': '00682c71c75b41628cd3eee3f4ba27e0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.242, 'Rank IC': 0.078, 'Rank ICIR': 0.451}, 'data_train_vec': ['2023-06-11', '2025-09-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.451', 'recency_weight': '0.348', 'weight': '0.061'}

	Recorder: 668884b0d6444d2db9ffaa8c3546a30b

		Model: {'id': '668884b0d6444d2db9ffaa8c3546a30b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.248, 'Rank IC': 0.072, 'Rank ICIR': 0.514}, 'data_train_vec': ['2024-06-11', '2025-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.514', 'recency_weight': '0.494', 'weight': '0.112'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260611_11 752482452820544425 (Recorders: 6/6)

	Recorder: 15ded3b8f3174c3d875a49901e6e70cb

		Model: {'id': '15ded3b8f3174c3d875a49901e6e70cb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.331, 'Rank IC': 0.066, 'Rank ICIR': 0.479}, 'data_train_vec': ['2020-06-11', '2024-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.479', 'recency_weight': '0.121', 'weight': '0.024'}

	Recorder: 716201f0ade840399039ba06c60d4c15

		Model: {'id': '716201f0ade840399039ba06c60d4c15', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.274, 'Rank IC': 0.07, 'Rank ICIR': 0.503}, 'data_train_vec': ['2021-06-11', '2025-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.503', 'recency_weight': '0.171', 'weight': '0.037'}

	Recorder: d2e8be22fe3d4e13a8db3752f861777b

		Model: {'id': 'd2e8be22fe3d4e13a8db3752f861777b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.114, 'Rank IC': 0.06, 'Rank ICIR': 0.39}, 'data_train_vec': ['2022-06-11', '2025-06-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.390', 'recency_weight': '0.244', 'weight': '0.032'}

	Recorder: d428a02965ad466ba7ac1d8636e85b92

		Model: {'id': 'd428a02965ad466ba7ac1d8636e85b92', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.216, 'Rank IC': 0.061, 'Rank ICIR': 0.449}, 'data_train_vec': ['2023-06-11', '2025-09-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.449', 'recency_weight': '0.348', 'weight': '0.060'}

	Recorder: 92e7c0a4029f470d9da5d835b4543be8

		Model: {'id': '92e7c0a4029f470d9da5d835b4543be8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.186, 'Rank IC': 0.046, 'Rank ICIR': 0.369}, 'data_train_vec': ['2024-06-11', '2025-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.369', 'recency_weight': '0.494', 'weight': '0.058'}

	Recorder: 7b2c28e228a24d93b1d5a4fb4eb15d55

		Model: {'id': '7b2c28e228a24d93b1d5a4fb4eb15d55', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.227, 'Rank IC': 0.033, 'Rank ICIR': 0.155}, 'data_train_vec': ['2025-06-11', '2026-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.155', 'recency_weight': '0.699', 'weight': '0.014'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260611_11 312170066256318700 (Recorders: 6/6)

	Recorder: 9503fce7b1df4ddeb89c91f6856c2fb9

		Model: {'id': '9503fce7b1df4ddeb89c91f6856c2fb9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.342, 'Rank IC': 0.06, 'Rank ICIR': 0.393}, 'data_train_vec': ['2020-06-11', '2024-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.393', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 5cfb2486854848198ee9ff472ae04b1b

		Model: {'id': '5cfb2486854848198ee9ff472ae04b1b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.219, 'Rank IC': 0.068, 'Rank ICIR': 0.501}, 'data_train_vec': ['2021-06-11', '2025-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.501', 'recency_weight': '0.171', 'weight': '0.037'}

	Recorder: 32009f13815e48e6b16f220e63785d1d

		Model: {'id': '32009f13815e48e6b16f220e63785d1d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.247, 'Rank IC': 0.074, 'Rank ICIR': 0.442}, 'data_train_vec': ['2022-06-11', '2025-06-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.442', 'recency_weight': '0.244', 'weight': '0.041'}

	Recorder: 920e682d3c024b07a0c3b527003e6f29

		Model: {'id': '920e682d3c024b07a0c3b527003e6f29', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.386, 'Rank IC': 0.076, 'Rank ICIR': 0.477}, 'data_train_vec': ['2023-06-11', '2025-09-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.477', 'recency_weight': '0.348', 'weight': '0.068'}

	Recorder: b41fed7608b149e2a9a1e810dde3205b

		Model: {'id': 'b41fed7608b149e2a9a1e810dde3205b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.176, 'Rank IC': 0.062, 'Rank ICIR': 0.487}, 'data_train_vec': ['2024-06-11', '2025-12-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.487', 'recency_weight': '0.494', 'weight': '0.101'}

	Recorder: f4de0353c38c434d84911834b4b64a91

		Model: {'id': 'f4de0353c38c434d84911834b4b64a91', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.271, 'Rank IC': 0.014, 'Rank ICIR': 0.086}, 'data_train_vec': ['2025-06-11', '2026-03-10'], 'train_time_vec': ['2026-06-11', '2026-06-11'], 'rank_icir': '0.086', 'recency_weight': '0.699', 'weight': '0.004'}
