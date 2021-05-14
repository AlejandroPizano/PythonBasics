import scrapy

class RefrigSpider(scrapy.Spider):

    name='fridgespider'
    start_urls=['https://www.coppel.com/refrigeradores-y-congeladores']


    def parse(self, response):






        ''''
        for products in response.css('div.product_info.clearfix'):
            yield products.css('p.m0::text').get()
        '''

