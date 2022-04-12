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
rcv_data = pd.read_excel('./出生率.xlsx')

# 删除重复记录
rcv_data = rcv_data.drop_duplicates()
# 删除缺失值
rcv_data = rcv_data.dropna()

# 抽样展示5条数据
print(rcv_data.sample(5))

# 获取列内容
c_title = rcv_data['发帖内容'].tolist()
# 观影评论词云图
wordlist = jieba.cut(''.join(c_title))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['的', '了', '我', '也', '都', '是', '吧', '不', '吗', '还', '就', '在', '人', '没', '年', '啊', '说', '这', '好', '你', '会', '有', '才', '不是', '现在', '一个', '什么', '继续', '自己', '这个', '就是', ]

# 词云展示
def visual_ciyun():
    pic = './img.jpg'
    gen_stylecloud(text=result,
                   icon_name='fas fa-phone',
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

if __name__ == '__main__':
    visual_ciyun()
    visual_cipin()