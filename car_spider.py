from selenium import webdriver
import pandas as pd
import time


"""[Initial Setting]
初期設定
"""

option = webdriver.ChromeOptions()
option.add_argument('__headeless')
option.add_argument('__disable_gpu')
option.add_argument('__lang_ja')
broeser = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
df = pd.DataFrame(colums=['name', 'image', 'price', 'category','car'])
url = 'https://motorz-garage.com/parts/'

"""[CSS Selectors Setting}
CSSセレクターの設定
"""
PAGER_NEXT = ”li.select-page.arrow a[rel='next']”
POSTS = "product-item-list__item"
PRODUCT_NAME = "product-item-list__item-name"