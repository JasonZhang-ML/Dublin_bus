# -*- coding: utf-8 -*-
import scrapy


class Weather2018Spider(scrapy.Spider):
    name = 'weather2018'
    allowed_domains = ['https://www.wunderground.com/']
    start_urls = ['http://https://www.wunderground.com//']
    # def start_requests(self, ):
    def parse(self, response):
        pass
