# params 
 {'predict_dates': [{'start': '2026-04-02', 'end': '2026-04-02'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260402_15 779201012741844217 (Recorders: 4/5)

	Recorder: 551c3c3915cf49c09dda006a5382df2a

		Model: {'id': '551c3c3915cf49c09dda006a5382df2a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.04, 'Rank IC': 0.033, 'Rank ICIR': 0.159}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.159', 'weight': '0.041'}

	Recorder: 7a60b3a2461a45d58902ef9b13fc48d7

		Model: {'id': '7a60b3a2461a45d58902ef9b13fc48d7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.278, 'Rank IC': 0.053, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.327', 'weight': '0.084'}

	Recorder: 4d03a7fe04be446086ae0b561a4ba01b

		Model: {'id': '4d03a7fe04be446086ae0b561a4ba01b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.039, 'Rank IC': 0.04, 'Rank ICIR': 0.317}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.317', 'weight': '0.082'}

	Recorder: 9b89a6995dbb41e9ad9df6a4860fb36b

		Model: {'id': '9b89a6995dbb41e9ad9df6a4860fb36b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.104, 'Rank IC': 0.002, 'Rank ICIR': 0.017}, 'data_train_vec': ['2025-04-02', '2026-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.017', 'weight': '0.004'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260402_14 562722801782886973 (Recorders: 3/5)

	Recorder: d72d6b7b898b4f42a4638a1923143ec2

		Model: {'id': 'd72d6b7b898b4f42a4638a1923143ec2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.024, 'Rank ICIR': 0.155}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.155', 'weight': '0.040'}

	Recorder: e60b03d41daa4517ad73a39c2999a25c

		Model: {'id': 'e60b03d41daa4517ad73a39c2999a25c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.037, 'Rank IC': 0.046, 'Rank ICIR': 0.267}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.267', 'weight': '0.069'}

	Recorder: 9c49eec25b4644fb81d37a2c78be8a33

		Model: {'id': '9c49eec25b4644fb81d37a2c78be8a33', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.022, 'ICIR': 0.246, 'Rank IC': 0.04, 'Rank ICIR': 0.353}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.353', 'weight': '0.091'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260402_12 885444128432207214 (Recorders: 4/5)

	Recorder: 20bd8d1e68e24ec4a6c0200f7b7608a2

		Model: {'id': '20bd8d1e68e24ec4a6c0200f7b7608a2', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.112, 'Rank IC': 0.039, 'Rank ICIR': 0.214}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.214', 'weight': '0.055'}

	Recorder: 314fdc80a4494337960a00be25e1c5fa

		Model: {'id': '314fdc80a4494337960a00be25e1c5fa', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.019, 'Rank IC': 0.029, 'Rank ICIR': 0.163}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.163', 'weight': '0.042'}

	Recorder: 40b87a4a6422411dbfe2c8d6c3c2f355

		Model: {'id': '40b87a4a6422411dbfe2c8d6c3c2f355', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.107, 'Rank IC': 0.052, 'Rank ICIR': 0.294}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.294', 'weight': '0.076'}

	Recorder: 4711d637027c4df3b683fdfec185ef8f

		Model: {'id': '4711d637027c4df3b683fdfec185ef8f', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.224, 'Rank IC': 0.034, 'Rank ICIR': 0.313}, 'data_train_vec': ['2024-04-02', '2025-10-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.313', 'weight': '0.081'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260402_12 450234002724280900 (Recorders: 3/5)

	Recorder: 7acedb476e904bc68bcd7722b08554cb

		Model: {'id': '7acedb476e904bc68bcd7722b08554cb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.107, 'Rank IC': 0.024, 'Rank ICIR': 0.193}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.193', 'weight': '0.050'}

	Recorder: 40bbf2adfbca448d862ce01dce42b86a

		Model: {'id': '40bbf2adfbca448d862ce01dce42b86a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.021, 'Rank ICIR': 0.178}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.178', 'weight': '0.046'}

	Recorder: 48f9eb01eeeb46449676a7e6fadcf8b5

		Model: {'id': '48f9eb01eeeb46449676a7e6fadcf8b5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.113, 'Rank IC': 0.039, 'Rank ICIR': 0.327}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.327', 'weight': '0.084'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260402_12 332736752876721727 (Recorders: 4/5)

	Recorder: 223a189ba37b4f88994c5e2de7ae7bb9

		Model: {'id': '223a189ba37b4f88994c5e2de7ae7bb9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.064, 'Rank IC': 0.03, 'Rank ICIR': 0.16}, 'data_train_vec': ['2021-04-02', '2025-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.160', 'weight': '0.041'}

	Recorder: c61daff865a94bc0bb10fddd74df1aae

		Model: {'id': 'c61daff865a94bc0bb10fddd74df1aae', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.018, 'Rank IC': 0.026, 'Rank ICIR': 0.15}, 'data_train_vec': ['2022-04-02', '2025-04-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.150', 'weight': '0.039'}

	Recorder: d7cf77eb4bec4b53ad3efebe4c924fb8

		Model: {'id': 'd7cf77eb4bec4b53ad3efebe4c924fb8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.043, 'Rank ICIR': 0.252}, 'data_train_vec': ['2023-04-02', '2025-07-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.252', 'weight': '0.065'}

	Recorder: 63d2193a01b9493f91942acaf7767e66

		Model: {'id': '63d2193a01b9493f91942acaf7767e66', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.07, 'Rank IC': 0.005, 'Rank ICIR': 0.044}, 'data_train_vec': ['2025-04-02', '2026-01-01'], 'train_time_vec': ['2026-04-02', '2026-04-02'], 'rank_icir': '0.044', 'weight': '0.011'}
