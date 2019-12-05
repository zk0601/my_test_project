from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime

buy_time_str = '2019-9-10 10:20:21'


class TaoBao(object):
    @staticmethod
    def main():
        option = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'images': 2
        #     }
        # }
        # option.add_experimental_option('prefs', prefs)  #不加载图片
        # option.set_preference('permissions.default.stylesheet', 2)  #不加载css
        browser = webdriver.Chrome(chrome_options=option)
        browser.get('https://www.taobao.com/')
        if browser.find_element_by_link_text("亲，请登录"):
            browser.find_element_by_link_text("亲，请登录").click()

        print("请在60秒内完成扫码")
        time.sleep(60)

        browser.get('https://cart.taobao.com/cart.htm')
        time.sleep(3)
        if browser.find_element(By.CSS_SELECTOR, "#J_SelectAll1"):
            browser.find_element(By.CSS_SELECTOR, "#J_SelectAll1").click()

        while True:
            now = datetime.datetime.now()
            now_str = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            buy_time = datetime.datetime.strptime(buy_time_str, "%Y-%m-%d %H:%M:%S")
            print('current time is :%s' % now_str)
            if now > buy_time:
                try:
                    if browser.find_element(By.CSS_SELECTOR, "#J_Go"):
                        browser.find_element(By.CSS_SELECTOR, "#J_Go").click()
                        WebDriverWait(browser, 2, poll_frequency=0.5).until(expected_conditions.visibility_of(By.LINK_TEXT('提交订单')))
                        browser.find_element_by_link_text('提交订单').click()
                        print('OK!')
                        time.sleep(5)
                    else:
                        time.sleep(0.1)
                        continue
                except:
                    time.sleep(0.1)
                    continue
            time.sleep(0.1)


if __name__ == '__main__':
    TaoBao.main()
