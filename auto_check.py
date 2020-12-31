# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import random
import datetime
import requests

loing_url = 'https://newsso.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2MDI2MzgzODMzNzQ2NzE2MzYsInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IldVSFdmcm50bldZSFpmelE1UXZYVUNWeSIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly9zZWxmcmVwb3J0LnNodS5lZHUuY24vTG9naW5TU08uYXNweD9SZXR1cm5Vcmw9JTJmRGVmYXVsdC5hc3B4Iiwic3RhdGUiOiIifQ=='
main_url = 'https://selfreport.shu.edu.cn/DayReport.aspx'

zk_account = 'K2001858'
zk_password = 'wyl4608310zK,'
su_account = 'K2001785'
su_password = '1234Qwer'

chrome_driver = r'D:\chromedriver_win32\chromedriver.exe'


def main(user, passwd):
    option = webdriver.ChromeOptions()
    # option.add_argument('--no-sandbox')
    # option.add_argument('--headless')
    option.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')

    browser = webdriver.Chrome(chrome_options=option, executable_path=chrome_driver)

    try:
        browser.get(loing_url)
        time.sleep(1)
        username = browser.find_element(By.CSS_SELECTOR, '#username')
        password = browser.find_element(By.CSS_SELECTOR, '#password')
        username.send_keys(user)
        password.send_keys(passwd)
        login = browser.find_element(By.CSS_SELECTOR, '#submit')
        time.sleep(2)
        login.click()
        browser.get(main_url)
        promise_button = browser.find_element(By.CSS_SELECTOR, '#p1_ChengNuo-inputEl-icon')
        promise_button.click()
        temperature = browser.find_element(By.CSS_SELECTOR, '#p1_TiWen-inputEl')
        temperature.send_keys('36.6')
        button1 = browser.find_element(By.CSS_SELECTOR, '#fineui_0-inputEl-icon')
        button1.click()
        button2 = browser.find_element(By.CSS_SELECTOR, '#fineui_7-inputEl-icon')
        button2.click()
        button3 = browser.find_element(By.CSS_SELECTOR, '#fineui_12-inputEl-icon')
        button3.click()
        button4 = browser.find_element(By.CSS_SELECTOR, '#fineui_16-inputEl-icon')
        button4.click()


        button5 = browser.find_element(By.CSS_SELECTOR, '#fineui_20-inputEl-icon')
        button5.click()
        button6 = browser.find_element(By.CSS_SELECTOR, '#fineui_22-inputEl-icon')
        button6.click()
        # button7 = browser.find_element(By.CSS_SELECTOR, '#fineui_28-inputEl-icon')
        # button7.click()
        button8 = browser.find_element(By.CSS_SELECTOR, '#fineui_28-inputEl-icon')
        button8.click()
        button9 = browser.find_element(By.CSS_SELECTOR, '#fineui_26-inputEl-icon')
        button9.click()
        time.sleep(1)
        commit_button = browser.find_element(By.CSS_SELECTOR, '#p1_ctl00_btnSubmit')
        commit_button.click()
        time.sleep(1)
        # sure_button = browser.find_element(By.CSS_SELECTOR, '#fineui_35')
        # sure_button.click()
        sure_button = browser.find_elements(By.CSS_SELECTOR, '.f-panel-bodyct .f-toolbar-bodyct>.f-toolbar-body>a')[3]
        sure_button.click()
        time.sleep(3)


    except Exception as e:
        print(e, e.__traceback__.tb_lineno)
        time.sleep(30)
        return

    finally:
        browser.close()


if __name__ == '__main__':
    main(zk_account, zk_password)
