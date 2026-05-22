# params 
 {'predict_dates': [{'start': '2026-05-22', 'end': '2026-05-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260522_12 540361641213673027 (Recorders: 6/6)

	Recorder: 25ee33aed88c403dacf6791cc74d0c7c

		Model: {'id': '25ee33aed88c403dacf6791cc74d0c7c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.363, 'Rank IC': 0.057, 'Rank ICIR': 0.389}, 'data_train_vec': ['2020-05-22', '2024-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.389', 'recency_weight': '0.122', 'weight': '0.027'}

	Recorder: b34cf06b6b9e488ea999f67e413ec43f

		Model: {'id': 'b34cf06b6b9e488ea999f67e413ec43f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.217, 'Rank IC': 0.052, 'Rank ICIR': 0.36}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.360', 'recency_weight': '0.173', 'weight': '0.033'}

	Recorder: 80c2b3b8122341fdb795e663de969f0d

		Model: {'id': '80c2b3b8122341fdb795e663de969f0d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.215, 'Rank IC': 0.062, 'Rank ICIR': 0.394}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.394', 'recency_weight': '0.244', 'weight': '0.055'}

	Recorder: 7a4da7d97cc944c08f0f05e02712852c

		Model: {'id': '7a4da7d97cc944c08f0f05e02712852c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.205, 'Rank IC': 0.052, 'Rank ICIR': 0.329}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.329', 'recency_weight': '0.348', 'weight': '0.055'}

	Recorder: be2f956963f04677a6ccf7cca1b465c1

		Model: {'id': 'be2f956963f04677a6ccf7cca1b465c1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.131, 'Rank IC': 0.04, 'Rank ICIR': 0.293}, 'data_train_vec': ['2024-05-22', '2025-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.293', 'recency_weight': '0.496', 'weight': '0.062'}

	Recorder: 7f6f5b3f656f43abaf7b27d078e3b69e

		Model: {'id': '7f6f5b3f656f43abaf7b27d078e3b69e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.055, 'ICIR': 0.426, 'Rank IC': 0.036, 'Rank ICIR': 0.24}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.240', 'recency_weight': '0.707', 'weight': '0.059'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260522_12 475035820925907993 (Recorders: 5/6)

	Recorder: 32f16ccb4e414da1829276444bcf2ee2

		Model: {'id': '32f16ccb4e414da1829276444bcf2ee2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.328, 'Rank IC': 0.056, 'Rank ICIR': 0.376}, 'data_train_vec': ['2020-05-22', '2024-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.376', 'recency_weight': '0.122', 'weight': '0.025'}

	Recorder: 7dc80fba218540cf904ae8e6c16c8444

		Model: {'id': '7dc80fba218540cf904ae8e6c16c8444', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.185, 'Rank IC': 0.049, 'Rank ICIR': 0.347}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.347', 'recency_weight': '0.173', 'weight': '0.030'}

	Recorder: 67a9246469434db0bd0d83ffb2b61f4c

		Model: {'id': '67a9246469434db0bd0d83ffb2b61f4c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.146, 'Rank IC': 0.059, 'Rank ICIR': 0.352}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.352', 'recency_weight': '0.244', 'weight': '0.044'}

	Recorder: 50dde21e52ee4e67844e8c8fa0c18d33

		Model: {'id': '50dde21e52ee4e67844e8c8fa0c18d33', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.123, 'Rank IC': 0.051, 'Rank ICIR': 0.317}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.317', 'recency_weight': '0.348', 'weight': '0.051'}

	Recorder: ac386aa417ab4973900e36d42328e519

		Model: {'id': 'ac386aa417ab4973900e36d42328e519', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.396, 'Rank IC': 0.032, 'Rank ICIR': 0.26}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.260', 'recency_weight': '0.707', 'weight': '0.070'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260522_12 984995543408839521 (Recorders: 4/6)

	Recorder: aac50af20f3f4303b2e76c0e07b7d57d

		Model: {'id': 'aac50af20f3f4303b2e76c0e07b7d57d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.307, 'Rank IC': 0.059, 'Rank ICIR': 0.455}, 'data_train_vec': ['2020-05-22', '2024-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.455', 'recency_weight': '0.122', 'weight': '0.037'}

	Recorder: 110a8d0ea5c24dedb6dca4632a25e27a

		Model: {'id': '110a8d0ea5c24dedb6dca4632a25e27a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.24, 'Rank IC': 0.058, 'Rank ICIR': 0.446}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.446', 'recency_weight': '0.173', 'weight': '0.050'}

	Recorder: abdd54621eb247eb944db3e49b5567d7

		Model: {'id': 'abdd54621eb247eb944db3e49b5567d7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.135, 'Rank IC': 0.061, 'Rank ICIR': 0.394}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.394', 'recency_weight': '0.244', 'weight': '0.055'}

	Recorder: e854d22f34964531836f67bc7ffdc3e4

		Model: {'id': 'e854d22f34964531836f67bc7ffdc3e4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.385, 'Rank IC': 0.073, 'Rank ICIR': 0.375}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.375', 'recency_weight': '0.707', 'weight': '0.145'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260522_11 812293024796916357 (Recorders: 5/6)

	Recorder: 75059453c01547108cb507af030d93da

		Model: {'id': '75059453c01547108cb507af030d93da', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.342, 'Rank IC': 0.057, 'Rank ICIR': 0.396}, 'data_train_vec': ['2020-05-22', '2024-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.396', 'recency_weight': '0.122', 'weight': '0.028'}

	Recorder: 289717d961e549dbbfe7836c24189fee

		Model: {'id': '289717d961e549dbbfe7836c24189fee', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.155, 'Rank IC': 0.044, 'Rank ICIR': 0.342}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.342', 'recency_weight': '0.173', 'weight': '0.030'}

	Recorder: 50d561c6f7994ac4853940a80507e177

		Model: {'id': '50d561c6f7994ac4853940a80507e177', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.238, 'Rank IC': 0.06, 'Rank ICIR': 0.385}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.385', 'recency_weight': '0.244', 'weight': '0.053'}

	Recorder: da34c363a52e4092b394d10fb3fb3cbc

		Model: {'id': 'da34c363a52e4092b394d10fb3fb3cbc', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.145, 'Rank IC': 0.053, 'Rank ICIR': 0.335}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.335', 'recency_weight': '0.348', 'weight': '0.057'}

	Recorder: aea35148eb644972b9555e3520448b26

		Model: {'id': 'aea35148eb644972b9555e3520448b26', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.306, 'Rank IC': 0.028, 'Rank ICIR': 0.184}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.184', 'recency_weight': '0.707', 'weight': '0.035'}
