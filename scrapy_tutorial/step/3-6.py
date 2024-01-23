import requests
from bs4 import BeatifulSoup
import urllib

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")

# 全てのaタグを検索 リンクを表示
for element in soup.find_all("a"):
    print(element.text)
    url=element.get("href")
    link_url=urllib.parser.urljoin(load_url, url)