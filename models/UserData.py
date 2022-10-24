from ORM.sql_requests import declarativeDataBase
from sqlalchemy import Column, String, JSON


class UserData(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String, primary_key=True)

    firstname = Column('firstname', String)
    middlename = Column('middlename', String)
    lastname = Column('lastname', String)
    groupname = Column(JSON)

    def __repr__(self):
        return "".format(self.code)
