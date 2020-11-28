import scrapy


# 进港
class OutPortInfo(scrapy.Item):
    flight_id = scrapy.Field()

    # 目的地
    dest = scrapy.Field()

    dest_terminal = scrapy.Field()

    take_off_time = scrapy.Field()

    take_off_real_time = scrapy.Field()

    origin_state = scrapy.Field()
