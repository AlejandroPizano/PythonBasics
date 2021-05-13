import scrapy


class WhiskeySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky']



    def parse(self, response):

        for index,products in enumerate(response.css('div.product-item-info')):
            try:
                yield {
                    'Product #':index+1,
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('£', ''),
                    'link': products.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'Product #': index+1,
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'Sold out',
                    'link': products.css('a.product-item-link').attrib['href'],
                }
        next_page = response.css('a.action.next').attrib['href']
        if next_page:
            yield response.follow(next_page, callback=self.parse)
