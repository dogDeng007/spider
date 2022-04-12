# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelSummerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    travel_city = scrapy.Field()        #热门城市

    travel_numb = scrapy.Field()      # 旅游人数

    travel_hot = scrapy.Field()     # 热门景点

    travel_url = scrapy.Field()     # 城市详情页面地址
