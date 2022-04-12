# encoding:utf-8
import os
from tqdm import tqdm
import requests
from icecream import ic
import base64

'''# 读取一张图片
f = open('pictures\\Cic小野猫.jpg', mode='rb')
# 转base64
img_base64 = base64.b64encode(f.read())

'''
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GD9bcCHcQETq37OdxwImqH6X&client_secret=tbtX8c5GG7BGkSXe874LLVtaOi3exAQN'
response = requests.get(host)
token = response.json()['access_token']
ic(token)

import requests

'''
人脸检测与属性分析
'''
def get_beauty(img_base64):
    request_url = f"https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token={token}" # 传入获取到的token值

    params = {
        'image': img_base64,  # 读取图片
        'image_type': 'BASE64',
        'face_field': 'beauty',
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    try:
        beauty = response.json()['result']['face_list'][0]['beauty']
        return beauty
    except:
        return '人脸识别失败！'
lis = []
files = os.listdir('pictures\\')
print('正在识别人脸，颜值检测中......')
for file in tqdm(files[:30]):
    img_file = 'pictures\\' + file
    img_name = file.split('.')[0]
    f = open(img_file, mode='rb')
    # 转base64
    img_base64 = base64.b64encode(f.read())
    # 调用评分函数
    beauty = get_beauty(img_base64)
    # 颜值排名
    if beauty != '人脸识别失败！':
        dit = {
            '主播': img_name,
            '颜值': beauty
        }
        # 字典添加到空列表
        lis.append(dit)

lis.sort(key=lambda x:x['颜值'], reverse=True)
num = 1
for index in lis:
    print(f'颜值排名第{num}的主播{index["主播"]},颜值评分是{index["颜值"]}')
    num += 1
