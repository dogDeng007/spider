import scrapy
from travel_summer.items import TravelSummerItem

class SpiderTravelSpider(scrapy.Spider):
    name = 'spider_travel'
    allowed_domains = ['place.qyer.com/china/citylist-0-0-1/']
    start_urls = ['https://place.qyer.com/china/citylist-0-0-1/']

    def start_requests(self):
        for page in range(1, 50 + 1):
            url = f'https://place.qyer.com/china/citylist-0-0-{page}'
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):

        now_page = response.xpath("//a[@class='ui_page_item ui_page_item_current']/text()").get()
        print(f'--------正在爬取第{now_page}页数据--------')

        # 实例化item对象
        item = TravelSummerItem()

        lis = response.xpath("//ul[@class='plcCitylist']/li")
        print(len(lis))

        for li in lis:

            item['travel_city'] = li.xpath('./h3/a/text()').get()   # 城市名称

            item['travel_numb'] = li.xpath('./p[2]/text()').get()   # 旅游人数

            travel_hot = li.xpath('./p[@class = "pois"]/a/text()').getall()      # 热门城市
            travel_hot = [hot.strip() for hot in travel_hot]
            item['travel_hot'] = '、'.join(travel_hot)       # join()合并列表对象

            travel_url = li.xpath('./h3/a/@href').get()
            item['travel_url'] = 'https:' + travel_url           # 城市详情页面地址

            yield item