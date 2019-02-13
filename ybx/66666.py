from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class AwsQuestion(Base):
    __tablename__ = 'aws_question'

    question_id = Column(INTEGER, primary_key=True)
    question_content = Column(VARCHAR(255))
    add_time = Column(INTEGER)
    published_uid = Column(VARCHAR(11))

    def keys(self):
        return [c.name for c in self.__table__.columns]


class PostIndex(Base):
    __tablename__ = 'aws_posts_index'

    id = Column(INTEGER, primary_key=True)
    post_id = Column(INTEGER)
    post_type = Column(VARCHAR(16))
    uid = Column(INTEGER)


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    index = session.query(PostIndex).filter(PostIndex.post_type == 'question').all()

    for i in index:
        question_id = i.post_id
        question = session.query(AwsQuestion).filter(AwsQuestion.question_id == question_id).first()
        i.uid = question.published_uid
        print(i.id, i.uid, question.published_uid)

    session.commit()
    session.remove()


if __name__ == '__main__':
    main()
