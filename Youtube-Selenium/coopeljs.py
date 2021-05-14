from requests_html import HTMLSession



url='https://www.coppel.com/refrigeradores-y-congeladores'
s= HTMLSession()
res = s.get(url)
res.html.render(sleep=1)

print(res.status_code)
products = res.html.xpath('//*[@id="searchBasedNavigation_widget_6_2303"]/div[1]/div[2]', first= True)
for product in products.absolute_links:
    res= s.get(product)
    name = res.html.find('div.top.namePartPriceContainer.clearfix', first= True).text
    price = res.html.find('div.pcontado', first=True).text.replace("de contado","")
    print(product)
    if res.html.find('div.p_oferta'):
        print("Producto en oferta")
    else:
        print("Precio regular")

    print(name, price)
