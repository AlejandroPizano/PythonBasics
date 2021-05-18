from requests_html import HTMLSession


urllist=[
        'https://www.amazon.com/Apple-AirPods-Charging-Previous-Model/dp/B01MQWUXZS/ref=sr_1_1_sspa?dchild=1&keywords=airpods&qid=1621363967&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTlEMDdGUUdWSk1LJmVuY3J5cHRlZElkPUEwMjQ5NzYxMjAzVlVMSElERURTRSZlbmNyeXB0ZWRBZElkPUEwNTgwMTYxMVJSUkxEVTE1R1g2QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
         'https://www.amazon.com/Apple-MWP22AM-A-cr-AirPods-Renewed/dp/B0828BJGD2/ref=sr_1_4?crid=50HTSI0WD5FM&dchild=1&keywords=airpods+pro+2&qid=1621364539&sprefix=airpods%2Caps%2C442&sr=8-4',
         'https://www.amazon.com/Apple-AirPods-Charging-Case-Renewed/dp/B07SKLLYTW/ref=sr_1_6?crid=50HTSI0WD5FM&dchild=1&keywords=airpods+pro+2&qid=1621364561&sprefix=airpods%2Caps%2C442&sr=8-6'
         ]

def getPrice(url):
    s=HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'Name': r.html.xpath('//*[@id="productTitle"]', first= True).text,
        'price': r.html.xpath('//*[@id="price_inside_buybox"]', first=True).text

    }
    print(product)
    return(product)

products=[]
for url in urllist:
     products.append(getPrice(url))
price=[]
max_price = max(product['price'] for product in products)

print (products['price'])