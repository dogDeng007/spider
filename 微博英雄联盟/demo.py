import pandas as pd
import jieba
from stylecloud import gen_stylecloud
from collections import Counter
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from icecream import ic
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.charts import Scatter
from pyecharts.faker import Faker

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

# 读取数据
rcv_data = pd.read_excel('./英雄联盟.xlsx')

# 删除重复记录和缺失值
rcv_data = rcv_data.drop_duplicates()
rcv_data = rcv_data.dropna()

# 抽样展示
print(rcv_data.sample(5))

#-----------------------------------

# 获取列内容
c_title = rcv_data['评论'].tolist()
# 观影评论词云图
wordlist = jieba.cut(''.join(c_title))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['的', '了', '也', '很', '用', '有', '是', '东西', '终于', '不', '还', '高']

# 词云展示
def visual_ciyun():
    pic = '../img.jpg'
    gen_stylecloud(text=result,
                   icon_name='fas fa-cookie-bite',
                   font_path='msyh.ttc',
                   background_color='white', #'字酷堂清楷体.ttf
                   output_name=pic,
                   custom_stopwords=stop_words
                   )
    print('词云图绘制成功！')


 # 词频设置
all_words = [word for word in result.split(' ') if len(word) > 1 and word not in stop_words]
wordcount = Counter(all_words).most_common(10)

x1_data, y1_data = list(zip(*wordcount))
print(x1_data)
print(y1_data)

#================================================================================================
def bar_datazoom_slider() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(chart_id=1, bg_color='#ADD8E6'))
        .add_xaxis(x1_data)
        .add_yaxis("网易词频展示图", y1_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-网易词频展示图"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(chart_id=2, bg_color='#ADD8E6'))
        .add_xaxis(x1_data)
        .add_yaxis(
            "网易词频展示图",
            y1_data,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-网易词频展示图"))
    )
    return c


def pie_rosetype() -> Pie:
    v = x1_data
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=3, bg_color='#ADD8E6'))
        .add(
            "",
            [list(z) for z in zip(v, y1_data)],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-网易词频展示图"))
    )
    return c


def liquid_data_precision() -> Liquid:
    c = (
        Liquid(init_opts=opts.InitOpts(chart_id=4, bg_color='#ADD8E6'))
        .add(
            "lq",
            [0.994],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="网易手机好评率"))
    )
    return c

def title():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=5, bg_color='#ADD8E6'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="----------网易手机高频词汇排行榜----------",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#000000'),
                                      pos_left='center',
                                      pos_top='middle'))
    )
    return c


def page_simple_layout():
    page = Page(layout=Page.DraggablePageLayout, page_title="网易手机高频词汇")
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        liquid_data_precision(),
        title(),
    )
    page.render("网易手机好评率.html")
    #page.save_resize_html('网易手机好评率.html', cfg_file='chart_config.json', dest='网易手机高频词汇统计展示图.html')


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 手机评分分布
# 划分价格区间
rcv_data['手机评分'] = pd.cut(rcv_data['手机评分'], [0, 1, 2, 5], labels=['差评', '中评', '好评'])

# 统计数量
stars = rcv_data['手机评分'].value_counts()
stars1 = stars.index.tolist()  # 人气值分类
stars2 = stars.tolist()   # 人气值分类对应数量'''
print(stars1)
print(stars2)

def bar_stars() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(chart_id=11, bg_color='#ADD8E6'))
            .add_xaxis(stars1)
            .add_yaxis("评价", stars2)
            .set_global_opts(title_opts=opts.TitleOpts(title='手机评价'))
    )
    return c


def line_stars() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(chart_id=21, bg_color='#ADD8E6'))
            .add_xaxis(xaxis_data=stars1)
            .add_yaxis(
            "评价",
            stars2,
            symbol="triangle",
            symbol_size=20,
            linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=3, border_color="yellow", color="blue"
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="手机评价"))
    )
    return c



def pie_stars() -> Pie:
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=31, bg_color='#ADD8E6'))
            .add(
            "",
            [list(z) for z in zip(stars1, stars2)],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Radius"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def titles():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=5, bg_color='#ADD8E6'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="----------网易手机评价图----------",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#000000'),
                                      pos_left='center',
                                      pos_top='middle'))
    )
    return c


def page_pingfen():
    page = Page(layout=Page.DraggablePageLayout, page_title="网易手机高频词汇")
    page.add(
        bar_stars(),
        line_stars(),
        pie_stars(),
        titles(),
    )
    page.render("手机评分.html")
    page.save_resize_html('手机评分.html', cfg_file='chart_config.json', dest='网易手机评分计展示图.html')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 提取时间月份
rcv_data['评论时间'] = rcv_data['评论时间'].map(lambda x: x.split('-')[1])
rcv_data['评论时间'] = pd.cut(rcv_data['评论时间'], ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'], labels=['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月'])

# 统计数量
dates = rcv_data['评论时间'].value_counts()
dates1 = dates.index.tolist()  # 月份分类
dates2 = dates.tolist()  # 月份分类对应数量
ic(dates1)
ic(dates2)

def title_date():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=12, bg_color='#ADD8E6'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="----------网易手机下单时间图----------",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#000000'),
                                      pos_left='center',
                                      pos_top='middle'))
    )
    return c

def funnel_dates():
    c = (
        Funnel(init_opts=opts.InitOpts(chart_id=22, bg_color='#ADD8E6'))
            .add(
            "月份",
            [list(z) for z in zip(dates1, dates2)],
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="iphone 下单时间"))
    )
    return c

def pie_dates():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=32, bg_color='#ADD8E6'))
            .add(
            "",
            [list(z) for z in zip(dates1, dates2)],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="iphone 下单时间"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

def bar_dates():
    c = (
        Bar(init_opts=opts.InitOpts(chart_id=42, bg_color='#ADD8E6'))
            .add_xaxis(dates1)
            .add_yaxis("月份", dates2)
            .set_global_opts(
            title_opts={"text": "iphone 下单时间"}
        )
    )
    return c

def scatter_dates():
    c = (
        Scatter(init_opts=opts.InitOpts(chart_id=52, bg_color='#ADD8E6'))
            .add_xaxis(dates1)
            .add_yaxis("月份", dates2)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="iphone 下单时间"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c

def page_dates():
    page = Page(layout=Page.DraggablePageLayout, page_title="网易手机下单时间")
    page.add(
        title_date(),
        funnel_dates(),
        pie_dates(),
        bar_dates(),
        scatter_dates()
    )
    page.render("手机下单时间.html")
    page.save_resize_html('手机下单时间.html', cfg_file='chart_config.json', dest='网易手机下单时间展示图.html')


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 内存大小
storage = rcv_data['手机内存'].value_counts()
storage1 = storage.index.tolist()  # 内存种类
storage2 = storage.tolist()  # 内存种类对应数量
ic(storage1)
ic(storage2)

def title_storage():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=31, bg_color='#ADD8E6'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="----------网易内存分布图----------",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#000000'),
                                      pos_left='center',
                                      pos_top='middle'))
    )
    return c

def line_storage():
    c = (
        Line(init_opts=opts.InitOpts(chart_id=32, bg_color='#ADD8E6'))
            .add_xaxis(storage1)
            .add_yaxis("内存", storage2, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
            .set_global_opts(title_opts=opts.TitleOpts(title="手机内存展示"))
    )
    return c


def bar_storage():
    c = (
        Bar(init_opts=opts.InitOpts(chart_id=33, bg_color='#ADD8E6'))
            .add_xaxis(storage1)
            .add_yaxis("内存", storage2)
            .set_global_opts(title_opts=opts.TitleOpts(title="手机内存展示"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(y=50, name="yAxis=50")]
            ),
        )
    )
    return c

def pie_storage():
    x_data = storage1
    y_data = storage2

    c = (
            Pie(init_opts=opts.InitOpts(width="1600px", height="1000px",chart_id=34, bg_color='#ADD8E6'))
                .add(
                series_name="手机内存",
                data_pair=[list(z) for z in zip(x_data, y_data)],
                radius=["50%", "70%"],
                label_opts=opts.LabelOpts(is_show=False, position="center"),
            )
                .set_global_opts(legend_opts=opts.LegendOpts(pos_left="legft", orient="vertical"))
                .set_series_opts(
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
                ),
                # label_opts=opts.LabelOpts(formatter="{b}: {c}")
            )
        )
    return c



def page_storage():
    page = Page(layout=Page.DraggablePageLayout, page_title="网易手机内存展示")
    page.add(
        title_storage(),
        line_storage(),
        pie_storage(),
        bar_storage()
    )
    page.render("手机内存.html")
    page.save_resize_html('手机内存.html', cfg_file='chart_config.json', dest='网易手机内存展示图.html')


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 颜色分布
rcv_datas = rcv_data[rcv_data['手机颜色'].str.len()==2]
colors = rcv_datas['手机颜色'].value_counts()
colors1 = colors.index.tolist()  # 内存种类
colors2 = colors.tolist()  # 内存种类对应数量
ic(colors1)
ic(colors2)

def title_color():
    c = (
        Pie(init_opts=opts.InitOpts(chart_id=40, bg_color='#ADD8E6'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="----------手机颜色最受欢迎图----------",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=36, color='#000000'),
                                      pos_left='center',
                                      pos_top='middle'))
    )
    return c


def funnnel_color():
    c = (
        Funnel(init_opts=opts.InitOpts(width="1600px", height="1000px",chart_id=41, bg_color='#ADD8E6'))
            .add(
            "颜色",
            [list(z) for z in zip(colors1, colors2)],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="手机颜色"))
    )
    return c

def pie_color():
    v = colors1
    c = (
        Pie(init_opts=opts.InitOpts(width="1600px", height="1000px",chart_id=42, bg_color='#ADD8E6'))
            .add(
            "",
            [list(z) for z in zip(v, colors2)],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add(
            "",
            [list(z) for z in zip(v, colors2)],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="手机颜色"))
    )
    return c


def bar_color():
    c = (
        Bar(init_opts=opts.InitOpts(width="1600px", height="1000px",chart_id=43, bg_color='#ADD8E6'))
            .add_xaxis(colors1)
            .add_yaxis("颜色", colors2, category_gap=0, color=Faker.rand_color())
            .set_global_opts(title_opts=opts.TitleOpts(title="手机颜色"))
    )
    return c

def line_color():
    c = (
        Line(init_opts=opts.InitOpts(width="1600px", height="1000px",chart_id=44, bg_color='#ADD8E6'))
            .add_xaxis(colors1)
            .add_yaxis(
            "颜色",
            colors2,
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="手机颜色"))
    )
    return c

def page_color():
    page = Page(layout=Page.DraggablePageLayout, page_title="网易手机颜色展示")
    page.add(
        title_color(),
        funnnel_color(),
        pie_color(),
        bar_color(),
        line_color()
    )
    page.render("手机颜色.html")
    page.save_resize_html('手机颜色.html', cfg_file='chart_config.json', dest='网易手机颜色展示图.html')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 会员等级
member = rcv_data['会员等级'].value_counts()
member1 = member.index.tolist()  # 内存种类
member2 = member.tolist()  # 内存种类对应数量
ic(member1)
ic(member2)


if __name__ == "__main__":
    #page_default_layout()
    #page_pingfen()
    #page_dates()
    #page_storage()
    #page_color()
    visual_ciyun()
