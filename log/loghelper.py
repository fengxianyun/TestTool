# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
'''
import logging


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

