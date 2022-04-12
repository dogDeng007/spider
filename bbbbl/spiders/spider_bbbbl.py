import scrapy
from bbbbl.items import BbbblItem
import time
from icecream import ic

'''
https://api.bilibili.com/x/web-interface/search/type?context=&page=2&order=&keyword=%E5%B0%8F%E5%A7%90%E5%A7%90&duration=&tids_1=&tids_2=&from_source=webtop_search&from_spmid=333.1007&platform=pc&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0
https://api.bilibili.com/x/web-interface/search/type?context=&page=3&order=&keyword=%E5%B0%8F%E5%A7%90%E5%A7%90&duration=&tids_1=&tids_2=&from_source=webtop_search&from_spmid=333.1007&platform=pc&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0
https://api.bilibili.com/x/web-interface/search/type?context=&page=3&order=&keyword=%E5%B0%8F%E5%A7%90%E5%A7%90&duration=&tids_1=&tids_2=&from_source=webtop_search&from_spmid=333.1007&platform=pc&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0
'''


class SpiderBbbblSpider(scrapy.Spider):
    name = 'spider_bbbbl'
    allowed_domains = ['search.bilibili.com']
    start_urls = ['http://search.bilibili.com/']

    def start_requests(self):
        for page in range(1, 5+1):
            url = f'https://api.bilibili.com/x/web-interface/search/type?context=&page={page}&order=&keyword=%E5%B0%8F%E5%A7%90%E5%A7%90&duration=&tids_1=&tids_2=&from_source=webtop_search&from_spmid=333.1007&platform=pc&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0'
            #print(url)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # 实例化item对象
        item = BbbblItem()

        ic(response.text)
        bl_list = response.json()['data']['result']

        for bl in bl_list:

            # 视频标题
            item['title_video'] = bl['title']

            # 视频时长
            item['time_video'] = bl['duration']

            # 视频播放量
            item['num_video'] =bl['video_review']

            # 发布时间
            date_rls = bl['pubdate']
            item['date_rls'] = time.strftime('%Y-%m-%d %H:%M', time.localtime(date_rls))

            # 视频作者
            item['author'] = bl['author']

            # 图片链接
            link_pic = bl['pic']
            item['link_pic'] = 'https:'+link_pic

            # 视频链接
            item['link_video'] = bl['arcurl']

            yield item
