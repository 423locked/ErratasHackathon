from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from configs.geturl import getUrlByConfigs

declarativeDataBase = declarative_base()


'''class UserRegister(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String)

    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    identifiers = Column(JSON)

    def __repr__(self):
        return "".format(self.code)'''


def get_engine():
    return create_engine(getUrlByConfigs())


class ORM:
    @staticmethod
    def register_user(username, password, name, surname, phone="None", mail="None"):
        session_class = sessionmaker(get_engine())
        session = session_class()# init class

        #user = UserRegister(id = "123456789012345678", firstname = name, lastname = surname, identifiers= {"mail": mail,"phone":phone})
        #print(user.id, user.identifiers)
        print('aint no way')
