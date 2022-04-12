import scrapy
from icecream import ic
from wangyi.items import WangyiItem
import time

'''
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1632473177210&itemId=3999301&tag=%E5%85%A8%E9%83%A8&size=20&page=1&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1632473070850&itemId=3999301&tag=%E5%85%A8%E9%83%A8&size=20&page=2&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1632473139434&itemId=3999301&tag=%E5%85%A8%E9%83%A8&size=20&page=3&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0
'''
class SpiderWySpider(scrapy.Spider):
    name = 'spider_wy'
    allowed_domains = ['you.163.com/']
    start_urls = ['http://you.163.com//']

    def start_requests(self):
        for page in range(1, 5 + 1):
            url = f'http://you.163.com/xhr/comment/listByItemByTag.json?__timestamp=1632473177210&itemId=3999301&tag=%E5%85%A8%E9%83%A8&size=20&page={page}&orderBy=0&oldItemTag=%E5%85%A8%E9%83%A8&oldItemOrderBy=0&tagChanged=0'
            print(url)
            print(f'------------------正在抓取第{page}页数据------------------')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #ic(response.json())

        # 实例化对象
        item = WangyiItem()

        # 获取浏览器响应信息
        phone_info = response.json()

        phone_list = phone_info['data']['commentList']
        # ic(phone_list)

        # 打印所需信息
        for phone in phone_list:

            # 名称
            item['name'] = phone['frontUserName']

            # 等级
            item['level'] = phone['memberLevel']

            # 评分
            item['star'] = phone['star']

            # 时间
            rls_time = phone['createTime']
            item['rls_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(rls_time/1000)).split(' ')[0]

            # 颜色
            item['color'] = phone['skuInfo'][0].split(':')[1]

            # 内存
            item['storage'] = phone['skuInfo'][1].split(':')[1]

            # 评论
            item['content'] = phone['content']

            yield item