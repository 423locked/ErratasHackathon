from sqlalchemy import String, Column, JSON
from sqlalchemy.ext.declarative import declarative_base

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
