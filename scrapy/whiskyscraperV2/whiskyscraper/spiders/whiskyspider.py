import scrapy


class WhiskeySpider(scrapy.Spider):
    name='whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky']

    def parse(self, response):
        for products in response.css("div.product-item-info"):
            try:
                yield{
                    'Name': products.css("a.product-item-link::text").get(),
                    'Price': products.css("span.price::text").get().replace('£',''),
                    'Link': products.css("a.product-item-link").attrib['href'],
                }
            except:
                yield{
                    'Name': products.css("a.product-item-link::text").get(),
                    'Price': 'Sold Out',
                    'Link': products.css("a.product-item-link").attrib['href'],
                }
        next_page = response.css('a.action.next').attrib['href']
        if next_page:
            yield response.follow(next_page, callback=self.parse)
