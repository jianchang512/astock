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

    # 自动生成 pages 子页面链接和侧边栏（用户只需增删 md 文件）
    generate_pages_auto()

    # 更新 vitepress 侧边栏（数据目录）
    update_sidebar(sidebar_items)
    print(f'生成完成: {DOCS_DIR}')


# pages 下各文件夹的显示名称（与 nav 一致）
PAGES_TITLES: dict[str, str] = {
    'mahoupao': '分析回测',
    'huice':"操作使用方法",
    'guide':"量化交易"
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
