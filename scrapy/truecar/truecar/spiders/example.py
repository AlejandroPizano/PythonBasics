import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['exaple@example.com']
    start_urls = ['http://exaple@example.com/']

    def parse(self, response):
        pass
