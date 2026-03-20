#!/usr/bin/env python3
"""
扫描 qlib_score_csv 子目录，生成 VitePress 静态页面。
所有 CSV 转为 Markdown 表格，MD 文件直接引用。
"""
import csv
import os
import re
from pathlib import Path

# 路径配置：page/script/gen_page.py -> 项目根目录
PAGE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = PAGE_ROOT.parent
DATA_DIR = PROJECT_ROOT / 'qlib_score_csv'
DOCS_DIR = PAGE_ROOT / 'docs'


def csv_to_markdown_table(csv_path: Path) -> str:
    """将 CSV 转为 Markdown 表格"""
    with open(csv_path, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return ''
    lines = []
    # 表头
    rows[0][0]=''
    rows[0][1]='股票代码'
    rows[0][2]='预测明天收益率'
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


def generate_pages() -> None:
    """扫描并生成所有页面"""
    if not DATA_DIR.exists():
        print(f'错误: 数据目录不存在 {DATA_DIR}')
        return

    # 清空 docs（保留 .vitepress 和 pages 用户页面）
    ensure_dir(DOCS_DIR)
    preserve = {'.vitepress', 'pages'}
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
    index_lines = ["""# 基于微软 *Qlib开源量化库*，预测 CSI300 \n 点击左侧查看预测。\n以下是术语和规则解释\n\n

## **当前规则：稳健性**

1. 不要波动太大的股票
> - 最近5天看（STD5）
> - 最近20天看（STD20）  
> - 最近60天看（STD60）
>
> 价格波动都不能太大，都要在10%以内。

2. 要更加稳定的股票
> 在刚才的基础上，更严格：
> 最近60天的波动率要小于5%（长期很稳）
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
                                       
策略类型：防守型 / 稳健型            

风险等级：低                         

收益预期：稳定小幅增长               


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

---

## 表格字段完整解释

### **📊 基础字段（非Alpha158因子）**


instrument: 股票代码（如 SH600000）

avg_score: 多模型预测的加权平均分数（预测明天收益率）

pos_ratio: 看涨模型比例（0-1，如0.8表示80%模型预测上涨）

real_label: 真实标签（T+2日的实际收益率，用于复盘）

error: 预测误差（预测值 - 实际值）

abs_error: 绝对误差（|预测值 - 实际值|）

code: 股票代码

name: 股票名称

datetime: 日期时间戳


---

### **🔬 Alpha158 量化因子**

#### **1. K线形态因子（KXXX）** 描述K线的形态特征


KMID: K线中点位置 = (收盘价 - 开盘价) / (最高价 - 最低价)
      → 值域[-1, 1]，>0表示收盘在上半部分

KLEN: K线长度 = (最高价 - 最低价) / 收盘价
      → 衡量单日波动幅度，值越大波动越大

KMID2: KMID的平方（放大极端值）

KUP: 上影线长度 = (最高价 - max(开盘价, 收盘价)) / 收盘价
     → 值越大，抛压越强

KUP2: KUP的平方

KLOW: 下影线长度 = (min(开盘价, 收盘价) - 最低价) / 收盘价
      → 值越大，支撑越强

KLOW2: KLOW的平方

KSFT: K线偏移 = (收盘价 - 开盘价) / 收盘价
      → 正值看涨，负值看跌

KSFT2: KSFT的平方

---

#### **2. 当日价格因子（XXX0）**

OPEN0: 今日开盘价（原始值）

HIGH0: 今日最高价（原始值）

LOW0: 今日最低价（原始值）

VWAP0: 今日成交量加权平均价 = Σ(价格 × 成交量) / Σ成交量
       → 反映当日平均成交成本


---

#### **3. 变化率因子（ROCN）**

ROC5: 5日收益率 = 今日收盘价 / 5日前收盘价
      → 1.05表示5天涨了5%

ROC10: 10日收益率

ROC20: 20日收益率（约1个月）

ROC30: 30日收益率（约1.5个月）

ROC60: 60日收益率（约3个月）

---

#### **4. 移动平均因子（MAN）**

MA5: 5日收盘价移动平均（短期趋势）

MA10: 10日移动平均

MA20: 20日移动平均（重要支撑/阻力位）

MA30: 30日移动平均

MA60: 60日移动平均（长期趋势）

---

#### **5. 波动率因子（STDN）**


STD5: 5日收益率标准差（短期波动率）

STD10: 10日波动率

STD20: 20日波动率

STD30: 30日波动率

STD60: 60日波动率

→ 值越大，股票越不稳定


---

#### **6. Beta系数因子（BETAN）**

Beta = 股票收益率与市场收益率的协方差 / 市场收益率方差

BETA5: 5日Beta系数

BETA10: 10日Beta系数

BETA20: 20日Beta系数

BETA30: 30日Beta系数

BETA60: 60日Beta系数

→ Beta=1: 与市场同步

→ Beta>1: 比市场波动大（进攻型）

→ Beta<1: 比市场波动小（防守型）

---

#### **7. R平方因子（RSQRN）**

RSQR = R² = 拟合优度（0-1）

RSQR5: 5日R平方

RSQR10: 10日R平方

RSQR20: 20日R平方

RSQR30: 30日R平方

RSQR60: 60日R平方

→ 值越接近1，股票走势越规律（与市场相关性越强）

→ 值越接近0，走势越独立

---

#### **8. 残差因子（RESIN）**

RESI = Residual（回归残差）

RESI5: 5日残差

RESI10: 10日残差

RESI20: 20日残差

RESI30: 30日残差

RESI60: 60日残差

→ 正值：股票表现优于预期（超额收益）

→ 负值：股票表现劣于预期

---

#### **9. 极值因子（MAX/MIN）**

MAX5: 5日最高价

MAX10: 10日最高价

MAX20: 20日最高价

MAX30: 30日最高价

MAX60: 60日最高价

MIN5: 5日最低价

MIN10: 10日最低价

MIN20: 20日最低价

MIN30: 30日最低价

MIN60: 60日最低价

---

#### **10. 分位数因子（QTLU/QTLD）**

QTLU = Quantile Upper（上四分位数，75%分位点）

QTLD = Quantile Lower（下四分位数，25%分位点）

QTLU5: 5日价格上四分位数

QTLU10/20/30/60: 10/20/30/60日上四分位数

QTLD5: 5日价格下四分位数

QTLD10/20/30/60: 10/20/30/60日下四分位数



---

#### **11. 排名因子（RANKN）**

RANK5: 今日价格在5日内的排名（0-1）

RANK10: 今日价格在10日内的排名

RANK20: 今日价格在20日内的排名

RANK30: 今日价格在30日内的排名

RANK60: 今日价格在60日内的排名

→ 1.0 = 最高价，0.0 = 最低价

---

#### **12. RSV因子（未成熟随机值）**

RSV = Raw Stochastic Value = (收盘价 - N日最低价) / (N日最高价 - N日最低价)

RSV5: 5日RSV

RSV10: 10日RSV

RSV20: 20日RSV

RSV30: 30日RSV

RSV60: 60日RSV

→ 0-100，>80超买，<20超卖（KDJ指标的基础）

---

#### **13. 极值位置因子（IMAX/IMIN）**

IMAX = Index of Maximum（最高价出现的位置）

IMIN = Index of Minimum（最低价出现的位置）

IMAX5: 5日内最高价出现的天数（0-4）

IMAX10/20/30/60: 10/20/30/60日内最高价位置

IMIN5: 5日内最低价出现的天数

IMIN10/20/30/60: 10/20/30/60日内最低价位置

→ 0 = 今天，4 = 4天前

---

#### **14. 极值距离因子（IMXD）**

IMXD = Index Max Distance = IMAX - IMIN

IMXD5: 5日内最高最低价位置的距离

IMXD10: 10日距离

IMXD20: 20日距离

IMXD30: 30日距离

IMXD60: 60日距离

→ 正值大：先低后高（上涨趋势）

→ 负值大：先高后低（下跌趋势）

---

#### **15. 相关系数因子（CORR）**

CORR = Correlation（与时间的相关系数，衡量趋势性）

CORR5: 5日价格与时间的相关系数

CORR10/20/30/60: 10/20/30/60日相关系数

→ 正值：上涨趋势

→ 负值：下跌趋势

→ 接近0：震荡无趋势

---

#### **16. 序数相关系数因子（CORD）**

CORD = Correlation with Ordinal（使用排名计算的相关系数）

CORD5: 5日序数相关系数

CORD10/20/30/60: 10/20/30/60日序数相关系数

→ 比CORR更稳健（对异常值不敏感）

---

#### **17. 计数因子（CNT）**

CNTP5: 5日内正收益天数（涨的天数）

CNTP10/20/30/60: 10/20/30/60日内正收益天数

CNTN5: 5日内负收益天数（跌的天数）

CNTN10/20/30/60: 10/20/30/60日内负收益天数

CNTD5: 5日内正负天数差 = CNTP5 - CNTN5

CNTD10/20/30/60: 10/20/30/60日正负天数差

→ CNTD越大，上涨动能越强

---

#### **18. 收益总和因子（SUM）**

SUMP5: 5日内所有正收益的总和

SUMP10/20/30/60: 10/20/30/60日正收益总和

SUMN5: 5日内所有负收益的绝对值总和

SUMN10/20/30/60: 10/20/30/60日负收益总和

SUMD5: 正负收益差 = SUMP5 - SUMN5

SUMD10/20/30/60: 10/20/30/60日收益差

→ SUMD越大，累计涨幅越大

---

#### **19. 成交量均线因子（VMA）**

VMA5: 5日成交量移动平均

VMA10: 10日成交量移动平均

VMA20: 20日成交量移动平均

VMA30: 30日成交量移动平均

VMA60: 60日成交量移动平均

---

#### **20. 成交量波动率因子（VSTD）**

VSTD5: 5日成交量标准差

VSTD10: 10日成交量标准差

VSTD20: 20日成交量标准差

VSTD30: 30日成交量标准差

VSTD60: 60日成交量标准差

→ 衡量成交量的不稳定性

---

#### **21. 加权成交量均线因子（WVMA）**

WVMA5: 5日加权成交量移动平均

WVMA10: 10日加权成交量移动平均

WVMA20: 20日加权成交量移动平均

WVMA30: 30日加权成交量移动平均

WVMA60: 60日加权成交量移动平均

→ 近期成交量权重更大

---

#### **22. 成交量计数与总和因子（VSUM/VCNT）**

VSUMP5: 5日内成交量放大的天数总量

VSUMP10/20/30/60: 10/20/30/60日成交量放大总量

VSUMN5: 5日内成交量萎缩的天数总量

VSUMN10/20/30/60: 10/20/30/60日成交量萎缩总量

VSUMD5: 成交量变化差 = VSUMP5 - VSUMN5

VSUMD10/20/30/60: 10/20/30/60日成交量变化差   
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

    # 自动生成 pages 子页面链接和侧边栏（用户只需增删 md 文件）
    generate_pages_auto()

    # 更新 vitepress 侧边栏（数据目录）
    update_sidebar(sidebar_items)
    print(f'生成完成: {DOCS_DIR}')


# pages 下各文件夹的显示名称（与 nav 一致）
PAGES_TITLES: dict[str, str] = {
    'mahoupao': '分析回测',
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

    for subdir in sorted(pages_dir.iterdir()):
        if not subdir.is_dir():
            continue
        subdir_name = subdir.name
        title = PAGES_TITLES.get(subdir_name, subdir_name)

        md_files = [
            f for f in subdir.iterdir()
            if f.is_file() and f.suffix == '.md' and f.name != 'index.md'
        ]
        md_files = sorted(md_files, key=lambda x: x.stem)

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
    generate_pages()
