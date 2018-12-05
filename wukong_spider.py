import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'

    qid = Column(VARCHAR(64), primary_key=True)
    question = Column(VARCHAR(255))
    url = Column(VARCHAR(255))

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('root', 123456,
                                                                             '47.75.49.133', 'user')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

    browser = webdriver.Chrome()

    try:
        browser.get("https://www.wukong.com/tag/6213187423061412353/")
        i = 0
        while True:
            question = browser.find_elements(By.CSS_SELECTOR, '.question-title h2 a')
            print(len(question))
            for item in question[i:]:
                title = item.text
                url = item.get_attribute('href')
                qid = url.split('/')[-2]
                qq = session.query(Question).filter(Question.qid == qid).first()
                if not qq:
                    q = Question(qid=qid, question=title, url=url)
                    session.add(q)
                    print(title)
                else:
                    print('pass')
            session.commit()
            loadmore = browser.find_element(By.CSS_SELECTOR, '.w-feed-loadmore')
            if not loadmore:
                break
            action = ActionChains(browser)
            action.move_to_element(loadmore)
            action.perform()
            time.sleep(10)
            print('!!!!!!!!!!!!!!!!!!')
            i += 15

    finally:
        browser.close()

if __name__ == '__main__':
    main()
