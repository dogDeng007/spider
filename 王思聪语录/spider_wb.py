'''
https://m.weibo.cn/comments/hotflow?id=4648381753067388&mid=4648381753067388&max_id_type=0
id: 4648381753067388
mid: 4648381753067388
max_id_type: 0
max_id: 142838039062228


https://m.weibo.cn/comments/hotflow?id=4648381753067388&mid=4648381753067388&max_id=142838039062228&max_id_type=0
id: 4648381753067388
mid: 4648381753067388
max_id: 142838039062228
max_id_type: 0
max_id: 139539503327152

https://m.weibo.cn/comments/hotflow?id=4648381753067388&mid=4648381753067388&max_id=139539503327152&max_id_type=0
id: 4648381753067388
mid: 4648381753067388
max_id: 139539503327152
max_id_type: 0
max_id: 139264625624790
'''

#https://m.weibo.cn/detail/4648411616512135

import requests
from fake_useragent import UserAgent
import re

headers = {
    'cookie': 'SUB=_2A25NyTOqDeRhGeVG7lAZ9S_PwjiIHXVvMl3irDV6PUJbktB-LVDmkW1NT7e8qozwK1pqWVKX_PsKk5dhdCyPXwW1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGibRIp_iSfMUfmcr5kb295NHD95Q01h-E1h-pe0.XWs4DqcjLi--fi-2Xi-2Ni--fi-z7iKysi--Ri-8si-zXi--fi-88i-zce7tt; _T_WM=98961943286; MLOGIN=1; WEIBOCN_FROM=1110006030; XSRF-TOKEN=70a1e0; M_WEIBOCN_PARAMS=oid%3D4648381753067388%26luicode%3D20000061%26lfid%3D4648381753067388%26uicode%3D20000061%26fid%3D4648381753067388',
    'referer': 'https://m.weibo.cn/detail/4648381753067388/',
    'user-agent': str(UserAgent().random)
}

# 获取第一页内容
def spider_wb(url):
    param = {
        'id': 4648381753067388,
        'mid': 4648381753067388,
        'max_id_type': 0
    }
    resp = requests.get(url = url, headers = headers, params = param)

    try:
        if resp.status_code == 200:
            return resp.json()
        else:
            print('something wrong~~~')
    except:
        return None

# 解析首页内容并获取max_id
def parse_wb(datas):
    wb_info = datas['data']['data']

    for item in wb_info:
        user_id = item.get("user")["id"]  # 用户id

        author = item['user']['screen_name']  # 作者名称

        auth_sign = item['user']['description']  # 作者座右铭

        time = str(item['created_at']).split(' ')[1:4]
        rls_time = '-'.join(time)  # 发帖时间

        text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))  # 发帖内容

        print(user_id, author, auth_sign, rls_time, text)

    max_id = datas['data']['max_id']
    return max_id

def spider_nextPage(max_id):

    param = {
        'id': 4648381753067388,
        'mid': 4648381753067388,
        'max_id': max_id,
        'max_id_type': 0
    }

    url = f'https://m.weibo.cn/comments/hotflow?id=4648381753067388&mid=4648381753067388&max_id={max_id}&max_id_type=0'

    response = requests.get(url = url, headers = headers, params = param).json()
    wb_info = response['data']['data']

    for item in wb_info:

        user_id = item.get("user")["id"]  # 用户id

        author = item['user']['screen_name']  # 作者名称

        auth_sign = item['user']['description']  # 作者座右铭

        time = str(item['created_at']).split(' ')[1:4]
        rls_time = '-'.join(time)  # 发帖时间

        text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))  # 发帖内容

        print(user_id, author, auth_sign, rls_time, text)
    max_id = response['data']['max_id']


    spider_nextPage(max_id)

if __name__ == '__main__':
    url = 'https://m.weibo.cn/comments/hotflow?id=4648381753067388&mid=4648381753067388&max_id_type=0'
    datas = spider_wb(url)

    max_id = parse_wb(datas)

    spider_nextPage(max_id)


