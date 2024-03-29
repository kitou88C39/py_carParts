from selenium from webdriver
from time import sleep

# ログインする方法
USERNAME = "yoshitaka"
PASSWORD = "password"
driver = webdriver.Chrome("chromedriver")
target_url="https://www.instagram.com/"
driver.get(target_url)
sleep(3)

# ログイン画面でユーザーネーム・パスワードの入力
error_flg = False
try:
    username_input = driver.find_element_by_xpath("//input[@aria-label='電話番号、ユーザーネーム、メールアドレス']")
    username_input.send_keys(USERNAME)
    sleep(1)

    password_input = driver.find_element_by_xpath("//input[@aria-label='パスワード']")
    password_input.send_keys(PASSWORD)
    sleep(1)

except Exception:
    error_flg = True
    print("ユーザー名、パスワード入力時にエラーが発生しました")
