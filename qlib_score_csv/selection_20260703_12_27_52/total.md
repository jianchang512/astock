# params 
 {'predict_dates': [{'start': '2026-07-03', 'end': '2026-07-03'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260703_11 277346026532182318 (Recorders: 6/6)

	Recorder: 42462b7b116b48219c50cebc2d65fdca

		Model: {'id': '42462b7b116b48219c50cebc2d65fdca', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.349, 'Rank IC': 0.067, 'Rank ICIR': 0.453}, 'data_train_vec': ['2020-07-03', '2025-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.453', 'recency_weight': '0.122', 'weight': '0.019'}

	Recorder: 402bc217d819484098a3d30c8b963835

		Model: {'id': '402bc217d819484098a3d30c8b963835', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.243, 'Rank IC': 0.07, 'Rank ICIR': 0.428}, 'data_train_vec': ['2021-07-03', '2025-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.428', 'recency_weight': '0.172', 'weight': '0.024'}

	Recorder: d73268eb0eda4804ac0212f9b6d4a0c6

		Model: {'id': 'd73268eb0eda4804ac0212f9b6d4a0c6', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.171, 'Rank IC': 0.065, 'Rank ICIR': 0.393}, 'data_train_vec': ['2022-07-03', '2025-07-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.393', 'recency_weight': '0.244', 'weight': '0.028'}

	Recorder: 308bec5e99e241bdb98c51455115455e

		Model: {'id': '308bec5e99e241bdb98c51455115455e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.369, 'Rank IC': 0.074, 'Rank ICIR': 0.476}, 'data_train_vec': ['2023-07-03', '2025-10-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.476', 'recency_weight': '0.348', 'weight': '0.059'}

	Recorder: 684b3901c9f14a53b8d900fd2885d4e0

		Model: {'id': '684b3901c9f14a53b8d900fd2885d4e0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.29, 'Rank IC': 0.062, 'Rank ICIR': 0.474}, 'data_train_vec': ['2024-07-03', '2026-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.474', 'recency_weight': '0.496', 'weight': '0.084'}

	Recorder: 8ea4ef8830cd4cfeb12b2aa566f35600

		Model: {'id': '8ea4ef8830cd4cfeb12b2aa566f35600', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.108, 'ICIR': 0.555, 'Rank IC': 0.066, 'Rank ICIR': 0.363}, 'data_train_vec': ['2025-07-03', '2026-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.363', 'recency_weight': '0.702', 'weight': '0.070'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260703_11 791659265401094083 (Recorders: 6/6)

	Recorder: e85700b721de4a1680efde0dfe5f8e8f

		Model: {'id': 'e85700b721de4a1680efde0dfe5f8e8f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.294, 'Rank IC': 0.061, 'Rank ICIR': 0.392}, 'data_train_vec': ['2020-07-03', '2025-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.392', 'recency_weight': '0.122', 'weight': '0.014'}

	Recorder: 8477158108014d00b08b0e073a430bec

		Model: {'id': '8477158108014d00b08b0e073a430bec', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.194, 'Rank IC': 0.061, 'Rank ICIR': 0.369}, 'data_train_vec': ['2021-07-03', '2025-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.369', 'recency_weight': '0.172', 'weight': '0.018'}

	Recorder: 3c64434f127d401ba14f5f5252fc5861

		Model: {'id': '3c64434f127d401ba14f5f5252fc5861', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.125, 'Rank IC': 0.062, 'Rank ICIR': 0.374}, 'data_train_vec': ['2022-07-03', '2025-07-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.374', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: 6ad85e727f9648709769bbd47257bfed

		Model: {'id': '6ad85e727f9648709769bbd47257bfed', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.266, 'Rank IC': 0.065, 'Rank ICIR': 0.421}, 'data_train_vec': ['2023-07-03', '2025-10-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.421', 'recency_weight': '0.348', 'weight': '0.047'}

	Recorder: 21f1cb59278b42e4bcf6918f510ff9da

		Model: {'id': '21f1cb59278b42e4bcf6918f510ff9da', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.303, 'Rank IC': 0.048, 'Rank ICIR': 0.365}, 'data_train_vec': ['2024-07-03', '2026-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.365', 'recency_weight': '0.496', 'weight': '0.050'}

	Recorder: e9956ed3fa5a4ed0bac4a97a65931520

		Model: {'id': 'e9956ed3fa5a4ed0bac4a97a65931520', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.378, 'Rank IC': 0.07, 'Rank ICIR': 0.337}, 'data_train_vec': ['2025-07-03', '2026-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.337', 'recency_weight': '0.702', 'weight': '0.060'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260703_11 651240158413341600 (Recorders: 5/6)

	Recorder: 46def84404264eb28cb3a048011f9201

		Model: {'id': '46def84404264eb28cb3a048011f9201', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.264, 'Rank IC': 0.06, 'Rank ICIR': 0.42}, 'data_train_vec': ['2020-07-03', '2025-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.420', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 247e198b0ce24bb89f2a3149e269b1f1

		Model: {'id': '247e198b0ce24bb89f2a3149e269b1f1', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.119, 'Rank IC': 0.049, 'Rank ICIR': 0.335}, 'data_train_vec': ['2021-07-03', '2025-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.335', 'recency_weight': '0.172', 'weight': '0.015'}

	Recorder: 389f3eeac24a471695ecaf768b3eddf9

		Model: {'id': '389f3eeac24a471695ecaf768b3eddf9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.234, 'Rank IC': 0.051, 'Rank ICIR': 0.378}, 'data_train_vec': ['2023-07-03', '2025-10-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.378', 'recency_weight': '0.348', 'weight': '0.038'}

	Recorder: ca4e586cfcb64bb6865a1e2826ea698e

		Model: {'id': 'ca4e586cfcb64bb6865a1e2826ea698e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.254, 'Rank IC': 0.041, 'Rank ICIR': 0.298}, 'data_train_vec': ['2024-07-03', '2026-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.298', 'recency_weight': '0.496', 'weight': '0.033'}

	Recorder: 93805b26cf0e41fda9cc49ff9464a899

		Model: {'id': '93805b26cf0e41fda9cc49ff9464a899', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.086, 'ICIR': 0.398, 'Rank IC': 0.075, 'Rank ICIR': 0.384}, 'data_train_vec': ['2025-07-03', '2026-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.384', 'recency_weight': '0.702', 'weight': '0.078'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260703_11 975998231475356286 (Recorders: 6/6)

	Recorder: ace16d9c59004ebea0f289af808f6a31

		Model: {'id': 'ace16d9c59004ebea0f289af808f6a31', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.319, 'Rank IC': 0.061, 'Rank ICIR': 0.419}, 'data_train_vec': ['2020-07-03', '2025-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.419', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: 4081e3e462774f0a818dd9a7932a947a

		Model: {'id': '4081e3e462774f0a818dd9a7932a947a', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.176, 'Rank IC': 0.067, 'Rank ICIR': 0.418}, 'data_train_vec': ['2021-07-03', '2025-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.418', 'recency_weight': '0.172', 'weight': '0.023'}

	Recorder: 2e57dc86388b49739cc77633cb74bd9c

		Model: {'id': '2e57dc86388b49739cc77633cb74bd9c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.14, 'Rank IC': 0.06, 'Rank ICIR': 0.388}, 'data_train_vec': ['2022-07-03', '2025-07-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.388', 'recency_weight': '0.244', 'weight': '0.028'}

	Recorder: 53a9caf4ead74d9abce408575e0209d8

		Model: {'id': '53a9caf4ead74d9abce408575e0209d8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.251, 'Rank IC': 0.053, 'Rank ICIR': 0.365}, 'data_train_vec': ['2023-07-03', '2025-10-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.365', 'recency_weight': '0.348', 'weight': '0.035'}

	Recorder: 7071d2a65ed24c1ca68104d2a68de77e

		Model: {'id': '7071d2a65ed24c1ca68104d2a68de77e', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.232, 'Rank IC': 0.058, 'Rank ICIR': 0.496}, 'data_train_vec': ['2024-07-03', '2026-01-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.496', 'recency_weight': '0.496', 'weight': '0.092'}

	Recorder: abfc783dfb954a83ad70bb2a82ebe4e1

		Model: {'id': 'abfc783dfb954a83ad70bb2a82ebe4e1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.519, 'Rank IC': 0.076, 'Rank ICIR': 0.493}, 'data_train_vec': ['2025-07-03', '2026-04-02'], 'train_time_vec': ['2026-07-03', '2026-07-03'], 'rank_icir': '0.493', 'recency_weight': '0.702', 'weight': '0.129'}
