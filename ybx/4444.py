from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
import requests
import shutil

Base = declarative_base()

class AwsUser(Base):
    __tablename__ = 'aws_users'

    uid = Column(INTEGER, primary_key=True)
    question_count = Column(INTEGER)
    password = Column(VARCHAR(32))
    avatar_file = Column(VARCHAR(128))
    salt = Column(VARCHAR(16))
    is_first_login = Column(INTEGER)

    def keys(self):
        return [c.name for c in self.__table__.columns]


def main():
    database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format('kun', 1234567890,
                                                                             '39.104.65.73', 'ybx')
    engine = create_engine(database_url, encoding='utf8', pool_size=20,
                           pool_recycle=3600, echo=False, echo_pool=False)
    session = scoped_session(sessionmaker(bind=engine, autocommit=False))

    users = session.query(AwsUser).filter(AwsUser.uid >= 13, AwsUser.uid <= 2000).order_by(AwsUser.uid.asc())

    path = '/home/wwwroot/ybx2/domain/ybx.com/web/uploads/avatar/000/00/00/'

    for user in users:
        image = user.avatar_file
        if image.endswith('real.jpg'):
            m = image.replace('real', 'min')
            user.avatar_file = m
        # if image.startswith('http://'):
        #     uid = user.uid
        #     file_name = str(uid) + '_avatar_real.jpg'
        #     print(file_name)
        #     file = os.path.join(path, file_name)
        #     res = requests.get(image)
        #     with open(file, 'wb') as f:
        #         f.write(res.content)
        #     mid_file = os.path.join(path, str(uid) + '_avatar_mid.jpg')
        #     min_file = os.path.join(path, str(uid) + '_avatar_min.jpg')
        #     max_file = os.path.join(path, str(uid) + '_avatar_max.jpg')
        #     shutil.copyfile(file, mid_file)
        #     shutil.copyfile(file, max_file)
        #     shutil.copyfile(file, min_file)
        #     user.avatar_file = '000/00/00/' + file_name
    # session.commit()
    # session.remove()

    # for user in users:
    #     if user.is_first_login == 1:
    #         user.is_first_login = 0
    session.commit()
    session.remove()


if __name__ == '__main__':
    main()
