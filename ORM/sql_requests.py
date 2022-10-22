from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from configs.hosts import *

declarativeDataBase = declarative_base()

class NewUserData(declarativeDataBase):
    __tablename__ = "UserData"

    id = Column("id", String)

    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    identifiers = Column({"mail":"value", "phone":"value"}, JSON)

    def __repr__(self):
        return "".format(self.code)


class SQLrequests:

	def __init__(self):
		host_url = f"postgresql://{HOST_USER}:{HOST_PASS}@{HOST_IP}:{HOST_PORT}/{DB_NAME}"
		self.dataBase = create_engine(db_string)


	def register_user(username, password, name, surname, phone="None", mail="None"):
		session = self.Session_class() # init class

		user = NewUserData(id = "123456789012345678", firstname = name, lastname = surname, identifiers= {"mail": mail,"phone":phone})
		print(user.id,user.identifiers)


s = SQLrequests()

s.register_user(username="alah",password="asd",name = "Bob", surname = "Dilan")
