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
from snownlp import SnowNLP

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

# 读取数据
rcv_data = pd.read_excel('./结婚率.xlsx')

# 删除重复记录
rcv_data = rcv_data.drop_duplicates()
# 删除缺失值
rcv_data = rcv_data.dropna()

# 抽样展示5条数据
print(rcv_data.sample(5))

# 获取列内容
c_title = rcv_data['评论内容'].tolist()
# 观影评论词云图
wordlist = jieba.cut(''.join(c_title))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['的', '了', '不', '就', '我', '都', '没', '有', '吗', '少', '也', '人', '还', '在', '这', '对', '啊', '是', '多', '好', '和', '要', '没有', '自己', '下降', '谁',
              '吧', '年', '会', '想', '一个', '呢', '你', '什么', '现在', '就是', '还是', '不是', '',  '问题', '捂脸', '年轻人',]

# 词云展示
def visual_ciyun():
    pic = './img.jpg'
    gen_stylecloud(text=result,
                   icon_name='fas fa-feather-alt',
                   font_path='msyh.ttc',
                   background_color='white',
                   output_name=pic,
                   custom_stopwords=stop_words
                   )
    print('词云图绘制成功！')

def visual_cipin():
    # 词频设置
    all_words = [word for word in result.split(' ') if len(word) > 1 and word not in stop_words]
    wordcount = Counter(all_words).most_common(10)

    x1_data, y1_data = list(zip(*wordcount))
    print(x1_data)
    print(y1_data)

def datas_anay():
    max_stars = rcv_data[rcv_data['评论点赞'] == rcv_data['评论点赞'].max()]
    ic(max_stars)

    max_reply = rcv_data[rcv_data['贴子回复'] == rcv_data['贴子回复'].max()]
    ic(max_reply)


# 情感分析

def anay_data():
    all_words = [word for word in result.split(' ') if len(word) > 1 and word not in stop_words]
    positibe = negtive = middle = 0
    for i in all_words:
        pingfen = SnowNLP(i)
        if pingfen.sentiments > 0.7:
            positibe += 1
        elif pingfen.sentiments < 0.3:
            negtive += 1
        else:
            middle += 1
    print(positibe, negtive, middle)

if __name__ == '__main__':
    #visual_ciyun()
    #visual_cipin()
    datas_anay()
    anay_data()