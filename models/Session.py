from sqlalchemy import String, Column
from sqlalchemy.ext.declarative import declarative_base

declarativeDataBase = declarative_base()


class CleanSession(declarativeDataBase):
    __tablename__ = "Session"

    id = Column("id", String, primary_key=True)

    accesstoken = Column('accesstoken', String)
    start_time = Column('start_time', String)

    def __repr__(self):
        return "".format(self.code)