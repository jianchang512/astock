# params 
 {'predict_dates': [{'start': '2026-03-31', 'end': '2026-03-31'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260331_15 982147968703799356 (Recorders: 3/5)

	Recorder: 97f498af5ef94283a9211b35a9f27311

		Model: {'id': '97f498af5ef94283a9211b35a9f27311', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.105, 'Rank IC': 0.026, 'Rank ICIR': 0.173}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.173', 'weight': '0.042'}

	Recorder: de23838eea624fa889c4ad6c1254e167

		Model: {'id': 'de23838eea624fa889c4ad6c1254e167', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.08, 'Rank IC': 0.048, 'Rank ICIR': 0.29}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.290', 'weight': '0.070'}

	Recorder: f615a5fc4bef4751b51eb90df86cc309

		Model: {'id': 'f615a5fc4bef4751b51eb90df86cc309', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.056, 'Rank IC': 0.053, 'Rank ICIR': 0.378}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.378', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260331_15 646750275206500185 (Recorders: 3/5)

	Recorder: c0c127803e984a5eb132cffb3ae46ae0

		Model: {'id': 'c0c127803e984a5eb132cffb3ae46ae0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.011, 'Rank IC': 0.022, 'Rank ICIR': 0.141}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.141', 'weight': '0.034'}

	Recorder: a437bff9e25c4a158fc1c78743567c9c

		Model: {'id': 'a437bff9e25c4a158fc1c78743567c9c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.062, 'Rank IC': 0.043, 'Rank ICIR': 0.27}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.270', 'weight': '0.065'}

	Recorder: 023acae847f745878b0907ee30233cf7

		Model: {'id': '023acae847f745878b0907ee30233cf7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.303, 'Rank IC': 0.051, 'Rank ICIR': 0.383}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.383', 'weight': '0.093'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260331_12 318267037046470197 (Recorders: 5/5)

	Recorder: 4f927f08a55a465982369f6af33522fc

		Model: {'id': '4f927f08a55a465982369f6af33522fc', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.102, 'Rank IC': 0.038, 'Rank ICIR': 0.212}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.212', 'weight': '0.051'}

	Recorder: 38b152b935e841e98e31fc30ec4a1e65

		Model: {'id': '38b152b935e841e98e31fc30ec4a1e65', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.018, 'Rank IC': 0.029, 'Rank ICIR': 0.159}, 'data_train_vec': ['2022-03-30', '2025-03-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.159', 'weight': '0.039'}

	Recorder: b18485f0974e45b1878e9e4426b1bbb6

		Model: {'id': 'b18485f0974e45b1878e9e4426b1bbb6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.079, 'Rank IC': 0.048, 'Rank ICIR': 0.285}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.285', 'weight': '0.069'}

	Recorder: 524d9ce12ced41438bfbc09cf077949e

		Model: {'id': '524d9ce12ced41438bfbc09cf077949e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.354, 'Rank IC': 0.043, 'Rank ICIR': 0.401}, 'data_train_vec': ['2024-03-30', '2025-09-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.401', 'weight': '0.097'}

	Recorder: 78c04ac275cd4a2799ddb11d8df5c4d2

		Model: {'id': '78c04ac275cd4a2799ddb11d8df5c4d2', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.01, 'Rank ICIR': 0.093}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.093', 'weight': '0.023'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260331_12 588728779438643895 (Recorders: 4/5)

	Recorder: d8f8d47aebaf436287e39686c472cf58

		Model: {'id': 'd8f8d47aebaf436287e39686c472cf58', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.143, 'Rank IC': 0.027, 'Rank ICIR': 0.229}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.229', 'weight': '0.056'}

	Recorder: 6d6ba50b05374c7a93f58ab740e285de

		Model: {'id': '6d6ba50b05374c7a93f58ab740e285de', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.037, 'Rank IC': 0.021, 'Rank ICIR': 0.184}, 'data_train_vec': ['2022-03-30', '2025-03-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.184', 'weight': '0.045'}

	Recorder: d0ef8a173f99479894cc40dfe1e40d78

		Model: {'id': 'd0ef8a173f99479894cc40dfe1e40d78', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.156, 'Rank IC': 0.042, 'Rank ICIR': 0.388}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.388', 'weight': '0.094'}

	Recorder: 06480fe405144fc9b4689cafb5470ac4

		Model: {'id': '06480fe405144fc9b4689cafb5470ac4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.043, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2025-03-28', '2025-12-27'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.072', 'weight': '0.017'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260331_12 542202873448039495 (Recorders: 2/5)

	Recorder: 76e49ecd435f47a8827eaa81f06f9cab

		Model: {'id': '76e49ecd435f47a8827eaa81f06f9cab', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.077, 'Rank IC': 0.038, 'Rank ICIR': 0.205}, 'data_train_vec': ['2021-03-31', '2024-12-30'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.205', 'weight': '0.050'}

	Recorder: 565c05ddf39b4fc78808f52495f5b84b

		Model: {'id': '565c05ddf39b4fc78808f52495f5b84b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.077, 'Rank IC': 0.043, 'Rank ICIR': 0.263}, 'data_train_vec': ['2023-03-30', '2025-06-29'], 'train_time_vec': ['2026-03-31', '2026-03-31'], 'rank_icir': '0.263', 'weight': '0.064'}
