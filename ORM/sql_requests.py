from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import _sha256
from utils import utils
from configs.geturl import getUrlByConfigs

declarativeDataBase = declarative_base()


class UserData(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String, primary_key=True)

    firstname = Column('firstname', String)
    middlename = Column('middlename', String)
    lastname = Column('lastname', String)
    groupname = Column(JSON)

    def __repr__(self):
        return "".format(self.code)


class UserLogin(declarativeDataBase):
    __tablename__ = "UserLogin"

    id = Column("id", String, primary_key=True)

    username = Column('username', String)
    password = Column('password', String)
    identifier = Column(JSON)

    def __repr__(self):
        return "".format(self.code)


def get_engine():
    return create_engine(getUrlByConfigs())


# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
class ORM:
    @staticmethod
    def register_user(username, password, name, surname, phone="None", mail="None"):
        Session = sessionmaker(get_engine())
        db = Session()# init class

        userData = UserData(id=utils.generatePK(), firstname=name, middlename='Bebra', lastname=surname, groupname='default')
        userLogin = UserLogin(id=utils.generatePK(), username=username, password=_sha256.sha256(password.encode()).hexdigest(), identifier={"mail": mail,"phone":phone})

        db.add(userData)
        db.add(userLogin)
        db.commit()

        print('COMMITED SESSION')

