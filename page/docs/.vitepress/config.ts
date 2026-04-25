import { defineConfig } from 'vitepress'
import { pagesSidebar } from './sidebar-pages.generated'

export default defineConfig({
  base: '/astock/',
  metaChunk: true,
  title: 'Qlib CSI300 沪深300',
  description: 'qlib CSI300 沪深300量化选股评分数据展示',
  lang: 'zh-CN',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
       { text: '基础知识', link: '/pages/mahoupao' },
       { text: '回测模拟', link: '/pages/guide' },
    ],
    sidebar: {
      ...pagesSidebar,
      '/': [
        {
          text: '数据目录',
          link: '/',
          items: [{ text: 'selection_20260313_16_10_28', link: '/score/selection_20260313_16_10_28/' },
      { text: 'selection_20260312_17_09_40', link: '/score/selection_20260312_17_09_40/' },
      { text: 'selection_20260312_15_28_31', link: '/score/selection_20260312_15_28_31/' },
      { text: 'selection_20260311_15_14_44', link: '/score/selection_20260311_15_14_44/' },
      { text: 'selection_20260310_17_37_47', link: '/score/selection_20260310_17_37_47/' },
      { text: 'selection_20260309_15_48_03', link: '/score/selection_20260309_15_48_03/' },
      { text: 'selection_20260308_21_11_10', link: '/score/selection_20260308_21_11_10/' },
      { text: 'selection_20260308_18_24_44', link: '/score/selection_20260308_18_24_44/' },
      { text: 'selection_20260308_16_54_35', link: '/score/selection_20260308_16_54_35/' },
      { text: 'selection_20260307_18_13_28', link: '/score/selection_20260307_18_13_28/' },
      { text: 'selection_20260307_14_52_24', link: '/score/selection_20260307_14_52_24/' },
      { text: 'selection_20260306_14_23_13', link: '/score/selection_20260306_14_23_13/' },
      { text: 'selection_20260306_08_46_19', link: '/score/selection_20260306_08_46_19/' }],
        },
      ],
    },
    outline: false
    
  },
  markdown: {
  },
})
