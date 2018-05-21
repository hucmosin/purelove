#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

#模块使用说明
docs = '''

#==============================================================================
#title                  :example
#description            :This is poc speak
#author                 :mosin
#date                   :20170609
#version                :0.1
#usage                  :python example
#notes                  :
#python_version         :2.7.5
#==============================================================================

'''

from modules.exploit import BGExploit



class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "",  # 该POC的名称
            "product": "",  # 该POC所针对的应用名称,
            "product_version": "",  # 应用的版本号
            "desc": '''

            ''',  # 该POC的描述
            "author": [""],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "listen": self.handler.listen,  #开启监听
            "payload": self.handler.payload, #payload监听模块名称
            "disclosure_date": "2017-05-17",  # 漏洞公开时间
            "create_date": "2017-06-17",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "target": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "目标",
                "Required":"no"
            },
            "port": {
                "default": 4444,
                "convert": self.convert.int_field,
                "desc": "端口",
                "Required":"no"
            },
            "mode": {
                "default": "payload",
                "convert": self.convert.str_field,
                "desc": "执行exploit,或者执行payload",
                "Required":"no"
            },
            #以下内容可以自定义
            "example": {
                "default": "",
                "prints": "HELLO PURELOVE",
                "desc": "例如",
                "Required":"no"
            }
        })
        
        #自定义返回内容
        self.register_result({
            #检测标志位，成功返回置为True,失败返回False
            "status": False,
            "exp_status":False, #exploit，攻击标志位，成功返回置为True,失败返回False
            #定义返回的数据，用于打印获取到的信息
            "data": {

            },
            #程序返回信息
            "description": "this is test ",
            "error": ""
        })


    def payload(self):
        """
        检测类型
        :return:
        """
        pass

    def exploit(self):
        """
        攻击类型
        :return:
        """
        pass


#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())
