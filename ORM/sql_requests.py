from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from configs.geturl import getUrlByConfigs

declarativeDataBase = declarative_base()


class UserRegister(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String, primary_key=True)

    firstname = Column('firstname', String)
    middlename = Column('middlename', String)
    lastname = Column('lastname', String)
    identifiers = Column(JSON)

    def __repr__(self):
        return "".format(self.code)


def get_engine():
    return create_engine(getUrlByConfigs())


#https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
class ORM:
    @staticmethod
    def register_user(username, password, name, surname, phone="None", mail="None"):
        Session = sessionmaker(get_engine())
        session = Session()# init class

        user = UserRegister(id="123456789012345678", firstname = name, middlename='Bebra', lastname = surname, identifiers= {"mail": mail,"phone":phone})

        session.add(user)
        session.commit()

        print('COMMITED SESSION')

