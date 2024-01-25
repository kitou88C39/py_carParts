import requests

response = requests.get("https://www.yahoo.co.jp")
response.status_code
response.text
response.content
response.encoding
response.headers
response.cookies

for key, value in response.headers.items():
    print(key, " ", value)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
header = ["user_agent": user_agent]
url = "https://www.yahoo.co.jp/"

response = requests.get(url, headers=header)
response.status_code
response.text

response = requests.get(url, timeout=3)
response.text[:500]
param = ["q":"python"]
response = requests.get("https://www.yahoo.co.jp/search", params=param)