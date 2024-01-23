import requests
from bs4 import BeatifulSoup

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")
# 要素を取り出す
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)