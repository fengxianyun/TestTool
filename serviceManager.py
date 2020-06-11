# coding: utf-8
'''
Created on 2020年6月8日

@author: 10226475
初始化单例资源的类，所有单例资源都通过此文件获取
'''


class ServiceManager():
    
    def __init__(self):
        self.log_helper = None
        self.proxy = None
        self.sql_connection = None
        self.task_manager = None
    
    def getProxy(self):
        return self.proxy
    
    def setProxy(self, proxy):
        self.proxy = proxy
    
    def getSQLConnection(self):
        return self.sql_connection
    
    def setSQLConnection(self, sql_connection):
        self.sql_connection = sql_connection
    
    def getTaskManager(self):
        return self.task_manager
    
    def setTaskManager(self, task_manager):
        self.task_manager = task_manager
    
    def getLogHelper(self):
        return self.log_helper
    
    def setLogHelper(self, log_helper):
        self.log_helper = log_helper
        
service_manager = ServiceManager()
