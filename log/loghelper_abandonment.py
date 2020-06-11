# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
考虑使用协程，所以废弃了多进程的日志记录方式
'''
import logging.handlers
import logging

loghelper = None


def getLogHelper():
    global loghelper
    if loghelper is None:
        socket_handler = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
        logging.getLogger().setLevel(logging.INFO)
        logging.getLogger().addHandler(socket_handler)
        loghelper = LogHelper()
    
    return loghelper


class LogHelper(object):
    
    @staticmethod
    def info(message):
        logging.info(message)
    
    @staticmethod
    def warn(message):
        logging.warn(message)
    
    @staticmethod
    def error(message):
        logging.error(message)
    
    @staticmethod
    def critical(message):
        logging.critical(message)


