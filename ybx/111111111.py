#coding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import random
import sys
import traceback

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


class AwsAction(Base):
    __tablename__ = 'aws_user_action_history'

    history_id = Column(INTEGER, primary_key=True)
    uid = Column(INTEGER)
    associate_id = Column(INTEGER)
    associate_action = Column(INTEGER)

    def keys(self):
        return [c.name for c in self.__table__.columns]


class PostIndex(Base):
    __tablename__ = 'aws_posts_index'

    id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER)
    post_type = Column(VARCHAR(16))
    uid = Column(INTEGER)

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main(uid):
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    try:
        questions = session.query(AwsQuestion).filter(AwsQuestion.published_uid == uid).all()
        print("选择的用户为: %s" % uid)
        for question in questions:
            qid = question.question_id
            print('对问题id为：%s的问题进行操作' % qid)
            uuid = random.randint(11, 2000)
            print('随机到的用户id为：%s' % uuid)
            question.published_uid = uuid
            index = session.query(PostIndex).filter(PostIndex.post_id == qid, PostIndex.post_type == 'question').first()
            index.uid = uuid
            session.flush()
            actions = session.query(AwsAction).filter(AwsAction.associate_id == qid, AwsAction.associate_action == 101).all()
            for action in actions:
                print('处理的action为%s' % action.history_id)
                action.uid = uuid
            session.flush()
            uuser = session.query(AwsUser).filter(AwsUser.uid == uuid).first()
            print('用户：%s的提出问题数目加1' % uuser.uid)
            uuser.question_count = uuser.question_count + 1
            session.flush()
        user = session.query(AwsUser).filter(AwsUser.uid == uid).first()
        user.question_count = 0
        session.commit()
        print("完成")

    except Exception as e:
        print(e)
        print(traceback.print_exc())
        session.rollback()
    finally:
        session.remove()


if __name__ == '__main__':
    for i in range(2007, 2028):
        main(i)
