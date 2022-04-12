import json
import time
import random

import requests

headers = {
    'cookie': ''
}

for i in range(6909, 40001, 5):
    url = f'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7031475732526255364&cursor={i}&count=5&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=92.0.4515.131&browser_online=true&engine_name=Blink&engine_version=92.0.4515.131&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&msToken=mQzVNZDLJ3LapBrq7uG29H_8g2T1Zido3DF9g66NQbIopQZM8rzpwodLl9OfpNHTJCln-ay1Oa8Rb61kQsY_QdOU0HuVqlHa7ordODy25aMz5LGoVDsceQ==&X-Bogus=DFSzsdVLYETANVGvSEvOYr7Tlqe5&_signature=_02B4Z6wo00001ZjsgAAAAIDCDDrbDeBRPsGY6ISAAAeMPBI21RrYQ-EFH9wOL5pd4496o70e.lVEOrrZ38vCtzDizxRV21.xY1ZY-8O76KuSxn5KZGgG6t7-dL8gLO6u1UeMoTy4p4WSRWOu53'
    out_dict = {}

    print(url)
    res = requests.get(url, headers=headers)
    res_json = res.json()
    with open(f'./cmts/{i}.txt', 'w') as f:
        for cmt in res_json['comments']:
            out_dict['create_time'] = cmt['create_time']
            out_dict['digg_count'] = cmt['digg_count']
            out_dict['text'] = cmt['text']
            out_dict['custom_verify'] = cmt['user']['custom_verify']
            out_dict['nickname'] = cmt['user']['nickname']

            f.write(json.dumps(out_dict, ensure_ascii=False))
            f.write('\r\n')

    sleep_ts = random.uniform(2, 5)
    print('sleep', sleep_ts)
    time.sleep(sleep_ts)
    print(i)
