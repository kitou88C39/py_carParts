import requests
from bs4 import BeatifulSoup

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")

# 全てのliタグを解析する
for element in soup.find_all("li"):
    print(element.text)