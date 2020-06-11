# coding: utf-8
'''
Created on 2020年4月13日

@author: 10226475
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TaskEntity(Base):
    __tablename__ = "Task"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    poc_name = Column("poc_name", String)
    base_url = Column("base_url", String)
    check_status = Column("check_status", String)
    attack_status = Column("attack_status", String)
    modify_timestamp = Column("modify_timestamp", String)
    args = Column("args", String)
    kwargs = Column("args", String)

