# params 
 {'predict_dates': [{'start': '2026-08-03', 'end': '2026-08-03'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260803_14 979403953916937165 (Recorders: 4/6)

	Recorder: 50b91b074aac4ae998a899121b7ff5de

		Model: {'id': '50b91b074aac4ae998a899121b7ff5de', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.309, 'Rank IC': 0.069, 'Rank ICIR': 0.432}, 'data_train_vec': ['2020-08-03', '2025-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.432', 'recency_weight': '0.122', 'weight': '0.061'}

	Recorder: 7a7fd543f8f84ff5b89b9ff91eb0b1fc

		Model: {'id': '7a7fd543f8f84ff5b89b9ff91eb0b1fc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.183, 'Rank IC': 0.066, 'Rank ICIR': 0.39}, 'data_train_vec': ['2021-08-03', '2025-05-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.390', 'recency_weight': '0.171', 'weight': '0.070'}

	Recorder: cbc79b9284934daab3a53adf565f63d3

		Model: {'id': 'cbc79b9284934daab3a53adf565f63d3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.06, 'Rank IC': 0.053, 'Rank ICIR': 0.318}, 'data_train_vec': ['2022-08-03', '2025-08-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.318', 'recency_weight': '0.244', 'weight': '0.067'}

	Recorder: 318064d5cb724d9e9c919a65c02182bf

		Model: {'id': '318064d5cb724d9e9c919a65c02182bf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.06, 'Rank IC': 0.066, 'Rank ICIR': 0.367}, 'data_train_vec': ['2023-08-03', '2025-11-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.367', 'recency_weight': '0.348', 'weight': '0.126'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260803_14 211499531342681766 (Recorders: 5/6)

	Recorder: d4533a7ad98242afbd6b0c4edbf42254

		Model: {'id': 'd4533a7ad98242afbd6b0c4edbf42254', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.315, 'Rank IC': 0.069, 'Rank ICIR': 0.424}, 'data_train_vec': ['2020-08-03', '2025-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.424', 'recency_weight': '0.122', 'weight': '0.059'}

	Recorder: 5a49789f7ae14af4829b337d9d246bec

		Model: {'id': '5a49789f7ae14af4829b337d9d246bec', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.218, 'Rank IC': 0.064, 'Rank ICIR': 0.398}, 'data_train_vec': ['2021-08-03', '2025-05-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.398', 'recency_weight': '0.171', 'weight': '0.073'}

	Recorder: 8ba4c47522a042bc84afa8a6b7c68cf4

		Model: {'id': '8ba4c47522a042bc84afa8a6b7c68cf4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.095, 'Rank IC': 0.048, 'Rank ICIR': 0.297}, 'data_train_vec': ['2022-08-03', '2025-08-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.297', 'recency_weight': '0.244', 'weight': '0.058'}

	Recorder: a51528c3cbf24bcc8e6e69844f4ad8fc

		Model: {'id': 'a51528c3cbf24bcc8e6e69844f4ad8fc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.215, 'Rank IC': 0.062, 'Rank ICIR': 0.386}, 'data_train_vec': ['2023-08-03', '2025-11-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.386', 'recency_weight': '0.348', 'weight': '0.140'}

	Recorder: 332948b11b3640a0bb507b772f399fd7

		Model: {'id': '332948b11b3640a0bb507b772f399fd7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.052, 'Rank IC': 0.014, 'Rank ICIR': 0.073}, 'data_train_vec': ['2024-08-03', '2026-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.073', 'recency_weight': '0.496', 'weight': '0.007'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260803_14 483386841581910065 (Recorders: 5/6)

	Recorder: 6cbf48032d204b5b9c2524868385efc0

		Model: {'id': '6cbf48032d204b5b9c2524868385efc0', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.194, 'Rank IC': 0.051, 'Rank ICIR': 0.314}, 'data_train_vec': ['2020-08-03', '2025-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.314', 'recency_weight': '0.122', 'weight': '0.032'}

	Recorder: 23f715c0e1f946fa98a99475ae8b37cc

		Model: {'id': '23f715c0e1f946fa98a99475ae8b37cc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.125, 'Rank IC': 0.047, 'Rank ICIR': 0.275}, 'data_train_vec': ['2021-08-03', '2025-05-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.275', 'recency_weight': '0.171', 'weight': '0.035'}

	Recorder: 4e8d64dedeae4de0bf8267e3e8e7d595

		Model: {'id': '4e8d64dedeae4de0bf8267e3e8e7d595', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.099, 'Rank IC': 0.047, 'Rank ICIR': 0.292}, 'data_train_vec': ['2022-08-03', '2025-08-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.292', 'recency_weight': '0.244', 'weight': '0.056'}

	Recorder: dfe7e1fab52a44afbe7825966f5bd16d

		Model: {'id': 'dfe7e1fab52a44afbe7825966f5bd16d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.213, 'Rank IC': 0.053, 'Rank ICIR': 0.292}, 'data_train_vec': ['2023-08-03', '2025-11-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.292', 'recency_weight': '0.348', 'weight': '0.080'}

	Recorder: 98f47d3ebed349d4a6145d845772b375

		Model: {'id': '98f47d3ebed349d4a6145d845772b375', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.04, 'Rank IC': 0.018, 'Rank ICIR': 0.083}, 'data_train_vec': ['2024-08-03', '2026-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.083', 'recency_weight': '0.496', 'weight': '0.009'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260803_14 957458548048570240 (Recorders: 2/6)

	Recorder: e2ede29692af4aeaa7e3f3f6f4bfc06b

		Model: {'id': 'e2ede29692af4aeaa7e3f3f6f4bfc06b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.256, 'Rank IC': 0.066, 'Rank ICIR': 0.441}, 'data_train_vec': ['2020-08-03', '2025-02-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.441', 'recency_weight': '0.122', 'weight': '0.064'}

	Recorder: 54d11562505d4fbea15042d8568a1d6d

		Model: {'id': '54d11562505d4fbea15042d8568a1d6d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.147, 'Rank IC': 0.059, 'Rank ICIR': 0.366}, 'data_train_vec': ['2021-08-03', '2025-05-02'], 'train_time_vec': ['2026-08-03', '2026-08-03'], 'rank_icir': '0.366', 'recency_weight': '0.171', 'weight': '0.062'}
