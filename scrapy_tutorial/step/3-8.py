import requests

# 画像ファイルを取得
image_url="https://creaters-you.com/pc.png"
imgdata=requests.get(image_url)
# URLから最後のファイル名を取り出す
filename=image_url.split("/")[-1]
# 画像データをファイルに書き出す
with open(filename, mode="wb")as f:
    f.write(imgdata.content)