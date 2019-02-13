from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class Relation(Base):
    __tablename__ = 'relation'

    id = Column(INTEGER, primary_key=True)
    activity_id = Column(INTEGER)
    parent_id = Column(INTEGER)
    child_id = Column(INTEGER)

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('root', '4608310zk',
                                                                             '47.110.232.145', 'wechat')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    items = session.query(Relation).filter(Relation.activity_id == 8).all()

    print("总共扫码数:", len(items) - 1)
    result = dict()
    for item in items:
        if str(item.parent_id) in result:
            result[str(item.parent_id)] = result[str(item.parent_id)] + 1
        else:
            result[str(item.parent_id)] = 1

    print(len(result))
    print(result)


if __name__ == '__main__':
    main()