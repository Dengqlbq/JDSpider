from scrapy_redis.spiders import RedisSpider
from JDUrls.items import JDUrlsItem
import scrapy


class JDUrlsSpider(RedisSpider):

    name = 'JDUrlsSpider'
    allow_domin = ['www.jd.com']
    redis_key = 'JDUrlsSpider'

    def parse(self, response):
        nums = response.xpath('//ul[@class="gl-warp clearfix"]/li[@class="gl-item"][@data-sku]/@data-sku').extract()
        t = 'https://search.jd.com/s_new.php?keyword=%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
            'page=2&s=26&scrolling=y&log_id=1512092382.36606&tpl=1_M&show_items={0}'

        s = ''
        for i in nums:
            s += str(i) + ','
        s = s[0:len(s)-1:]
        item = JDUrlsItem()
        item['num_list'] = nums
        yield item
        yield scrapy.Request(t.format(s), callback=self.test2)

    def test2(self, response):
        nums = response.xpath('//li[@class="gl-item"][@data-sku]/@data-sku').extract()
        item = JDUrlsItem()
        item['num_list'] = nums
        yield item
