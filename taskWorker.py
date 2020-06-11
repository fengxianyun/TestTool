# coding: utf-8
'''
Created on 2020年6月6日

@author: 10226475
'''
from testQueue import queue
from serviceManager import service_manager
# from taskCondition import condition


class TaskWorker():
    
    def __init__(self, worker_id):
        self.id = worker_id
        self.log_helper = service_manager.getLogHelper()
        self.log_helper.info("start init worker {}".format(worker_id))
    
    async def run(self, condition):
        while True:
            self.log_helper.info("worker {} start run".format(self.id))
            task = self.getTask()
            if task is None:
                self.log_helper.info("worker {} task is None".format(self.id))
                async with condition:
                    await condition.wait()
                self.log_helper.info("worker {} get notify message".format(self.id))
                continue
            self.log_helper.info("worker {} start to do task".format(self.id))
    
    def getTask(self):
        result = None
        try:
            result = queue.get_nowait()
        except:
            result = None
        return result
