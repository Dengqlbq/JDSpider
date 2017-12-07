from scrapy_redis.spiders import RedisSpider
from JDDetail.items import JDDetailItem


class JDDetailSpider(RedisSpider):

    name = 'JDDetailSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDDetailSpider'

    def parse(self, response):

        item = JDDetailItem()

        name = response.xpath('//div[@class="sku-name"]/text()').extract()[0]
        price = 100
        comment_count = 100
        owner = True

        item['name'] = name
        item['price'] = price
        item['comment_count'] = comment_count
        item['owner'] = owner

        yield item
