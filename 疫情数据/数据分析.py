import pandas as pd
from pyecharts.charts import Bar, Line, Page, Pie
from pyecharts import options as opts
from pyecharts.charts import Map

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

# 读取数据
rcv_data = pd.read_csv('疫情.csv', encoding='gbk')

# 抽样展示
print(rcv_data.sample(5))

'''
x_data = rcv_data['地区'].values.tolist()
y_data = rcv_data['新增人数'].values.tolist()
'''
x_data = rcv_data['地区'].values.tolist()
y_data = rcv_data['死亡人数'].values.tolist()


print(x_data)
print(y_data)


def bar_datazoom_slider() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(bg_color='#ADD8E6'))
        .add_xaxis(x_data)
        .add_yaxis("死亡人数", y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="死亡人数柱状图"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(bg_color='#ADD8E6'))
        .add_xaxis(x_data)
        .add_yaxis(
            "死亡人数",
            y_data,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="死亡人数折线图"))
    )
    return c

def pie_markpoint() -> Line:
    c = (
        Pie(init_opts=opts.InitOpts(bg_color='#ADD8E6'))
            .add(
            "",
            [list(z) for z in zip(x_data, y_data)],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="死亡人数饼图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c



def table_base() -> Bar:
    c = (
        Map(init_opts=opts.InitOpts(bg_color='#ADD8E6'))
            .add("死亡人数", [list(z) for z in zip(x_data, y_data)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="死亡人数"),
            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),
        )
    )
    return c


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_markpoint(),
        table_base(),
    )
    page.render("死亡人数页面.html")


if __name__ == "__main__":
    page_simple_layout()
