# -*- coding: utf-8 -*-
# Date: 2021/12/2 10:00
# Author: 不卖萌的邓肯
# wechat: 印象python

import requests
import re, os
import jieba
from wordcloud import WordCloud
from imageio import imread

comment_file_path = 'B站弹幕1.csv'

def spider_page(cid):
    url = f'http://comment.bilibili.com/{cid}.xml'

    headers = {
        'referer': 'xxxxx',
        'User-Agent': 'xxxxx',
        'cookie': "xxxxx"
     }

    resp = requests.get(url, headers = headers)
    # 调用.encoding属性获取requests模块的编码方式
    # 调用.apparent_encoding属性获取网页编码方式
    # 将网页编码方式赋值给response.encoding
    resp.encoding = resp.apparent_encoding

    print(resp.text)

    if resp.status_code == 200:
        # 获取所有评论内容
        content_list = re.findall('<d p=".*?">(.*?)</d>', resp.text)

        if os.path.exists(comment_file_path):
            os.remove(comment_file_path)
        for item in content_list:

            with open(comment_file_path, 'a', encoding = 'utf-8')as fin:
                fin.write(item + '\n')
                print(item)
        print('-------------弹幕获取完毕！-------------')

def data_visual():
    with open(comment_file_path, encoding='utf-8')as file:
        comment_text = file.read()
        wordlist = jieba.lcut_for_search(comment_text)
        new_wordlist = ' '.join(wordlist)
        mask = imread('img_1.png')
        wordcloud = WordCloud(font_path='msyh.ttc', mask=mask).generate(new_wordlist)
        wordcloud.to_file('picture_1.png')

if __name__ == '__main__':
    cid = '512470713'
    print('正在解析，开始爬取弹幕中。。。。。')
    spider_page(cid)
    #data_visual()