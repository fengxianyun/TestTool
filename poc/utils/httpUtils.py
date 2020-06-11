# coding: utf-8
'''
Created on 2020年5月22日

@author: raytine
'''
import requests
from requests.exceptions import ChunkedEncodingError, ConnectionError, ConnectTimeout


# TODO:抛出异常太多了，尝试使用aop的思想替换

def get(url, headers=None, encoding='UTF-8', proxies=None, tiemout=10):
    """GET请求发送包装"""
    try:
        html = requests.get(url, headers=headers, proxies=proxies, timeout=tiemout)
        html = html.content.decode(encoding)
        return html.replace('\x00', '').strip()
    except ChunkedEncodingError as e:
        html = get_stream(url, headers, encoding, proxies, tiemout)
        return html
    except ConnectionError as e:
        raise ConnectionError("ERROR:" + "HTTP连接错误")
    except ConnectTimeout as e:
        raise ConnectTimeout("ERROR:" + "HTTP连接超时错误")
    except Exception as e:
        raise Exception('ERROR:' + str(e))


def get_stream(url, headers=None, encoding='UTF-8', proxies=None, tiemout=10):
    """分块接受数据"""
    try:
        lines = requests.get(url, headers=headers, proxies=proxies, timeout=tiemout, stream=True)
        html = list()
        for line in lines.iter_lines():
            if b'\x00' in line:
                break
            line = line.decode(encoding)
            html.append(line.strip())
        return '\r\n'.join(html).strip()
    except ChunkedEncodingError as e:
        return '\r\n'.join(html).strip()
    except ConnectionError as e:
        raise ConnectionError("ERROR:" + "HTTP连接错误")
    except ConnectTimeout as e:
        raise ConnectTimeout("ERROR:" + "HTTP连接超时错误")
    except Exception as e:
        raise Exception('ERROR:' + str(e))


def post(url, data=None, headers=None, encoding='UTF-8', files=None, proxies=None, tiemout=10):
    """POST请求发送包装"""
    try:
        html = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=tiemout, files=files)
        html = html.content.decode(encoding)
        return html.replace('\x00', '').strip()
    except ChunkedEncodingError as e:
        html = post_stream(url, data, headers, encoding, files)
        return html
    except ConnectionError as e:
        raise ConnectionError("ERROR:" + "HTTP连接错误")
    except ConnectTimeout as e:
        raise ConnectTimeout("ERROR:" + "HTTP连接超时错误")
    except Exception as e:
        raise Exception('ERROR:' + str(e))


def post_stream(url, data=None, headers=None, encoding='UTF-8', files=None, proxies=None, tiemout=10):
    """分块接受数据"""
    try:
        lines = requests.post(url, data=data, headers=headers, timeout=tiemout, stream=True, proxies=proxies,
                              files=None)
        html = list()
        for line in lines.iter_lines():
            line = line.decode(encoding)
            html.append(line.strip())
        return '\r\n'.join(html).strip()
    except ChunkedEncodingError as e:
        return '\r\n'.join(html).strip()
    except ConnectionError as e:
        raise ConnectionError("ERROR:" + "HTTP连接错误")
    except ConnectTimeout as e:
        raise ConnectTimeout("ERROR:" + "HTTP连接超时错误")
    except Exception as e:
        raise Exception('ERROR:' + str(e))
