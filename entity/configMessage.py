# coding: utf-8
'''
Created on 2020年5月24日

@author: raytine
'''


class ConfigMessage():
    
    def __init__(self):
        self.__reverse_ip = None
        self.__reverse_port = None
        self.__headers = None
        self.__proxy = None
    
    @property
    def reverse_ip(self):
        return self.__reverse_ip
    
    @reverse_ip.setter
    def reverse_ip(self, ip: str):
        self.__reverse_ip = ip
    
    @property
    def reverse_port(self):
        return self.__reverse_port
    
    @reverse_port.setter
    def reverse_port(self, port: int):
        self.__reverse_port = port
    
    @property
    def headers(self):
        return self.__headers
    
    @headers.setter
    def headers(self, headers: dict):
        self.__headers = headers
    
    @property
    def proxy(self):
        return self.__proxy
    
    @proxy.setter
    def proxy(self, proxy):
        self.__proxy = proxy