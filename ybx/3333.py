from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


Base = declarative_base()


class AwsQuestion(Base):
    __tablename__ = 'aws_question'

    question_id = Column(INTEGER, primary_key=True)
    question_content = Column(VARCHAR(255))
    add_time = Column(INTEGER)
    published_uid = Column(VARCHAR(11))

    def keys(self):
        return [c.name for c in self.__table__.columns]


class AwsUser(Base):
    __tablename__ = 'aws_users'

    uid = Column(INTEGER, primary_key=True)
    question_count = Column(INTEGER)

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    users = session.query(AwsUser).order_by(AwsUser.uid.asc())

    questions = session.query(AwsQuestion).order_by(AwsQuestion.question_id.asc())

    users_txt = os.path.join(os.path.dirname(__file__), 'users.txt')
    questions_txt = os.path.join(os.path.dirname(__file__), 'questions.txt')

    with open(users_txt, 'w', newline='\n') as f:
        for user in users:
            word = 'http://www.ybx.com/p_%s.html' % user.uid
            f.write(word)
            f.write('\n')

    with open(questions_txt, 'w', newline='\n', encoding='utf-8') as ff:
        for question in questions:
            word = 'http://www.ybx.com/q_%s.html' % question.question_id
            ff.write(word)
            ff.write('\n')

    session.remove()


if __name__ == '__main__':
    main()
