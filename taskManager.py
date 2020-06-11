# coding: utf-8
'''
Created on 2020年4月8日

@author: 10226475
'''
from multiprocessing.pool import worker

'''
.任务模块，主要用于多进程/协程处理任务
本来考虑使用多进程实现，后来经过考虑还是使用协程实现比较好，主要有以下理由
1.性能方面使用协程可以达到很高的并发，使用多进程更适合于cpu密集型任务。使用python进程池的话更是限制只会最多有cpu核数的进程。
2.新建、销毁进程的开销明显更大
3.调试方面，多进程必定要考虑到各种锁，数据库锁、日志锁、等等各种共享资源都要考虑占用问题。而协程仍然是单线程，很大程度上这些贡献资源都可以直接使用
'''

import asyncio
from threading import Thread
from taskWorker import TaskWorker
from serviceManager import service_manager
from testQueue import queue
# from taskCondition import condition


class TaskManager():
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, coroutine_num):
        # 初始化
        service_manager.getLogHelper().info("start init taskManager")
        self.coroutine_num = coroutine_num
        self.workers = []
        self.loop = asyncio.new_event_loop()
        self.condition = asyncio.Condition(loop=self.loop)
        self.log_helper = service_manager.getLogHelper()
        self.__initCoroutine()
    
    def __initCoroutine(self):
        service_manager.getLogHelper().info("start init Coroutine")
        for index, _ in enumerate(range(self.coroutine_num)):
            task_worker = TaskWorker(index)
            self.workers.append(task_worker)
        t = Thread(target=self.__initWorker, args=(self.loop,))
        t.start()
        for worker in self.workers:
            asyncio.run_coroutine_threadsafe(worker.run(self.condition), self.loop)
        service_manager.getLogHelper().info("Coroutine init end")
    
    def __initWorker(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    def addTask(self, poc_name, *args, **kwargs):
        queue.put_nowait(poc_name)
        asyncio.run_coroutine_threadsafe(self.notify(), self.loop)
    
    async def notify(self):
        async with self.condition:
            self.condition.notify()
            self.log_helper.info("send notify message")
    
    def addTaskToDataBase(self):
        pass
    
    def deleteTask(self):
        pass

if __name__ == "__main__":
    from log.loghelper import LogHelper
    loghelper = LogHelper("log.txt")
    service_manager.setLogHelper(loghelper)
    taskmanager = TaskManager(10)
    while True:
        poc_name = input("input poc\n")
        taskmanager.addTask(poc_name)
