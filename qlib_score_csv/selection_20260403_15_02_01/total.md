# params 
 {'predict_dates': [{'start': '2026-04-03', 'end': '2026-04-03'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260403_14 327583977472429674 (Recorders: 3/5)

	Recorder: e108908cd0bf49d0a2133720f5cde9a4

		Model: {'id': 'e108908cd0bf49d0a2133720f5cde9a4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.077, 'Rank IC': 0.027, 'Rank ICIR': 0.153}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.153', 'weight': '0.044'}

	Recorder: bf7458ca8b6547f2bce6ff0a5b47f285

		Model: {'id': 'bf7458ca8b6547f2bce6ff0a5b47f285', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.204, 'Rank IC': 0.048, 'Rank ICIR': 0.324}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.324', 'weight': '0.093'}

	Recorder: 1b965a94d9ea4fdfbc52b726c3c7e7f8

		Model: {'id': '1b965a94d9ea4fdfbc52b726c3c7e7f8', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.13, 'Rank IC': 0.047, 'Rank ICIR': 0.392}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.392', 'weight': '0.112'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260403_14 697452918707808780 (Recorders: 3/5)

	Recorder: a3be86db6f824e0ea43de45eebb11eea

		Model: {'id': 'a3be86db6f824e0ea43de45eebb11eea', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.027, 'Rank IC': 0.029, 'Rank ICIR': 0.178}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.178', 'weight': '0.051'}

	Recorder: c5fca3846d9348ddbddf21336b1a5128

		Model: {'id': 'c5fca3846d9348ddbddf21336b1a5128', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.063, 'Rank IC': 0.052, 'Rank ICIR': 0.305}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.305', 'weight': '0.087'}

	Recorder: 2c65e34c8b714bdaaf3bfcde1a393dd1

		Model: {'id': '2c65e34c8b714bdaaf3bfcde1a393dd1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.181, 'Rank IC': 0.027, 'Rank ICIR': 0.234}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.234', 'weight': '0.067'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260403_12 389083208813082702 (Recorders: 4/5)

	Recorder: 2c0531aa26a6445bb15191c76cd3114e

		Model: {'id': '2c0531aa26a6445bb15191c76cd3114e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.098, 'Rank IC': 0.039, 'Rank ICIR': 0.217}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.217', 'weight': '0.062'}

	Recorder: 98b8f5a442ec4a0d8528382c8eec5a40

		Model: {'id': '98b8f5a442ec4a0d8528382c8eec5a40', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.009, 'Rank IC': 0.028, 'Rank ICIR': 0.158}, 'data_train_vec': ['2022-04-03', '2025-04-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.158', 'weight': '0.045'}

	Recorder: 1ebedde834ae47c29cbc3e2e5df30e91

		Model: {'id': '1ebedde834ae47c29cbc3e2e5df30e91', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.103, 'Rank IC': 0.053, 'Rank ICIR': 0.316}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.316', 'weight': '0.091'}

	Recorder: 036fc8b5b086486dbce3449a0213135b

		Model: {'id': '036fc8b5b086486dbce3449a0213135b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.255, 'Rank IC': 0.034, 'Rank ICIR': 0.331}, 'data_train_vec': ['2024-04-03', '2025-10-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.331', 'weight': '0.095'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260403_11 130636781357421843 (Recorders: 3/5)

	Recorder: f9a2a37f65564b7e95354e100c280362

		Model: {'id': 'f9a2a37f65564b7e95354e100c280362', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.106, 'Rank IC': 0.024, 'Rank ICIR': 0.199}, 'data_train_vec': ['2021-04-03', '2025-01-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.199', 'weight': '0.057'}

	Recorder: 89f8c9557503458a9ac6e4fd744bed35

		Model: {'id': '89f8c9557503458a9ac6e4fd744bed35', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.028, 'Rank IC': 0.021, 'Rank ICIR': 0.177}, 'data_train_vec': ['2022-04-03', '2025-04-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.177', 'weight': '0.051'}

	Recorder: 4738288a255b471b879171d63a6ae878

		Model: {'id': '4738288a255b471b879171d63a6ae878', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.097, 'Rank IC': 0.039, 'Rank ICIR': 0.33}, 'data_train_vec': ['2023-04-03', '2025-07-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.330', 'weight': '0.095'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260403_11 140227513901982417 (Recorders: 1/5)

	Recorder: 6a0fc5ab94754b49a5798c5afccc0a40

		Model: {'id': '6a0fc5ab94754b49a5798c5afccc0a40', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.031, 'Rank ICIR': 0.175}, 'data_train_vec': ['2022-04-03', '2025-04-02'], 'train_time_vec': ['2026-04-03', '2026-04-03'], 'rank_icir': '0.175', 'weight': '0.050'}
