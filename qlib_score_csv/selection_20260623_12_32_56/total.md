# params 
 {'predict_dates': [{'start': '2026-06-23', 'end': '2026-06-23'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260623_11 177530234489107429 (Recorders: 6/6)

	Recorder: 659d6348466748c4b4f6461bc014eac5

		Model: {'id': '659d6348466748c4b4f6461bc014eac5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.349, 'Rank IC': 0.062, 'Rank ICIR': 0.41}, 'data_train_vec': ['2020-06-23', '2024-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.410', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 78f85aea6a3241ae882c9555efe85121

		Model: {'id': '78f85aea6a3241ae882c9555efe85121', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.255, 'Rank IC': 0.075, 'Rank ICIR': 0.467}, 'data_train_vec': ['2021-06-23', '2025-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.467', 'recency_weight': '0.171', 'weight': '0.024'}

	Recorder: 91b8a1d035044c12bee100ac14365a1c

		Model: {'id': '91b8a1d035044c12bee100ac14365a1c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.193, 'Rank IC': 0.07, 'Rank ICIR': 0.404}, 'data_train_vec': ['2022-06-23', '2025-06-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.404', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 0ec4f94c65294861a747a7cdd2d735c6

		Model: {'id': '0ec4f94c65294861a747a7cdd2d735c6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.32, 'Rank IC': 0.072, 'Rank ICIR': 0.432}, 'data_train_vec': ['2023-06-23', '2025-09-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.432', 'recency_weight': '0.348', 'weight': '0.041'}

	Recorder: 423a019d1dc343a3b874f403796155ac

		Model: {'id': '423a019d1dc343a3b874f403796155ac', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.511, 'Rank IC': 0.075, 'Rank ICIR': 0.592}, 'data_train_vec': ['2024-06-23', '2025-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.592', 'recency_weight': '0.494', 'weight': '0.110'}

	Recorder: ed7d1388ed444fc1bfc2e6538af5ed1b

		Model: {'id': 'ed7d1388ed444fc1bfc2e6538af5ed1b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.105, 'ICIR': 0.652, 'Rank IC': 0.087, 'Rank ICIR': 0.514}, 'data_train_vec': ['2025-06-23', '2026-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.514', 'recency_weight': '0.699', 'weight': '0.117'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260623_11 546961725867436262 (Recorders: 6/6)

	Recorder: 38c30ce765cb4de3a865a17107bb2b8f

		Model: {'id': '38c30ce765cb4de3a865a17107bb2b8f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.311, 'Rank IC': 0.063, 'Rank ICIR': 0.407}, 'data_train_vec': ['2020-06-23', '2024-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.407', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 8224ae66b9b544d1b218bf781932ef4c

		Model: {'id': '8224ae66b9b544d1b218bf781932ef4c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.239, 'Rank IC': 0.07, 'Rank ICIR': 0.435}, 'data_train_vec': ['2021-06-23', '2025-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.435', 'recency_weight': '0.171', 'weight': '0.021'}

	Recorder: 91209c78c64c4613b9c3d425099c5c4e

		Model: {'id': '91209c78c64c4613b9c3d425099c5c4e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.137, 'Rank IC': 0.063, 'Rank ICIR': 0.375}, 'data_train_vec': ['2022-06-23', '2025-06-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.375', 'recency_weight': '0.244', 'weight': '0.022'}

	Recorder: 3eb9aee1f95745b3a0e8de3e3a24ed5c

		Model: {'id': '3eb9aee1f95745b3a0e8de3e3a24ed5c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.215, 'Rank IC': 0.06, 'Rank ICIR': 0.356}, 'data_train_vec': ['2023-06-23', '2025-09-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.356', 'recency_weight': '0.348', 'weight': '0.028'}

	Recorder: 88738f2729b542b8b100fdfa004804cc

		Model: {'id': '88738f2729b542b8b100fdfa004804cc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.328, 'Rank IC': 0.066, 'Rank ICIR': 0.519}, 'data_train_vec': ['2024-06-23', '2025-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.519', 'recency_weight': '0.494', 'weight': '0.084'}

	Recorder: 7e3d9414f1ed4606b6ceab4e7e350e70

		Model: {'id': '7e3d9414f1ed4606b6ceab4e7e350e70', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.105, 'ICIR': 0.458, 'Rank IC': 0.068, 'Rank ICIR': 0.338}, 'data_train_vec': ['2025-06-23', '2026-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.338', 'recency_weight': '0.699', 'weight': '0.051'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260623_11 627409212451738386 (Recorders: 6/6)

	Recorder: 877ae3bd20e94c739b8656f6ecc1e3dc

		Model: {'id': '877ae3bd20e94c739b8656f6ecc1e3dc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.34, 'Rank IC': 0.069, 'Rank ICIR': 0.503}, 'data_train_vec': ['2020-06-23', '2024-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.503', 'recency_weight': '0.121', 'weight': '0.019'}

	Recorder: d786dde1a32c461ea1240cf54fead1e9

		Model: {'id': 'd786dde1a32c461ea1240cf54fead1e9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.231, 'Rank IC': 0.069, 'Rank ICIR': 0.48}, 'data_train_vec': ['2021-06-23', '2025-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.480', 'recency_weight': '0.171', 'weight': '0.025'}

	Recorder: 3987074587b5450eaabac8be0f7028e4

		Model: {'id': '3987074587b5450eaabac8be0f7028e4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.133, 'Rank IC': 0.062, 'Rank ICIR': 0.397}, 'data_train_vec': ['2022-06-23', '2025-06-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.397', 'recency_weight': '0.244', 'weight': '0.024'}

	Recorder: dbe9c1754996414db63ef8108351d44a

		Model: {'id': 'dbe9c1754996414db63ef8108351d44a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.214, 'Rank IC': 0.057, 'Rank ICIR': 0.397}, 'data_train_vec': ['2023-06-23', '2025-09-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.397', 'recency_weight': '0.348', 'weight': '0.035'}

	Recorder: e98959b176154ba5b63d9f00cb856ca3

		Model: {'id': 'e98959b176154ba5b63d9f00cb856ca3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.352, 'Rank IC': 0.061, 'Rank ICIR': 0.451}, 'data_train_vec': ['2024-06-23', '2025-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.451', 'recency_weight': '0.494', 'weight': '0.064'}

	Recorder: 18bb97eb72454e3fa327a775553559ce

		Model: {'id': '18bb97eb72454e3fa327a775553559ce', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.086, 'ICIR': 0.381, 'Rank IC': 0.065, 'Rank ICIR': 0.323}, 'data_train_vec': ['2025-06-23', '2026-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.323', 'recency_weight': '0.699', 'weight': '0.046'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260623_11 907351701794663648 (Recorders: 6/6)

	Recorder: 0ed58a88f6364ce5b3ff88765e04cadf

		Model: {'id': '0ed58a88f6364ce5b3ff88765e04cadf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.294, 'Rank IC': 0.061, 'Rank ICIR': 0.411}, 'data_train_vec': ['2020-06-23', '2024-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.411', 'recency_weight': '0.121', 'weight': '0.013'}

	Recorder: 461d76e4d9ae4a71b525496c08920d11

		Model: {'id': '461d76e4d9ae4a71b525496c08920d11', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.231, 'Rank IC': 0.075, 'Rank ICIR': 0.487}, 'data_train_vec': ['2021-06-23', '2025-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.487', 'recency_weight': '0.171', 'weight': '0.026'}

	Recorder: e7c5c35831f04a6bb4f0c5dfc99b6c37

		Model: {'id': 'e7c5c35831f04a6bb4f0c5dfc99b6c37', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.163, 'Rank IC': 0.068, 'Rank ICIR': 0.409}, 'data_train_vec': ['2022-06-23', '2025-06-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.409', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: a5c695fa99b947c5a2752b6a9b0e36da

		Model: {'id': 'a5c695fa99b947c5a2752b6a9b0e36da', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.212, 'Rank IC': 0.063, 'Rank ICIR': 0.383}, 'data_train_vec': ['2023-06-23', '2025-09-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.383', 'recency_weight': '0.348', 'weight': '0.032'}

	Recorder: b0f613f8445d4912823ef53b4c0be4f7

		Model: {'id': 'b0f613f8445d4912823ef53b4c0be4f7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.248, 'Rank IC': 0.065, 'Rank ICIR': 0.54}, 'data_train_vec': ['2024-06-23', '2025-12-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.540', 'recency_weight': '0.494', 'weight': '0.091'}

	Recorder: f0bf52f5ae95406ebdbb2b0e0778e7a4

		Model: {'id': 'f0bf52f5ae95406ebdbb2b0e0778e7a4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.088, 'ICIR': 0.521, 'Rank IC': 0.056, 'Rank ICIR': 0.342}, 'data_train_vec': ['2025-06-23', '2026-03-22'], 'train_time_vec': ['2026-06-23', '2026-06-23'], 'rank_icir': '0.342', 'recency_weight': '0.699', 'weight': '0.052'}
