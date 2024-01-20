from selenium import webdriver
import pandas as pd
import time


# Initial setting

option = webdriver.ChromeOptions()
option.add_argument('__headeless')
option.add_argument('__disable_gpu')
option.add_argument('__lang_ja')