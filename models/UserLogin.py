from sqlalchemy import String, Column, JSON
from sqlalchemy.ext.declarative import declarative_base

declarativeDataBase = declarative_base()


class UserLogin(declarativeDataBase):
    __tablename__ = "UserLogin"

    id = Column("id", String, primary_key=True)

    username = Column('username', String)
    password = Column('password', String)
    identifier = Column(JSON)

    def __repr__(self):
        return "".format(self.code)
