import requests
from bs4 import BeatifulSoup
import urllib

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")

# ファイルを書き込みモードで開く
filename="linklist.txt"
with open(filename, "w") as f:
# 全てのaタグを検索 リンクを絶対URLで書き出す
    for element in soup.find_all("a"):
           url=element.get("href")
           link_url=urllib.parser.urljoin(load_url, url)