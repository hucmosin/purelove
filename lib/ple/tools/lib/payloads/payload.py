#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2016-2017
"""

import os
import sys
import json
from dotted import DottedDict
from abc import ABCMeta, abstractmethod



"""
封装调用类，方便以后扩展
"""

class BGConvert(object):
    """
    参数转换，工具调用
    """
    @staticmethod
    def int_field(string):
        assert isinstance(string, (basestring, int)) #判断是否是来自项目，出错终止点 ...
        return int(string)

    @staticmethod
    def str_field(string):
        assert isinstance(string, basestring)
        return str(string)

    @staticmethod
    def bool_field(string):
        assert isinstance(string, (basestring, int))
        if string.lower() == 'false' or string == '0':
            return False
        return bool(string)

    @staticmethod
    def json_field(string):
        assert isinstance(string, basestring)
        return json.loads(string)

    @staticmethod
    def url_field(string):
        assert isinstance(string, basestring)
        #判断是否以"HTTP"头开始，不是就加上并返回
        domain = string if string.startswith('http') else "http://{domain}".format(domain=string)
        return str(domain)

    @staticmethod
    def email_field(string):
        # TODO: there is no need to implement this in here
        assert isinstance(string, basestring)
        return string

class BGExploit(object):
    __metaclass__ = ABCMeta   #虚拟抽象本类

    convert  = BGConvert()    #参数转换

    def __init__(self):
        super(BGExploit, self).__init__()  #初始化
        self.options    = {}                #新增参数


    def register_option(self, dict_option):
        assert isinstance(dict_option, dict)
        self.options = DottedDict(dict_option)
        
    """
    payload框架利用输出
    """
        
    @abstractmethod
    def payload(self):
        pass

