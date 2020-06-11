# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
'''
import abc
from log.loghelper import getLogHelper


class BasePoc(metaclass=abc.ABCMeta):
    target = None
    log_helper = None
    success_status = "success"
    fail_status = "fail"
    uncertain_status = "uncertain"
    
    def __init__(self):
        self.log_helper = getLogHelper()
        
    @abc.abstractmethod
    def getFunctionList(self) -> list:
        pass
    
    @abc.abstractmethod
    def execFunction(self) -> str:
        pass
    
    @abc.abstractmethod
    def sendRequest(self) -> str:
        pass
    
    @abc.abstractmethod
    def checkResult(self, res) -> str:
        '''
        .结果分为三种
        success
        fail
        uncertain
        '''
        pass
    
    @abc.abstractmethod
    def sendDefaultPoc(self) -> str:
        pass
    
    @abc.abstractmethod
    def checkPoc(self) -> str:
        pass
    
    @abc.abstractmethod
    def getPocInfo(self) -> str:
        pass
    
    def run(self, target: str):
        self.LogHelper.info("PocName is {}".format(self.getPocName()))
        self.LogHelper.info("{} start check weak point".format(self.getPocName()))
        res = self.sendRequest()
        result, poc = self.checkResult(res)
        if result:
            self.LogHelper.info("{} have weak point, poc is {}".format(self.getPocName(), poc))
            # 增加将检查结果送入检查队列的内容
        else:
            self.LogHelper.info("don't have weak point".format(self.getPocName(), poc))
            return
        self.LogHelper.info("{} start attack weak point".format(self.getPocName()))
        res = self.sendDefaultPoc()
        result = self.checkPoc(res)
        self.LogHelper.info("{} start attack result: {}".format(self.getPocName(), result))
        # 增加将攻击结果送入结果队列的内容


