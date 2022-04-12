'''
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=0&objecttype=album&page=1&count=20
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page=3&count=20
https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page=4&count=20
'''

import requests
from fake_useragent import UserAgent

url = 'https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page=1&count=20'

headers = {
        'referer': 'https://www.hanfuhui.com/',
        'User-Agent': str(UserAgent().random)
    }

resp = requests.get(url, headers = headers, verify=False)

if resp.status_code == 200:
    girl_list = resp.json()['Data']
    NickName = [item['User']['NickName'] for item in girl_list]
    NickName = '\n'.join(NickName)
    info = []
    for item in girl_list:
        info.extend(item['ImageSrcs'])
    srcs = '_700x.jpg\n'.join(info)
    print(type(srcs))
    print(type(NickName))
'''
    for name, pic in zip(NickName, srcs):
        res = requests.get(srcs, headers = headers, verify=False)
        data = res.content
        with open(f'./pictures/{NickName}.jpg', 'wb+', encoding = 'utf-8') as fin:
            fin.write(data)
            print('下载完成！')'''