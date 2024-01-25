import requests

response = requests.get("https://www.yahoo.co.jp")
response.status_code
response.text
response.content
response.encoding
response.headers

for key, value in response.headers.items():
    print(key, " ", value)