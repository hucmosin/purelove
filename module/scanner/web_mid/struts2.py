#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

#模块使用说明
docs = '''

#title                  :Struts2 Struts2漏洞集合
#description            :Struts2漏洞集合
#author                 :mosin
#date                   :20171009
#version                :0.1
#notes                  :
#python_version         :2.7.5

'''

from modules.exploit import BGExploit
from lib.ple.vfunc.strut2 import load_struts_frame as smain

class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "Struts2漏洞集合",  # 该POC的名称
            "product": "Struts2漏洞集合",  # 该POC所针对的应用名称,
            "product_version": "1.0",  # 应用的版本号
            "desc": '''
                Struts漏洞集合s-05-s045
            ''',  # 该POC的描述
            "author": ["Mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2017-10-17",  # 漏洞公开时间
            "create_date": "2017-10-17",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "target": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "目标URL",
                "Required":"no"
            },
            "port": {
                "default": "",
                "convert": self.convert.int_field,
                "desc": "目标端口",
                "Required":""
            },
            "debug": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "用于调试，排查poc中的问题",
                "Required":""
            },
            "mode": {
                "default": "exploit",
                "convert": self.convert.str_field,
                "desc": "执行exploit,或者执行payload",
                "Required":""
            },
            "filename": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "批量文件目录",
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
            "description": "Exploit Error.",
            "error": ""
        })

    def payload(self):
        pass

    def exploit(self):
        try:
            url = self.option.target['default']
            filename = self.option.filename['default']
            smain.s_main(url,filename)
        except:
            print_error(self.result.description)


#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())
