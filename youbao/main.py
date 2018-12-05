import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import time
import random

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'

    qid = Column(VARCHAR(64), primary_key=True)
    question = Column(VARCHAR(255))
    url = Column(VARCHAR(255))

    def keys(self):
        return [c.name for c in self.__table__.columns]


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    user_name = Column(VARCHAR(255))
    avatar_file = Column(VARCHAR(255))

    def keys(self):
        return [c.name for c in self.__table__.columns]


class AwsUser(Base):
    __tablename__ = 'aws_users'

    uid = Column(INTEGER, primary_key=True)
    user_name = Column(VARCHAR(255))
    avatar_file = Column(VARCHAR(255))
    group_id = Column(INTEGER)
    reputation_group = Column(INTEGER)
    invitation_available = Column(INTEGER)


class AwsQuestion(Base):
    __tablename__ = 'aws_question'

    question_id = Column(INTEGER, primary_key=True)
    question_content = Column(VARCHAR(255))
    add_time = Column(INTEGER)
    published_uid = Column(VARCHAR(11))

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url1 = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('root', 123456,
                                                                             '47.75.49.133', 'user')
    engine1 = create_engine(database_url1, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session1 = scoped_session(sessionmaker(bind=engine1, autocommit=False))

    database_url2 = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine2 = create_engine(database_url2, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session2 = scoped_session(sessionmaker(bind=engine2, autocommit=False))

    # users = session1.query(User).all()
    # for user in users:
    #     aws_user = AwsUser(uid=user.id, user_name=user.user_name, avatar_file=user.avatar_file)
    #     session2.add(aws_user)
    # session2.commit()

    questions = session1.query(Question).all()
    for question in questions:
        print(question.question)
        uid = random.randint(11, 2000)
        aws_question = AwsQuestion(question_content=question.question, add_time=int(time.time()), published_uid=uid)
        session2.add(aws_question)
    session2.commit()
    # users = session2.query(AwsUser).all()
    # for user in users[1:]:
    #     user.group_id = 5
    #     user.invitation_available = 5
    #     user.reputation_group = 5
    # session2.commit()


if __name__ == '__main__':
    main()
