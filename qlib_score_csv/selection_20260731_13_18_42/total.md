# params 
 {'predict_dates': [{'start': '2026-07-31', 'end': '2026-07-31'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260801_12 331984421981454771 (Recorders: 4/6)

	Recorder: 62c73cd36f364fbcb07d91edc4d29e59

		Model: {'id': '62c73cd36f364fbcb07d91edc4d29e59', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.315, 'Rank IC': 0.07, 'Rank ICIR': 0.435}, 'data_train_vec': ['2020-08-01', '2025-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.435', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: 32d9ba79a91b4bc8beec3c52602889cf

		Model: {'id': '32d9ba79a91b4bc8beec3c52602889cf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.179, 'Rank IC': 0.069, 'Rank ICIR': 0.4}, 'data_train_vec': ['2021-08-01', '2025-04-30'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.400', 'recency_weight': '0.172', 'weight': '0.063'}

	Recorder: 0bc02d248faa483fa1c57eaaf0718299

		Model: {'id': '0bc02d248faa483fa1c57eaaf0718299', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.086, 'Rank IC': 0.053, 'Rank ICIR': 0.307}, 'data_train_vec': ['2022-08-01', '2025-07-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.307', 'recency_weight': '0.245', 'weight': '0.053'}

	Recorder: f74a317b4df9443a8a51498791937bb6

		Model: {'id': 'f74a317b4df9443a8a51498791937bb6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.113, 'Rank IC': 0.074, 'Rank ICIR': 0.451}, 'data_train_vec': ['2023-08-01', '2025-10-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.451', 'recency_weight': '0.349', 'weight': '0.162'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260801_12 100753591831558629 (Recorders: 5/6)

	Recorder: 9131cb9aa8e34bb2bb082c429b166bd6

		Model: {'id': '9131cb9aa8e34bb2bb082c429b166bd6', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.331, 'Rank IC': 0.071, 'Rank ICIR': 0.436}, 'data_train_vec': ['2020-08-01', '2025-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.436', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: 2953612c970947d094de377c1c5269b3

		Model: {'id': '2953612c970947d094de377c1c5269b3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.243, 'Rank IC': 0.067, 'Rank ICIR': 0.414}, 'data_train_vec': ['2021-08-01', '2025-04-30'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.414', 'recency_weight': '0.172', 'weight': '0.067'}

	Recorder: cde050b18fee4a378d3ff7e524782fce

		Model: {'id': 'cde050b18fee4a378d3ff7e524782fce', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.13, 'Rank IC': 0.052, 'Rank ICIR': 0.321}, 'data_train_vec': ['2022-08-01', '2025-07-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.321', 'recency_weight': '0.245', 'weight': '0.057'}

	Recorder: dffa35fd443d4759b894848f4ed20f8b

		Model: {'id': 'dffa35fd443d4759b894848f4ed20f8b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.253, 'Rank IC': 0.07, 'Rank ICIR': 0.439}, 'data_train_vec': ['2023-08-01', '2025-10-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.439', 'recency_weight': '0.349', 'weight': '0.153'}

	Recorder: d32710360bd44380a4ce2c3aa5833018

		Model: {'id': 'd32710360bd44380a4ce2c3aa5833018', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.111, 'Rank IC': 0.021, 'Rank ICIR': 0.115}, 'data_train_vec': ['2024-08-01', '2026-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.115', 'recency_weight': '0.498', 'weight': '0.015'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260801_12 223003412083860235 (Recorders: 5/6)

	Recorder: 3f660c3aecdc422591ce961397ed3cbf

		Model: {'id': '3f660c3aecdc422591ce961397ed3cbf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.22, 'Rank IC': 0.055, 'Rank ICIR': 0.331}, 'data_train_vec': ['2020-08-01', '2025-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.331', 'recency_weight': '0.122', 'weight': '0.030'}

	Recorder: 1eb10ba8add04f53ad2a7d94b67a95ee

		Model: {'id': '1eb10ba8add04f53ad2a7d94b67a95ee', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.142, 'Rank IC': 0.05, 'Rank ICIR': 0.29}, 'data_train_vec': ['2021-08-01', '2025-04-30'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.290', 'recency_weight': '0.172', 'weight': '0.033'}

	Recorder: ff3a61a644f94cde87ba7dea3775ea80

		Model: {'id': 'ff3a61a644f94cde87ba7dea3775ea80', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.128, 'Rank IC': 0.049, 'Rank ICIR': 0.306}, 'data_train_vec': ['2022-08-01', '2025-07-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.306', 'recency_weight': '0.245', 'weight': '0.052'}

	Recorder: a5e160860a974b2dad47b82ad5438e30

		Model: {'id': 'a5e160860a974b2dad47b82ad5438e30', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.25, 'Rank IC': 0.057, 'Rank ICIR': 0.314}, 'data_train_vec': ['2023-08-01', '2025-10-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.314', 'recency_weight': '0.349', 'weight': '0.078'}

	Recorder: 344d6b0b50074dd185082e0a510436a5

		Model: {'id': '344d6b0b50074dd185082e0a510436a5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.114, 'Rank IC': 0.029, 'Rank ICIR': 0.141}, 'data_train_vec': ['2024-08-01', '2026-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.141', 'recency_weight': '0.498', 'weight': '0.023'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260801_12 719670460241221117 (Recorders: 2/6)

	Recorder: 6ad094d1fd15478c835235ffd1272e90

		Model: {'id': '6ad094d1fd15478c835235ffd1272e90', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.276, 'Rank IC': 0.068, 'Rank ICIR': 0.451}, 'data_train_vec': ['2020-08-01', '2025-01-31'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.451', 'recency_weight': '0.122', 'weight': '0.056'}

	Recorder: bab17f46280043d596f06f3af43dcef4

		Model: {'id': 'bab17f46280043d596f06f3af43dcef4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.129, 'Rank IC': 0.06, 'Rank ICIR': 0.367}, 'data_train_vec': ['2021-08-01', '2025-04-30'], 'train_time_vec': ['2026-08-01', '2026-08-01'], 'rank_icir': '0.367', 'recency_weight': '0.172', 'weight': '0.053'}
