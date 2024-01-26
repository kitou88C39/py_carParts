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