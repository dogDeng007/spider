'''
1:https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page=1&province_id=&ranktype=&request_type=1&school_type=&signsafe=&size=20&sort=view_total&top_school_id=[2858]&type=&uri=apidata/api/gk/school/lists
2:https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page=2&province_id=&ranktype=&request_type=1&school_type=&signsafe=&size=20&sort=view_total&top_school_id=[2858]&type=&uri=apidata/api/gk/school/lists
3:https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page=3&province_id=&ranktype=&request_type=1&school_type=&signsafe=&size=20&sort=view_total&top_school_id=[2858]&type=&uri=apidata/api/gk/school/lists
'''
# -*- coding: utf-8 -*-
# Date: 2021/6/8 1:00
# Author: libiao
# wechat: 一条IT
# Software: PyCharm
# 导入包
import random
import requests
from fake_useragent import UserAgent
import time
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import  Map, Line, Bar, Pie, Funnel, Page  # 各个图形的类

# 获取一页
def spider_cl():

    # 请求的链接
    url = f'https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page=1&province_id=&ranktype=&request_type=1&school_type=&signsafe=&size=20&sort=view_total&top_school_id=[2858]&type=&uri=apidata/api/gk/school/lists'

    # 添加请求头
    headers = {
        'Referer': 'https://gkcx.eol.cn/',
        'User-Agent': str(UserAgent().random)
    }

    # 发起请求
    response = requests.post(url=url, headers = headers)
    if response.status_code == 200:
        college_info = response.json()['data']['item']

        # 长安大学
        college_name = [i.get('name') for i in college_info]
        # 2159.8w
        view_total = [i.get('view_total') for i in college_info]
        # 教育部
        belong = [i.get('belong') for i in college_info]
        # 普通本科
        level_name = [i.get('level_name') for i in college_info]
        # 公办
        nature_name = [i.get('nature_name') for i in college_info]
        # 双一流
        dual_class_name = [i.get('dual_class_name') for i in college_info]
        # 理工类
        type_name = [i.get('type_name') for i in college_info]
        # 陕西
        province_name = [i.get('province_name') for i in college_info]
        # 西安市
        city_name = [i.get('city_name') for i in college_info]
        # 碑林区
        county_name = [i.get('county_name') for i in college_info]
        # 陕西省西安市南二环路中段
        address = [i.get('address') for i in college_info]
        # 985
        f985 = [i.get('f985') for i in college_info]
        # 211
        f211 = [i.get('f211') for i in college_info]

        # 保存数据
        pd_data = pd.DataFrame({
            '学校名称': college_name,
            '人气值': view_total,
            '所属地': belong,
            'level_name': level_name,
            'nature_name': nature_name,
            'dual_class_name': dual_class_name,
            'type_name': type_name,
            '省': province_name,
            '市': city_name,
            '区': county_name,
            '详细地址': address,
            'f985': f985,
            'f211': f211,
        })
        return pd_data


# 获取多页
def get_all_page(all_page_num):
    # 存储表
    df_all = pd.DataFrame()
    # 循环页数
    for page in range(all_page_num):
        # 打印进度
        print(f'正在获取第{page + 1}页的高校信息')
        # 调用函数
        pd_data = spider_cl()
        # 追加
        df_all = df_all.append(pd_data, ignore_index=True)
        # 随机休眠
        time.sleep(random.random()*6)

    df_all.to_excel('./全国高校数据666.xlsx', index=False)

# 数据可视化操作
pd_data = pd.read_excel('./全国高校数据.xlsx')

def level_name():
    # 本科 vs 专职
    lev = pd_data['level_name'].value_counts()
    lev1 = lev.index.tolist()  # 本科 vs 专职
    lev2 = lev.tolist()  # 本科 vs 专职对应数量
    print(lev1)
    print(lev2)
    '''
    ['专科（高职）', '普通本科']
    [1498, 1359]
    '''

    return lev1, lev2


def f985():
    f985 = pd_data['f985'].value_counts()
    f9851 = f985.index.tolist()  # 985 vs 非985
    f9852 = f985.tolist()  #985 vs 非985对应数量
    print(f9851)
    print(f9852)
    '''
    [2, 1]
    [2811, 46]
    '''
    return f9851, f9852

def f211():
    f211 = pd_data['f211'].value_counts()
    f2111 = f211.index.tolist()  # 211 vs 211
    f2112 = f211.tolist()  #211 vs 非211对应数量
    print(f2111)
    print(f2112)
    '''
    [2, 1]
    [2731, 126]
    '''
    return f2111, f2112

def shuangfei():
    shuangfei = pd_data[(pd_data['f985'] == 2) & (pd_data['f211'] == 2)]['province_name'].value_counts()
    s1 = shuangfei.index.tolist()
    s2 = shuangfei.tolist()
    print(s1)
    print(s2)
    '''
    ['江苏', '广东', '河南', '山东', '四川', '湖北', '湖南', '河北', '安徽', '浙江', '江西', '辽宁', '陕西', '福建', '山西', '广西', '云南', '黑龙江', '贵州', '北京', '重庆', '吉林', '天津', '内蒙古', '上海', '新疆', '甘肃', '海南', '宁夏', '香港', '青海', '澳门', '西藏']
    [163, 158, 157, 155, 130, 127, 125, 124, 124, 111, 107, 106, 96, 88, 84, 84, 81, 77, 76, 75, 71, 67, 58, 55, 54, 53, 51, 20, 19, 14, 11, 5, 5]
    '''
    return s1, s2

def type_name():
    type_name = pd_data['type_name'].value_counts()
    type_name1 = type_name.index.tolist()  # 理工 vs 综合
    type_name2 = type_name.tolist()  # 理工 vs 综合对应数量
    print(type_name1)
    print(type_name2)
    '''
    ['理工类', '综合类', '师范类', '医药类', '财经类', '艺术类', '农林类', '政法类', '军事类', '其他', '语言类', '体育类', '民族类']
    [865, 829, 242, 216, 215, 106, 87, 68, 55, 55, 38, 35, 15]
    '''
    return type_name1, type_name2

# 人气值分析
def view_total():
    pd_data = pd.read_excel('./全国高校数据.xlsx')

    # 去除 30 ’w‘
    pd_data.loc[:, 'view_total1'] = pd_data['view_total'].str.replace('w', '').astype('float64')

    # 划分价格区间
    pd_data['view_total区间'] = pd.cut(pd_data['view_total1'], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500],
                                     labels=['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '>3000'])

    # 统计数量
    popular = pd_data['view_total区间'].value_counts()
    popular1 = popular.index.tolist()  # 人气值分类
    popular2 = popular.tolist()  # 人气值分类对应数量'''
    print(popular1)
    print(popular2)
    '''
    ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '>3000']
    [2500, 199, 42, 11, 5, 1, 1]
    '''

    return popular1, popular2

def map():
    school_num = pd_data.province_name.value_counts().sort_values()
    # 地图
    map1 = Map(init_opts=opts.InitOpts(width='1350px', height='750px'))
    map1.add("", [list(z) for z in zip(school_num.index.tolist(), school_num.values.tolist())],
             maptype='china'
             )
    map1.set_global_opts(title_opts=opts.TitleOpts(),
                         visualmap_opts=opts.VisualMapOpts(max_=174),
                         )
    map1.render('各省市地区高校数量分布.shtml')

def college_type():
    # 985/211/双非高校
    num_985 = pd_data[pd_data['f985'] == 1].groupby('province_name')['f985'].sum().reset_index()
    num_211 = pd_data[(pd_data['f211'] == 1) & (pd_data['f985'] == 2)].groupby('province_name')['f211'].sum().reset_index()
    num_shuangfei = pd_data[(pd_data['f985'] == 2) & (pd_data['f211'] == 2)]['province_name'].value_counts().reset_index().rename({
        'index': 'province_name',
        'province_name': 'num'
    }, axis=1)
    # 合并数据
    df_merge = pd.merge(num_shuangfei, num_985, on='province_name', how='left')
    df_merge = pd.merge(df_merge, num_211, on='province_name', how='left')

    # 填充数据
    df_merge.fillna(0, inplace=True)
    df_merge['all_num'] = df_merge['num'] + df_merge['f985'] + df_merge['f211']

    df_merge = df_merge.sort_values('all_num')

    x_data = df_merge['province_name'].values.tolist()

    y_data1 = df_merge['f985'].values.tolist()
    y_data2 = df_merge['f211'].values.tolist()
    y_data3 = df_merge['num'].values.tolist()

    bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
    bar1.add_xaxis(x_data)
    bar1.add_yaxis('985', y_data1, stack='stack1')
    bar1.add_yaxis('211', y_data2, stack='stack1')
    bar1.add_yaxis('双非', y_data3, stack='stack1')
    bar1.set_global_opts(opts.TitleOpts(),
                         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate='60'))
                        )
    bar1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    bar1.render('各个省的高校层次分布.shtml')

# 画图
def data_visual():
    x_data, y_data = shuangfei()

    # 1、柱状图
    def barPage() -> Bar:
        bar = (
            Bar()
                .add_xaxis(x_data)
                .add_yaxis("柱状图", y_data)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="柱状图分析"),
                legend_opts=opts.LegendOpts(is_show=False), )
        )
        return bar

    # 2、饼图
    def piePage() -> Pie:
        pie = (
            Pie()
                .add("", [list(z) for z in zip(x_data, y_data)])
                .set_global_opts(title_opts=opts.TitleOpts(title="饼图分析"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return pie

    # 3、折线图
    def linePage() -> Line:
        line = (
            Line()
                .add_xaxis(x_data)
                .add_yaxis("折线图", y_data)
                .set_global_opts(title_opts=opts.TitleOpts(title="折线图分析"))
        )
        return line

    # 4、漏斗图
    def funnelPage() -> Funnel:
        funnel = (
            Funnel()
                .add("漏斗图", [list(z) for z in zip(x_data, y_data)])
                .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图分析"))
        )
        return funnel


    # 上面是6个图形的代码，下面利用Page进行组合
    # !!! 关键步骤
    page = (
        Page(layout=Page.DraggablePageLayout)
            .add(
            barPage(),
            piePage(),
            linePage(),
            funnelPage())
    )

    page.render("985&211双非展示.html")
    print('绘图完成！')



if __name__ == '__main__':
    # 运行函数
    #df = get_all_page(134)
    #map()
    college_type()