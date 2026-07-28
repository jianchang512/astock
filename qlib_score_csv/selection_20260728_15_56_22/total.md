# params 
 {'predict_dates': [{'start': '2026-07-28', 'end': '2026-07-28'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260728_15 367639283309215108 (Recorders: 5/6)

	Recorder: ea928f71ed8242369b3276a586d8fa8d

		Model: {'id': 'ea928f71ed8242369b3276a586d8fa8d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.354, 'Rank IC': 0.067, 'Rank ICIR': 0.439}, 'data_train_vec': ['2020-07-28', '2025-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.439', 'recency_weight': '0.122', 'weight': '0.047'}

	Recorder: f6be011009d440f5aa0b617fbf27970e

		Model: {'id': 'f6be011009d440f5aa0b617fbf27970e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.19, 'Rank IC': 0.068, 'Rank ICIR': 0.39}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.390', 'recency_weight': '0.172', 'weight': '0.052'}

	Recorder: 15353abe70e34efb95efa8b3dfbc4393

		Model: {'id': '15353abe70e34efb95efa8b3dfbc4393', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.176, 'Rank IC': 0.064, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-07-28', '2025-07-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.073'}

	Recorder: 7977c1f3473747bdbc3f00af295c73c7

		Model: {'id': '7977c1f3473747bdbc3f00af295c73c7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.114, 'Rank IC': 0.068, 'Rank ICIR': 0.406}, 'data_train_vec': ['2023-07-28', '2025-10-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.406', 'recency_weight': '0.348', 'weight': '0.114'}

	Recorder: ef9a99daeb5547b1818a90c7eee944b1

		Model: {'id': 'ef9a99daeb5547b1818a90c7eee944b1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.082, 'Rank IC': 0.037, 'Rank ICIR': 0.19}, 'data_train_vec': ['2024-07-28', '2026-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.190', 'recency_weight': '0.496', 'weight': '0.036'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260728_15 171376120462975934 (Recorders: 5/6)

	Recorder: 28fd8d7b5d7048f1a82f709a42a7ce19

		Model: {'id': '28fd8d7b5d7048f1a82f709a42a7ce19', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.344, 'Rank IC': 0.07, 'Rank ICIR': 0.435}, 'data_train_vec': ['2020-07-28', '2025-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.435', 'recency_weight': '0.122', 'weight': '0.046'}

	Recorder: f25b91e278dd40be81aff92ff4e70d3c

		Model: {'id': 'f25b91e278dd40be81aff92ff4e70d3c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.233, 'Rank IC': 0.065, 'Rank ICIR': 0.394}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.394', 'recency_weight': '0.172', 'weight': '0.053'}

	Recorder: ef8308ec3071412bb08f1568539cf83c

		Model: {'id': 'ef8308ec3071412bb08f1568539cf83c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.157, 'Rank IC': 0.055, 'Rank ICIR': 0.351}, 'data_train_vec': ['2022-07-28', '2025-07-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.351', 'recency_weight': '0.244', 'weight': '0.060'}

	Recorder: 7259550e38e84226bbdd12fe083e6b8b

		Model: {'id': '7259550e38e84226bbdd12fe083e6b8b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.202, 'Rank IC': 0.057, 'Rank ICIR': 0.359}, 'data_train_vec': ['2023-07-28', '2025-10-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.359', 'recency_weight': '0.348', 'weight': '0.089'}

	Recorder: 9e6afb2022c54871a3efbdb78da01985

		Model: {'id': '9e6afb2022c54871a3efbdb78da01985', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.174, 'Rank IC': 0.027, 'Rank ICIR': 0.133}, 'data_train_vec': ['2024-07-28', '2026-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.133', 'recency_weight': '0.496', 'weight': '0.017'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260728_15 259226100587908871 (Recorders: 5/6)

	Recorder: ff319ad6404c413a9468e5536f15027f

		Model: {'id': 'ff319ad6404c413a9468e5536f15027f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.224, 'Rank IC': 0.055, 'Rank ICIR': 0.335}, 'data_train_vec': ['2020-07-28', '2025-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.335', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: bd5a628e4b24414899e51d6bae084c12

		Model: {'id': 'bd5a628e4b24414899e51d6bae084c12', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.116, 'Rank IC': 0.048, 'Rank ICIR': 0.282}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.282', 'recency_weight': '0.172', 'weight': '0.027'}

	Recorder: 91fd0c8edfb24ea5bd39d38885ba0bab

		Model: {'id': '91fd0c8edfb24ea5bd39d38885ba0bab', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.132, 'Rank IC': 0.051, 'Rank ICIR': 0.322}, 'data_train_vec': ['2022-07-28', '2025-07-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.322', 'recency_weight': '0.244', 'weight': '0.050'}

	Recorder: 4742b0f1a39c462c8680b4e2285b1d69

		Model: {'id': '4742b0f1a39c462c8680b4e2285b1d69', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.237, 'Rank IC': 0.057, 'Rank ICIR': 0.33}, 'data_train_vec': ['2023-07-28', '2025-10-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.330', 'recency_weight': '0.348', 'weight': '0.075'}

	Recorder: 089d281987e6428eb2fc4d71a4c47d99

		Model: {'id': '089d281987e6428eb2fc4d71a4c47d99', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.122, 'Rank IC': 0.021, 'Rank ICIR': 0.102}, 'data_train_vec': ['2024-07-28', '2026-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.102', 'recency_weight': '0.496', 'weight': '0.010'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260728_15 684559763851167000 (Recorders: 4/6)

	Recorder: fe5fd2b10eba4fd58832d783fe7077c4

		Model: {'id': 'fe5fd2b10eba4fd58832d783fe7077c4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.275, 'Rank IC': 0.064, 'Rank ICIR': 0.442}, 'data_train_vec': ['2020-07-28', '2025-01-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.442', 'recency_weight': '0.122', 'weight': '0.047'}

	Recorder: b86c579e90f34b0ca535bf3de16c004a

		Model: {'id': 'b86c579e90f34b0ca535bf3de16c004a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.189, 'Rank IC': 0.062, 'Rank ICIR': 0.388}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.388', 'recency_weight': '0.172', 'weight': '0.051'}

	Recorder: d52deaf9a5f84de18d12dd6506fd7850

		Model: {'id': 'd52deaf9a5f84de18d12dd6506fd7850', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.112, 'Rank IC': 0.057, 'Rank ICIR': 0.362}, 'data_train_vec': ['2022-07-28', '2025-07-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.362', 'recency_weight': '0.244', 'weight': '0.064'}

	Recorder: 0d596994c1d14b90ab845ce72a659c43

		Model: {'id': '0d596994c1d14b90ab845ce72a659c43', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.051, 'Rank IC': 0.048, 'Rank ICIR': 0.299}, 'data_train_vec': ['2023-07-28', '2025-10-27'], 'train_time_vec': ['2026-07-28', '2026-07-28'], 'rank_icir': '0.299', 'recency_weight': '0.348', 'weight': '0.062'}
