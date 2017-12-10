from scrapy_redis.spiders import RedisSpider
from JDUrls.items import JDUrlsItem
import scrapy
import re


class JDUrlsSpider(RedisSpider):
    # 获取指定页面中所有商品编号并整合成detail-relate url 和comment-relate url
    name = 'JDUrlsSpider'
    allow_domains = ['www.jd.com']
    redis_key = 'JDUrlsSpider'

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

        hide_num_page = 'https://search.jd.com/s_new.php?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
                        'page={1}&s=26&scrolling=y&log_id=1512092382.36606&tpl=1_M&show_items={2}'
        yield scrapy.Request(hide_num_page.format(keyword, page, s), callback=self.get_hidden)

    def get_hidden(self, response):
        # 页面中隐藏的所有商品编号
        nums = response.xpath('//li[@class="gl-item"][@data-sku]/@data-sku').extract()

        item = JDUrlsItem()
        item['num_list'] = nums
        yield item

