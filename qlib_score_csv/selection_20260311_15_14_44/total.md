# params 
 {'predict_dates': [{'start': '2026-03-11', 'end': '2026-03-11'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.02}, {'icir': 0.25}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260311_12 259273911298020093 (Recorders: 1/5)

	Recorder: 5f26c3b035404ebcb748fed864d8e09c

		Model: {'id': '5f26c3b035404ebcb748fed864d8e09c', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.269, 'Rank IC': 0.029, 'Rank ICIR': 0.269}, 'data_train_vec': ['2024-03-11', '2025-09-10'], 'train_time_vec': ['2026-03-11', '2026-03-11']}
