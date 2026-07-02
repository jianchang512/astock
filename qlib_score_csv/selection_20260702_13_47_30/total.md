# params 
 {'predict_dates': [{'start': '2026-07-02', 'end': '2026-07-02'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260702_13 398200793113368211 (Recorders: 6/6)

	Recorder: 074d7cda3c484a48963578575554f8eb

		Model: {'id': '074d7cda3c484a48963578575554f8eb', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.328, 'Rank IC': 0.063, 'Rank ICIR': 0.421}, 'data_train_vec': ['2020-07-02', '2025-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.421', 'recency_weight': '0.122', 'weight': '0.017'}

	Recorder: dc43f7de11f349f18fbc3f713ad27299

		Model: {'id': 'dc43f7de11f349f18fbc3f713ad27299', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.197, 'Rank IC': 0.066, 'Rank ICIR': 0.39}, 'data_train_vec': ['2021-07-02', '2025-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.390', 'recency_weight': '0.172', 'weight': '0.020'}

	Recorder: 6c1702133527408aa0989ae76986efd7

		Model: {'id': '6c1702133527408aa0989ae76986efd7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.123, 'Rank IC': 0.063, 'Rank ICIR': 0.374}, 'data_train_vec': ['2022-07-02', '2025-07-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.374', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: 3f5d2b4924094efe991f7959339f8634

		Model: {'id': '3f5d2b4924094efe991f7959339f8634', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.349, 'Rank IC': 0.072, 'Rank ICIR': 0.465}, 'data_train_vec': ['2023-07-02', '2025-10-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.465', 'recency_weight': '0.348', 'weight': '0.058'}

	Recorder: ef308f877e224da7bfb67f2f7b3ce358

		Model: {'id': 'ef308f877e224da7bfb67f2f7b3ce358', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.399, 'Rank IC': 0.077, 'Rank ICIR': 0.569}, 'data_train_vec': ['2024-07-02', '2026-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.569', 'recency_weight': '0.496', 'weight': '0.124'}

	Recorder: 3dce9e9f927a48c79b7896857629e468

		Model: {'id': '3dce9e9f927a48c79b7896857629e468', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.087, 'ICIR': 0.515, 'Rank IC': 0.074, 'Rank ICIR': 0.441}, 'data_train_vec': ['2025-07-02', '2026-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.441', 'recency_weight': '0.702', 'weight': '0.105'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260702_12 585241588055187595 (Recorders: 6/6)

	Recorder: 43a9e137b7454626a9eab5ac6a5fe919

		Model: {'id': '43a9e137b7454626a9eab5ac6a5fe919', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.3, 'Rank IC': 0.063, 'Rank ICIR': 0.406}, 'data_train_vec': ['2020-07-02', '2025-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.406', 'recency_weight': '0.122', 'weight': '0.015'}

	Recorder: a507be97ad3f4c7688f3e41b88564a15

		Model: {'id': 'a507be97ad3f4c7688f3e41b88564a15', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.198, 'Rank IC': 0.062, 'Rank ICIR': 0.377}, 'data_train_vec': ['2021-07-02', '2025-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.377', 'recency_weight': '0.172', 'weight': '0.019'}

	Recorder: d79adfe6ffb24ca1845681a92e21d1de

		Model: {'id': 'd79adfe6ffb24ca1845681a92e21d1de', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.104, 'Rank IC': 0.061, 'Rank ICIR': 0.361}, 'data_train_vec': ['2022-07-02', '2025-07-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.361', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 5dcb86577400487d8ff5c2b7ced78ad0

		Model: {'id': '5dcb86577400487d8ff5c2b7ced78ad0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.249, 'Rank IC': 0.064, 'Rank ICIR': 0.412}, 'data_train_vec': ['2023-07-02', '2025-10-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.412', 'recency_weight': '0.348', 'weight': '0.046'}

	Recorder: 50d2adc1e1444f0b9cf98b8e5fb37667

		Model: {'id': '50d2adc1e1444f0b9cf98b8e5fb37667', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.3, 'Rank IC': 0.051, 'Rank ICIR': 0.389}, 'data_train_vec': ['2024-07-02', '2026-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.389', 'recency_weight': '0.496', 'weight': '0.058'}

	Recorder: fe7b4ba6133c409d92b9b1c7c5ca8249

		Model: {'id': 'fe7b4ba6133c409d92b9b1c7c5ca8249', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.08, 'ICIR': 0.357, 'Rank IC': 0.07, 'Rank ICIR': 0.365}, 'data_train_vec': ['2025-07-02', '2026-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.365', 'recency_weight': '0.702', 'weight': '0.072'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260702_12 708451188366657842 (Recorders: 5/6)

	Recorder: 14a95cbfa9fd4d69b02ea95b05976256

		Model: {'id': '14a95cbfa9fd4d69b02ea95b05976256', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.258, 'Rank IC': 0.06, 'Rank ICIR': 0.417}, 'data_train_vec': ['2020-07-02', '2025-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.417', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 807d9f932c8149cfb34634d58a3523ee

		Model: {'id': '807d9f932c8149cfb34634d58a3523ee', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.125, 'Rank IC': 0.052, 'Rank ICIR': 0.346}, 'data_train_vec': ['2021-07-02', '2025-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.346', 'recency_weight': '0.172', 'weight': '0.016'}

	Recorder: 4038519a08974cfcb0f7ab9123a3dfc4

		Model: {'id': '4038519a08974cfcb0f7ab9123a3dfc4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.203, 'Rank IC': 0.05, 'Rank ICIR': 0.365}, 'data_train_vec': ['2023-07-02', '2025-10-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.365', 'recency_weight': '0.348', 'weight': '0.036'}

	Recorder: 3b1090fdb1464673acfbcc1a7d3a3fe6

		Model: {'id': '3b1090fdb1464673acfbcc1a7d3a3fe6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.23, 'Rank IC': 0.041, 'Rank ICIR': 0.289}, 'data_train_vec': ['2024-07-02', '2026-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.289', 'recency_weight': '0.496', 'weight': '0.032'}

	Recorder: 8da0f25e71954ad594a0da71dd20f077

		Model: {'id': '8da0f25e71954ad594a0da71dd20f077', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.342, 'Rank IC': 0.07, 'Rank ICIR': 0.358}, 'data_train_vec': ['2025-07-02', '2026-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.358', 'recency_weight': '0.702', 'weight': '0.069'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260702_12 646136137969539423 (Recorders: 6/6)

	Recorder: a9be8ef3e8b14393901fc2d1b6a28961

		Model: {'id': 'a9be8ef3e8b14393901fc2d1b6a28961', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.318, 'Rank IC': 0.066, 'Rank ICIR': 0.45}, 'data_train_vec': ['2020-07-02', '2025-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.450', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 2c7e91301a4347b2ac4ad041f9e3e7f9

		Model: {'id': '2c7e91301a4347b2ac4ad041f9e3e7f9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.196, 'Rank IC': 0.065, 'Rank ICIR': 0.418}, 'data_train_vec': ['2021-07-02', '2025-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.418', 'recency_weight': '0.172', 'weight': '0.023'}

	Recorder: 6ec85fa2162445df8803cb645ca01cf0

		Model: {'id': '6ec85fa2162445df8803cb645ca01cf0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.093, 'Rank IC': 0.062, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-07-02', '2025-07-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.029'}

	Recorder: 1668d0d62ce94ebbbe217c7c7f98fcb4

		Model: {'id': '1668d0d62ce94ebbbe217c7c7f98fcb4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.233, 'Rank IC': 0.052, 'Rank ICIR': 0.361}, 'data_train_vec': ['2023-07-02', '2025-10-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.361', 'recency_weight': '0.348', 'weight': '0.035'}

	Recorder: e26f63c745f14014949cbab6f62d976e

		Model: {'id': 'e26f63c745f14014949cbab6f62d976e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.217, 'Rank IC': 0.054, 'Rank ICIR': 0.424}, 'data_train_vec': ['2024-07-02', '2026-01-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.424', 'recency_weight': '0.496', 'weight': '0.069'}

	Recorder: 9476e7a3bf2340898c1724b5d105cab0

		Model: {'id': '9476e7a3bf2340898c1724b5d105cab0', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.395, 'Rank IC': 0.055, 'Rank ICIR': 0.361}, 'data_train_vec': ['2025-07-02', '2026-04-01'], 'train_time_vec': ['2026-07-02', '2026-07-02'], 'rank_icir': '0.361', 'recency_weight': '0.702', 'weight': '0.071'}
