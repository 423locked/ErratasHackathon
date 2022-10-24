from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base

import _sha256
from utils import utils
from configs.geturl import getUrlByConfigs
from models.UserData import UserData
from models.UserLogin import UserLogin
from models.User import User

def get_engine():
    return create_engine(getUrlByConfigs())


def get_session():
    return sessionmaker(get_engine())()


# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
class ORM:
    @staticmethod
    def register_user(_user):
        db = get_session()

        print("IN REGISTER USER")
        userData = UserData(id=utils.generatePK(), firstname=_user.firstname, middlename=_user.middlename, lastname=_user.lastname, groupname='default')
        userLogin = UserLogin(id=utils.generatePK(), username=_user.username, password=utils.hash(_user.password), identifier=_user.identifier)

        db.add(userData)
        db.add(userLogin)
        db.commit()

        print('COMMITED REGISTER USER')

    @staticmethod
    def isUserRegisteredByUsername(_username):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(username=_username)).first()

        return user is not None

    @staticmethod
    def loginCheck(_username, _password):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(username=_username, password= utils.hash(_password))).first()
        return user is not None

    @staticmethod
    def getAllUsers():
        db = get_session()
        x = db.scalars(select(UserLogin).filter_by(username='mike')).first()
        return "id = " + str(x.id) + " username = " + str(x.username)