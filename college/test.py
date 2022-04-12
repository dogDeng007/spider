# -*- coding: utf-8 -*-
# Date: 2021/6/8 1:31
# Author: libiao
# wechat: 一条IT
# Software: PyCharm
import numpy as np
import pandas as pd
from pyecharts.charts import Pie, Bar, Map, Line, Grid, Page
from pyecharts import options as opts
from pyecharts.globals import SymbolType, WarningType
WarningType.ShowWarning = False

df = pd.read_excel('./全国高校数据.xlsx')
pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)

# 字段选择
# df.drop('address', axis=1, inplace=True)
print(df.head())
print(df.info())

# 985/211/双非高校
num_985 = df[df['f985']==1].groupby('province_name')['f985'].sum().reset_index()
num_211 = df[(df['f211']==1)&(df['f985']==2)].groupby('province_name')['f211'].sum().reset_index()
num_shuangfei = df[(df['f985']==2)&(df['f211']==2)]['province_name'].value_counts().reset_index().rename({
    'index': 'province_name',
    'province_name': 'num'
}, axis=1)

# 合并数据
df_merge = pd.merge(num_shuangfei, num_985, on='province_name', how='left')
df_merge = pd.merge(df_merge, num_211, on='province_name', how='left')

# 填充数据
df_merge.fillna(0, inplace=True)

# 计算合计
df_merge['all_num'] = df_merge['num'] + df_merge['f985'] + df_merge['f211']

df_merge = df_merge.sort_values('all_num')
print(df_merge.head())
school_num = df.province_name.value_counts().sort_values()
school_num[:5]
# 产生数据
x_data = school_num.index.tolist()
y_data = school_num.values.tolist()
bar0 = Bar(init_opts=opts.InitOpts(width='1350px', height='1000px'))
bar0.add_xaxis(xaxis_data=x_data)
bar0.add_yaxis('', y_data, color='#F29027')
bar0.set_global_opts(title_opts=opts.TitleOpts('各省市地区高校数量分布'),
                     legend_opts=opts.LegendOpts(pos_left='20%'))
bar0.set_series_opts(label_opts=opts.LabelOpts(position='right'))
bar0.reversal_axis()
bar0.render()

# 地图
map1 = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
map1.add("", [list(z) for z in zip(school_num.index.tolist(), school_num.values.tolist())],
         maptype='china'
        )
map1.set_global_opts(title_opts=opts.TitleOpts(title='各省市地区高校数量分布'),
                     visualmap_opts=opts.VisualMapOpts(max_=174),
                    )
map1.render()

# 产生数据
x_data = df_merge['province_name'].values.tolist()

y_data1 = df_merge['f985'].values.tolist()
y_data2 = df_merge['f211'].values.tolist()
y_data3 = df_merge['num'].values.tolist()


bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1.add_xaxis(x_data)
bar1.add_yaxis('985', y_data1, stack='stack1')
bar1.add_yaxis('211', y_data2, stack='stack1')
bar1.add_yaxis('双非', y_data3, stack='stack1')
bar1.set_global_opts(opts.TitleOpts(title='各个省的高校层次分布'),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate='60'))
                    )
bar1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
bar1.render()

type_num = df.type_name.value_counts()
type_num[:5]

# 数据对
data_pair =  [list(z) for z in zip(type_num.index.tolist(), type_num.values.tolist())]

# 绘制饼图
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
pie1.add('', data_pair, radius=['35%', '60%'])
pie1.set_global_opts(title_opts=opts.TitleOpts(title='全国高校类型分布'),
                     legend_opts=opts.LegendOpts(is_show=False, orient='vertical', pos_top='15%', pos_left='2%'))
pie1.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
# pie1.set_colors(['#EF9050', '#3B7BA9', '#6FB27C', '#FFAF34', '#D8BFD8', '#00BFFF', '#7FFFAA'])
pie1.render()

# 生成page
page1 = Page()
page1.add(bar0, map1, bar1, pie1)
page1.render('./全国高校分析.html')