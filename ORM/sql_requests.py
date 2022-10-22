from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from configs.geturl import getUrlByConfigs

declarativeDataBase = declarative_base()


class UserRegister(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String)

    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    identifiers = Column(JSON)

    def __repr__(self):
        return "".format(self.code)


class ORM:
    @staticmethod
    def __init__(self):
        self.dataBase = create_engine(getUrlByConfigs())

    @staticmethod
    def register_user(self, username, password, name, surname, phone="None", mail="None"):
        session_class = sessionmaker(self.dataBase)
        session = session_class() # init class

        user = UserRegister(id = "123456789012345678", firstname = name, lastname = surname, identifiers= {"mail": mail,"phone":phone})
        print(user.id, user.identifiers)
