import pandas as pd
# 読み込むページのURLを変数に格納する
url = "https://fainance.yahoo.com/"
data = pd.read_html(url, header=0)
data[0].head()