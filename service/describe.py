# coding: utf-8
'''
Created on 2020年6月1日

@author: 10226475
提供查询功能的文件
从注释和函数中提取这个函数需要哪些参数、参数是否必选、参数描述等信息
'''
import inspect
import collections


def getFuncDescribe(func):
    func_model = initFuncModel(func)
    optimizeFuncModelWithNotes(func, func_model)
    return func_model


def initFuncModel(func):
    # 通过insprct提取参数
    result = inspect.getfullargspec(func)
    args = result[0]
    varargs = result[1]
    varkw = result[2]
    defaults = result[3]
    kwonlyargs = result[4]
    kwonlydefaults = result[5]
    annotations = result[6]
    save_dict = collections.OrderedDict()
    # 初始化处理变量
    for item in args:
        save_dict[item] = {'default': "", "describe": "", "type": "unknow"}
    # 处理变量默认值
    add_defaults = [""] * (len(args) - len(defaults))
    defaults = add_defaults + list(defaults)
    for index, key in enumerate(save_dict.keys()):
        save_dict[key]["default"] = defaults[index]
    # 初始化*args之后**kwargs之前的变量
    for item in kwonlyargs:
        save_dict[item] = {'default': "", "describe": "", "type": "unknow"}
    # 处理*args之后**kwargs之前的变量默认值
    for key, val in kwonlydefaults.items():
        save_dict[key]["default"] = val
    # 处理*args
    if varargs is not None:
        save_dict[varargs] = {'default': None, "describe": "other values", "type": "unknow"}
    # 处理**kwargs
    if varkw is not None:
        save_dict[varkw] = {'default': None, "describe": "other kw values", "type": "unknow"}
    # 处理类型参数
    for key, val in annotations.items():
        save_dict[key]["type"] = str(val)
    return save_dict


def optimizeFuncModelWithNotes(func, func_model):
    notes = func.__doc__.split("\n")
    keywords = set(["return", "exception"])
    for line in notes:
        line = line.strip()
        if ":" not in line:
            continue
        split_result = line.split(":")
        if len(split_result) !=2:
            continue
        key, val = split_result
        if key is "para":
            continue
        if key in keywords:
            continue
        if key in func_model:
            func_model[key]["describe"] = val
        
        

def getClassDescribe(class_object):
    pass


def getFuncWithKeyWord():
    pass

if __name__ == "__main__":
    def test1(b, a=1, c=2):
        pass
    def test2(b, a=1, *args, **kwargs):
        pass
    def test3(b: int, a: int=1, *args, c=2, d, e=3, **kwargs):
        """
        .反弹shell
        para:
            a:反弹shell接收ip
            b:反弹shell接收端口
        return:
            shell_message
        exception:
            None
        """
        pass
    print(getFuncDescribe(test3))

