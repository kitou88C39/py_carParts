import pandas as pd
# 読み込むページのURLを変数に格納する
url = "https://fainance.yahoo.com/"
data = pd.read_html(url, header=0)
data[0].head()
data[0].tail()
data[0]["Adj Close**"]=pd.to_numeric(data[0]["Adj Close**"],errors="coerce")
data[0].tail()
data[0].dropna（inplace=True）
data[0].tail()

from datatime import datatime as dt
data[0]["Date2"]=dt.striptime(i,"%b","%d","%y") for i in data[0]["Date"]