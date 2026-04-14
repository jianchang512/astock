# params 
 {'predict_dates': [{'start': '2026-03-10', 'end': '2026-03-10'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.03}, {'icir': 0.3}, {'rankic': 0.02}, {'rankicir': 0.2}]}



 # model info 

Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260310_15 779775855199630550 (Recorders: 1/5)

	Recorder: 92df2fcc690a45b78449f3753112e83d

		Model: {'id': '92df2fcc690a45b78449f3753112e83d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.31, 'Rank IC': 0.056, 'Rank ICIR': 0.431}, 'data_train_vec': ['2025-03-10', '2025-12-09'], 'train_time_vec': ['2026-03-10', '2026-03-10']}
