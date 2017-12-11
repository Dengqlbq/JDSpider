# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDDetailItem(scrapy.Item):
    # define the fields for your item here like:

    # TINYTEXT
    name = scrapy.Field()
    # FLOAT
    price = scrapy.Field()
    # TINYTEXT
    owner = scrapy.Field()
    # TINYINT
    jd_sel = scrapy.Field()
    # TINYINT
    global_buy = scrapy.Field()
    # TINYINT
    flag = scrapy.Field()
    # INT
    comment_count = scrapy.Field()
    # INT
    good_count = scrapy.Field()
    # INT
    default_good_count = scrapy.Field()
    # INT
    general_count = scrapy.Field()
    # INT
    poor_count = scrapy.Field()
    # INT
    after_count = scrapy.Field()
    # FLOAT
    good_rate = scrapy.Field()
    # FLOAT
    general_rate = scrapy.Field()
    # FLOAT
    poor_rate = scrapy.Field()
    # FLOAT
    average_score = scrapy.Field()
    # TINYTEXT
    num = scrapy.Field()

