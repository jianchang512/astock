# params 
 {'predict_dates': [{'start': '2026-05-13', 'end': '2026-05-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260513_11 424905194610542787 (Recorders: 6/6)

	Recorder: 3c7f50b9369549ebad7510028ed302a0

		Model: {'id': '3c7f50b9369549ebad7510028ed302a0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.345, 'Rank IC': 0.052, 'Rank ICIR': 0.34}, 'data_train_vec': ['2020-05-13', '2024-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.340', 'recency_weight': '0.122', 'weight': '0.011'}

	Recorder: ceb8081db265487f8a740768f6ed1457

		Model: {'id': 'ceb8081db265487f8a740768f6ed1457', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.173, 'Rank IC': 0.039, 'Rank ICIR': 0.259}, 'data_train_vec': ['2021-05-13', '2025-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.259', 'recency_weight': '0.173', 'weight': '0.009'}

	Recorder: 301610885f6441eab0d2d767841759de

		Model: {'id': '301610885f6441eab0d2d767841759de', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.165, 'Rank IC': 0.045, 'Rank ICIR': 0.279}, 'data_train_vec': ['2022-05-13', '2025-05-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.279', 'recency_weight': '0.244', 'weight': '0.015'}

	Recorder: 999b5fe4fa7747419abc8829ea7e4fdd

		Model: {'id': '999b5fe4fa7747419abc8829ea7e4fdd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.21, 'Rank IC': 0.035, 'Rank ICIR': 0.227}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.227', 'recency_weight': '0.348', 'weight': '0.014'}

	Recorder: 02dfcd24a7be4ae088f03dd17baffc43

		Model: {'id': '02dfcd24a7be4ae088f03dd17baffc43', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.224, 'Rank IC': 0.047, 'Rank ICIR': 0.39}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.390', 'recency_weight': '0.496', 'weight': '0.061'}

	Recorder: 73a7c1ebf1664954b67195f5cd93fb4f

		Model: {'id': '73a7c1ebf1664954b67195f5cd93fb4f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.452, 'Rank IC': 0.053, 'Rank ICIR': 0.454}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.454', 'recency_weight': '0.707', 'weight': '0.117'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260513_11 757331203868940142 (Recorders: 4/6)

	Recorder: fbad707f9e144368b0a640940d4c5d80

		Model: {'id': 'fbad707f9e144368b0a640940d4c5d80', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.334, 'Rank IC': 0.055, 'Rank ICIR': 0.353}, 'data_train_vec': ['2020-05-13', '2024-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.353', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: 7b49e5372b5b423abfff7db80af5526c

		Model: {'id': '7b49e5372b5b423abfff7db80af5526c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.141, 'Rank IC': 0.04, 'Rank ICIR': 0.264}, 'data_train_vec': ['2021-05-13', '2025-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.264', 'recency_weight': '0.173', 'weight': '0.010'}

	Recorder: 7a9a650b306f4915899739d4307cfe13

		Model: {'id': '7a9a650b306f4915899739d4307cfe13', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.102, 'Rank IC': 0.041, 'Rank ICIR': 0.251}, 'data_train_vec': ['2022-05-13', '2025-05-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.251', 'recency_weight': '0.244', 'weight': '0.012'}

	Recorder: fa3b50b1b21e489184f88b7a772c69a1

		Model: {'id': 'fa3b50b1b21e489184f88b7a772c69a1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.411, 'Rank IC': 0.055, 'Rank ICIR': 0.57}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.570', 'recency_weight': '0.707', 'weight': '0.185'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260513_11 880116070852754880 (Recorders: 4/6)

	Recorder: 48aa98aae30343359a99e3d91e5768da

		Model: {'id': '48aa98aae30343359a99e3d91e5768da', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.33, 'Rank IC': 0.056, 'Rank ICIR': 0.448}, 'data_train_vec': ['2020-05-13', '2024-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.448', 'recency_weight': '0.122', 'weight': '0.020'}

	Recorder: c43fe5ddd0324e23a8e6d1950e96c31b

		Model: {'id': 'c43fe5ddd0324e23a8e6d1950e96c31b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.213, 'Rank IC': 0.049, 'Rank ICIR': 0.397}, 'data_train_vec': ['2021-05-13', '2025-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.397', 'recency_weight': '0.173', 'weight': '0.022'}

	Recorder: 6e8f13dacdd64b5cb528596fcee1d444

		Model: {'id': '6e8f13dacdd64b5cb528596fcee1d444', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.134, 'Rank IC': 0.052, 'Rank ICIR': 0.355}, 'data_train_vec': ['2022-05-13', '2025-05-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.355', 'recency_weight': '0.244', 'weight': '0.025'}

	Recorder: 57fb7dd2e30c4834ba99ba021308c35a

		Model: {'id': '57fb7dd2e30c4834ba99ba021308c35a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.474, 'Rank IC': 0.067, 'Rank ICIR': 0.483}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.483', 'recency_weight': '0.707', 'weight': '0.133'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260513_11 370431052694575049 (Recorders: 6/6)

	Recorder: ef07f0abcf1147d3afb4d0c681c8dc39

		Model: {'id': 'ef07f0abcf1147d3afb4d0c681c8dc39', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.331, 'Rank IC': 0.055, 'Rank ICIR': 0.368}, 'data_train_vec': ['2020-05-13', '2024-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.368', 'recency_weight': '0.122', 'weight': '0.013'}

	Recorder: eab41988c0944fe8a670243f091cb789

		Model: {'id': 'eab41988c0944fe8a670243f091cb789', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.196, 'Rank IC': 0.041, 'Rank ICIR': 0.286}, 'data_train_vec': ['2021-05-13', '2025-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.286', 'recency_weight': '0.173', 'weight': '0.011'}

	Recorder: f358155c8d5e4d7dbe14fa94faca5b55

		Model: {'id': 'f358155c8d5e4d7dbe14fa94faca5b55', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.176, 'Rank IC': 0.045, 'Rank ICIR': 0.289}, 'data_train_vec': ['2022-05-13', '2025-05-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.289', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: a60607fff7ea4a14bef2696cf736384b

		Model: {'id': 'a60607fff7ea4a14bef2696cf736384b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.146, 'Rank IC': 0.039, 'Rank ICIR': 0.246}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.246', 'recency_weight': '0.348', 'weight': '0.017'}

	Recorder: a488a360be90470399aedf91dad1170a

		Model: {'id': 'a488a360be90470399aedf91dad1170a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.256, 'Rank IC': 0.047, 'Rank ICIR': 0.423}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.423', 'recency_weight': '0.496', 'weight': '0.072'}

	Recorder: e170f026dddc481ba190eb3aa43705f6

		Model: {'id': 'e170f026dddc481ba190eb3aa43705f6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.583, 'Rank IC': 0.062, 'Rank ICIR': 0.625}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.625', 'recency_weight': '0.707', 'weight': '0.223'}
