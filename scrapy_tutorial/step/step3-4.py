import requests
from bs4 import BeatifulSoup

load_url="https://creaters-you.com/"
html=requests.get(load_url)
soup=BeatifulSoup(html.content,"html.parser")

# IDで検索 中身のliタグを表示