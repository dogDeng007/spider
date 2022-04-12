import requests
import re
from fake_useragent import UserAgent
import pandas as pd
import jieba
from stylecloud import gen_stylecloud
from wordcloud import WordCloud
from imageio import imread

headers = {
        'cookie': 'SUB=_2A25NyTOqDeRhGeVG7lAZ9S_PwjiIHXVvMl3irDV6PUJbktB-LVDmkW1NT7e8qozwK1pqWVKX_PsKk5dhdCyPXwW1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGibRIp_iSfMUfmcr5kb295NHD95Q01h-E1h-pe0.XWs4DqcjLi--fi-2Xi-2Ni--fi-z7iKysi--Ri-8si-zXi--fi-88i-zce7tt; _T_WM=98961943286; MLOGIN=1; WEIBOCN_FROM=1110006030; XSRF-TOKEN=70a1e0; M_WEIBOCN_PARAMS=oid%3D4648381753067388%26luicode%3D20000061%26lfid%3D4648381753067388%26uicode%3D20000061%26fid%3D4648381753067388',
        'referer': 'https://m.weibo.cn/detail/4648381753067388/',
        'user-agent': str(UserAgent().random)
    }

page = 0
def spider_wb():
    global max_id, page, ping_sum
    print(f'----------正在打印第{page + 2}页数据----------')
    if page > 14:
        max_id_type = 1
    else:
        max_id_type = 0
    url = f'https://m.weibo.cn/comments/hotflow?id=4650286486390483&mid=4650286486390483&max_id={max_id}&max_id_type={max_id_type}'
    print('当前url是：', url)

    resp = requests.get(url, headers=headers)
    print(resp)
    if resp.status_code == 200:
        comments = resp.json()

        if comments['ok'] == 1:
            max_id = comments['data']['max_id']
            wb_info = comments['data']['data']
            for item in wb_info:
                user_id = item.get('user')['id']  # 用户id

                author = item['user']['screen_name']  # 作者名称

                auth_sign = item['user']['description']  # 作者座右铭

                time = str(item['created_at']).split(' ')[1:4]
                rls_time = '-'.join(time)  # 发帖时间

                text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))  # 发帖内容

                print(user_id, author, auth_sign, rls_time, text)

                with open('./打针.csv', 'a+', encoding='utf-8') as f:
                    f.write(text + '\n')
            page += 1


# 爬虫可视化分析
def cut_word():
    with open('打针.csv',encoding='gbk')as file:
        comment_text = file.read()
        wordlist = jieba.lcut_for_search(comment_text)
        new_wordlist = ' '.join(wordlist)
        return new_wordlist

def create_word_cloud():
    mask = imread('3.jpg')
    wordcloud = WordCloud(font_path='msyh.ttc',mask = mask).generate(cut_word())
    wordcloud.to_file('picture2.png')
    print('绘图成功！')

if __name__ == '__main__':
    #create_word_cloud()

    # 爬取第一页
    print(f'----------正在打印第1页数据----------')
    url = 'https://m.weibo.cn/comments/hotflow?id=4650286486390483&mid=4650286486390483&max_id_type=0'
    print('当前url是：', url)
    resp = requests.get(url, headers=headers).json()
    print(resp)
    wb_info = resp['data']['data']
    for item in wb_info:
        user_id = item.get('user')['id']  # 用户id

        author = item['user']['screen_name']  # 作者名称

        auth_sign = item['user']['description']  # 作者座右铭

        time = str(item['created_at']).split(' ')[1:4]
        rls_time = '-'.join(time)  # 发帖时间

        text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))  # 发帖内容

        print(user_id, author, auth_sign, rls_time, text)
        with open('./打针.csv', 'a+', encoding='utf-8') as f:
            f.write(text + '\n')

    # 爬取第一页往后
    max_id = resp['data']['max_id']
    for i in range(2, 50+1):
        spider_wb()

