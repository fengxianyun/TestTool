# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
.测试多进程下的日志记录
'''
from log.loginit import LogInit
from poc.struts.S2001 import Struts001
import multiprocessing as mp
import time
import logging
import os


def job():
    for i in range(10):
        base_poc = Struts001("123")
        base_poc.log_helper.info(i)

if __name__ == "__main__":
    print(1)
    LogInit.init()
    print(2)
    p1 = mp.Process(target=job)
    p2 = mp.Process(target=job)
    p3 = mp.Process(target=job)
    p4 = mp.Process(target=job)
    p5 = mp.Process(target=job)
    print(3)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    print(4)


