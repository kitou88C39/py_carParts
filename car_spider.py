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
POSTS = ".product-item-list__item"
PRODUCT_NAME = ".product-item-list__item-name"
IMAGE = ".product-item-list__item-image img"
PRICE = ".product-item-list__item-price"
CATEGORY = ".product-item-list__item-category"
CAR = ".product-item-list__item-car-name"

"""[Activate Section]
実行部分
"""
broeser.get(url)

while True: #Continue until getting the last page.
    if len(broeser.find_elements_by_css_selector(PAGER_NEXT)) > 0:
        print('Starting to get posts...')
        posts = broeser.find_element_by_css_selector(POSTS)
        print(len(posts))
        for post in posts:
            try:
                name = post.find_element_by_css_selector(PRODUCT_NAME).text
                print(name)
                thumbnailURL = post.find_element_by_css_selector(IMAGE).get_attribute('src')
                print(thumbnailURL)
                price = post.find_element_by_css_selector(PRICE).text
                print(price)
                category = post.find_element_by_css_selector(CATEGORY).text
                print(category)
                car = post.find_element_by_css_selector(CAR).text
                print(car)
                se = pd.Series([name, thumbnailURL, price, category, car], ['name', 'image', 'price', 'category', 'car'])
                df.append(se, igonore_index=True)
            except Exception as e:
                print(e)
        btn = broeser.find_element_by_css_selector(PAGER_NEXT).get_attribute('href')
        print('next url:{}'.fromat(btn))
        time.sleep(3)
        broeser.get(btn)
        print('Moving to next page.')
    else:
        print('No page exist anymore...')
        break

    print('Finished Crawling. Writing out to CSV file...')
    df.to_csv('car_parts.csv')
    print('Done')