# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDDetailItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    owner = scrapy.Field()
    jd_sel = scrapy.Field()
    global_buy = scrapy.Field()
    flag = scrapy.Field()
    comment_count = scrapy.Field()
    good_count = scrapy.Field()
    default_good_count = scrapy.Field()
    general_count = scrapy.Field()
    poor_count = scrapy.Field()
    after_count = scrapy.Field()
    good_rate = scrapy.Field()
    general_rate = scrapy.Field()
    poor_rate = scrapy.Field()
    average_score = scrapy.Field()
    num = scrapy.Field()

