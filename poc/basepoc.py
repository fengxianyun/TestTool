# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
'''
import abc


class BasePoc(metaclass=abc.ABCMeta):
    target = None
    log_helper = None
    
    def __init__(self):
        from log.loghelper import LogHelper
        self.log_helper = LogHelper
    
    @abc.abstractmethod
    def sendRequest(self) -> str:
        pass
    
    @abc.abstractmethod
    def checkRsult(self, res) -> (bool, str):
        pass
    
    @abc.abstractmethod
    def sendPoc(self) -> str:
        pass
    
    @abc.abstractmethod
    def checkPoc(self) -> str:
        pass
    
    @abc.abstractmethod
    def getPocName(self) -> str:
        pass
    
    def run(self, target: str):
        self.LogHelper.info("PocName is {}, target is {}".format(self.getPocName(), target))
        self.target = target
        self.LogHelper.info("{} start check weak point".format(self.getPocName()))
        res = self.sendRequest()
        result, poc = self.checkRsult(res)
        if result:
            self.LogHelper.info("{} have weak point, poc is {}".format(self.getPocName(), poc))
            # 增加将检查结果送入检查队列的内容
        else:
            self.LogHelper.info("don't have weak point".format(self.getPocName(), poc))
            return
        self.LogHelper.info("{} start attack weak point".format(self.getPocName()))
        res = self.sendPoc()
        result = self.checkPoc(res)
        self.LogHelper.info("{} start attack result: {}".format(self.getPocName(), result))
        # 增加将攻击结果送入结果队列的内容

