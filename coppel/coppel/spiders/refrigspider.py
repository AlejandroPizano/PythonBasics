
from selenium import webdriver


url= 'https://www.youtube.com/'

driver= webdriver.Chrome("C:\\Users\\apizano\\Downloads\\chromedriver.exe")
driver.get(url)

products = driver.find_elements_by_class_name('style-scope ytd-rich-grid-media')

for product in products:
    name = product.find_element_by_xpath('.//*[@id="meta"]/h3').text


print(name)

'''
#import scrapy
class RefrigSpider(scrapy.Spider):
    name='fridgespider'
    start_urls=['https://www.coppel.com/refrigeradores-y-congeladores']

    def parse(self, response):
        for products in response.css('div.product_info.clearfix'):
            yield products.css('p.m0::text').get()
'''

