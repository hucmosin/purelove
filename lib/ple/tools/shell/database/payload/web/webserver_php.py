#! /usr/bin/env python
# -*- coding: utf-8 -*-

from lib.ple.tools.lib.payloads.payload import * 



class Payload(BGExploit):
        
    def __init__(self):
        super(self.__class__, self).__init__()

        #自定义显示参数
        self.register_option({
            "FILEPATH": {
                "default": "/test.php",
                "desc": "保存文件的路径名",
                "Required":"no"
            }
        })


    #写出文件
    def write_php(self,file_data,path_name):
        print u"[+] 保存中..."
        ff = open(path_name,'w')
        ff.write(file_data)
        ff.close()
        print u"[+] 文件保存路径在" + path_name

    #打开文件
    def open_file(self):
        try:
            f = open('lib/soure/web/shell/php.shell','r')
            file_data = f.read()
        except:
            print "[-] TempleteFile Open Fail"
        return file_data
        
    def payload(self):
        path_name = self.options.FILEPATH['default']
        print u"[+] 正在提取文件..."
        get_data = self.open_file()
        self.write_php(get_data,path_name)
