# params 
 {'predict_dates': [{'start': '2026-06-03', 'end': '2026-06-03'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260603_15 830955037920057586 (Recorders: 6/6)

	Recorder: 74373a4b289f4e369182ede82c8b4f4f

		Model: {'id': '74373a4b289f4e369182ede82c8b4f4f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.345, 'Rank IC': 0.057, 'Rank ICIR': 0.378}, 'data_train_vec': ['2020-06-03', '2024-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.378', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: d9fa643d459740cc8dade6678721d665

		Model: {'id': 'd9fa643d459740cc8dade6678721d665', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.227, 'Rank IC': 0.06, 'Rank ICIR': 0.388}, 'data_train_vec': ['2021-06-03', '2025-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.388', 'recency_weight': '0.171', 'weight': '0.022'}

	Recorder: 65f316091c9445d88c1787d3ded940f3

		Model: {'id': '65f316091c9445d88c1787d3ded940f3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.236, 'Rank IC': 0.066, 'Rank ICIR': 0.378}, 'data_train_vec': ['2022-06-03', '2025-06-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.378', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: 6f17bb57f9bd4b7ab5c537f8383a38ba

		Model: {'id': '6f17bb57f9bd4b7ab5c537f8383a38ba', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.27, 'Rank IC': 0.062, 'Rank ICIR': 0.367}, 'data_train_vec': ['2023-06-03', '2025-09-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.367', 'recency_weight': '0.348', 'weight': '0.040'}

	Recorder: a38306a1f7b842d3ba90c63650c60c93

		Model: {'id': 'a38306a1f7b842d3ba90c63650c60c93', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.28, 'Rank IC': 0.067, 'Rank ICIR': 0.481}, 'data_train_vec': ['2024-06-03', '2025-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.481', 'recency_weight': '0.494', 'weight': '0.097'}

	Recorder: f1e6c01c0a49474ca57c995228068e59

		Model: {'id': 'f1e6c01c0a49474ca57c995228068e59', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.096, 'ICIR': 0.639, 'Rank IC': 0.058, 'Rank ICIR': 0.32}, 'data_train_vec': ['2025-06-03', '2026-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.320', 'recency_weight': '0.699', 'weight': '0.061'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260603_15 809755628235728116 (Recorders: 6/6)

	Recorder: 1b98368dd88c4214967d141ac805f8f3

		Model: {'id': '1b98368dd88c4214967d141ac805f8f3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.317, 'Rank IC': 0.059, 'Rank ICIR': 0.383}, 'data_train_vec': ['2020-06-03', '2024-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.383', 'recency_weight': '0.121', 'weight': '0.015'}

	Recorder: 7814851beb8645208c439eb893ebaab1

		Model: {'id': '7814851beb8645208c439eb893ebaab1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.198, 'Rank IC': 0.056, 'Rank ICIR': 0.369}, 'data_train_vec': ['2021-06-03', '2025-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.369', 'recency_weight': '0.171', 'weight': '0.020'}

	Recorder: 3b723672de484e0d93950740d1bc00ae

		Model: {'id': '3b723672de484e0d93950740d1bc00ae', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.11, 'Rank IC': 0.06, 'Rank ICIR': 0.338}, 'data_train_vec': ['2022-06-03', '2025-06-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.338', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: 4d0683fdddce4507bec5ca0a880c5a75

		Model: {'id': '4d0683fdddce4507bec5ca0a880c5a75', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.222, 'Rank IC': 0.065, 'Rank ICIR': 0.383}, 'data_train_vec': ['2023-06-03', '2025-09-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.383', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: 73cd68a07d704ff09410fda8911e387b

		Model: {'id': '73cd68a07d704ff09410fda8911e387b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.131, 'Rank IC': 0.054, 'Rank ICIR': 0.358}, 'data_train_vec': ['2024-06-03', '2025-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.358', 'recency_weight': '0.494', 'weight': '0.054'}

	Recorder: d4d3e6b1ed334af4be1d6aa155025dc3

		Model: {'id': 'd4d3e6b1ed334af4be1d6aa155025dc3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.333, 'Rank IC': 0.037, 'Rank ICIR': 0.229}, 'data_train_vec': ['2025-06-03', '2026-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.229', 'recency_weight': '0.699', 'weight': '0.031'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260603_15 156046275059544659 (Recorders: 6/6)

	Recorder: 477da3504c384e328b80add621556df8

		Model: {'id': '477da3504c384e328b80add621556df8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.324, 'Rank IC': 0.063, 'Rank ICIR': 0.459}, 'data_train_vec': ['2020-06-03', '2024-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.459', 'recency_weight': '0.121', 'weight': '0.022'}

	Recorder: 2e09d4209fe44979b66f36831d6b4dfa

		Model: {'id': '2e09d4209fe44979b66f36831d6b4dfa', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.239, 'Rank IC': 0.065, 'Rank ICIR': 0.473}, 'data_train_vec': ['2021-06-03', '2025-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.473', 'recency_weight': '0.171', 'weight': '0.032'}

	Recorder: 787b47d0e0b942b5b0fdae16eb5c42db

		Model: {'id': '787b47d0e0b942b5b0fdae16eb5c42db', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.113, 'Rank IC': 0.058, 'Rank ICIR': 0.38}, 'data_train_vec': ['2022-06-03', '2025-06-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.380', 'recency_weight': '0.244', 'weight': '0.030'}

	Recorder: f27c9711707448099aef014c753fccfd

		Model: {'id': 'f27c9711707448099aef014c753fccfd', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.103, 'Rank IC': 0.044, 'Rank ICIR': 0.309}, 'data_train_vec': ['2023-06-03', '2025-09-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.309', 'recency_weight': '0.348', 'weight': '0.028'}

	Recorder: e265f0029e174a96987d52161dc71507

		Model: {'id': 'e265f0029e174a96987d52161dc71507', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.194, 'Rank IC': 0.051, 'Rank ICIR': 0.401}, 'data_train_vec': ['2024-06-03', '2025-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.401', 'recency_weight': '0.494', 'weight': '0.067'}

	Recorder: 0b4b16ff2aba4b6cabafbe4dd7a5368c

		Model: {'id': '0b4b16ff2aba4b6cabafbe4dd7a5368c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.374, 'Rank IC': 0.068, 'Rank ICIR': 0.328}, 'data_train_vec': ['2025-06-03', '2026-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.328', 'recency_weight': '0.699', 'weight': '0.064'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260603_15 300630688028896929 (Recorders: 6/6)

	Recorder: 00a5311c8e414e6581eff9665099a6e0

		Model: {'id': '00a5311c8e414e6581eff9665099a6e0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.312, 'Rank IC': 0.056, 'Rank ICIR': 0.37}, 'data_train_vec': ['2020-06-03', '2024-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.370', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 3f5cc429285d473a940770fdf01e5f96

		Model: {'id': '3f5cc429285d473a940770fdf01e5f96', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.241, 'Rank IC': 0.061, 'Rank ICIR': 0.428}, 'data_train_vec': ['2021-06-03', '2025-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.428', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 3e27e3b1cdb44d279657187ad242e06f

		Model: {'id': '3e27e3b1cdb44d279657187ad242e06f', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.265, 'Rank IC': 0.067, 'Rank ICIR': 0.412}, 'data_train_vec': ['2022-06-03', '2025-06-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.412', 'recency_weight': '0.244', 'weight': '0.035'}

	Recorder: 9fbe1414746a41598c70b2913ca56555

		Model: {'id': '9fbe1414746a41598c70b2913ca56555', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.263, 'Rank IC': 0.063, 'Rank ICIR': 0.387}, 'data_train_vec': ['2023-06-03', '2025-09-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.387', 'recency_weight': '0.348', 'weight': '0.044'}

	Recorder: 73888b64a931488580eb59d8911468d9

		Model: {'id': '73888b64a931488580eb59d8911468d9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.362, 'Rank IC': 0.07, 'Rank ICIR': 0.537}, 'data_train_vec': ['2024-06-03', '2025-12-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.537', 'recency_weight': '0.494', 'weight': '0.121'}

	Recorder: ca2bda6dd37f4785a6c63496cfd37cea

		Model: {'id': 'ca2bda6dd37f4785a6c63496cfd37cea', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.476, 'Rank IC': 0.05, 'Rank ICIR': 0.336}, 'data_train_vec': ['2025-06-03', '2026-03-02'], 'train_time_vec': ['2026-06-03', '2026-06-03'], 'rank_icir': '0.336', 'recency_weight': '0.699', 'weight': '0.067'}
