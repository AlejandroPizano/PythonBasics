import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://es.wikipedia.org/wiki/Tesla,_Inc."

downloaded_page = requests.get(url)

soup = BeautifulSoup(downloaded_page.text.encode("utf-8"))

# with io.open('tesla.html', 'w', encoding="utf-8") as file:
#   file.write(soup.prettify())

with open('tesla.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())
