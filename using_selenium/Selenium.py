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