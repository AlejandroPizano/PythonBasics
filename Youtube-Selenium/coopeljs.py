from requests_html import HTMLSession
import pandas as pd
lista=[]
url='https://www.coppel.com/refrigeradores-y-congeladores'
def page(url):
    s= HTMLSession()
    res = s.get(url)
    res.html.render(sleep=1)

    print(res.status_code)
    products = res.html.xpath('//*[@id="searchBasedNavigation_widget_6_2303"]/div[1]/div[2]', first= True)
    for product in products.absolute_links:
        res= s.get(product)
        name = res.html.find('div.top.namePartPriceContainer.clearfix', first= True).text
        price = res.html.find('div.pcontado', first=True).text.replace("de contado","")
        if res.html.find('div.p_oferta'):
            price = res.html.find('div.tam_normal', first=True).text.replace("de contado","").replace('&nbsp;', '')
            oferta ="Producto en oferta"
        else:
            price = res.html.find('div.pcontado', first=True).text.replace("de contado","").replace('&nbsp;', '')
            oferta = "Precio regular"
        datos={
            'Nombre': name,
            'Precio':price,
            'Promo':oferta,
            'link': product,
        }
        lista.append(datos)
acum = -12
if (acum<156):
    acum=acum+12
    page(f"https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:{acum}&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&")
page(url)
df = pd.DataFrame(lista)
df.to_csv("coppel.csv")


#https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:12&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&
#https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:24&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&