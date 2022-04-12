# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 名称
    name = scrapy.Field()

    # 等级
    level = scrapy.Field()

    # 评分
    star = scrapy.Field()

    # 时间
    rls_time = scrapy.Field()

    # 颜色
    color = scrapy.Field()

    # 内存
    storage = scrapy.Field()

    # 评论
    content = scrapy.Field()