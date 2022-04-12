# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from travel_summer.settings import *

class TravelSummerPipeline:

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = mongo_db_collection
        client = pymongo.MongoClient(host=host, port = port)
        db = client[dbname]
        self.post = db[collection]


    def process_item(self, item, spider):
        print(item['travel_city'], item['travel_numb'], item['travel_hot'], item['travel_url'])

        data = dict(item)
        self.post.insert(data)
        return item
