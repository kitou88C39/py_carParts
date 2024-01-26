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
elems = soup.select("")
elems[0]
elems[0].contents