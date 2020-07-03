# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from weather.items import WeatherItem


class Weather2018Spider(scrapy.Spider):
    name = 'weather2018'
    # allowed_domains = ['wunderground.com/','wunderground.com/history/daily/EIDW/date/' ]
    # allowed_domains = ["*"]
    start_urls = ["https://wunderground.com/history/daily/EIDW/date"]

    # def start_requests(self):
    #     for i in range(1,32):
    #         url = "https://wunderground.com/history/daily/EIDW/date/2018-1-{}".format(i)
    #         yield Request(url, callback=self.weather_parse)

    def parse(self, response):
        for i in range(1, 32): # 32
            date = '2018-1-{}'.format(i)
            url = "https://wunderground.com/history/daily/EIDW/date/2018-1-{}".format(i)
            yield Request(url,meta={'date':date}, callback=self.second_parse)

    def second_parse(self, response):

        gets = response.xpath('//tr[@class="mat-row cdk-row ng-star-inserted"]')
        print("##################INFOMATION############\nThe nue of rows is "+ str(len(gets)))
        for r in gets:
            item = WeatherItem()
            item['date'] = response.meta['date']

            item['time'] = r.xpath('td[1]/span/text()').extract()
            item['temp'] = r.xpath("td[2]//span[@class='wu-value wu-value-to']/text()").extract()
            item['humid'] = r.xpath("td[4]//span[@class='wu-value wu-value-to']/text()").extract()
            item['windspeed'] = r.xpath("td[6]//span[@class='wu-value wu-value-to']/text()").extract()
            item['condition'] = r.xpath('td[10]/span/text()').extract()
            yield item

