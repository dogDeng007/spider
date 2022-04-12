# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from icecream import ic
import openpyxl as op

class WangyiPipeline:
    def process_item(self, item, spider):
        ic(item)
        return item

class ExcelPipeline:

    def __init__(self):
        self.wb = op.Workbook()
        self.ws = self.wb.active
        self.ws.append(['用户名称', '会员等级', '手机评分', '评论时间', '手机颜色', '手机内存', '评论'])

    def process_item(self, item, spider):
        line = [item['name'], item['level'], item['star'], item['rls_time'], item['color'], item['storage'],item['content']]
        self.ws.append(line)
        self.wb.save('../网易.xlsx')
        print('网易数据成功保存！')
        return item