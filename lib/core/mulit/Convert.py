#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Convert:
    """
    参数转换，工具调用
    """
    @staticmethod
    def convert_int_field(string):
        assert isinstance(string, (basestring, int)) #判断是否是来自项目，出错终止点 ...
        return int(string)

    @staticmethod
    def convert_str_field(string):
        assert isinstance(string, basestring)
        return str(string)

    @staticmethod
    def convert_bool_field(string):
        assert isinstance(string, (basestring, int))
        if string.lower() == 'false' or string == '0':
            return False
        return bool(string)

    @staticmethod
    def convert_json_field(string):
        assert isinstance(string, basestring)
        return json.loads(string)

    @staticmethod
    def convert_url_field(string):
        assert isinstance(string, basestring)
        #判断是否以"HTTP"头开始，不是就加上并返回
        domain = string if string.startswith('http') else "http://{domain}".format(domain=string)
        return str(domain)

    @staticmethod
    def convert_ip(address):
        """ Convert IP to bytes"""
        try:
            res = ""
            for i in address.split("."):
                res += chr(int(i))
            return res
        except:
            print "[-] Convert ip Error."

    @staticmethod
    def convert_port(port):
        """ Convert Port to bytes"""
        try:
            res = "%.4x" % int(port)
            return res.decode('hex')
        except:
            print "[-] Convert port Error."
            
    @staticmethod
    def convert_addr2dec(address):
        #"将点分十进制IP地址转换成十进制整数"
        items = [int(x) for x in addr.split(".")]
        return sum([items[i] << [24, 16, 8, 0][i] for i in range(4)])
    
    @staticmethod
    def convert_dec2addr(dec):
        #"将十进制整数IP转换成点分十进制的字符串IP地址"
        return ".".join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])
