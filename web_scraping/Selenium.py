from selenium import webdriver
#timeモジュールには、時間や日付に関するさまざまな関数が含まれています。
#その中の1つであるsleep()関数は、指定した秒数だけプログラムの実行を一時停止します。
from time import seleep
from selenium.webdriver.chorme.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("chormedriver.exe", options=options)
driver.get("https://www.google.com/")
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
for elem_h3 driver.find_element_by_path("//a/h3"):
    print(elem_h3.text)
    elem_a = elem_h3.find_element_by_path("..")
    print(elem_a.get_attribute("href"))