# params 
 {'predict_dates': [{'start': '2026-03-04', 'end': '2026-03-04'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha360', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'stock_list': ['SH601699', 'SH601318'], 'model_filter': ['Alpha158.*csi300.*(sliding|expanding)'], 'rec_filter': None}



 # model info 

Experiment: EXP_LGBModel_Alpha158_csi300_expanding_step40_s_20260121_01 611339367194711669 (Recorders: 1/1)

	Recorder: 0d5b2c317ad04013b1cb76da95b478fc

		Model: {'id': '0d5b2c317ad04013b1cb76da95b478fc', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.093, 'ICIR': 0.841, 'Rank IC': 0.082, 'Rank ICIR': 0.823}, 'data_train_vec': ['2015-01-05', '2017-08-28'], 'train_time_vec': ['2026-01-20', '2026-01-20']}
Experiment: EXP_LGBModel_Alpha158_csi300_sliding_step40_s_20260121_01 757025753236486275 (Recorders: 1/1)

	Recorder: 741bdd0f113c4c1eaf23c429f63dfa1d

		Model: {'id': '741bdd0f113c4c1eaf23c429f63dfa1d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.687, 'Rank IC': 0.093, 'Rank ICIR': 0.764}, 'data_train_vec': ['2015-03-09', '2017-03-06'], 'train_time_vec': ['2026-01-20', '2026-01-20']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_expanding_step40_s_20260112_22 794416563899598277 (Recorders: 1/1)

	Recorder: 5dfe27da14f64e55b157c5d6f03705b8

		Model: {'id': '5dfe27da14f64e55b157c5d6f03705b8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.105, 'ICIR': 0.894, 'Rank IC': 0.084, 'Rank ICIR': 0.69}, 'data_train_vec': ['2015-01-05', '2017-10-30'], 'train_time_vec': ['2026-01-12', '2026-01-12']}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_sliding_step40_s_20260111_23 138765183226751267 (Recorders: 1/1)

	Recorder: 12f4cb9e2e654b22a3588e4374ed56b1

		Model: {'id': '12f4cb9e2e654b22a3588e4374ed56b1', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.087, 'ICIR': 0.762, 'Rank IC': 0.065, 'Rank ICIR': 0.823}, 'data_train_vec': ['2015-01-05', '2016-12-30'], 'train_time_vec': ['2026-01-11', '2026-01-11']}
Experiment: EXP_LinearModel_Alpha158_csi300_expanding_step40_s_20260111_12 257540138222805258 (Recorders: 1/1)

	Recorder: ab464936a4bd47ddb5b42e4aa3319072

		Model: {'id': 'ab464936a4bd47ddb5b42e4aa3319072', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.599, 'Rank IC': 0.084, 'Rank ICIR': 0.62}, 'data_train_vec': ['2015-01-05', '2020-10-16'], 'train_time_vec': ['2026-01-11', '2026-01-11']}
Experiment: EXP_LinearModel_Alpha158_csi300_sliding_step40_s_20260111_11 840314380328755388 (Recorders: 1/1)

	Recorder: 91c306e388e8433fbae734de03637583

		Model: {'id': '91c306e388e8433fbae734de03637583', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.542, 'Rank IC': 0.068, 'Rank ICIR': 0.467}, 'data_train_vec': ['2015-08-27', '2017-08-28'], 'train_time_vec': ['2026-01-11', '2026-01-11']}
Experiment: EXP_XGBModel_Alpha158_csi300_sliding_step40_s_20260111_01 947052225543624310 (Recorders: 1/1)

	Recorder: 44df6c59b159490fa0b22d3c198cd0a9

		Model: {'id': '44df6c59b159490fa0b22d3c198cd0a9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.101, 'ICIR': 1.221, 'Rank IC': 0.072, 'Rank ICIR': 0.733}, 'data_train_vec': ['2015-11-02', '2017-10-30'], 'train_time_vec': ['2026-01-10', '2026-01-10']}
Experiment: EXP_XGBModel_Alpha158_csi300_expanding_step40_s_20260111_00 887979660755679496 (Recorders: 1/1)

	Recorder: 2f2d4eb181db4668bdbd3b6e264ca822

		Model: {'id': '2f2d4eb181db4668bdbd3b6e264ca822', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.118, 'ICIR': 1.272, 'Rank IC': 0.073, 'Rank ICIR': 0.627}, 'data_train_vec': ['2015-01-05', '2017-10-30'], 'train_time_vec': ['2026-01-10', '2026-01-10']}
