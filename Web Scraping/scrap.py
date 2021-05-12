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
for index, element in enumerate(table_head):
    if index > 0:
        labels.append("Tesla model X version:  " + element.text.strip())
print(labels)
print(len(labels))
with open('tesla_tables.html', 'w', encoding="utf-8") as file:
    file.write(str(labels))

df = pd.DataFrame(labels)
print(df)
with open('tesla_excel.html', 'w', encoding="utf-8") as file:
    file.write(str(df.to_excel))

with open("tesla.html", "r") as file:
    print(file.read())
