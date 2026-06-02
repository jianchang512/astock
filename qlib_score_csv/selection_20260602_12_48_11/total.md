# params 
 {'predict_dates': [{'start': '2026-06-02', 'end': '2026-06-02'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'trade_buy_offset': 0, 'trade_sell_offset': 1, 'top_num_list': [3, 5, 10, 20], 'selection_score_quantile': 0.7, 'selection_min_pos_ratio': 0.5, 'selection_volatility_quantile': 0.6, 'selection_overheat_quantile': 0.7, 'selection_fallback_count': 10, 'selection_weight_score': 1.0, 'selection_weight_pos_ratio': 0.35, 'selection_weight_momentum': 0.2, 'selection_weight_volatility': 0.25, 'selection_weight_overheat': 0.15, 'recency_halflife_days': 180, 'backtest_fee_rate': 0.002, 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.01}, {'icir': 0.01}, {'rankic': 0.01}, {'rankicir': 0.01}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260602_11 282479692339755729 (Recorders: 6/6)

	Recorder: 9ff9c4efd747492c8faf9553ca1aae19

		Model: {'id': '9ff9c4efd747492c8faf9553ca1aae19', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.357, 'Rank IC': 0.06, 'Rank ICIR': 0.398}, 'data_train_vec': ['2020-06-02', '2024-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.398', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 36c57152a6f24015b2938a2eb4d9f7f5

		Model: {'id': '36c57152a6f24015b2938a2eb4d9f7f5', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.283, 'Rank IC': 0.067, 'Rank ICIR': 0.446}, 'data_train_vec': ['2021-06-02', '2025-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.446', 'recency_weight': '0.171', 'weight': '0.029'}

	Recorder: 941f05b19cb84f23a2e6ad438d7d31cd

		Model: {'id': '941f05b19cb84f23a2e6ad438d7d31cd', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.189, 'Rank IC': 0.063, 'Rank ICIR': 0.363}, 'data_train_vec': ['2022-06-02', '2025-06-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.363', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: 64856631ad2a4f859b8b38ea51997ca7

		Model: {'id': '64856631ad2a4f859b8b38ea51997ca7', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.256, 'Rank IC': 0.064, 'Rank ICIR': 0.377}, 'data_train_vec': ['2023-06-02', '2025-09-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.377', 'recency_weight': '0.348', 'weight': '0.042'}

	Recorder: 0a6cdd306be64b2d91c7c380372ae119

		Model: {'id': '0a6cdd306be64b2d91c7c380372ae119', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.041, 'ICIR': 0.313, 'Rank IC': 0.066, 'Rank ICIR': 0.448}, 'data_train_vec': ['2024-06-02', '2025-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.448', 'recency_weight': '0.494', 'weight': '0.084'}

	Recorder: 9445a0e6a6214dc88252e81bea0d7209

		Model: {'id': '9445a0e6a6214dc88252e81bea0d7209', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.1, 'ICIR': 0.599, 'Rank IC': 0.061, 'Rank ICIR': 0.337}, 'data_train_vec': ['2025-06-02', '2026-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.337', 'recency_weight': '0.699', 'weight': '0.068'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260602_11 560848395172580445 (Recorders: 6/6)

	Recorder: 6040bb2803fc4254979302b2a94c37c7

		Model: {'id': '6040bb2803fc4254979302b2a94c37c7', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.325, 'Rank IC': 0.058, 'Rank ICIR': 0.373}, 'data_train_vec': ['2020-06-02', '2024-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.373', 'recency_weight': '0.121', 'weight': '0.014'}

	Recorder: 8230aec3f0d54bc99d5ac416ed366928

		Model: {'id': '8230aec3f0d54bc99d5ac416ed366928', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.032, 'ICIR': 0.208, 'Rank IC': 0.058, 'Rank ICIR': 0.387}, 'data_train_vec': ['2021-06-02', '2025-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.387', 'recency_weight': '0.171', 'weight': '0.022'}

	Recorder: 7f91ab1697bb43e892a5e2ad31b935d4

		Model: {'id': '7f91ab1697bb43e892a5e2ad31b935d4', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.136, 'Rank IC': 0.063, 'Rank ICIR': 0.359}, 'data_train_vec': ['2022-06-02', '2025-06-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.359', 'recency_weight': '0.244', 'weight': '0.027'}

	Recorder: e0e6059583464b7db21fe20a987e879c

		Model: {'id': 'e0e6059583464b7db21fe20a987e879c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.037, 'ICIR': 0.22, 'Rank IC': 0.069, 'Rank ICIR': 0.401}, 'data_train_vec': ['2023-06-02', '2025-09-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.401', 'recency_weight': '0.348', 'weight': '0.048'}

	Recorder: 8c5d36765ad24f099ee287da09814d6b

		Model: {'id': '8c5d36765ad24f099ee287da09814d6b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.124, 'Rank IC': 0.053, 'Rank ICIR': 0.358}, 'data_train_vec': ['2024-06-02', '2025-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.358', 'recency_weight': '0.494', 'weight': '0.054'}

	Recorder: 445ecccb2dfc4dea82c23309b4184e9e

		Model: {'id': '445ecccb2dfc4dea82c23309b4184e9e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.32, 'Rank IC': 0.033, 'Rank ICIR': 0.197}, 'data_train_vec': ['2025-06-02', '2026-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.197', 'recency_weight': '0.699', 'weight': '0.023'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260602_11 584325813165304009 (Recorders: 6/6)

	Recorder: 864d7626d2824659aa7694aa314c7d99

		Model: {'id': '864d7626d2824659aa7694aa314c7d99', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.049, 'ICIR': 0.344, 'Rank IC': 0.065, 'Rank ICIR': 0.475}, 'data_train_vec': ['2020-06-02', '2024-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.475', 'recency_weight': '0.121', 'weight': '0.023'}

	Recorder: 5a313b0e2dbe4b249805713829cef110

		Model: {'id': '5a313b0e2dbe4b249805713829cef110', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.038, 'ICIR': 0.251, 'Rank IC': 0.067, 'Rank ICIR': 0.487}, 'data_train_vec': ['2021-06-02', '2025-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.487', 'recency_weight': '0.171', 'weight': '0.035'}

	Recorder: 1fb36f9a9dbc44689372ddf8fcf1264f

		Model: {'id': '1fb36f9a9dbc44689372ddf8fcf1264f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.144, 'Rank IC': 0.063, 'Rank ICIR': 0.417}, 'data_train_vec': ['2022-06-02', '2025-06-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.417', 'recency_weight': '0.244', 'weight': '0.036'}

	Recorder: 020baebf216e424fa2054b2a794e48c8

		Model: {'id': '020baebf216e424fa2054b2a794e48c8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.102, 'Rank IC': 0.047, 'Rank ICIR': 0.326}, 'data_train_vec': ['2023-06-02', '2025-09-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.326', 'recency_weight': '0.348', 'weight': '0.031'}

	Recorder: 1f51b51d86a6433aa1fcd58d61218651

		Model: {'id': '1f51b51d86a6433aa1fcd58d61218651', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.166, 'Rank IC': 0.048, 'Rank ICIR': 0.376}, 'data_train_vec': ['2024-06-02', '2025-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.376', 'recency_weight': '0.494', 'weight': '0.059'}

	Recorder: 863f51cb1fe14e39bd268a00c9cb3e57

		Model: {'id': '863f51cb1fe14e39bd268a00c9cb3e57', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.078, 'ICIR': 0.385, 'Rank IC': 0.068, 'Rank ICIR': 0.321}, 'data_train_vec': ['2025-06-02', '2026-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.321', 'recency_weight': '0.699', 'weight': '0.061'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260602_11 190316733712612944 (Recorders: 6/6)

	Recorder: e643928727c04d16bfb58fb7c2fbe55c

		Model: {'id': 'e643928727c04d16bfb58fb7c2fbe55c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.335, 'Rank IC': 0.057, 'Rank ICIR': 0.399}, 'data_train_vec': ['2020-06-02', '2024-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.399', 'recency_weight': '0.121', 'weight': '0.016'}

	Recorder: 9e3107bd6658447d87c6e26d37c5aeaa

		Model: {'id': '9e3107bd6658447d87c6e26d37c5aeaa', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.035, 'ICIR': 0.228, 'Rank IC': 0.061, 'Rank ICIR': 0.431}, 'data_train_vec': ['2021-06-02', '2025-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.431', 'recency_weight': '0.171', 'weight': '0.027'}

	Recorder: 8b728e6e5cfc41f7948ec9f4f6495763

		Model: {'id': '8b728e6e5cfc41f7948ec9f4f6495763', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.241, 'Rank IC': 0.071, 'Rank ICIR': 0.434}, 'data_train_vec': ['2022-06-02', '2025-06-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.434', 'recency_weight': '0.244', 'weight': '0.039'}

	Recorder: 67c97a359e0b496294cc903be5048f91

		Model: {'id': '67c97a359e0b496294cc903be5048f91', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.039, 'ICIR': 0.275, 'Rank IC': 0.064, 'Rank ICIR': 0.414}, 'data_train_vec': ['2023-06-02', '2025-09-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.414', 'recency_weight': '0.348', 'weight': '0.051'}

	Recorder: 6f490847059c4703a7997e63ad175d07

		Model: {'id': '6f490847059c4703a7997e63ad175d07', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.344, 'Rank IC': 0.063, 'Rank ICIR': 0.474}, 'data_train_vec': ['2024-06-02', '2025-12-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.474', 'recency_weight': '0.494', 'weight': '0.094'}

	Recorder: d83f818713764641b275a7c6392052d3

		Model: {'id': 'd83f818713764641b275a7c6392052d3', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.091, 'ICIR': 0.641, 'Rank IC': 0.058, 'Rank ICIR': 0.347}, 'data_train_vec': ['2025-06-02', '2026-03-01'], 'train_time_vec': ['2026-06-02', '2026-06-02'], 'rank_icir': '0.347', 'recency_weight': '0.699', 'weight': '0.072'}
