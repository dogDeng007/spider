'''
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=0&objecttype=album&page=1&count=20
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page=3&count=20
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page=4&count=20
'''

import requests
from fake_useragent import UserAgent
import os
import shutil
import time

headers = {
        'referer': 'https://www.hanfuhui.com/',
        'User-Agent': str(UserAgent().random)
    }

def run(url):
    try:
        res = requests.get(url=url, headers=headers)
        # 直接通过 res.json 方法获取到 JSON 格式数据
        json_text = res.json()
        # 访问 JSON 中的特定对象，这里没有对接口数据进行验证，如有必要，请通过 Status 属性进行接口请求状态验证
        data = json_text["Data"]
        img_srcs = []
        for item in data:
            img_srcs.extend(item["ImageSrcs"])
        long_str = "\n".join(img_srcs)
        print(long_str)
        # 保存数据
        save(long_str)

    except Exception as e:
        print(e)


def save(long_str):
    try:
        with open(f"./imgs.csv", "a+") as f:
            f.write("\n"+long_str)
    except Exception as e:
        print(e)

def save_img(img_src):
    try:
        url = img_src
        # 注意 verify 参数设置为 False ，不验证网站证书
        res = requests.get(url=url, headers=headers, verify=False)
        data = res.content

        with open(f"./hanfu/{int(time.time())}.jpg", "wb+") as f:
            f.write(data)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    run('https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=0&objecttype=album&page=1&count=20')