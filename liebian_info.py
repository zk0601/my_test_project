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


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True)
    nickname = Column(VARCHAR(100))


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('root', '4608310zk',
                                                                             '47.110.232.145', 'wechat')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    items = session.query(Relation).filter(Relation.activity_id == 8).all()

    print("总共扫码数:", len(items))
    result = dict()
    for item in items:
        if str(item.parent_id) in result:
            result[str(item.parent_id)] = result[str(item.parent_id)] + 1
        else:
            result[str(item.parent_id)] = 1

    print("总共被扫人数:", len(result))
    result = [(k, v) for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True)]
    for i, item in enumerate(result):
        id, count = item[0], item[1]
        if id == '0':
            continue
        name = session.query(User).filter(User.id == int(id)).first().nickname
        print("排行第%s位的是:%s, 他的助力次数为%s次" % (i+1, name, count))

    session.remove()


if __name__ == '__main__':
    main()