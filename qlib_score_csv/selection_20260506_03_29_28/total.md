# params 
 {'predict_dates': [{'start': '2026-05-06', 'end': '2026-05-06'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260506_12 637767287572363479 (Recorders: 6/6)

	Recorder: cbe4c00b2a584b589c52daa96a7f49b8

		Model: {'id': 'cbe4c00b2a584b589c52daa96a7f49b8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.062, 'ICIR': 0.427, 'Rank IC': 0.061, 'Rank ICIR': 0.399}, 'data_train_vec': ['2020-05-06', '2024-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.399', 'recency_weight': '0.122', 'weight': '0.016'}

	Recorder: e68f2a78004046c992632de2c6d06a48

		Model: {'id': 'e68f2a78004046c992632de2c6d06a48', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.253, 'Rank IC': 0.047, 'Rank ICIR': 0.313}, 'data_train_vec': ['2021-05-06', '2025-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.313', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: bdc591a844c04a8cb108a5fb8b6fa100

		Model: {'id': 'bdc591a844c04a8cb108a5fb8b6fa100', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.215, 'Rank IC': 0.044, 'Rank ICIR': 0.273}, 'data_train_vec': ['2022-05-06', '2025-05-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.273', 'recency_weight': '0.244', 'weight': '0.015'}

	Recorder: 0a69fb2585574776b8c02d3f7c015803

		Model: {'id': '0a69fb2585574776b8c02d3f7c015803', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.165, 'Rank IC': 0.042, 'Rank ICIR': 0.258}, 'data_train_vec': ['2023-05-06', '2025-08-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.258', 'recency_weight': '0.348', 'weight': '0.019'}

	Recorder: b9147cc4500d4396bde6c180e16045d4

		Model: {'id': 'b9147cc4500d4396bde6c180e16045d4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.08, 'Rank IC': 0.022, 'Rank ICIR': 0.177}, 'data_train_vec': ['2024-05-06', '2025-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.177', 'recency_weight': '0.496', 'weight': '0.013'}

	Recorder: 1729b841fbb44ab09905001d23e97596

		Model: {'id': '1729b841fbb44ab09905001d23e97596', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.086, 'ICIR': 0.681, 'Rank IC': 0.079, 'Rank ICIR': 0.622}, 'data_train_vec': ['2025-05-06', '2026-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.622', 'recency_weight': '0.707', 'weight': '0.226'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260506_12 988781653240449655 (Recorders: 4/6)

	Recorder: 33122f564de44c2fa6673e3c2849b52c

		Model: {'id': '33122f564de44c2fa6673e3c2849b52c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.367, 'Rank IC': 0.058, 'Rank ICIR': 0.347}, 'data_train_vec': ['2020-05-06', '2024-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.347', 'recency_weight': '0.122', 'weight': '0.012'}

	Recorder: d8411ca4db3d497abb1cbe2efc1282d5

		Model: {'id': 'd8411ca4db3d497abb1cbe2efc1282d5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.217, 'Rank IC': 0.048, 'Rank ICIR': 0.314}, 'data_train_vec': ['2021-05-06', '2025-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.314', 'recency_weight': '0.173', 'weight': '0.014'}

	Recorder: 01cc59f8abbb446b803afafa6acef74a

		Model: {'id': '01cc59f8abbb446b803afafa6acef74a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.115, 'Rank IC': 0.044, 'Rank ICIR': 0.278}, 'data_train_vec': ['2022-05-06', '2025-05-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.278', 'recency_weight': '0.244', 'weight': '0.016'}

	Recorder: ae77f0ce439d4661887e5fc38b1af71d

		Model: {'id': 'ae77f0ce439d4661887e5fc38b1af71d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.06, 'ICIR': 0.507, 'Rank IC': 0.056, 'Rank ICIR': 0.519}, 'data_train_vec': ['2025-05-06', '2026-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.519', 'recency_weight': '0.707', 'weight': '0.157'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260506_12 625384440485424538 (Recorders: 4/6)

	Recorder: ed8bb9ffc96340d698bdc146b2ea90df

		Model: {'id': 'ed8bb9ffc96340d698bdc146b2ea90df', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.364, 'Rank IC': 0.058, 'Rank ICIR': 0.454}, 'data_train_vec': ['2020-05-06', '2024-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.454', 'recency_weight': '0.122', 'weight': '0.021'}

	Recorder: 9ceda1054f49458ebf8831177be3a0bc

		Model: {'id': '9ceda1054f49458ebf8831177be3a0bc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.26, 'Rank IC': 0.05, 'Rank ICIR': 0.41}, 'data_train_vec': ['2021-05-06', '2025-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.410', 'recency_weight': '0.173', 'weight': '0.024'}

	Recorder: 3e139711d73b4f8f9c31c51885ea1b0e

		Model: {'id': '3e139711d73b4f8f9c31c51885ea1b0e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.149, 'Rank IC': 0.051, 'Rank ICIR': 0.357}, 'data_train_vec': ['2022-05-06', '2025-05-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.357', 'recency_weight': '0.244', 'weight': '0.026'}

	Recorder: ab409500611240239771541067589b16

		Model: {'id': 'ab409500611240239771541067589b16', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.292, 'Rank IC': 0.026, 'Rank ICIR': 0.222}, 'data_train_vec': ['2025-05-06', '2026-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.222', 'recency_weight': '0.707', 'weight': '0.029'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260506_12 531038970118824684 (Recorders: 6/6)

	Recorder: 36c11088c0594c3eb953fc0f90ea1cfa

		Model: {'id': '36c11088c0594c3eb953fc0f90ea1cfa', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.342, 'Rank IC': 0.058, 'Rank ICIR': 0.379}, 'data_train_vec': ['2020-05-06', '2024-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.379', 'recency_weight': '0.122', 'weight': '0.014'}

	Recorder: c036673bb539415bb92e52da101a5ab5

		Model: {'id': 'c036673bb539415bb92e52da101a5ab5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.224, 'Rank IC': 0.049, 'Rank ICIR': 0.349}, 'data_train_vec': ['2021-05-06', '2025-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.349', 'recency_weight': '0.173', 'weight': '0.017'}

	Recorder: 7dbc17295ffb4df98b32a51c00318e02

		Model: {'id': '7dbc17295ffb4df98b32a51c00318e02', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.226, 'Rank IC': 0.049, 'Rank ICIR': 0.31}, 'data_train_vec': ['2022-05-06', '2025-05-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.310', 'recency_weight': '0.244', 'weight': '0.019'}

	Recorder: fda901effcb34815981ea85113525546

		Model: {'id': 'fda901effcb34815981ea85113525546', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.302, 'Rank IC': 0.043, 'Rank ICIR': 0.288}, 'data_train_vec': ['2023-05-06', '2025-08-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.288', 'recency_weight': '0.348', 'weight': '0.024'}

	Recorder: 5fbab44e5f444c1a81875cb3fa8a49ec

		Model: {'id': '5fbab44e5f444c1a81875cb3fa8a49ec', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.264, 'Rank IC': 0.028, 'Rank ICIR': 0.233}, 'data_train_vec': ['2024-05-06', '2025-11-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.233', 'recency_weight': '0.496', 'weight': '0.022'}

	Recorder: fd4ad2c588ec45cea6d37407006bebd7

		Model: {'id': 'fd4ad2c588ec45cea6d37407006bebd7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.532, 'Rank IC': 0.069, 'Rank ICIR': 0.717}, 'data_train_vec': ['2025-05-06', '2026-02-05'], 'train_time_vec': ['2026-05-06', '2026-05-06'], 'rank_icir': '0.717', 'recency_weight': '0.707', 'weight': '0.301'}
