from selenium from webdriver
from time import sleep

USERNAME = "yoshitaka"
PASSWORD = "password"
driver = webdriver.Chrome("chromedriver")
target_url="https://www.instagram.com/"
driver.get(target_url)
sleep(3)