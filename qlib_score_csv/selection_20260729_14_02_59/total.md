# params 
 {'predict_dates': [{'start': '2026-07-29', 'end': '2026-07-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260729_13 232893309524035755 (Recorders: 5/6)

	Recorder: 694639f66d4f4f40816182a1c2411298

		Model: {'id': '694639f66d4f4f40816182a1c2411298', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.337, 'Rank IC': 0.067, 'Rank ICIR': 0.443}, 'data_train_vec': ['2020-07-29', '2025-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.443', 'recency_weight': '0.122', 'weight': '0.059'}

	Recorder: cfefdf6275a64229956ae9d9978353a1

		Model: {'id': 'cfefdf6275a64229956ae9d9978353a1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.19, 'Rank IC': 0.066, 'Rank ICIR': 0.382}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.382', 'recency_weight': '0.171', 'weight': '0.061'}

	Recorder: 38c4b6d2098f46bdbb2b83d633f92884

		Model: {'id': '38c4b6d2098f46bdbb2b83d633f92884', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.166, 'Rank IC': 0.057, 'Rank ICIR': 0.338}, 'data_train_vec': ['2022-07-29', '2025-07-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.338', 'recency_weight': '0.244', 'weight': '0.069'}

	Recorder: 7cd35a5ca25346b8b9296ea57b8bf98b

		Model: {'id': '7cd35a5ca25346b8b9296ea57b8bf98b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.113, 'Rank IC': 0.063, 'Rank ICIR': 0.365}, 'data_train_vec': ['2023-07-29', '2025-10-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.365', 'recency_weight': '0.348', 'weight': '0.114'}

	Recorder: 90e47a9432044bddb836c985ec09ae88

		Model: {'id': '90e47a9432044bddb836c985ec09ae88', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.065, 'Rank IC': 0.021, 'Rank ICIR': 0.107}, 'data_train_vec': ['2024-07-29', '2026-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.107', 'recency_weight': '0.496', 'weight': '0.014'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260729_13 264260840940925606 (Recorders: 5/6)

	Recorder: bea6971f21d0492b8b5f5debad8500ee

		Model: {'id': 'bea6971f21d0492b8b5f5debad8500ee', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.328, 'Rank IC': 0.068, 'Rank ICIR': 0.42}, 'data_train_vec': ['2020-07-29', '2025-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.420', 'recency_weight': '0.122', 'weight': '0.053'}

	Recorder: cf68003418734499bf0d0bd4ca1e8057

		Model: {'id': 'cf68003418734499bf0d0bd4ca1e8057', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.228, 'Rank IC': 0.063, 'Rank ICIR': 0.382}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.382', 'recency_weight': '0.171', 'weight': '0.061'}

	Recorder: 4c2341a45f784df79e0118fc74a98905

		Model: {'id': '4c2341a45f784df79e0118fc74a98905', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.14, 'Rank IC': 0.051, 'Rank ICIR': 0.323}, 'data_train_vec': ['2022-07-29', '2025-07-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.323', 'recency_weight': '0.244', 'weight': '0.063'}

	Recorder: 476ecee3232d4757b209f6f21bb48120

		Model: {'id': '476ecee3232d4757b209f6f21bb48120', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.176, 'Rank IC': 0.059, 'Rank ICIR': 0.341}, 'data_train_vec': ['2023-07-29', '2025-10-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.341', 'recency_weight': '0.348', 'weight': '0.099'}

	Recorder: ebb2865d989a4b0e9fa79bccc037b9a7

		Model: {'id': 'ebb2865d989a4b0e9fa79bccc037b9a7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.119, 'Rank IC': 0.022, 'Rank ICIR': 0.114}, 'data_train_vec': ['2024-07-29', '2026-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.114', 'recency_weight': '0.496', 'weight': '0.016'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260729_13 796469256952124332 (Recorders: 5/6)

	Recorder: 50166b5be35f4dd79cbef1c34f471b2e

		Model: {'id': '50166b5be35f4dd79cbef1c34f471b2e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.223, 'Rank IC': 0.054, 'Rank ICIR': 0.331}, 'data_train_vec': ['2020-07-29', '2025-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.331', 'recency_weight': '0.122', 'weight': '0.033'}

	Recorder: a18db767c6c64391a430019375ed8698

		Model: {'id': 'a18db767c6c64391a430019375ed8698', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.112, 'Rank IC': 0.045, 'Rank ICIR': 0.27}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.270', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: 71746a05ed9c4cb6abc93820d418a04c

		Model: {'id': '71746a05ed9c4cb6abc93820d418a04c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.12, 'Rank IC': 0.047, 'Rank ICIR': 0.299}, 'data_train_vec': ['2022-07-29', '2025-07-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.299', 'recency_weight': '0.244', 'weight': '0.054'}

	Recorder: b17bfd4a125741fe9a03582ba1e3f14d

		Model: {'id': 'b17bfd4a125741fe9a03582ba1e3f14d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.206, 'Rank IC': 0.051, 'Rank ICIR': 0.287}, 'data_train_vec': ['2023-07-29', '2025-10-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.287', 'recency_weight': '0.348', 'weight': '0.070'}

	Recorder: 8f5aba69689444c8ab34c01f9e45ba68

		Model: {'id': '8f5aba69689444c8ab34c01f9e45ba68', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.089, 'Rank IC': 0.019, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-07-29', '2026-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.092', 'recency_weight': '0.496', 'weight': '0.010'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260729_13 712427010411231633 (Recorders: 3/6)

	Recorder: 8497351977c54eff90790e5826535b3d

		Model: {'id': '8497351977c54eff90790e5826535b3d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.281, 'Rank IC': 0.065, 'Rank ICIR': 0.434}, 'data_train_vec': ['2020-07-29', '2025-01-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.434', 'recency_weight': '0.122', 'weight': '0.056'}

	Recorder: 7f70031f474b4703914815691d7edca6

		Model: {'id': '7f70031f474b4703914815691d7edca6', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.177, 'Rank IC': 0.06, 'Rank ICIR': 0.374}, 'data_train_vec': ['2021-07-28', '2025-04-27'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.374', 'recency_weight': '0.171', 'weight': '0.059'}

	Recorder: c7f464ce2b6940e69d83f2689b297a4e

		Model: {'id': 'c7f464ce2b6940e69d83f2689b297a4e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.095, 'Rank IC': 0.056, 'Rank ICIR': 0.361}, 'data_train_vec': ['2022-07-29', '2025-07-28'], 'train_time_vec': ['2026-07-29', '2026-07-29'], 'rank_icir': '0.361', 'recency_weight': '0.244', 'weight': '0.078'}
