#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
说明：该类用于接收框架的参数,并提供文件操作函数
"""

# python standard library
import os
import sys

root_path = "../"
sys.path.append(root_path)

# local pret classes
import pl_shell_cmd_const as const
import pl_os_operation as operation
import pl_file_ch as ch
import modules.getinfo as getinfo
import pl_print_world_color as setcolor


#用于打印poc用法
def usage():
    usages = '''

Module Main Console Help
-------------------------

    info        Display module information
    set         Set module parameters
    show        show options settings information
    run         Run Module
    exploit     Run Module
    unset       Unset options
    
'''
    print usages

#执行poc
def read_cmd_lines(poc_re,PL_POC_FILE, poc_module_path_first_name, poc_module_path_end_name):
    poc = getinfo.import_pocs(PL_POC_FILE) #导入poc主函数
    while True:
        ple = setcolor.UseStyle("ple",mode = 'underline')
        poc_shell_input = raw_input(ple + " " + poc_module_path_first_name + "(" + poc_module_path_end_name +") > ").strip().lower()
          
        if poc_shell_input == const.PL_BACK:
            return
        else:
            if poc_shell_input[:3] == const.PL_SET:
                poc_shell = poc_shell_input[3:].strip().lower()
                if poc_shell == None:
                    pass
                else:
                    try:
                        poc_shells   = poc_shell.split(" ")
                        option_key   = poc_shells[0]
                        option_value = poc_shells[1]
                        for option, option_filter in poc.option.items():
                            if option_filter['default'] == None:
                                option_filter['default'] = ''
                            if option_filter['desc'] == None:
                                option_filter['desc'] = ''
                        for option, option_filter in poc.option.items():
                            if option_key == option:
                                if option_filter['Required'] == "":
                                    print setcolor.set_yellow("[-] ") + "参数为固定值,无法修改!"
                                else:
                                    print option_key + " => " + option_value
                                    option_filter['default'] = option_filter['convert'](option_value) #转换option的类型
                                    option_filter['Required'] = "yes"
                            if not option_key:
                                pass
                    except:
                        print setcolor.set_red("[!] ") + "参数错误"
            elif poc_shell_input == const.PL_INFO:
                ch.pl_show_poc_info(PL_POC_FILE) 
            elif poc_shell_input == const.PL_RUN or poc_shell_input == const.PL_EXPLOIT: #后期更改时，改为全局变量const
                ch.pl_run_poc(poc)
            elif poc_shell_input == const.PL_SHOW_OPTIONS:
                ch.pl_run_poc_show(poc,poc_re)
            elif poc_shell_input == const.PL_HELP or poc_shell_input == "?":
                usage()
            elif poc_shell_input[:5] == "unset":
                try:
                    poc_shell = poc_shell_input[5:].strip().lower()
                    print poc_shell
                    for option, option_filter in poc.option.items():
                        if poc_shell == option:
                            print poc_shell + " => unset" 
                            option_filter['default'] = "" #转换option的类型
                            option_filter['Required'] = "no"
                        if not poc_shell:
                            pass
                except:
                    print setcolor.set_red("[!] ") + "参数错误"
                
                #监听shell,暂不开放
            #elif poc_shell_input[:10] == "set hander":
                #poc_shell = poc_shell_input[10:].strip().lower()
                #if poc_shell == None:
                    #pass
                #else:
                    #poc.hander.listen = True
                    #pl_set_hander(poc)
            else:
                #print "error please debug"
                pass

#-------------------------------------------------------------------------------


#设置hander模块，
def pl_set_hander(poc):
    if poc.hander.listen:
        lhost = poc.hander.LHOST
        lport = poc.hander.LPORT
        pl_hander_loop(lhost,lport)


#监听端口
def pl_hander_loop(lhost,lport):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((lhost, lport))
    server.listen()
    print "[+] Start Listening host %s..." %lhost
    print "[+] Start Listening port %s..." %lport
    while True:
        #接收shell和发送客户端信息
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((lhost, lport))
    server.listen(1)
    BUFSIZ = 2048
    print "[+] Start Listening host %s..." %lhost
    print "[+] Start Listening port %s..." %lport
    while True:
        #接收shell和发送客户端信息
        client, addr = server.accept()
        data = raw_input('pl_shell >')
        try:
            client.send(data.encode('utf-8'))
            if data.upper()=="BACK":
                break
            #backdoor出错必须返回空，否则将死循环
            os_result = client.recv(BUFSIZ)
            if os_result == "":
                client.close()
                break
        except:
            client.close()
            break
        print (os_result)





            
