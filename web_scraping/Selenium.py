from selenium import webdriver
#timeモジュールには、時間や日付に関するさまざまな関数が含まれています。
#その中の1つであるsleep()関数は、指定した秒数だけプログラムの実行を一時停止します。
from time import seleep

driver = webdriver.Chrome("chormedriver.exe")
driver.get("https://www.google.com/")
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")