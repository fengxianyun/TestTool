# coding: utf-8
'''
考虑使用协程，所以废弃了多进程的日志记录方式
'''
import logging
from logging import handlers
import sys
import os


class LogHelper(object):
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, file_name, file_path=None, maxBytes=2048, backupCount=20):
        if not file_path:
            file_path = sys.path[0]
        file_path = os.path.join(file_path, file_name)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S')
        self.logger = logging.getLogger('mylogger')
        
        file_handler = handlers.RotatingFileHandler(file_path, maxBytes=maxBytes, backupCount=backupCount)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'))
        logging.getLogger('mylogger').addHandler(file_handler)
        
    def info(self, msg):
        self.logger.info(msg)
        
    def warn(self, msg):
        self.logger.warn(msg)
        
    def error(self, msg):
        self.logger.error(msg)
        
    def debug(self, msg):
        logging.debug(msg)


if __name__ == '__main__':
    mylog = Log('test')
    mylog.debug('llll')
    mylog.info('hhh')
    mylog.warn('fhjosiadf')
    mylog.error('dddddd')

