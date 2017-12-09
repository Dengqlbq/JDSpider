from scrapy_redis.spiders import RedisSpider
from JDDetail.items import JDDetailItem
from scrapy.utils.project import get_project_settings
import scrapy
import re
import json


class JDDetailSpider(RedisSpider):

    name = 'JDDetailSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDDetailSpider'

    settings = get_project_settings()
    comment_url = settings['COMMENT_URL']
    price_url = settings['PRICE_URL']

    def parse(self, response):
        item = JDDetailItem()

        raw_name = re.findall(r'<div class="sku-name">(.*?)</div>', response.text, re.S)[0].strip()
        if re.match(r'<img', raw_name) is None:
            name = raw_name
        else:
            name = raw_name.split('>')[1].strip()

        owner_list = response.xpath('//div[@class="J-hove-wrap EDropdown fr"]/div[@class="item"]/div[@class="name"]'
                                    '/a/text()').extract()
        if len(owner_list) == 0:
            owner = '自营'
            flag = True
        else:
            owner = owner_list[0]
            if '自营' in owner:
                flag = True
            else:
                flag = False
        num = re.findall(r'(\d+)', response.url)[0]

        item['name'] = name
        item['owner'] = owner
        item['flag'] = flag
        item['num'] = num

        price_request = scrapy.Request(self.price_url.format(num), callback=self.get_price)
        price_request.meta['item'] = item
        yield price_request

    def get_price(self, response):
        item = response.meta['item']

        price_json = json.loads(response.text)
        item['price'] = price_json[0]['p']
        num = item['num']

        comment_request = scrapy.Request(self.comment_url.format(num), callback=self.get_comment)
        comment_request.meta['item'] = item
        yield comment_request

    def get_comment(self, response):
        item = response.meta['item']

        comment_json = json.loads(response.text)
        comment_json = comment_json['CommentsCount'][0]

        item['comment_count'] = comment_json['CommentCount']
        item['good_count'] = comment_json['GoodCount']
        item['default_good_count'] = comment_json['DefaultGoodCount']
        item['general_count'] = comment_json['GeneralCount']
        item['poor_count'] = comment_json['PoorCount']
        item['after_count'] = comment_json['AfterCount']
        item['good_rate'] = comment_json['GoodRate']
        item['general_rate'] = comment_json['GeneralRate']
        item['poor_rate'] = comment_json['PoorRate']
        item['average_score'] = comment_json['AverageScore']

        yield item


