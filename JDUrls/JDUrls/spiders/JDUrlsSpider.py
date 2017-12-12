from scrapy_redis.spiders import RedisSpider
from JDUrls.items import JDUrlsItem
from scrapy.utils.project import get_project_settings
import scrapy
import re


class JDUrlsSpider(RedisSpider):
    # 获取指定页面中所有商品编号并整合成detail-relate url 和comment-relate url
    name = 'JDUrlsSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDUrlsSpider'

    settings = get_project_settings()
    hide_url = settings['HIDE_URL']

    def parse(self, response):
        # 页面中未隐藏的所有商品编号
        nums = response.xpath('//ul[@class="gl-warp clearfix"]/li[@class="gl-item"][@data-sku]/@data-sku').extract()
        keyword = re.findall(r'keyword=(.*?)&enc', response.url)[0]

        # 虽然是同一个页面的商品编号，但异步加载请求隐藏的商品编号时请求的页面编号不同
        page = re.findall(r'page=(\d+)', response.url)[0]
        page = int(page) + 1

        s = ''
        for i in nums:
            s += str(i) + ','
        s = s[0:len(s)-1:]

        item = JDUrlsItem()
        item['num_list'] = nums
        yield item

        yield scrapy.Request(self.hide_url.format(keyword, page, s), callback=self.get_hidden)

    def get_hidden(self, response):
        # 页面中隐藏的所有商品编号
        nums = response.xpath('//li[@class="gl-item"][@data-sku]/@data-sku').extract()

        item = JDUrlsItem()
        item['num_list'] = nums
        yield item

