'''
https://www.gaoding.com/api/aggregate/search?q=&page_size=120&page_num=2&design_cid=&channel_cid=&industry_cid=&filter_id=1612599&type_filter_id=1612599&channel_filter_id=&channel_children_filter_id=&sort=&styles=&colors=&ratios=
https://www.gaoding.com/api/aggregate/search?q=&page_size=120&page_num=4&design_cid=&channel_cid=&industry_cid=&filter_id=1612599&type_filter_id=1612599&channel_filter_id=&channel_children_filter_id=&sort=&styles=&colors=&ratios=

'''
import requests
from fake_useragent import UserAgent
import os
import shutil
import uuid

headers = {
        'referer': 'https://www.gaoding.com/templates/pn4-f1612599',
        'user-agent': str(UserAgent().random)
    }

def spider_page():
    url_list = []
    for page in range(1, 5+1):
        print(f'----------正在下载第{page}页数据----------')
        url = f'https://www.gaoding.com/api/aggregate/search?q=&page_size=120&page_num={page}&design_cid=&channel_cid=&industry_cid=&filter_id=1612599&type_filter_id=1612599&channel_filter_id=&channel_children_filter_id=&sort=&styles=&colors=&ratios='
        resp = requests.get(url, headers = headers)

        if resp.status_code == requests.codes.ok:
            pic_list = resp.json()['searchMaterials']['nodes']

            for item in pic_list:
                urls = item['preview']['url']
                url_list.append(urls)
    return url_list

# 图片保存路径
pic_path = './pictures'

def down_pic(urls):
    # 判断文件夹是否存在
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    else:
        # 判断文件夹是否为空
        shutil.rmtree(pic_path)
        os.mkdir(pic_path)

    count = 1
    for url in urls:
        r = requests.get(url, headers = headers)
        try:
            with open(f'./pictures/{uuid.uuid4()}.gif', 'wb')as fin:
                print(f'正在爬取第{count}张图片')
                fin.write(r.content)
                print(f'{uuid.uuid4()}.gif----下载成功')
        except:
            print('下载失败！')
        count += 1

if __name__ == '__main__':
    data = spider_page()
    down_pic(data)


