from scrapy_redis.spiders import RedisSpider
from JDUrls.items import JDUrlsItem
import scrapy
import re


class JDUrlsSpider(RedisSpider):

    name = 'JDUrlsSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDUrlsSpider'
    page_num = {}

    def parse(self, response):
        nums = response.xpath('//ul[@class="gl-warp clearfix"]/li[@class="gl-item"][@data-sku]/@data-sku').extract()

        keyword = re.findall(r'keyword=(.*?)&enc', response.url)[0]
        page = re.findall(r'page=(\d+)', response.url)[0]
        page = int(page) + 1
        s = ''
        for i in nums:
            s += str(i) + ','
        s = s[0:len(s)-1:]

        item = JDUrlsItem()
        item['num_list'] = nums
        yield item

        t = 'https://search.jd.com/s_new.php?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
            'page={1}&s=26&scrolling=y&log_id=1512092382.36606&tpl=1_M&show_items={2}'
        yield scrapy.Request(t.format(keyword, page, s), callback=self.get_hidden)

    def get_hidden(self, response):
        nums = response.xpath('//li[@class="gl-item"][@data-sku]/@data-sku').extract()

        item = JDUrlsItem()
        item['num_list'] = nums
        yield item

