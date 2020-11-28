# -*- coding: utf-8 -*-
import scrapy
from extractor.out_port_info import OutPortInfo


class ExtractOutSpider(scrapy.Spider):
    name = "out_port"
    allowed_domains = ['www.carnoc.com']
    start_urls = ['http://data.carnoc.com/corp/airport/cgq__airportflight.html']

    def parse(self, response):
        node_list = response.xpath("//div[@class='fly right']/ul/div[@id='icefable2']/li")
        items = []
        for node in node_list:
            item = OutPortInfo()

            item['flight_id'] = node.xpath("./span[1]/text()").extract()[0]

            # 始发地
            item['dest'] = node.xpath("./span[@class='flt_city']/text()").extract()[0]
            # 接机楼
            item['dest_terminal'] = node.xpath("./span[@class='terminal']/text()").extract()[0]

            item['take_off_time'] = node.xpath("./span[4]/text()").extract()[0]

            item['take_off_real_time'] = node.xpath("./span[5]/text()").extract()[0]

            item['origin_state'] = node.xpath("./span[6]/text()").extract()[0]

            items.append(item)

        return items
