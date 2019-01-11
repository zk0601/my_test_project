# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import random
import datetime
import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class AwsUser(Base):
    __tablename__ = 'aws_users'

    uid = Column(INTEGER, primary_key=True)
    user_name = Column(VARCHAR(255))
    question_count = Column(INTEGER)
    password = Column(VARCHAR(32))
    avatar_file = Column(VARCHAR(128))
    salt = Column(VARCHAR(16))

    def keys(self):
        return [c.name for c in self.__table__.columns]


def login(browser):
    login_button = browser.find_element(By.CSS_SELECTOR, '.login')
    login_button.click()
    time.sleep(1)
    login_info = random_user()
    login_user = login_info['user']
    login_password = login_info['password']
    user = browser.find_element(By.CSS_SELECTOR, '#aw-login-user-name')
    user.send_keys(login_user)
    password = browser.find_element(By.CSS_SELECTOR, '#aw-login-user-password')
    password.send_keys(login_password)
    confirm = browser.find_element(By.CSS_SELECTOR, '#login_submit')
    confirm.click()


def random_user():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    users = session.query(AwsUser).order_by(AwsUser.uid.asc())

    user = users[random.randint(11, 2000)]

    return {'user': user.user_name, 'password': 123456}


def get_page_num(url):
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(url)
    next_page = browser.find_elements(By.CSS_SELECTOR, '.page-control .pagination li')
    for page in next_page:
        if page.text == '>>':
            a = page.find_element(By.CSS_SELECTOR, 'a')
            a.click()
    next_page = browser.find_elements(By.CSS_SELECTOR, '.page-control .pagination li')
    return int(next_page[-1].text)


def main(url, ip, port, page_num=1):
    option = webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    option.add_argument("--proxy-server=http://%s:%s" % (ip, port))
    browser = webdriver.Chrome(chrome_options=option)

    i = 1
    try:
        browser.get(url)
        login(browser)
        time.sleep(3)
        while i <= page_num:
            try:
                questions = browser.find_elements(By.CSS_SELECTOR, '.aw-common-list div .aw-question-content h4')
                j = random.randint(0, 49)
                question = questions[j]
                href = question.find_element(By.CSS_SELECTOR, 'a')
                print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(href.text)
                href.click()
                time.sleep(random.randint(1, 10))
                follow = browser.find_element(By.CSS_SELECTOR, '.operate.clearfix a')
                follow.click()
                thanks = browser.find_element(By.CSS_SELECTOR, '.pull-right.more-operate a')
                thanks.click()
                agreements = browser.find_elements(By.CSS_SELECTOR, '.operate .agree')
                for agreement in agreements:
                    if agreement.get_attribute('class') != 'agree active ':
                        agreement.click()
                browser.back()
                next_page = browser.find_elements(By.CSS_SELECTOR, '.page-control .pagination li')
                i += 1
                for page in next_page:
                    if page.text in ['>', '<', '>>', '<<']:
                        continue
                    if int(page.text) == i:
                        page.find_element(By.CSS_SELECTOR, 'a').click()
                        break
                time.sleep(1)
            except Exception as e:
                print(e)
                i += 1
                continue
        time.sleep(3)

    except Exception as e:
        print(e)
        browser.close()

    finally:
        browser.close()


def get_ip():
    url = 'http://http.tiqu.qingjuhe.cn/getip?num=80&type=2&pro=0&city=0&yys=0&port=1&pack=25861&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=0&regions='
    res = requests.get(url)
    return res.json()


if __name__ == '__main__':
    print("start time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    ip_list = get_ip()['data']
    print(ip_list)
    end = len(ip_list) - 1
    page_num = get_page_num('http://www.ybx.com/explore/')
    print(page_num)
    user_number = int(sys.argv[1])
    for _ in range(0, user_number):
        ip_info = ip_list[random.randint(0, end)]
        main('http://www.ybx.com/explore/', ip_info['ip'], ip_info['port'], page_num)
    for _ in range(0, user_number):
        ip_info = ip_list[random.randint(0, end)]
        main('http://m.ybx.com/explore/', ip_info['ip'], ip_info['port'], page_num)
    print("end time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
