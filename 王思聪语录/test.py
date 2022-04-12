import requests
import pandas as pd
from time import sleep


header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Content-Type":"application/json; charset=utf-8"
}
cookie = {
    'cookie': 'SUB=_2A25NyTOqDeRhGeVG7lAZ9S_PwjiIHXVvMl3irDV6PUJbktB-LVDmkW1NT7e8qozwK1pqWVKX_PsKk5dhdCyPXwW1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFGibRIp_iSfMUfmcr5kb295NHD95Q01h-E1h-pe0.XWs4DqcjLi--fi-2Xi-2Ni--fi-z7iKysi--Ri-8si-zXi--fi-88i-zce7tt; _T_WM=98961943286; MLOGIN=1; WEIBOCN_FROM=1110006030; XSRF-TOKEN=70a1e0; M_WEIBOCN_PARAMS=oid%3D4648381753067388%26luicode%3D20000061%26lfid%3D4648381753067388%26uicode%3D20000061%26fid%3D4648381753067388',
}
max_id = ""
max_id_type = 0
while True:
    if max_id == "":
        url = "https://m.weibo.cn/comments/hotflow?id=4623286263356667&mid=4623286263356667&max_id_type=0"
    else:
        url = "https://m.weibo.cn/comments/hotflow?id=4623286263356667&mid=4623286263356667&max_id={}&max_id_type={}".format(max_id,max_id_type)

    res = requests.get(url,headers=header,cookies=cookie)
    commont = res.json()
    if commont['ok'] == 0:
        break
    max_id = commont['data']['max_id']
    max_id_type = commont['data']['max_id_type']
    for commontData in commont['data']['data']:
        print(commontData)
        data = [(commontData['user']['screen_name'],commontData['text'])]
        data = pd.DataFrame(data)
        data.to_csv("sina.csv",header=False,index=False,mode="a+")
    sleep(1)