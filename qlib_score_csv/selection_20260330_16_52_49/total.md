# params 
 {'predict_dates': [{'start': '2026-03-30', 'end': '2026-03-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260330_16 920777266162741081 (Recorders: 3/5)

	Recorder: 520f301866a5494098fe2e4081dc2c79

		Model: {'id': '520f301866a5494098fe2e4081dc2c79', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.144, 'Rank IC': 0.044, 'Rank ICIR': 0.295}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.295', 'weight': '0.068'}

	Recorder: 5086575f129948cb87f5653f8b30a2f9

		Model: {'id': '5086575f129948cb87f5653f8b30a2f9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.021, 'Rank IC': 0.04, 'Rank ICIR': 0.24}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.240', 'weight': '0.055'}

	Recorder: 4cd35c546f224d359c1971b40ee4a642

		Model: {'id': '4cd35c546f224d359c1971b40ee4a642', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.137, 'Rank IC': 0.055, 'Rank ICIR': 0.367}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.367', 'weight': '0.084'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260330_16 177947461041118294 (Recorders: 3/5)

	Recorder: 73a91953ed4b4f9882ad8e54cdc18632

		Model: {'id': '73a91953ed4b4f9882ad8e54cdc18632', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.026, 'Rank ICIR': 0.163}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.163', 'weight': '0.037'}

	Recorder: 283284bbe3ba4cf190f78a3b46b55d11

		Model: {'id': '283284bbe3ba4cf190f78a3b46b55d11', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.036, 'Rank ICIR': 0.221}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.221', 'weight': '0.051'}

	Recorder: e2bbc27b32ea4270a3c9bdb3b4e7f496

		Model: {'id': 'e2bbc27b32ea4270a3c9bdb3b4e7f496', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.312, 'Rank IC': 0.048, 'Rank ICIR': 0.366}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.366', 'weight': '0.084'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260330_13 905328889089700192 (Recorders: 4/5)

	Recorder: fed2f509cb2f44069be71f8881e6d975

		Model: {'id': 'fed2f509cb2f44069be71f8881e6d975', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.105, 'Rank IC': 0.036, 'Rank ICIR': 0.21}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.210', 'weight': '0.048'}

	Recorder: ee26d82a4dd34b9ba190141fd9cd96e7

		Model: {'id': 'ee26d82a4dd34b9ba190141fd9cd96e7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.042, 'Rank IC': 0.041, 'Rank ICIR': 0.24}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.240', 'weight': '0.055'}

	Recorder: f36f8500f67545cd9c24774a1cf6e477

		Model: {'id': 'f36f8500f67545cd9c24774a1cf6e477', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.356, 'Rank IC': 0.044, 'Rank ICIR': 0.393}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.393', 'weight': '0.090'}

	Recorder: affb6b13fdd844dd9132fe03051e1a74

		Model: {'id': 'affb6b13fdd844dd9132fe03051e1a74', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.082, 'Rank IC': 0.022, 'Rank ICIR': 0.221}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.221', 'weight': '0.051'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260330_13 593392651088476173 (Recorders: 5/5)

	Recorder: f0dca343bf0a4e3d9ded6185104cc0ae

		Model: {'id': 'f0dca343bf0a4e3d9ded6185104cc0ae', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.139, 'Rank IC': 0.027, 'Rank ICIR': 0.228}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.228', 'weight': '0.052'}

	Recorder: 9408df17d1f045b981d6b0ee8021dea7

		Model: {'id': '9408df17d1f045b981d6b0ee8021dea7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.024, 'Rank IC': 0.019, 'Rank ICIR': 0.168}, 'data_train_vec': ['2022-03-30', '2025-03-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.168', 'weight': '0.038'}

	Recorder: 5ba994e2a4ba4922ae09062a4ec2836a

		Model: {'id': '5ba994e2a4ba4922ae09062a4ec2836a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.118, 'Rank IC': 0.037, 'Rank ICIR': 0.334}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.334', 'weight': '0.076'}

	Recorder: 773588a575484b958549aee628df473e

		Model: {'id': '773588a575484b958549aee628df473e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.08, 'Rank IC': 0.012, 'Rank ICIR': 0.095}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.095', 'weight': '0.022'}

	Recorder: bf29a38ad21b4249a047709858e6d106

		Model: {'id': 'bf29a38ad21b4249a047709858e6d106', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.134, 'Rank IC': 0.022, 'Rank ICIR': 0.194}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.194', 'weight': '0.044'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260330_13 983034835873777960 (Recorders: 3/5)

	Recorder: 6105a3b139bf4b028145e5907af409ca

		Model: {'id': '6105a3b139bf4b028145e5907af409ca', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.063, 'Rank IC': 0.038, 'Rank ICIR': 0.216}, 'data_train_vec': ['2021-03-30', '2024-12-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.216', 'weight': '0.049'}

	Recorder: 9a4e6ffec422416bbcf85c7cb4d26543

		Model: {'id': '9a4e6ffec422416bbcf85c7cb4d26543', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.033, 'Rank ICIR': 0.199}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.199', 'weight': '0.046'}

	Recorder: e17b7ffb51784a49a1861d582ce62d64

		Model: {'id': 'e17b7ffb51784a49a1861d582ce62d64', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.071, 'Rank IC': 0.024, 'Rank ICIR': 0.22}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-30', '2026-03-30'], 'rank_icir': '0.220', 'weight': '0.050'}
