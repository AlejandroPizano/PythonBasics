import scrapy


class productSpider(scrapy.Spider):
    name='whisky'
    start_urls = ['https://super.walmart.com.mx/productos?Ntt=colchon']
