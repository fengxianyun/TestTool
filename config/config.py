# coding: utf-8
'''
Created on 2020年5月24日

@author: raytine
'''
from entity.configMessage import ConfigMessage
from config.header import *
from config.proxy import *
from config.reverseMessage import *


def getConfigMessage() -> ConfigMessage:
    configMessage = ConfigMessage()
    configMessage.headers = getDefaultHeader()
    configMessage.proxy = getDefaultProxy()
    configMessage.reverse_ip, configMessage.reverse_port = getDefaultReverseMessage()
    return configMessage
