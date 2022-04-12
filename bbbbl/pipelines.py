# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl as op
import pymysql
from icecream import ic
import json
import os
import requests
import time,  random

class BbbblPipeline:

    def process_item(self, item, spider):

        print(item)
        # 保存文件到本地
        with open('../B站小姐姐.json', 'a+', encoding='utf-8') as f:
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(lines)

        # 检查路径
        if not os.path.exists('images'):
            os.mkdir('images')

        # 保存图片到本地
        with open('images/{}.jpg'.format(item['title_video']), 'wb') as f:
            req = requests.get(item['link_pic'])
            f.write(req.content)
            time.sleep(random.random() * 4)

        return item

class ExcelPipeline:

    def __init__(self):
        self.wb = op.Workbook()
        self.ws = self.wb.active
        self.ws.append(['视频标题', '视频时长', '视频播放量', '发布时间', '视频作者', '图片链接', '视频链接'])

    def process_item(self, item, spider):
        line = [item['title_video'], item['time_video'], item['num_video'], item['date_rls'], item['author'], item['link_pic'],item['link_video']]
        self.ws.append(line)
        self.wb.save('../B站小姐姐.xlsx')
        print('Excel数据成功保存！')
        return item

class MysqlPipeline():

    def __init__(self):
        username = "root"
        password = "211314"
        dbname = "BLBL"
        host = "localhost"
        self.db = pymysql.connect(charset='utf8', host=host, user=username, password=password, database=dbname)

    def open_spider(self, spider):
        cursor = self.db.cursor()
        cursor.execute('drop table if exists bbbbl3')
        sql = '''
                CREATE TABLE bbbbl3
                (id int primary key auto_increment
                , title_video  VARCHAR(200) NOT NULL
                , time_video  VARCHAR(100)
                , num_video  INTEGER
                , date_rls  VARCHAR(100)
                , author  VARCHAR(100)
                , link_pic  VARCHAR(1000)
                , link_video VARCHAR(1000)
                );
            '''
        cursor.execute(sql)

    def process_item(self, item, spider):
        try:
            cursor = self.db.cursor()
            value = (item["title_video"], item["time_video"], item["num_video"], item["date_rls"], item["author"], item["link_pic"], item["link_video"])
            sql = "insert into bbbbl3(title_video,time_video,num_video,date_rls,author,link_pic,link_video) value (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, value)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            print("存储失败", e)
        return item

    def close_spider(self, spider):
        print('数据插入已成功！')
        self.db.close()



