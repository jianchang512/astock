# params 
 {'predict_dates': [{'start': '2026-05-25', 'end': '2026-05-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260525_11 508765450346694865 (Recorders: 6/6)

	Recorder: 70de47b765e04d4293dabb81b7b1e594

		Model: {'id': '70de47b765e04d4293dabb81b7b1e594', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.363, 'Rank IC': 0.056, 'Rank ICIR': 0.388}, 'data_train_vec': ['2020-05-25', '2024-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.388', 'recency_weight': '0.122', 'weight': '0.025'}

	Recorder: ba208ba64c3247dfa9fbf2d5d16c09b3

		Model: {'id': 'ba208ba64c3247dfa9fbf2d5d16c09b3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.209, 'Rank IC': 0.051, 'Rank ICIR': 0.363}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.363', 'recency_weight': '0.173', 'weight': '0.032'}

	Recorder: 4cc2902874af4961a008af07ccef37bd

		Model: {'id': '4cc2902874af4961a008af07ccef37bd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.232, 'Rank IC': 0.062, 'Rank ICIR': 0.39}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.390', 'recency_weight': '0.244', 'weight': '0.052'}

	Recorder: bce1dae612ae453689d83b6b66c0305b

		Model: {'id': 'bce1dae612ae453689d83b6b66c0305b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.214, 'Rank IC': 0.052, 'Rank ICIR': 0.333}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.333', 'recency_weight': '0.348', 'weight': '0.054'}

	Recorder: 542278f2758142378dec88be123e8c1b

		Model: {'id': '542278f2758142378dec88be123e8c1b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.162, 'Rank IC': 0.042, 'Rank ICIR': 0.323}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.323', 'recency_weight': '0.496', 'weight': '0.072'}

	Recorder: f01c9133da9d427989d59daf152eecca

		Model: {'id': 'f01c9133da9d427989d59daf152eecca', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.452, 'Rank IC': 0.041, 'Rank ICIR': 0.284}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.284', 'recency_weight': '0.707', 'weight': '0.079'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260525_11 617758274842310939 (Recorders: 5/6)

	Recorder: 172b874adc1f469ba9989ce95ce84b95

		Model: {'id': '172b874adc1f469ba9989ce95ce84b95', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.293, 'Rank IC': 0.051, 'Rank ICIR': 0.344}, 'data_train_vec': ['2020-05-25', '2024-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.344', 'recency_weight': '0.122', 'weight': '0.020'}

	Recorder: e3483ae35e654f76a0e5d0f8bce3b983

		Model: {'id': 'e3483ae35e654f76a0e5d0f8bce3b983', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.179, 'Rank IC': 0.052, 'Rank ICIR': 0.363}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.363', 'recency_weight': '0.173', 'weight': '0.032'}

	Recorder: 2e764f71e94142a4957a9cd0f852d77d

		Model: {'id': '2e764f71e94142a4957a9cd0f852d77d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.104, 'Rank IC': 0.054, 'Rank ICIR': 0.328}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.328', 'recency_weight': '0.244', 'weight': '0.037'}

	Recorder: 2a8100f002024be3abd54a3af7b30d83

		Model: {'id': '2a8100f002024be3abd54a3af7b30d83', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.123, 'Rank IC': 0.052, 'Rank ICIR': 0.32}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.320', 'recency_weight': '0.348', 'weight': '0.050'}

	Recorder: e290b7c9738a4616abcdb4e457f63349

		Model: {'id': 'e290b7c9738a4616abcdb4e457f63349', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.206, 'Rank IC': 0.018, 'Rank ICIR': 0.141}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.141', 'recency_weight': '0.707', 'weight': '0.020'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260525_11 715764984621780877 (Recorders: 4/6)

	Recorder: 270e8c4fe352443aa8017f0edeb7120a

		Model: {'id': '270e8c4fe352443aa8017f0edeb7120a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.305, 'Rank IC': 0.058, 'Rank ICIR': 0.445}, 'data_train_vec': ['2020-05-25', '2024-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.445', 'recency_weight': '0.122', 'weight': '0.033'}

	Recorder: c51de37a366741aeb9eb2041031065af

		Model: {'id': 'c51de37a366741aeb9eb2041031065af', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.031, 'ICIR': 0.211, 'Rank IC': 0.056, 'Rank ICIR': 0.422}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.422', 'recency_weight': '0.173', 'weight': '0.043'}

	Recorder: a4255b4af92242fa81765ecaecd039f6

		Model: {'id': 'a4255b4af92242fa81765ecaecd039f6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.127, 'Rank IC': 0.058, 'Rank ICIR': 0.382}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.382', 'recency_weight': '0.244', 'weight': '0.050'}

	Recorder: 4358d25a47454cdb9978e1577c0d134d

		Model: {'id': '4358d25a47454cdb9978e1577c0d134d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.393, 'Rank IC': 0.082, 'Rank ICIR': 0.396}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.396', 'recency_weight': '0.707', 'weight': '0.154'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260525_11 962047148536873905 (Recorders: 6/6)

	Recorder: 9fd55309495d445bbdc4acc39f6c8476

		Model: {'id': '9fd55309495d445bbdc4acc39f6c8476', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.298, 'Rank IC': 0.052, 'Rank ICIR': 0.373}, 'data_train_vec': ['2020-05-25', '2024-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.373', 'recency_weight': '0.122', 'weight': '0.024'}

	Recorder: 1c7a1d03453a415e8556d4205fffe959

		Model: {'id': '1c7a1d03453a415e8556d4205fffe959', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.183, 'Rank IC': 0.048, 'Rank ICIR': 0.354}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.354', 'recency_weight': '0.173', 'weight': '0.030'}

	Recorder: f8e6a0ba36ad4c5aa6844bd47a2352fa

		Model: {'id': 'f8e6a0ba36ad4c5aa6844bd47a2352fa', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.246, 'Rank IC': 0.064, 'Rank ICIR': 0.389}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.389', 'recency_weight': '0.244', 'weight': '0.051'}

	Recorder: cd0071b811e04872a1d1790a47fadbb7

		Model: {'id': 'cd0071b811e04872a1d1790a47fadbb7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.213, 'Rank IC': 0.055, 'Rank ICIR': 0.367}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.367', 'recency_weight': '0.348', 'weight': '0.065'}

	Recorder: ea0ee6c561934e74a04c1dd5500e4d8c

		Model: {'id': 'ea0ee6c561934e74a04c1dd5500e4d8c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.137, 'Rank IC': 0.028, 'Rank ICIR': 0.235}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.235', 'recency_weight': '0.496', 'weight': '0.038'}

	Recorder: ecbf58805ac94959980039b1d69e5626

		Model: {'id': 'ecbf58805ac94959980039b1d69e5626', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.489, 'Rank IC': 0.031, 'Rank ICIR': 0.203}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.203', 'recency_weight': '0.707', 'weight': '0.040'}
