import json

import requests
import re
import time
import csv
import prettytable as pt

# 数据保存
f = open('疫情.csv', mode='a', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
        '地区',
        '时间',
        '新增人数',
        '现有确诊人数',
        '累计确诊',
        '治愈人数',
        '死亡人数'
    ])
# 写入表格
csv_writer.writeheader()

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4878.0 Safari/537.36',
    'referer': 'https://www.baidu.com/s?wd=%E7%96%AB%E6%83%85&rsv_spt=1&rsv_iqid=0xadf826fc00082fff&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=88093251_25_hao_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=9&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E7%2596%25AB%25E6%2583%2585&rsp=9&inputT=1784&rsv_sug4=2658',
    'cookie': 'BIDUPSID=440C06166811E5AD2190E15C51179ACA; PSTM=1645842712; BAIDUID=440C06166811E5AD0730BE539F645BA7:FG=1; __yjs_duid=1_6b5001b3a0fe17d4f003e18310defc131645862847829; BDUSS=dKRU9veXRLaEdKdzM4enJGbzNqTUZUZHhRc0h3UTR2bG04clVWdUM3VlBsMFppRVFBQUFBJCQAAAAAAAAAAAEAAAAKdUtVsrvC9MPItcS1y7~PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE8KH2JPCh9iY0; BDUSS_BFESS=dKRU9veXRLaEdKdzM4enJGbzNqTUZUZHhRc0h3UTR2bG04clVWdUM3VlBsMFppRVFBQUFBJCQAAAAAAAAAAAEAAAAKdUtVsrvC9MPItcS1y7~PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE8KH2JPCh9iY0; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; BDRCVFR[30tQLoY7sAT]=mk3SLVN4HKm; H_PS_PSSID=31660_26350; delPer=0; PSINO=3; BAIDUID_BFESS=6515A046E87A4C858219EDD039A117F2:FG=1; BDRCVFR[RB6UgyQ9j86]=mk3SLVN4HKm; BA_HECTOR=8g0g2h25ah8025811p1h2l4bv0q; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1646871791,1646956932; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1646956932',
}

html_data = requests.get(url).text
# 字符串->列表
component = re.findall('"component":\[(.*)\],', html_data)[0]
# 列表->json
json_data = json.loads(component)
caselist = json_data['caseList']

# 格式化数据
tb = pt.PrettyTable()
tb.field_names = ['地区', '时间', '新增人数', '现有确诊人数', '累计确诊', '治愈人数', '死亡人数']

for case in caselist:
    area = case['area']         # 地区
    relativeTime = int(case['relativeTime'])     # 时间
    content_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(relativeTime))
    nativeRelative = case['confirmedRelative']  # 新增人数
    curConfirm = case['curConfirm']  # 现有确诊人数
    confirmed = case['confirmed']  # 累计确诊
    crued = case['crued']  # 治愈人数
    died = case['died']         # 死亡人数

    dit = {
            '地区': area,
            '时间': content_time,
            '新增人数': nativeRelative,
            '现有确诊人数': curConfirm,
            '累计确诊': confirmed,
            '治愈人数': crued,
            '死亡人数': died
            }
    csv_writer.writerow(dit)
    tb.add_row([area, content_time, nativeRelative, curConfirm, confirmed, crued, died])
print(tb)









