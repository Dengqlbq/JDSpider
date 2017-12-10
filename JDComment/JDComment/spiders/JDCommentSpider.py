from scrapy_redis.spiders import RedisSpider
from JDComment.items import JDCommentItem
from scrapy.utils.project import get_project_settings
import scrapy
import json
import re


class JDCommentSpider(RedisSpider):
    # 获取指定商品的评论（完整评论，非摘要）
    name = 'JDCommentSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDCommentSpider'

    settings = get_project_settings()
    comment_url = settings['COMMENT_URL']

    def parse(self, response):
        comment_json = json.loads(response.text)
        good_number = re.findall(r'productId=(\d+)', response.url)[0]
        # 目前maxPage最大值都是100，待解决
        max_page_num = comment_json['maxPage']

        for com in comment_json['comments']:
            item = JDCommentItem()
            item['good_num'] = good_number
            item['content'] = com['content']
            yield item

        for i in range(2, max_page_num):
            yield scrapy.Request(self.comment_url.format(good_number, i), callback=self.get_leftover)

    def get_leftover(self, response):
        comment_json = json.loads(response.text)
        good_number = re.findall(r'productId=(\d+)', response.url)[0]

        for com in comment_json['comments']:
            item = JDCommentItem()
            item['good_num'] = good_number
            item['content'] = com['content']
            yield item
