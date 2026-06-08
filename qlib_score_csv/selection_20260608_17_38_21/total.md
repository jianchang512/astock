# params 
 {'predict_dates': [{'start': '2026-06-08', 'end': '2026-06-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260608_16 351024495401231145 (Recorders: 6/6)

	Recorder: 7fe62ecf8ce84b6f8495a5e9c60a21b7

		Model: {'id': '7fe62ecf8ce84b6f8495a5e9c60a21b7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.05, 'ICIR': 0.336, 'Rank IC': 0.059, 'Rank ICIR': 0.38}, 'data_train_vec': ['2020-06-08', '2024-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.380', 'recency_weight': '0.121', 'weight': '0.020'}

	Recorder: 806dc4a98b354eca9795f88c0e756a94

		Model: {'id': '806dc4a98b354eca9795f88c0e756a94', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.268, 'Rank IC': 0.066, 'Rank ICIR': 0.437}, 'data_train_vec': ['2021-06-08', '2025-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.437', 'recency_weight': '0.171', 'weight': '0.038'}

	Recorder: b17738b06aae46b2ac5f45559c9ebe83

		Model: {'id': 'b17738b06aae46b2ac5f45559c9ebe83', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.27, 'Rank IC': 0.072, 'Rank ICIR': 0.43}, 'data_train_vec': ['2022-06-08', '2025-06-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.430', 'recency_weight': '0.244', 'weight': '0.052'}

	Recorder: 69d7863b2cb943dbb1e88f756c89684f

		Model: {'id': '69d7863b2cb943dbb1e88f756c89684f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.219, 'Rank IC': 0.062, 'Rank ICIR': 0.329}, 'data_train_vec': ['2023-06-08', '2025-09-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.329', 'recency_weight': '0.348', 'weight': '0.043'}

	Recorder: e84fae11e1c24436af769306a0dc6ffa

		Model: {'id': 'e84fae11e1c24436af769306a0dc6ffa', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.23, 'Rank IC': 0.053, 'Rank ICIR': 0.382}, 'data_train_vec': ['2024-06-08', '2025-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.382', 'recency_weight': '0.494', 'weight': '0.083'}

	Recorder: 0464ed231dcc49aaad72205c3ad1560c

		Model: {'id': '0464ed231dcc49aaad72205c3ad1560c', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.058, 'ICIR': 0.342, 'Rank IC': 0.023, 'Rank ICIR': 0.123}, 'data_train_vec': ['2025-06-08', '2026-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.123', 'recency_weight': '0.699', 'weight': '0.012'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260608_16 834637653436924694 (Recorders: 6/6)

	Recorder: fa30a5699a704623b1daa2383bad9585

		Model: {'id': 'fa30a5699a704623b1daa2383bad9585', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.323, 'Rank IC': 0.06, 'Rank ICIR': 0.385}, 'data_train_vec': ['2020-06-08', '2024-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.385', 'recency_weight': '0.121', 'weight': '0.021'}

	Recorder: d663ac716fe443dd93fa37778aff446e

		Model: {'id': 'd663ac716fe443dd93fa37778aff446e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.224, 'Rank IC': 0.059, 'Rank ICIR': 0.399}, 'data_train_vec': ['2021-06-08', '2025-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.399', 'recency_weight': '0.171', 'weight': '0.031'}

	Recorder: bd605cafd2914f92af6893b3ae37c87f

		Model: {'id': 'bd605cafd2914f92af6893b3ae37c87f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.154, 'Rank IC': 0.065, 'Rank ICIR': 0.382}, 'data_train_vec': ['2022-06-08', '2025-06-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.382', 'recency_weight': '0.244', 'weight': '0.041'}

	Recorder: 75a004efef6742808b9ad924837101b2

		Model: {'id': '75a004efef6742808b9ad924837101b2', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.196, 'Rank IC': 0.067, 'Rank ICIR': 0.373}, 'data_train_vec': ['2023-06-08', '2025-09-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.373', 'recency_weight': '0.348', 'weight': '0.056'}

	Recorder: 7e9406a636054352a94d1d8dc0ecea21

		Model: {'id': '7e9406a636054352a94d1d8dc0ecea21', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.12, 'Rank IC': 0.047, 'Rank ICIR': 0.357}, 'data_train_vec': ['2024-06-08', '2025-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.357', 'recency_weight': '0.494', 'weight': '0.072'}

	Recorder: 2236babee9a74be78e808dfa5b0f6874

		Model: {'id': '2236babee9a74be78e808dfa5b0f6874', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.192, 'Rank IC': 0.014, 'Rank ICIR': 0.082}, 'data_train_vec': ['2025-06-08', '2026-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.082', 'recency_weight': '0.699', 'weight': '0.005'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260608_16 543924280042184083 (Recorders: 6/6)

	Recorder: a2fc9589bc094ff99ca12ee436c993cf

		Model: {'id': 'a2fc9589bc094ff99ca12ee436c993cf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.327, 'Rank IC': 0.065, 'Rank ICIR': 0.472}, 'data_train_vec': ['2020-06-08', '2024-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.472', 'recency_weight': '0.121', 'weight': '0.031'}

	Recorder: b5405e332a0946f894b849b7e54a79a2

		Model: {'id': 'b5405e332a0946f894b849b7e54a79a2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.24, 'Rank IC': 0.065, 'Rank ICIR': 0.471}, 'data_train_vec': ['2021-06-08', '2025-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.471', 'recency_weight': '0.171', 'weight': '0.044'}

	Recorder: a7d98537e8f346b79af33f5d0f100050

		Model: {'id': 'a7d98537e8f346b79af33f5d0f100050', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.121, 'Rank IC': 0.059, 'Rank ICIR': 0.397}, 'data_train_vec': ['2022-06-08', '2025-06-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.397', 'recency_weight': '0.244', 'weight': '0.044'}

	Recorder: de4c759dc9104d6096aede6495523d73

		Model: {'id': 'de4c759dc9104d6096aede6495523d73', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.08, 'Rank IC': 0.043, 'Rank ICIR': 0.293}, 'data_train_vec': ['2023-06-08', '2025-09-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.293', 'recency_weight': '0.348', 'weight': '0.034'}

	Recorder: f2c247bc9fcf40d791619539ed4f64cf

		Model: {'id': 'f2c247bc9fcf40d791619539ed4f64cf', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.146, 'Rank IC': 0.042, 'Rank ICIR': 0.324}, 'data_train_vec': ['2024-06-08', '2025-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.324', 'recency_weight': '0.494', 'weight': '0.060'}

	Recorder: f7b7d6e75ab845c0b140152e15855052

		Model: {'id': 'f7b7d6e75ab845c0b140152e15855052', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.201, 'Rank IC': 0.039, 'Rank ICIR': 0.191}, 'data_train_vec': ['2025-06-08', '2026-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.191', 'recency_weight': '0.699', 'weight': '0.029'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260608_16 896623942275769750 (Recorders: 6/6)

	Recorder: b4a014665c67484ea260f44553715a35

		Model: {'id': 'b4a014665c67484ea260f44553715a35', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.337, 'Rank IC': 0.061, 'Rank ICIR': 0.424}, 'data_train_vec': ['2020-06-08', '2024-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.424', 'recency_weight': '0.121', 'weight': '0.025'}

	Recorder: e3914a1ff30d4131a584a9b5288f185d

		Model: {'id': 'e3914a1ff30d4131a584a9b5288f185d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.28, 'Rank IC': 0.067, 'Rank ICIR': 0.481}, 'data_train_vec': ['2021-06-08', '2025-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.481', 'recency_weight': '0.171', 'weight': '0.046'}

	Recorder: 7bbc4194975c4192a2dfd0184b654d61

		Model: {'id': '7bbc4194975c4192a2dfd0184b654d61', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.026, 'ICIR': 0.166, 'Rank IC': 0.069, 'Rank ICIR': 0.419}, 'data_train_vec': ['2022-06-08', '2025-06-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.419', 'recency_weight': '0.244', 'weight': '0.049'}

	Recorder: d2b9743d55954abbb05d537b262acd35

		Model: {'id': 'd2b9743d55954abbb05d537b262acd35', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.274, 'Rank IC': 0.064, 'Rank ICIR': 0.378}, 'data_train_vec': ['2023-06-08', '2025-09-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.378', 'recency_weight': '0.348', 'weight': '0.057'}

	Recorder: 132317ad97174541aecfaa64c2dcf41c

		Model: {'id': '132317ad97174541aecfaa64c2dcf41c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.028, 'ICIR': 0.214, 'Rank IC': 0.047, 'Rank ICIR': 0.393}, 'data_train_vec': ['2024-06-08', '2025-12-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.393', 'recency_weight': '0.494', 'weight': '0.088'}

	Recorder: ab367c49b917424cbf9f38480371643b

		Model: {'id': 'ab367c49b917424cbf9f38480371643b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.367, 'Rank IC': 0.023, 'Rank ICIR': 0.148}, 'data_train_vec': ['2025-06-08', '2026-03-07'], 'train_time_vec': ['2026-06-08', '2026-06-08'], 'rank_icir': '0.148', 'recency_weight': '0.699', 'weight': '0.018'}
