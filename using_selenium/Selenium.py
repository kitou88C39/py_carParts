# webブラウザを起動する
from selenium import webdriver
# 自動でブラウザが起動する webdriver
browser = webdriver.Chrome()
browser.get("https//scraping-for-beginner.herokuapp.com/login_page")
# ブラウザを閉じる
browser.quit()

browser = webdriver.Chrome()
browser.get("https//scraping-for-beginner.herokuapp.com/login_page")
# 要素を指定
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

# テキストデータを取得
elem_hn = browser.find_element_by_tag_name('th')
elem_hn.text

# テキストデータを一括取得
elems_th = browser.find_elements_by_tag_name('th')
elems_th[0].text
elems_th[1].text

# テキストデータを一括取得
elems_th = browser.find_elements_by_tag_name('th')
elem_th = elems_th[3]
key = elems_th.text

keys = []
elems_th = browser.find_elements_by_tag_name('th')
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

values = []
elems_td = browser.find_elements_by_tag_name('td')
elem_td = elems_td[0]

# 情報を一個ずつ取り出す
values = []
for elem_th in elems_td:
    value = elem_td.text
    values.append(value)

# csvファイルに出力する
import pandas as pd
# 空のDataFrameを定義
df = pd.DataFrame()