# params 
 {'predict_dates': [{'start': '2026-03-16', 'end': '2026-03-16'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260316_11 404601162640043939 (Recorders: 1/5)

	Recorder: 12f1351121a3481f908663fb103095af

		Model: {'id': '12f1351121a3481f908663fb103095af', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.311, 'Rank IC': 0.067, 'Rank ICIR': 0.627}, 'data_train_vec': ['2025-03-16', '2025-12-15'], 'train_time_vec': ['2026-03-16', '2026-03-16']}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260316_11 409741987687039248 (Recorders: 1/5)

	Recorder: 8236e62f26a34dd3a1d76fd7efb48be5

		Model: {'id': '8236e62f26a34dd3a1d76fd7efb48be5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.024, 'ICIR': 0.255, 'Rank IC': 0.044, 'Rank ICIR': 0.473}, 'data_train_vec': ['2025-03-16', '2025-12-15'], 'train_time_vec': ['2026-03-16', '2026-03-16']}
