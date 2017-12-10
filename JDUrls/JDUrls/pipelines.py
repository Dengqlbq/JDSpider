# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from scrapy.utils.project import get_project_settings


class JDUrlsPipeline(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.detail_url = self.settings['GOODS_DETAIL_URL']
        self.comment_url = self.settings['COMMENT_URL']

        self.r = redis.Redis(host=self.settings['REDIS_HOST'], port=self.settings['REDIS_PORT'],
                             password=self.settings['REDIS_PARAMS']['password'])

    def process_item(self, item, spider):
        # 将商品编号整合成detail-relate url 和comment-relate url后存到服务器redis数据库
        for n in item['num_list']:
            self.r.lpush('JDDetailSpider', self.detail_url.format(n))
            self.r.lpush('JDCommentSpider', self.comment_url.format(n))
