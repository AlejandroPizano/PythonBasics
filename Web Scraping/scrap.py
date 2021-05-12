import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://es.wikipedia.org/wiki/Tesla,_Inc."

downloaded_page = requests.get(url)

soup = BeautifulSoup(downloaded_page.text)

tables_wiki = soup.select('table.sortable.wikitable')[0]
print(tables_wiki)
print("--------------------------------------------------")
table_head = tables_wiki.select('tr th')
print(table_head)
labels = []
for element in table_head:
    labels.append("Tesla model X version:  "+element.text)
labels.pop(0)
print (labels)
with open('tesla_tables.html', 'w', encoding="utf-8") as file:
    file.write(str(labels))

