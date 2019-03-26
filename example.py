# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['yahoo.com']
    start_urls = ['http://yahoo.com/']

    def parse(self, response):
        pass
