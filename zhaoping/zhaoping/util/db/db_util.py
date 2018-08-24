# coding:utf-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
url = 'mysql+pymysql://root:root@localhost/spider_tools?charset=utf8'
engine = create_engine(url, echo=False)


class DB_Util(object):
    @staticmethod
    def get_session(url=None):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    @staticmethod
    def init_db():
        Base.metadata.create_all(engine)


class ZhilianCompany(Base):
    __tablename__ = 't_ZhilianCompany'
    job = Column(String(100), primary_key=True)
    salary = Column(String(100), nullable=True)
    position = Column(String(100), nullable=True)
    education = Column(String(30), nullable=True)
    operatinghours = Column(String(30), nullable=True)
    company = Column(String(30),nullable=True)
