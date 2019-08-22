from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class User_Base(Base):
    __tablename__ = 'user_base'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    openid = Column(VARCHAR(255), unique=True)
    nickname = Column(VARCHAR(255), nullable=False)
    image_url = Column(VARCHAR(255), nullable=False)
    gender = Column(VARCHAR(12))
    province = Column(VARCHAR(255))
    city = Column(VARCHAR(255))
    country = Column(VARCHAR(255))
    create_time = Column(DATETIME, default=datetime.now(), nullable=False)

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('root', '4608310zk',
                                                                             '47.75.49.133', 'youbao_sql')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    users = session.query(User_Base).filter(User_Base.openid == 'ohRGKwRuo7TvxQCC8VMVpanWhvuA').first()

    print(users.nickname)

if __name__ == '__main__':
    main()
