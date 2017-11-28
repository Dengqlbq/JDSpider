from scrapy_redis.spiders import RedisSpider
import redis
from scrapy.utils.project import get_project_settings


class JDUrlsSpider(RedisSpider):

    name = 'JDUrlsSpider'
    allow_domin = ['www.jd.com']
    redis_key = 'JDUrlsSpider'

    settings = get_project_settings()
    url = settings['GOODS_DETAIL_URL']
    r = redis.Redis(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'],
                    password=settings['REDIS_PARAMS']['password'])

    def parse(self, response):
        nums = response.xpath('//ul[@class="gl-warp clearfix"]/li[@class="gl-item"][@data-sku]/@data-sku').extract()
        for n in nums:
            self.r.sadd('JDDetailSpider', self.url.format(n))
