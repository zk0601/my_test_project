# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os


def login(browser):
    time.sleep(5)
    browser.implicitly_wait(10)
    browser.set_page_load_timeout(3)
    browser.set_script_timeout(3)
    try:
        login_button = browser.find_element(By.CSS_SELECTOR, '.login .auth-login')
        login_button.click()
    except exceptions.TimeoutException:
        browser.execute_script("window.stop();")
    passwdlogin = browser.find_element(By.CSS_SELECTOR, '.tang-pass-footerBar .tang-pass-footerBarULogin')
    passwdlogin.click()
    user = browser.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_4__userName')
    time.sleep(2)
    user.send_keys('wkandlc')
    password = browser.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_4__password')
    time.sleep(2)
    password.send_keys('wk19841117')
    while True:
        confirm = browser.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_4__submit')
        time.sleep(2)
        confirm.click()
        time.sleep(3)
        browser.implicitly_wait(10)
        try:
            cancel = browser.find_element(By.CSS_SELECTOR, '.forceverify-header-a')
            time.sleep(3)
            browser.implicitly_wait(10)
        except Exception:
            break
        cancel.click()
        time.sleep(2)


def submit_ip(browser, filename):
    next_page = browser.find_element(By.CSS_SELECTOR, '#toolsMainLeft>dl:nth-child(2)>dd>a:first-child')
    next_page.click()
    time.sleep(3)
    manual_submit = browser.find_element(By.CSS_SELECTOR, '.tool-sub-tab.clearfix>a:last-child')
    manual_submit.click()

    file = os.path.join(os.path.realpath(os.path.dirname(__file__)), filename)
    if not os.path.exists(file):
        browser.back()
        browser.back()
        time.sleep(3)
        return

    with open(file, 'r') as f:
        stop_tag = False
        while True:
            data = ""
            for _ in range(15):
                one_item = f.readline().strip('\n')
                if not one_item:
                    stop_tag = True
                    break
                print(one_item)
                data = data + one_item + '\n'
            if len(data) != 0:
                text = browser.find_element(By.CSS_SELECTOR, '#siteurl-urls')
                text.clear()
                text.send_keys(data)
                submit = browser.find_element(By.CSS_SELECTOR, '#siteurl-btn-submit')
                submit.click()
                time.sleep(3)
                complete = browser.find_element(By.CSS_SELECTOR, '#dialog-foot button')
                complete.click()

            if stop_tag:
                time.sleep(3)
                browser.back()
                browser.back()
                time.sleep(3)
                return


def main(url):
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    option = webdriver.ChromeOptions()
    # option.add_argument('--no-sandbox')
    # option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=option)

    try:
        browser.get(url)
        browser.implicitly_wait(10)
        login(browser)
        time.sleep(3)

        user_center = browser.find_element(By.CSS_SELECTOR, '.nav-user-center.nav-tab a')
        user_center.click()

        www_mibaoxian = browser.find_element(By.CSS_SELECTOR, '.site-list-box>ul>li.domain-box.clearfix:nth-child(2) .site-item:first-child>a:last-child')
        print(www_mibaoxian.text)
        if www_mibaoxian.text == 'www.mibaoxian.com':
            www_mibaoxian.click()
            submit_ip(browser, 'mibaoxian_www.txt')
        m_mibaoxian = browser.find_element(By.CSS_SELECTOR, '.site-list-box>ul>li.domain-box.clearfix:nth-child(2) .site-item:last-child>a:last-child')
        print(m_mibaoxian.text)
        if m_mibaoxian.text == 'm.mibaoxian.com':
            m_mibaoxian.click()
            submit_ip(browser, 'mibaoxian_m.txt')
        m_ybx = browser.find_element(By.CSS_SELECTOR, '.site-list-box>ul>li.domain-box.clearfix:nth-child(4) .site-item:first-child>a:last-child')
        print(m_ybx.text)
        if m_ybx.text == 'm.ybx.com':
            m_ybx.click()
            submit_ip(browser, 'ybx_m.txt')
        www_ybx = browser.find_element(By.CSS_SELECTOR, '.site-list-box>ul>li.domain-box.clearfix:nth-child(4) .site-item:last-child>a:last-child')
        print(www_ybx.text)
        if www_ybx.text == 'www.ybx.com':
            www_ybx.click()
            submit_ip(browser, 'ybx_www.txt')
        exit()
    except Exception as e:
        print(e, e.__traceback__.tb_lineno)

    finally:
        browser.close()


if __name__ == '__main__':
    while True:
        try:
            main('https://ziyuan.baidu.com/')
        except Exception:
            time.sleep(3)
            continue
    print('complete')
