# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BbbblItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 视频标题
    title_video = scrapy.Field()

    # 视频时长
    time_video = scrapy.Field()

    # 播放量
    num_video = scrapy.Field()

    # 发布时间
    date_rls = scrapy.Field()

    # 作者
    author = scrapy.Field()

    # 图片链接
    link_pic = scrapy.Field()

    # 视频地址
    link_video = scrapy.Field()




