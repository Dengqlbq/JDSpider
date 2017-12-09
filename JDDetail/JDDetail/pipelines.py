# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymysql


class JDDetailPipeline(object):

    def __init__(self):

        self.settings = get_project_settings()
        self.connect = pymysql.connect(
            host=self.settings['MYSQL_HOST'],
            db=self.settings['MYSQL_DBNAME'],
            user=self.settings['MYSQL_USER'],
            passwd=self.settings['MYSQL_PASSWD'],
            charset=self.settings['MYSQL_CHARSET'],
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

            sql = 'insert into Scrapy_test.JDDetail(name,price,owner,flag,comment_count,good_count,default_good_count,' \
                  'general_count,poor_count,after_count,good_rate,general_rate,poor_rate,average_score,num)'\
                  'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['price'], item['owner'], item['flag'], item['comment_count'],
                                      item['good_count'], item['default_good_count'], item['general_count'],
                                      item['poor_count'], item['after_count'], item['good_rate'], item['general_rate'],
                                      item['poor_rate'], item['average_score'], item['num']))
            self.connect.commit()

