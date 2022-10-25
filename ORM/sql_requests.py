from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base

import _sha256
from utils import utils
from configs.geturl import getUrlByConfigs
from models.UserData import UserData
from models.UserLogin import UserLogin
from models.Session import CleanSession
from models.User import User

def get_engine():
    return create_engine(getUrlByConfigs())


def get_session():
    return sessionmaker(get_engine())()


# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
class ORM:
    @staticmethod
    def getUserId(_username):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(username=_username)).first()
        return user.id

    def getUsernameById(_id):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(id=_id)).first()
        return user.username

    @staticmethod
    def isUserRegisteredByUsername(_username):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(username=_username)).first()
        return user is not None
  
    @staticmethod
    def getAccessToken(_username):
        _id = ORM.getUserId(_username)
        db = get_session()
        user = db.scalars(select(CleanSession).filter_by(id=_id)).first()
        return user.accesstoken

    @staticmethod
    def loginCheck(_username, _password):
        db = get_session()
        user = db.scalars(select(UserLogin)
                          .filter_by(username=_username, password= utils.hash(_password))).first()
        return user is not None

    @staticmethod
    def isSessionExist(_username):
        db = get_session()
        _id = ORM.getUserId(_username)
        Session = db.scalars(select(CleanSession).filter_by(id=_id)).first()
        return Session is not  None

    # POST DB

    @staticmethod
    def refreshToken(_username):
        _id = ORM.getUserId(_username)

        db = get_session()
        Session = db.scalars(select(CleanSession).filter_by(id=_id)).first()
        Session.start_time = utils.getTime()
        db.commit()

        # print(f"TOKEN REFESHED: {_username}")

    @staticmethod
    def register_user(_user):
        db = get_session()

        userData = UserData(id=utils.generatePK(), firstname=_user.firstname, middlename=_user.middlename, lastname=_user.lastname, groupname='default')
        userLogin = UserLogin(id=utils.generatePK(), username=_user.username, password=utils.hash(_user.password), identifier=_user.identifier)

        db.add(userData) # Поле "userData" в БД
        db.add(userLogin) # Поле "userLogin" в БД
        db.commit()

        # print(f'COMMITED REGISTER USER {_user.firstname}')

    @staticmethod
    def createSession(_username):
        token = str(utils.genJWT(_username))
        _id = ORM.getUserId(_username)

        # Поле "Session" в БД
        Session = CleanSession(id=_id, accesstoken=token, start_time = utils.getTime())

        db = get_session()
        db.add(Session)
        db.commit()


    # root
    @staticmethod
    def getAllUsers():
        db = get_session()
        x = db.scalars(select(UserLogin).filter_by(username='mike')).first()
        return "id = " + str(x.id) + " username = " + str(x.username)
