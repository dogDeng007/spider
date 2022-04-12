import pandas as pd
import jieba
from stylecloud import gen_stylecloud
from collections import Counter
from imageio import imread
from icecream import ic
from wordcloud import WordCloud
from snownlp import SnowNLP

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据

# 读取数据
rcv_data = pd.read_excel('./王力宏.xlsx')

# 删除重复记录
rcv_data = rcv_data.drop_duplicates()
# 删除缺失值
rcv_data = rcv_data.dropna()

# 抽样展示5条数据
#print(rcv_data.sample(5))

# 获取列内容
c_title = rcv_data['发帖内容'].tolist()
# 观影评论词云图
wordlist = jieba.cut(''.join(c_title))
result = ' '.join(wordlist)

# 设置停用词
stop_words = ['都', '我', '了', '的', '是', '他', '你', '有', '啊', '就', '吧', '不', '人', '还', '这', '事', '也', '没', '吗',
              '知道', '男人', '这么', '就是', '一个', '好', '说', '太', '要', '给', '对', '很', '和', '又', '在', '一直', '自己', '真的', '这个']

# 词云展示
def visual_ciyun():
    pic = './img.jpg'
    gen_stylecloud(text=result,
                   icon_name='fas fa-fish',
                   font_path='msyh.ttc',
                   background_color='white',
                   output_name=pic,
                   custom_stopwords=stop_words
                   )
    print('词云图绘制成功！')

def visual_ciyun1():
    mask = imread('wlh.jpg')
    wordcloud = WordCloud(font_path='msyh.ttc', mask = mask, stopwords=stop_words, background_color='white').generate(result)
    wordcloud.to_file('pic.jpg')
    print('词云图1绘制成功！')


def visual_cipin():
    # 词频设置
    all_words = [word for word in result.split(' ') if len(word) > 1 and word not in stop_words]
    wordcount = Counter(all_words).most_common(10)

    x1_data, y1_data = list(zip(*wordcount))
    #print(x1_data)
    #print(y1_data)


def datas_anay():
    max_stars = rcv_data[rcv_data['点赞人数'] == rcv_data['点赞人数'].max()]
    ic(max_stars)


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
    visual_ciyun()
    visual_ciyun1()
    #visual_cipin()
    datas_anay()
    anay_data()