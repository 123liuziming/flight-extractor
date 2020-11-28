# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 进港
class InPortInfo(scrapy.Item):
    flight_id = scrapy.Field()

    # 始发地
    origin = scrapy.Field()

    origin_terminal = scrapy.Field()

    take_off_time = scrapy.Field()

    take_off_real_time = scrapy.Field()

    origin_state = scrapy.Field()

