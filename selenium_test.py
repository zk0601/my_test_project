# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()

try:
    browser.get("https://www.wukong.com/tag/6213187423061412353/")
    i = 0
    while True:
        question = browser.find_elements(By.CSS_SELECTOR, '.question-title h2 a')
        for item in question[i:]:
            title = item.text
            url = item.get_attribute('href')
            pid = url.split('/')[-2]
            print(item.text)
            print(item.get_attribute('href'))
            print(pid)
        loadmore = browser.find_element(By.CSS_SELECTOR, '.w-feed-loadmore')
        if not loadmore:
            break
        action = ActionChains(browser)
        action.move_to_element(loadmore)
        action.perform()
        time.sleep(4)
        print('!!!!!!!!!!!!!!!!!!')
        i += 15

finally:
    browser.close()

