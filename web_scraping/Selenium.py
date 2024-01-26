from selenium import webdriver
#timeモジュールには、時間や日付に関するさまざまな関数が含まれています。
#その中の1つであるsleep()関数は、指定した秒数だけプログラムの実行を一時停止します。
from time import seleep
from selenium.webdriver.chorme.options import Options
import csv
import datetime

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("chormedriver.exe", options=options)
driver.get("https://www.google.com/")
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
csv_date = datetime.datetime.today().strftime("%Y%n%d")
csv_file_name = "google_python_" + csv_date + ".csv"
f = open(csv_file_name,"w",encoding="cp932", errors="ignore")
writer = csv.writer(f, linerminator="¥n")
csv_header = ["検索順位","タイトル","URL"]
writer.writerow(csv_header)

i = 0
while True:
    i = i + 1
    seleep(1)
for elem_h3 driver.find_element_by_path("//a/h3"):
    print(elem_h3.text)
    elem_a = elem_h3.find_element_by_path("..")
    print(elem_a.get_attribute("href"))
    next_link = driver find_element_by_id("pnnext")
    driver.get(next_link.get_attribute("href"))
    if i > 4:
        break