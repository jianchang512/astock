#!/usr/bin/env python3
"""
扫描 qlib_score_csv 子目录，生成 VitePress 静态页面。
所有 CSV 转为 Markdown 表格，MD 文件直接引用。
"""
import csv
import json
import os
import re
import shutil
from pathlib import Path
import pandas as pd
# 路径配置：page/script/gen_page.py -> 项目根目录
PAGE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = PAGE_ROOT.parent
DATA_DIR = PROJECT_ROOT / 'qlib_score_csv'
DOCS_DIR = PAGE_ROOT / 'docs'
BACKTEST_DIR = PROJECT_ROOT / 'backtest_csv'

def csv_to_markdown_table2(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return ''
    lines = []
    # 表头

    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    for row in rows[1:]:
        # 补齐列数
        while len(row) < len(rows[0]):
            row.append('')
        row = row[:len(rows[0])]
        lines.append('| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |')
    return '\n'.join(lines)




def generate_echarts_script(csv_path: str | Path) -> str:
    """
    读取回测结果 CSV 文件，生成 ECharts 变化趋势图的 HTML/JS 代码段。
    
    :param csv_path: CSV 文件的绝对路径
    :return: 包含 CDN 引用、DOM 容器以及渲染逻辑的完整字符串
    """
    file_path = Path(csv_path)
    if not file_path.exists():
        return f"<!-- 错误: 找不到文件 {file_path} -->"

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return f"<!-- 读取 CSV 失败: {e} -->"

    # 确定列名 (兼容可能的列名变体)
    date_col = "交易日期"
    profit_col = "累计净利润"
    return_col = "收益率%" if "收益率%" in df.columns else "收益率"

    # 校验必要列是否存在
    missing_cols = [col for col in[date_col, profit_col, return_col] if col not in df.columns]
    if missing_cols:
        return f"<!-- 数据列缺失: {', '.join(missing_cols)} -->"

    # 过滤空值，提取数据转为列表
    df = df.dropna(subset=[date_col, return_col, profit_col])
    
    dates = df[date_col].tolist()
    returns = df[return_col].tolist()
    profits = df[profit_col].tolist()

    # 将 Python 列表转为 JSON 字符串，以便直接注入到 JavaScript 中
    dates_js = json.dumps(dates)
    returns_js = json.dumps(returns)
    profits_js = json.dumps(profits)

    # 构造 HTML 和 JS 脚本段
    # 注意：严格使用您指定的 ECharts 6.0.0 CDN
    html_template = f"""
<!-- 引入 ECharts -->
<script src="https://cdn.jsdelivr.net/npm/echarts@6.0.0/dist/echarts.min.js"></script>

<!-- 图表容器 -->
<div id="chart-return" style="width: 100%; height: 400px; margin-bottom: 40px;"></div>
<div id="chart-profit" style="width: 100%; height: 400px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {{
    // === 图表1：收益率变化趋势 ===
    var chartReturn = echarts.init(document.getElementById('chart-return'));
    var optionReturn = {{
        title: {{
            text: '日收益率变化趋势',
            left: 'center'
        }},
        tooltip: {{
            trigger: 'axis',
            formatter: '{{b}}<br/>收益率: {{c}}%'
        }},
        xAxis: {{
            type: 'category',
            data: {dates_js},
            boundaryGap: false
        }},
        yAxis: {{
            type: 'value',
            name: '收益率 (%)',
            axisLabel: {{ formatter: '{{value}}%' }}
        }},
        dataZoom:[
            {{ type: 'inside', start: 0, end: 100 }},
            {{ type: 'slider', start: 0, end: 100 }}
        ],
        series:[{{
            data: {returns_js},
            type: 'line',
            smooth: true,
            itemStyle: {{ color: '#ee6666' }},
            markLine: {{
                data:[{{ type: 'average', name: '平均值' }}, {{ yAxis: 0, name: '零刻度' }}],
                label: {{ formatter: '{{b}}: {{c}}' }}
            }}
        }}]
    }};
    chartReturn.setOption(optionReturn);

    // === 图表2：累计净利润变化趋势 ===
    var chartProfit = echarts.init(document.getElementById('chart-profit'));
    var optionProfit = {{
        title: {{
            text: '累计净利润变化趋势',
            left: 'center'
        }},
        tooltip: {{
            trigger: 'axis',
            formatter: '{{b}}<br/>累计净利润: ¥{{c}}'
        }},
        xAxis: {{
            type: 'category',
            data: {dates_js},
            boundaryGap: false
        }},
        yAxis: {{
            type: 'value',
            name: '累计净利润 (元)',
            axisLabel: {{ formatter: '¥{{value}}' }}
        }},
        dataZoom:[
            {{ type: 'inside', start: 0, end: 100 }},
            {{ type: 'slider', start: 0, end: 100 }}
        ],
        series:[{{
            data: {profits_js},
            type: 'line',
            smooth: true,
            itemStyle: {{ color: '#5470c6' }},
            areaStyle: {{
                opacity: 0.3,
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1,[
                    {{offset: 0, color: 'rgba(84, 112, 198, 0.8)'}},
                    {{offset: 1, color: 'rgba(84, 112, 198, 0.1)'}}
                ])
            }},
            markLine: {{
                data:[{{ yAxis: 0, name: '盈亏平衡点' }}]
            }}
        }}]
    }};
    chartProfit.setOption(optionProfit);

    // 监听窗口大小变化自动缩放图表
    window.addEventListener('resize', function() {{
        chartReturn.resize();
        chartProfit.resize();
    }});
}});
</script>
"""
    return html_template

def csv_to_md_sim():
    
    csv_map = {
        
        "sim_trade_result_top1-300.csv": "前1只股票[300股]",
        "sim_trade_result_top1-600.csv": "前1只股票[600股]",
        "sim_trade_result_top1-1000.csv": "前1只股票[1000股]",
        
        "sim_trade_result_top3-300.csv": "前3只股票[300股]",
        "sim_trade_result_top3-600.csv": "前3只股票[600股]",
        "sim_trade_result_top3-1000.csv": "前3只股票[1000股]",
        
        "sim_trade_result_top5-300.csv": "前5只股票[300股]",
        "sim_trade_result_top5-600.csv": "前5只股票[600股]",
        "sim_trade_result_top5-1000.csv": "前5只股票[1000股]",
        
        "sim_trade_result_top10-300.csv": "前10只股票[300股]",
        "sim_trade_result_top10-600.csv": "前10只股票[600股]",
        "sim_trade_result_top10-1000.csv": "前10只股票[1000股]",
        
        "sim_trade_result_top15-300.csv": "前15只股票[300股]",
        "sim_trade_result_top15-600.csv": "前15只股票[600股]",
        "sim_trade_result_top15-1000.csv": "前15只股票[1000股]",
        
        "sim_trade_result_compare-300.csv": "收益对比[300股]",
        "sim_trade_result_compare-600.csv": "收益对比[600股]",
        "sim_trade_result_compare-1000.csv": "收益对比[1000股]",
    }
    
    _duibi=""
    
    for csvname,title in csv_map.items():
        csv_path=Path(f'{PROJECT_ROOT}/tests/{csvname}')
    
            
        # 2. 检查源 CSV 是否存在
        source_file = Path(csv_path)
        if not source_file.exists():
            print(f"⚠️ 找不到文件，跳过生成: {source_file}")
            return
            
        # 3. 读取 CSV 文件（处理 NaN 防止出现难看的字符串）
        try:
            df = pd.read_csv(source_file)
            df = df.fillna("")  # 将空缺值替换为空字符串
        except Exception as e:
            print(f"❌ 读取 CSV 失败: {source_file} \n错误信息: {e}")
            return

        # 4. 手动生成 Markdown 表格（不依赖外部 tabulate 库，适合 CI 运行）
        headers = df.columns.tolist()
        header_row = "| " + " | ".join(str(h) for h in headers) + " |"
        separator_row = "| " + " | ".join("---" for _ in headers) + " |"
        
        data_rows =[]
        for _, row in df.iterrows():
            # 将每行的数据转为字符串，并用 | 拼接
            row_str = "| " + " | ".join(str(val) for val in row.values) + " |"
            data_rows.append(row_str)
            
        md_table = "\n".join([header_row, separator_row] + data_rows)
        
        # 5. 构建最终写入的 Markdown 文本
        md_content = f"# {title}\n\n{md_table}\n"
        
        # 6. 确认输出目录并写入
        out_md_path = DOCS_DIR / f'pages/guide/{csv_path.stem}.md'
        out_md_path.parent.mkdir(parents=True, exist_ok=True)  # 确保 guide 目录存在
        
        if csvname.startswith('sim_trade_result_top'):
            jscode=generate_echarts_script(csv_path)
            jsfile=DOCS_DIR / f'public/{csv_path.stem}.html'
            print(f'生成 js代码到 {jsfile}')
            with open(jsfile, 'w', encoding='utf-8') as f:
                f.write(jscode)
            (DOCS_DIR / '.vitepress/dist').mkdir(exist_ok=True)
            shutil.copy2(jsfile,DOCS_DIR / f'.vitepress/dist/{csv_path.stem}.html')
            md_content+=f"""<iframe style="width:800px;height:1000px;overflow:hidden" src="https://jianchang512.github.io/astock/{csv_path.stem}.html"></iframe>"""
            with open(out_md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
                
            print(f"✅ 成功生成 Markdown 文档: {out_md_path}")
        else:
            _duibi+=f"{title}\n\n{md_table}\n\n----\n----\n"
            
            
    out_md_path = DOCS_DIR / f'pages/guide/收益对比.md'
    with open(out_md_path, 'w', encoding='utf-8') as f:
        f.write(_duibi)



def csv_to_markdown_table000(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return ''
    lines = []
    # 表头
    if csv_path.name.endswith('_ret.csv'):
        rows[0][0]=''
        rows[0][1]='股票代码'
        rows[0][2]='预测涨幅'
        rows[0][3]='看涨概率'
        rows[0][4]='用于复盘'
        rows[0][5]='预测误差'
        rows[0][6]='预测误差(绝对值)'
    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    for row in rows[1:]:
        # 补齐列数
        while len(row) < len(rows[0]):
            row.append('')
        row = row[:len(rows[0])]
        lines.append('| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |')
    return '\n'.join(lines)



def csv_to_markdown_table(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格，并先按 pos_ratio 倒序，同值按 avg_score 倒序排列"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    if not rows or len(rows) < 2: # 如果为空或者只有表头
        return ''
        
    # --- 新增：排序逻辑开始 ---
    # 动态查找 avg_score 的列索引（增加代码健壮性），如果没有找到则默认使用索引 2
    try:
        avg_score_idx = rows[0].index('avg_score')
    except ValueError:
        avg_score_idx = 2 
        
    # 动态查找 pos_ratio 的列索引，如果没有找到则默认使用索引 3
    try:
        pos_ratio_idx = rows[0].index('pos_ratio')
    except ValueError:
        pos_ratio_idx = 3

    # 将数据分为表头和数据行
    header = rows[0]
    data_rows = rows[1:]

    # 定义排序的 key 函数
    def sort_key(row):
        # 1. 提取 pos_ratio（第一排序维度）
        try:
            ratio_val = float(row[pos_ratio_idx]) if pos_ratio_idx < len(row) else -float('inf')
        except (ValueError, IndexError):
            ratio_val = -float('inf')
            
        # 2. 提取 avg_score（第二排序维度）
        try:
            score_val = float(row[avg_score_idx]) if avg_score_idx < len(row) else -float('inf')
        except (ValueError, IndexError):
            score_val = -float('inf') 

        # 返回元组，外层 sort(reverse=True) 会先根据 ratio_val 倒序，同值再根据 score_val 倒序
        return (ratio_val, score_val)

    # 对数据行进行多重倒序排序
    data_rows.sort(key=sort_key, reverse=True)

    # 将表头和排序后的数据重新组合
    rows = [header] + data_rows
    # --- 新增：排序逻辑结束 ---

    lines =[]
    # 表头替换
    if csv_path.name.endswith('_ret.csv'):
        rows[0][0]=''
        rows[0][1]='股票代码'
        rows[0][2]='预测涨幅'  # 对应 avg_score
        rows[0][3]='看涨概率'  # 对应 pos_ratio
        rows[0][4]='用于复盘'
        rows[0][5]='预测误差'
        rows[0][6]='预测误差(绝对值)'
        
    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    
    for row in rows[1:]:
        # 补齐列数
        while len(row) < len(rows[0]):
            row.append('')
        row = row[:len(rows[0])]
        lines.append('| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |')
        
    return '\n'.join(lines)

def csv_to_markdown_table0423(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格，并按 avg_score 倒序排列"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    if not rows or len(rows) < 2: # 如果为空或者只有表头
        return ''
        
    # --- 新增：排序逻辑开始 ---
    # 动态查找 avg_score 的列索引（增加代码健壮性），如果没有找到则默认使用索引 2
    try:
        avg_score_idx = rows[0].index('avg_score')
    except ValueError:
        avg_score_idx = 2 

    # 将数据分为表头和数据行
    header = rows[0]
    data_rows = rows[1:]

    # 定义排序的 key 函数
    def sort_key(row):
        try:
            # 尝试将该列转换为浮点数用于正确的数值比较
            return float(row[avg_score_idx])
        except (ValueError, IndexError):
            # 如果遇到空值或无法转换为数字的值，将其排在最下面
            return -float('inf') 

    # 对数据行进行倒序排序
    data_rows.sort(key=sort_key, reverse=True)

    # 将表头和排序后的数据重新组合
    rows = [header] + data_rows
    # --- 新增：排序逻辑结束 ---

    lines =[]
    # 表头替换
    if csv_path.name.endswith('_ret.csv'):
        rows[0][0]=''
        rows[0][1]='股票代码'
        rows[0][2]='预测涨幅'  # 对应 avg_score
        rows[0][3]='看涨概率'
        rows[0][4]='用于复盘'
        rows[0][5]='预测误差'
        rows[0][6]='预测误差(绝对值)'
        
    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    
    for row in rows[1:]:
        # 补齐列数
        while len(row) < len(rows[0]):
            row.append('')
        row = row[:len(rows[0])]
        lines.append('| ' + ' | '.join(str(c).replace('|', '\\|') for c in row) + ' |')
        
    return '\n'.join(lines)

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def sort_backtest_name(stem: str):
    """
    排序规则:
    1) 先 ret，再 filter_ret
    2) 同类型按 topN 从小到大
    3) 不匹配规则的文件放末尾并按名称排序
    """
    m = re.match(r'^(\d+)_(ret|filter_ret)$', stem)
    if not m:
        return (2, float('inf'), stem)
    topn = int(m.group(1))
    t = 0 if m.group(2) == 'ret' else 1
    return (t, topn, stem)


def format_backtest_heading(stem: str) -> str:
    """将文件 stem 转成友好的中文标题，如 Top10策略 ret。"""
    m = re.match(r'^(\d+)_(ret|filter_ret)$', stem)
    if not m:
        return stem
    topn, typ = m.group(1), m.group(2)
    return f'Top{topn}策略 {typ}'


def sync_backtest_csv_to_public() -> list[str]:
    """同步项目根目录 backtest_csv 到 docs/public/backtest_csv，并生成 index.json 清单。"""
    src_dir = BACKTEST_DIR
    dst_dir = DOCS_DIR / 'public' / 'backtest_csv'
    ensure_dir(dst_dir)

    # 清理旧 csv，避免历史脏文件残留
    for old_csv in dst_dir.glob('*.csv'):
        old_csv.unlink()

    if not src_dir.exists() or not src_dir.is_dir():
        (dst_dir / 'index.json').write_text(json.dumps([], ensure_ascii=False, indent=2), encoding='utf-8')
        return []

    files = [p for p in src_dir.iterdir() if p.is_file() and p.suffix == '.csv']
    files = sorted(files, key=lambda p: sort_backtest_name(p.stem))
    names = []
    for f in files:
        shutil.copy2(f, dst_dir / f.name)
        names.append(f.name)

    (dst_dir / 'index.json').write_text(json.dumps(names, ensure_ascii=False, indent=2), encoding='utf-8')
    return names


def generate_nav_curve_md(backtest_files: list[str]) -> None:
    """根据 backtest csv 清单自动生成 nav_curve.md，保证右侧目录可跳转。"""
    out = DOCS_DIR / 'pages' / 'mahoupao' / 'nav_curve.md'
    ensure_dir(out.parent)

    lines = [
        '# 净值曲线（Lightweight Charts）\n\n',
        '该页面使用 `Lightweight Charts` 绘制回测策略净值曲线，并与 `CSI300` 同图对比。  \n',
        '数据来源为项目根目录的 `backtest_csv/*.csv`，构建时会自动同步到站点的 `/backtest_csv/` 目录。\n\n',
        '## 文件约定\n\n',
        '- 文件名：`<topN>_<type>.csv`，例如 `10_ret.csv`、`20_filter_ret.csv`\n',
        '- 关键字段：`date`、`strategy_equity`、`csi300_equity`\n',
        '- 排序规则：先 `ret`，后 `filter_ret`；组内按 `topN` 从小到大\n\n',
    ]

    strategy_stems = [f[:-4] for f in backtest_files if f.endswith('.csv')]
    if not strategy_stems:
        lines.append('> 当前未检测到 backtest csv 文件。\n')
    else:
        for name in strategy_stems:
            lines.append(f'## {format_backtest_heading(name)}\n\n')
            lines.append(f'<NavCurveChart strategy="{name}" />\n\n')

    out.write_text(''.join(lines), encoding='utf-8')


def generate_pages() -> None:
    """扫描并生成所有页面"""
    if not DATA_DIR.exists():
        print(f'错误: 数据目录不存在 {DATA_DIR}')
        return
    #table = csv_to_markdown_table2(f'{PROJECT_ROOT}/tests/sim_trade_result.csv')
    #print(f'########################{PROJECT_ROOT=}')
    #(DOCS_DIR / 'pages/guide/moni.md').write_text(table, encoding='utf-8')
    # 清空 docs（保留 .vitepress、pages 和 public 用户资源）
    ensure_dir(DOCS_DIR)
    preserve = {'.vitepress', 'pages', 'public'}
    for p in DOCS_DIR.iterdir():
        if p.name in preserve:
            continue
        if p.is_dir():
            import shutil
            shutil.rmtree(p)
        else:
            p.unlink()

    sidebar_items = []
    subdirs = sorted([d for d in DATA_DIR.iterdir() if d.is_dir()], reverse=True)
    limit = os.environ.get('GEN_PAGE_LIMIT')
    if limit:
        subdirs = subdirs[: int(limit)]
        print(f'[CI] 限制展示最近 {limit} 个子目录')

    # 根 index
    index_lines = ["""# 基于微软 `Qlib开源量化库`，预测 CSI300 
    
    > 点击左侧查看预测数据，顶部导航查看使用方法和各种数据解释
    
## 当前预测倾向：稳健性

1. 不要波动太大的股票
> - 最近5天看（STD5）
> - 最近20天看（STD20）  
> - 最近60天看（STD60）
>
> 价格波动都不能太大，都要在10%以内。

2. 要更加稳定的股票
> 在刚才的基础上，更严格：
>
> 最近60天的波动率要小于5%（长期很稳）
>
> 最近5天的波动率要小于6%（短期也稳）

3. 不要突然"发疯"的股票

> 最近5天的波动，不能超过最近60天平均波动的2倍。
>
> 就是说：
> - 如果这个股票平时很稳（60天波动小）
> - 但最近5天突然波动很大
> - 那就不要！
>
> 这是在防止"突发异常"。

4. 不要跌太多的股票

> ROC = 价格变化率（涨跌幅）
>
> 要求：
>
> - 最近10天跌幅不能超过20%（ROC10 > 0.80）
> - 最近20天跌幅不能超过20%（ROC20 > 0.80）
> - 最近60天跌幅不能超过20%（ROC60 > 0.80）
>
> 0.80 是什么意思？
>
>  1.00 表示不涨不跌
>
>  0.80 表示跌了20%
> 
> 所以 > 0.80 表示"跌幅不能超过20%"

5. 不要涨太多的股票

> 最近20天涨幅不能超过30%
>
> < 1.30 是什么意思？
>
>   1.30 表示涨了30%
> 
> 所以 < 1.30 表示"涨幅不能超过30%"
>
> 这是在排除"暴涨股"。


**整体规则**
- ✅ 价格稳定（波动率小于10%）         
- ✅ 长期稳定（60天波动率小于5%）      
- ✅ 没有异常波动（最近没发疯）        
- ✅ 没有暴跌（跌幅不超过20%）         
- ✅ 没有暴涨（涨幅不超过30%）         
                                       

> 策略类型：防守型 / 稳健型            
>
> 风险等级：低                         
> 
> 收益预期：稳定小幅增长               


```python
def filter_ret_df(self, df):
    # 过滤高风险股票
    
    # 波动率过滤（标准差 < 10%）
    df = df[(df['STD5'] < 0.10) & (df['STD20'] < 0.10) & (df['STD60'] < 0.10)]
    
    # 极低波动率（< 5%）
    df = df[(df['STD60'] < 0.05) & (df['STD5'] < 0.06)]
    
    # 波动率异常检测
    df = df[df['STD5'] < (df['STD60'] * 2)]
    
    # 涨跌幅过滤（ROC: Rate of Change）
    df = df[(df['ROC10'] > 0.80) & (df['ROC20'] > 0.80) & (df['ROC60'] > 0.80)]
    df = df[df['ROC20'] < 1.30]
    
    return df

```

    """]
    if (DATA_DIR / 'index.md').exists():
        index_lines.append((DATA_DIR / 'index.md').read_text(encoding='utf-8', errors='ignore'))
    index_lines.append('\n## 子目录列表\n')
    for d in subdirs:
        name = d.name
        link = f'/score/{name}/'
        index_lines.append(f'- [{name}]({link})\n')
        sidebar_items.append({
            'text': name,
            'link': f'/score/{name}/',
        })

    (DOCS_DIR / 'index.md').write_text(''.join(index_lines), encoding='utf-8')

    # 每个子目录
    for subdir in subdirs:
        rel = f'score/{subdir.name}'
        out_dir = DOCS_DIR / rel
        ensure_dir(out_dir)

        files = sorted(subdir.iterdir())
        md_files = [f for f in files if f.suffix == '.md']
        csv_files = [f for f in files if f.suffix == '.csv']

        # 子目录 index 先占位，生成页面后再写（确保与 page_content 一致）

        # 收集所有要生成的页面（MD 与 CSV 可能同名如 total）
        page_content: dict[str, list[str]] = {}  # base_name -> [sections]

        for f in md_files:
            content = f.read_text(encoding='utf-8', errors='ignore')
            if f.stem not in page_content:
                page_content[f.stem] = []
            page_content[f.stem].append(f'# {f.stem}\n\n{content}')

        for f in csv_files:
            table = csv_to_markdown_table(f)
            section = f'# {f.name}\n\n{table}'
            if f.stem not in page_content:
                page_content[f.stem] = []
            page_content[f.stem].append(section)

        for base_name, sections in page_content.items():
            out_path = out_dir / f'{base_name}.md'
            out_path.write_text('\n\n---\n\n'.join(sections), encoding='utf-8')

        # 子目录 index（按 base_name 排序）
        sub_index = [f'# {subdir.name}\n\n']
        for base_name in sorted(page_content.keys()):
            sub_index.append(f'- [{base_name}](/{rel}/{base_name})\n')
        (out_dir / 'index.md').write_text(''.join(sub_index), encoding='utf-8')

    # 同步回测 csv 到 public，供前端绘图，并生成马后炮净值页面
    backtest_files = sync_backtest_csv_to_public()
    generate_nav_curve_md(backtest_files)
    # 自动生成 pages 子页面链接和侧边栏（用户只需增删 md 文件）
    generate_pages_auto()

    # 更新 vitepress 侧边栏（数据目录）
    update_sidebar(sidebar_items)
    print(f'生成完成: {DOCS_DIR}')


# pages 下各文件夹的显示名称（与 nav 一致）
PAGES_TITLES: dict[str, str] = {
    'mahoupao': '基础知识',
    'guide':"模拟回测"
}


def _get_md_title(md_path: Path) -> str:
    """从 md 文件第一行 # 标题 提取显示名，否则用文件名"""
    try:
        text = md_path.read_text(encoding='utf-8', errors='ignore').strip()
        for line in text.split('\n')[:5]:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
    except Exception:
        pass
    return md_path.stem


def generate_pages_auto() -> None:
    """
    扫描 pages 下各子目录的 .md 文件，自动生成侧边栏配置。
    用户只需增删 md 文件，运行 gen 后侧边栏自动更新。
    """
    pages_dir = DOCS_DIR / 'pages'
    if not pages_dir.exists():
        return

    pages_sidebar: dict[str, list[dict[str, str]]] = {}
    csv_map = {
        
        "sim_trade_result_top1-300": "A",
        "sim_trade_result_top1-600": "B",
        "sim_trade_result_top1-1000": "C",
        
        "sim_trade_result_top3-300": "D",
        "sim_trade_result_top3-600": "E",
        "sim_trade_result_top3-1000": "F",
        
        "sim_trade_result_top5-300": "H",
        "sim_trade_result_top5-600": "I",
        "sim_trade_result_top5-1000": "J",
        
        "sim_trade_result_top10-300": "K",
        "sim_trade_result_top10-600": "L",
        "sim_trade_result_top10-1000": "M",
        
        "sim_trade_result_top15-300": "N",
        "sim_trade_result_top15-600": "O",
        "sim_trade_result_top15-1000": "P",
        
        "sim_trade_result_compare-300": "Q",
        "sim_trade_result_compare-600": "R",
        "sim_trade_result_compare-1000": "S",
    }

    for subdir in sorted(pages_dir.iterdir()):
        if not subdir.is_dir():
            continue
        subdir_name = subdir.name
        title = PAGES_TITLES.get(subdir_name, subdir_name)

        md_files = [
            f for f in subdir.iterdir()
            if f.is_file() and f.suffix == '.md' and f.name != 'index.md'
        ]
        if "guide" in subdir_name:
            md_files = sorted(md_files, key=lambda x: csv_map.get(x.stem,'Z'))
        else:
            md_files = sorted(md_files, key=lambda x: x.stem)
        if "guide" in subdir_name:
            print(md_files)
        # 只生成侧边栏，不修改 index.md 正文
        rel_path = f'/pages/{subdir_name}'
        sidebar_items = [
            {'text': title, 'link': f'{rel_path}/'},
        ]
        for f in md_files:
            display = _get_md_title(f)
            sidebar_items.append({'text': display, 'link': f'{rel_path}/{f.stem}'})

        # GitHub Pages 部署时 route 含 base，需两种 key 以兼容 dev 与 prod
        pages_sidebar[f'{rel_path}/'] = sidebar_items
        pages_sidebar[f'/astock{rel_path}/'] = sidebar_items

    # 写入 sidebar-pages.generated.ts
    _write_sidebar_pages(pages_sidebar)


def _write_sidebar_pages(pages_sidebar: dict[str, list[dict[str, str]]]) -> None:
    """生成 .vitepress/sidebar-pages.generated.ts"""
    out = DOCS_DIR / '.vitepress' / 'sidebar-pages.generated.ts'
    lines = ["/** 由 gen_page.py 自动生成，请勿手动修改 */\n", "export const pagesSidebar = {\n"]
    for path, items in pages_sidebar.items():
        lines.append(f"  '{path}': [")
        for it in items:
            t = it['text'].replace("'", "\\'").replace('\\', '\\\\')
            lines.append(f"    {{ text: '{t}', link: '{it['link']}' }},")
        lines.append('  ],')
    lines.append('}\n')
    out.write_text('\n'.join(lines), encoding='utf-8')


def update_sidebar(items: list) -> None:
    """更新 vitepress 配置中的 sidebar（当 sidebar 为 false 时跳过）"""
    config_path = DOCS_DIR / '.vitepress' / 'config.ts'
    if not config_path.exists():
        return
    content = config_path.read_text(encoding='utf-8')
    if 'sidebar: false' in content:
        return

    def esc(s: str) -> str:
        return s.replace("'", "\\'").replace('\\', '\\\\')
    items_str = ',\n      '.join(
        f"{{ text: '{esc(i['text'])}', link: '{i['link']}' }}" for i in items
    )
    new_items = f"items: [{items_str}]"
    # 使用正则替换，兼容：1) 占位符 items: []  2) 已被替换过的旧 items: [...]
    pattern = r"items:\s*\[[\s\S]*?\]"
    new_content = re.sub(pattern, new_items, content, count=1)
    config_path.write_text(new_content, encoding='utf-8')


if __name__ == '__main__':
    csv_to_md_sim()
    generate_pages()
