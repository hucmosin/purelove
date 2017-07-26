#! /usr/bin/env python
# -*- coding: utf-8 -*-


import json
"""
封装调用类，方便以后扩展
说明：字符类型转换
"""

class PLConvert(object):


    #--------------------------------------------------------------------

    #字符转整形
    @staticmethod
    def pl_to_int(string):
        assert isinstance(string, (basestring, int)) #判断是否是来自项目，出错终止点 ...
        return int(string)


    #--------------------------------------------------------------------

    #字符转字符
    @staticmethod
    def pl_to_str(string):
        assert isinstance(string, basestring)
        return str(string)

    
    #--------------------------------------------------------------------

    #判断真假
    @staticmethod
    def bool_field(string):
        assert isinstance(string, (basestring, int))
        if string.lower() == 'false' or string == '0':
            return False
        return bool(string)

    #--------------------------------------------------------------------

    #字符转json
    @staticmethod
    def json_field(string):
        assert isinstance(string, basestring)
        return json.loads(string)

    #--------------------------------------------------------------------

    #判断URL是否正确
    @staticmethod
    def url_field(string):
        assert isinstance(string, basestring)
        #判断是否以"HTTP"头开始，不是就加上并返回
        domain = string if string.startswith('http') else "http://{domain}".format(domain=string)
        return str(domain)
    #--------------------------------------------------------------------

    #小写字母转大写字母
    @staticmethod
    def pl_to_upper(str_or_words):
        if isinstance(str_or_words,str):
            value = str_or_words.decode('utf-8').upper()
            
        else:
            value = str_or_words.upper()

        return value

    #--------------------------------------------------------------------

    #大写字母转小写字母
    @staticmethod
    def pl_to_lower(str_or_words):
        if isinstance(str_or_words,str):
            value = str_or_words.decode('utf-8').lower()
            
        else:
            value = str_or_words.lower()

        return value

    #--------------------------------------------------------------------








            

