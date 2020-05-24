# coding: utf-8
'''
Created on 2020年5月22日

@author: raytine
'''
import shlex


def parse_cmd(cmd, type='string'):
    """命令解析，将要执行的命令解析为字符串格式"""
    cmd = shlex.split(cmd)
    if type == 'string':
        cmd_str = '"' + '","'.join(cmd) + '"'
    elif type == 'xml':
        cmd_str = '<string>' + '</string><string>'.join(cmd) + '</string>'
    else:
        cmd_str = cmd
    return cmd_str
