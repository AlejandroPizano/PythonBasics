import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://super.walmart.com.mx/productos?Ntt=colchon"

downloaded_page = requests.get(url)

soup = BeautifulSoup(downloaded_page.content)
print(soup.prettify())

productos = soup.find_all('div', class_ = 'product_container__1Z_GP.grid_productBox__2MtRC')
print(productos)









''' from selenium import webdriver
import time


url= 'https://super.walmart.com.mx/productos?Ntt=colchon'

driver= webdriver.Chrome("C:\\Users\\apizano\\Downloads\\chromedriver.exe")


driver.get(url)
productos = driver.find_elements_by_class_name('product_container__1Z_GP grid_productBox__2MtRC')
print(productos)

for producto in productos:
    name = producto.find_element_by_xpath('.//*[@id="scrollToTopComponent"]/section/div/div[3]/div[2]/div/div/div/div[1]/div[2]/a/p').text
    price = producto.find_element_by_xpath('.//*[@id="scrollToTopComponent"]/section/div/div[3]/div[2]/div/div/div/div[1]/div[3]/div[1]/p').text
    link = producto.find_element_by_xpath('.//*[@id="scrollToTopComponent"]/section/div/div[3]/div[2]/div/div/div/div[1]/div[2]/a').get_attribute('href')
    if name:
        print(name, price, link)'''