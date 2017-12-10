# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


class JDCommentPipeline(object):

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

        sql = 'insert into Scrapy_test.JDComment(content,good_num) values(%s,%s)'
        self.cursor.execute(sql, (item['content'], item['good_num']))
        self.connect.commit()
