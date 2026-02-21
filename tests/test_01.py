import pytest
import pandas as pd
import numpy as np

# 假设这是你项目中的工具函数
def process_stock_code(code):
    return f"SH{code}" if code.startswith('6') else f"SZ{code}"

# 1. 测试简单的工具函数
def test_stock_code_conversion():
    assert process_stock_code("600000") == "SH600000"
    assert process_stock_code("000001") == "SZ000001"

# 2. 测试你最关心的聚合逻辑 (selection 模式)
def test_score_aggregation():
    # 准备模拟数据：两只股票，每只由两个模型评分
    data = {
        'instrument': ['SH600', 'SH600', 'SZ001', 'SZ001'],
        'score': [0.1, 0.3, -0.2, 0.4] # SH600平均0.2, 正向100%；SZ001平均0.1, 正向50%
    }
    df = pd.DataFrame(data)

    # 执行聚合
    ret_df = df.groupby('instrument')['score'].agg(
        avg_score='mean',
        pos_ratio=lambda x: (x > 0).mean()
    ).reset_index()

    # 断言结果是否符合预期
    sh600 = ret_df[ret_df['instrument'] == 'SH600'].iloc[0]
    assert sh600['avg_score'] == pytest.approx(0.2)
    assert sh600['pos_ratio'] == 1.0

# 3. 测试合并校验 (防止数据爆炸)
def test_merge_validation():
    # 模拟结果表
    ret_df = pd.DataFrame({'instrument': ['SH600'], 'avg_score': [0.2]})
    # 模拟错误的标签表（某股票出现了两条重复标签）
    labels = pd.DataFrame({
        'instrument': ['SH600', 'SH600'],
        'real_label': [0.05, 0.05]
    })

    # 验证当你使用 validate='one_to_one' 时，pytest 应该捕获到异常
    with pytest.raises(pd.errors.MergeError):
        pd.merge(ret_df, labels, on='instrument', how='left', validate='one_to_one')
