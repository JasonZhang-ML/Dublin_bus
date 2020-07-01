# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class Weather2018Spider(scrapy.Spider):
    name = 'weather2018'
    allowed_domains = ['wunderground.com/']

    def start_requests(self):
        for i in range(1,32):
            url = "https://jwunderground.com/history/daily/EIDW/date/2018-1-{}".format(i)
            yield Request(url, callback=self.weather_parse)

    def weather_parse(self, response):
        print(response.xpath('//tr[@class="mat-row cdk-row ng-star-inserted"]'))
        yield 0


