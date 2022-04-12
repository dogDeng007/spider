'''
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856130970&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=1&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856339147&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=2&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856354947&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=3&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
'''
import requests
from fake_useragent import UserAgent
import time, random
from faker import Faker
from pyecharts.charts import Funnel, Page  # 各个图形的类
from pyecharts.charts import Line
import pandas as pd
import jieba
from stylecloud import gen_stylecloud
from pyecharts.charts import Bar,Pie
from pyecharts import options as opts

def spider_page():
    url = 'http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1624856130970&itemId=3987228&tag=%E5%85%A8%E9%83%A8&size=20&page=1&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0'

    headers = {
        'Cookie': '_ntes_nnid=501cb75ada402fbcf47eefe12cccc23a,1623327742969; _ntes_nuid=501cb75ada402fbcf47eefe12cccc23a; UM_distinctid=17a3365a7592d2-008996d874143d-5c4f2f15-1fa400-17a3365a75a526; hb_MA-8E16-605C3AFFE11F_source=www.baidu.com; yx_aui=6da18d10-f072-41ac-912f-b14dff79cbb9; mail_psc_fingerprint=66f4d93f8163fe521a151b828d49e1cd; yx_s_device=32d4255-6232-2537-51c2-4e819468e8; yx_but_id=d03335c54b02488a8507463681ed337bca142a4f6d33ff62_v1_nl; yx_s_tid=tid_web_38d7721d61b649199f8af09017ae76b3_d0a48cb2b_1; yx_search_history=%5B%22%u6587%u80F8%22%5D; yx_from=search_sem_bdpc_25; yx_show_painted_egg_shell=false; yx_delete_cookie_flag=true; yx_stat_seesionId=6da18d10-f072-41ac-912f-b14dff79cbb91624855735580; yx_new_user_modal_show=1; yx_page_key_list=http%3A//you.163.com/search%3Fkeyword%3D%25E6%2596%2587%25E8%2583%25B8%26timestamp%3D1624845943619%26_stat_search%3Dhistory%26searchWordSource%3D5%23page%3D1%26sortType%3D0%26descSorted%3Dtrue%26categoryId%3D0%26matchType%3D0%2Chttp%3A//you.163.com/item/detail%3Fid%3D3987228%26_stat_area%3D3%26_stat_referer%3Dsearch%26_stat_query%3D%25E6%2596%2587%25E8%2583%25B8%26_stat_count%3D132%26_stat_searchversion%3Ddcn_model-1.1.0-1.3; yx_subscribe_showtime=1624856134666; yx_stat_seqList=v_ecb98e3f92%7Cv_377304616a%3B-1%3Bv_780ef75480%3Bc_350809ccfe%3Bv_cf5074d5c0%3B-1%3Bv_ecb98e3f92%3B-1',
        'Referer': 'http://you.163.com/item/detail?id=3987228&_stat_area=3&_stat_referer=search&_stat_query=%E6%96%87%E8%83%B8&_stat_count=132&_stat_searchversion=dcn_model-1.1.0-1.3',
        'User-Agent': str(UserAgent().random)
    }

    resp = requests.get(url, headers = headers)

    if resp.status_code == 200:
        comts_List = resp.json()['data']['commentList']
        print('comts_List', comts_List)


        size = [item['skuInfo'][0] for item in comts_List]
        colors = [item['skuInfo'][1] for item in comts_List]
        prof_phot = [item['frontUserAvatar'] for item in comts_List]
        star = [item['star'] for item in comts_List]
        content = [item['content'] for item in comts_List]

        # 保存数据
        pd_data = pd.DataFrame({
            '型号': size,
            '颜色': colors,
            '小姐姐': prof_phot,
            '评分': star,
            '评论': content
        })

        pd.set_option('display.max_columns', None)  # 显示完整的列
        pd.set_option('display.max_rows', None)  # 显示完整的行
        pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
        return pd_data

fake = Faker(locale='zh_CN')

# 获取多页
def get_all_page(all_page_num):
    # 存储表
    df_all = pd.DataFrame()
    # 循环页数
    for page in range(all_page_num):
        # 打印进度
        print(f'-------------正在获取第{page + 1}页的文胸信息-------------')
        # 调用函数
        pd_data = spider_page()
        # 追加
        df_all = df_all.append(pd_data, ignore_index=True)
        # 随机休眠
        time.sleep(random.random()*4)

        count = 1
        for img in pd_data['小姐姐']:
            if img != None:
                try:
                    with open('./pictures/{}.jpg'.format(fake.name()), 'wb') as fin:
                        print(f'正在爬取第{count}张图片')
                        fin.write(requests.get(img).content)
                        print('{}.jpg----下载成功'.format(img))
                except:
                    print('下载失败！')
                count += 1

    df_all.to_excel('./小姐姐文胸.xlsx', index=False)

def ciyun():
    pd_data = pd.read_excel('./小姐姐文胸.xlsx')
    c_title = pd_data['评论'].tolist()
    # 观影评论词云图
    wordlist = jieba.cut(''.join(c_title))
    result = ' '.join(wordlist)
    pic = 'img.jpg'
    gen_stylecloud(text=result,
                   icon_name='fab fa-qq',  #s
                   font_path='msyh.ttc',
                   background_color="black",
                   output_name=pic)
    print('绘图成功！')


def size_analys():
    # 读取数据
    pd_data = pd.read_excel('./小姐姐文胸1.xlsx')
    # 去除不需要数据
    pd_data.loc[:, '型号new'] = pd_data['型号'].str.replace('尺码:', '')

    size = pd_data['型号new'].value_counts()

    # 型号分类
    size1 = size.index.tolist()
    # 分类数据统计
    size2 = size.tolist()
    print(size1)
    print(size2)

    return size1, size2

def color_analys():
    # 读取数据
    pd_data = pd.read_excel('./小姐姐文胸.xlsx')
    # 去除不需要数据
    pd_data.loc[:, '颜色new'] = pd_data['颜色'].str.replace('颜色:', '')

    color = pd_data['颜色new'].value_counts()

    # 型号分类
    color1 = color.index.tolist()
    # 分类数据统计
    color2 = color.tolist()
    print(color1)
    print(color2)

    return color1, color2


def data_visual():
    x_data, y_data = color_analys()

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
        Page(layout=Page.DraggablePageLayout).add(
            barPage(),
            piePage(),
            linePage(),
            funnelPage())
    )

    page.render("颜色信息展示.html")
    print('绘图完成！')

if __name__ == '__main__':
    get_all_page(100)
    #ciyun()
    #data_visual()
