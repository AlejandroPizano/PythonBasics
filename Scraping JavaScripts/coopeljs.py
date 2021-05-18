from requests_html import HTMLSession
import pandas as pd
lista = []
#url='https://www.coppel.com/refrigeradores-y-congeladores'
s= HTMLSession()
def request (url):
    res = s.get(url)
    res.html.render(sleep=1)

    print(res.status_code)
    return res.html.xpath('//*[@id="searchBasedNavigation_widget_6_2303"]/div[1]/div[2]', first= True)


def parse(products):
    for product in products.absolute_links:
        try:
            res= s.get(product)
            name = res.html.find('div.top.namePartPriceContainer.clearfix', first= True).text
            price = res.html.find('div.pcontado', first=True).text.replace("de contado","")
            flag=True
        except:
            print("No se encontro el producto!!")
            flag=False

        if res.html.find('div.p_oferta'):
            price = res.html.find('div.tam_normal', first=True).text.replace("de contado","").replace('&nbsp;', '')
            oferta ="Producto en oferta"
        else:
            price = res.html.find('div.pcontado', first=True).text.replace("de contado","").replace('&nbsp;', '')
            oferta = "Precio regular"
        datos={
            'Nombre': name,
            'Precio': price,
            'Promo': oferta,
            'link': product,
        }
        lista.append(datos)


def output():
    df = pd.DataFrame(lista)
    df.to_csv("coppel.csv")


x=0
while x<48 and x!= 48:
    print("pagina :" + str(x))
    products= request(f'https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:{x}&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&')
    parse(products)
    x=x+12
else:
    print("No more items!")


output()
#https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:12&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&
#https://www.coppel.com/refrigeradores-y-congeladores/#facet:&productBeginIndex:24&orderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&