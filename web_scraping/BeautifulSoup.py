# 基本的な使い方
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup)
print(soup.prettify())

print(soup.html.head.title)
print(soup.title)

print(soup.find_all("a"))

for tag_a in soup.find_all("a"):
    print(tag_a, end="¥n¥n")

or tag_a in soup.find_all("a"):
    print(tag_a.string)
    print(tag_a["href"], end="¥n¥n")

print(soup.select("body > p.end > b")[0].string)

## 読売新聞オンライン
import requests
from bs4 import BeautifulSoup

# HTMLデータの取得
url = "https://www.yahoo.co.jp"
response = requests.get(url)
response.status_code
response.text
soup = BeautifulSoup(response.text, "html.parser")
elems = soup.select('body > div.layout-contents > div.layout-contents__main > div > div.home-main-news-organization.p-category-latest > section > ul > li:nth-of-type(1) > article > div.p-list-item__inner > h3 > a')
elems[0]
elems[0].contents[0]
elems[0].attrs[0]

elems = soup.select('ul > li:nth-of-type(1) > article > div.p-list-item__inner > h3 > a')
elems[0]
print(elems[0].prettify())