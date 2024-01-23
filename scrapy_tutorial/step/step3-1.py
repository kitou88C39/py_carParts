import requests
from bs4 import BeatifulSoup

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")
# 要素を取り出す
print(soup.find("title"))
print(soup.find("h2"))