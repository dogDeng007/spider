import pandas as pd
import jieba.analyse
from stylecloud import gen_stylecloud

# 读取文件
pd_data = pd.read_excel('鸿星尔克.xlsx')
exist_col = pd_data.dropna()  # 删除空行

# 读取内容
text = exist_col['发帖内容'].tolist()

# 切割分词
wordlist = jieba.cut_for_search(''.join(text))
result = ' '.join(wordlist)

gen_stylecloud(text=result,
                icon_name='fas fa-cloud-rain',
                font_path='msyh.ttc',
                background_color='white',
                output_name='666.jpg',
                custom_stopwords=['你', '我', '的', '了', '在', '吧', '相信', '是', '也', '都', '不', '吗', '就', '我们', '还', '大家', '你们', '就是', '以后']
               )
print('绘图成功！')


'''# 读取图片
im = cv2.imread('11.jpg')
# 设置参数，创建WordCloud对象
wc = WordCloud(
    font_path='msyh.ttc',       # 中文
    background_color='white',    # 设置背景颜色为白色
    stopwords=stop_words,        # 设置禁用词，在生成的词云中不会出现set集合中的词
    mask=im
)
# 根据文本数据生成词云
wc.generate(ciyun_words)
# 保存词云文件
wc.to_file('img.jpg')'''








