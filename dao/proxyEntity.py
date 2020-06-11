# coding: utf-8
'''
Created on 2020年6月3日

@author: 10226475
'''
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProxyEntity(Base):
    __tablename__ = "proxy"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    ip = Column("ip", String)
    port = Column("port", Integer)
    is_default = Column("is_default", Boolean)
    is_select = Column("is_select", Boolean)
