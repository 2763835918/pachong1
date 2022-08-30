# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WonderlandPipeline:
    fp = None
    #重写父类方法
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./qiubai.text','w',encoding='utf-8')

    def process_item(self, item, spider):
        date = item['date']
        content = item['content']
        self.fp.write(date+':'+content)
        return item

    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()


class mysqlPiline(object):
    conn = None
    def open_spider (self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1')