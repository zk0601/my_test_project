from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def login(browser):
    login_button = browser.find_element(By.CSS_SELECTOR, '.login')
    login_button.click()
    time.sleep(1)
    login_user = 'wylshisb'
    login_password = '4608310zk'
    user = browser.find_element(By.CSS_SELECTOR, '#aw-login-user-name')
    user.send_keys(login_user)
    password = browser.find_element(By.CSS_SELECTOR, '#aw-login-user-password')
    password.send_keys(login_password)
    confirm = browser.find_element(By.CSS_SELECTOR, '#login_submit')
    confirm.click()


def main():
    option = webdriver.ChromeOptions()
    # option.add_argument('--no-sandbox')
    # option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=option)
    url = 'http://www.ybx.com/'
    try:
        browser.get(url)
        login(browser)
        time.sleep(2)
        hide = browser.find_element(By.CSS_SELECTOR, 'div.aw-user-nav')
        ActionChains(browser).move_to_element(hide).perform()
        time.sleep(1)
        admin = browser.find_elements(By.CSS_SELECTOR, 'ul.aw-dropdown-list li')
        admin = admin[2]
        admin.click()
        time.sleep(2)
        login_password = '4608310zk'
        password = browser.find_elements(By.CSS_SELECTOR, 'div.form-group')[1]
        password = password.find_element(By.CSS_SELECTOR, 'input')
        password.send_keys(login_password)
        login_button = browser.find_element(By.CSS_SELECTOR, 'button#login_submit')
        login_button.click()
        time.sleep(2)
        item = browser.find_elements(By.CSS_SELECTOR, 'ul.mod-bar>li')[3]
        item.click()
        item = item.find_elements(By.CSS_SELECTOR, 'ul>li')[0]
        item = item.find_element(By.CSS_SELECTOR, 'a')
        item.click()
        time.sleep(2)

        i = 1
        while i <= 101:
            user_items = browser.find_elements(By.CSS_SELECTOR, 'table.table.table-striped>tbody>tr')
            for j in range(20):
                user = user_items[j]
                td = user.find_elements(By.CSS_SELECTOR, 'td')
                uid = td[1].text
                if int(uid) in list(range(11, 931)):
                    action = td[-1].find_elements(By.CSS_SELECTOR, 'a')[0]
                    action.click()
                    image = browser.find_element(By.CSS_SELECTOR, 'span.mod-file .mod-input-file')
                    avatat_file = uid + '_avatar_real.jpg'
                    file = os.path.join('D:\\avatar', avatat_file)
                    if not os.path.exists(file):
                        print(uid)
                    else:
                        image.send_keys(file)
                    time.sleep(1)
                    group = browser.find_elements(By.CSS_SELECTOR, 'div.col-sm-5.col-xs-8 select')[-1]
                    group.click()
                    time.sleep(1)
                    option = group.find_elements(By.CSS_SELECTOR, 'option')[3]
                    option.click()
                    time.sleep(1)
                    save = browser.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>input')
                    save.click()
                    browser.back()
                    user_items = browser.find_elements(By.CSS_SELECTOR, 'table.table.table-striped>tbody>tr')
            next_page = browser.find_elements(By.CSS_SELECTOR, 'ul.pagination>li')
            i += 1
            for page in next_page:
                if page.text in ['>', '<', '>>', '<<']:
                    continue
                if int(page.text) == i:
                    page.find_element(By.CSS_SELECTOR, 'a').click()
                    break
            time.sleep(1)

    finally:
        browser.close()


if __name__ == '__main__':
    main()
