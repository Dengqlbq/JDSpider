# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JDCommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    good_num = scrapy.Field()
    content = scrapy.Field()
