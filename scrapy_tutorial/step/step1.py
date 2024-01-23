import requests

# 表示したいURLを持ってくる
url="https://creaters-you.com/"
# webページのurlを取得する
response=requests.get(url)
# 文字化けを防ぐ
response.encoding=response.apparent_encoding
# terminalに表示
print(response.text)