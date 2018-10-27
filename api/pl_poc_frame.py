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


def usage():
    usages = '''

Module Main Console Help
-------------------------

    use                 Select an module by name
    info                Display module information
    set                 Set module parameters
    back                Back purelove frame
    show options        Show options settings information
    run                 Run Module
    exploit             Run Module
    unset               Unset options
    
'''
    print usages

def read_cmd_lines(PL_PWD,poc_re,PL_POC_FILE, poc_module_path_first_name, poc_module_path_end_name):
    poc = getinfo.import_pocs(PL_POC_FILE) 
    while True:
        ple = setcolor.UseStyle("ple",mode = 'underline')
        poc_shell_input = raw_input(ple + " " + poc_module_path_first_name + "(" + setcolor.set_red(poc_module_path_end_name) +") > ").strip()
        if poc_shell_input == const.PL_BACK:
            poc.handler.__init__()
            return
        else:
            if poc_shell_input[:3] == const.PL_SET:
                poc_shell = poc_shell_input[3:].strip()
                pay_shell = poc_shell_input[:11].strip()
                if poc_shell == None:
                    pass
                elif pay_shell == const.PL_SET_PAYLOAD:
                    poc.handler.__init__()
                    payload_shell = const.PL_PAYLOAD_DIR + poc_shell_input[11:].strip().lower() #获取payload名，进行存在判断
                    if poc_shell == None:
                        pass
                    else:
                        PL_STATUS = operation.pl_judge_file_name(PL_PWD, payload_shell) #判断文件是否存在
                        if PL_STATUS and poc.handler.listen == False:
                            poc.handler.listen = True #exploit模块监听状态置True
                            poc.handler.payload = payload_shell #传入payload模块
                            poc.handler.pwd = ch.pl_return_path(PL_PWD, payload_shell)
                            poc.handler.payload_fun = getinfo.import_pocs(poc.handler.pwd) #装载模块
                        elif PL_STATUS and poc.handler.listen == True:
                            poc.handler.payload = payload_shell #传入payload模块
                            poc.handler.pwd = ch.pl_return_path(PL_PWD, payload_shell)
                            poc.handler.payload_fun = getinfo.import_pocs(poc.handler.pwd)#装载模块
                        else:
                            print setcolor.set_red(" [!] ") + "没有找到此模块 => ".decode('utf-8') + poc_shell
                else:
                    try:
                        poc_shells   = poc_shell.split(" ")
                        option_key   = poc_shells[0]
                        option_value = poc_shells[1]
                        if poc.handler.listen == True:
                            if poc.handler.payload == "":
                                pass
                            else:
                                for option_pay, option_filter_pay in poc.handler.payload_fun.option.items():
                                    if option_filter_pay['default'] == None:
                                        option_filter_pay['default'] = ''
                                    if option_filter_pay['desc'] == None:
                                        option_filter_pay['desc'] = ''
                                for option_pay, option_filter_pay in poc.handler.payload_fun.option.items():
                                    if option_key == option_pay:
                                        if option_filter_pay['Required'] == "":
                                            print setcolor.set_yellow("[-] ") + "参数为固定值,无法修改!"
                                        else:
                                            print option_key + " => " + option_value
                                            option_filter_pay['default'] = option_filter_pay['convert'](option_value) 
                                            option_filter_pay['Required'] = "yes"
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
                                    option_filter['default'] = option_filter['convert'](option_value) 
                                    option_filter['Required'] = "yes"
                            if not option_key:
                                pass
                    except:
                        print setcolor.set_red("[!] ") + "参数设置错误"
            elif poc_shell_input == const.PL_INFO:
                ch.pl_show_poc_info(PL_POC_FILE)
                ch.pl_show_poc_infos(poc)
            elif poc_shell_input == const.PL_RUN or poc_shell_input == const.PL_EXPLOIT: 
                ch.pl_run_poc(poc)
            elif poc_shell_input == const.PL_SHOW_OPTIONS:
                ch.pl_run_poc_show(poc,poc_re)
            elif poc_shell_input == const.PL_HELP or poc_shell_input == "?":
                usage()
            elif poc_shell_input[:5] == "unset":
                try:
                    poc_shell = poc_shell_input[5:].strip()
                    #Payload Listen
                    if poc.handler.listen == True:
                        if poc.handler.payload == "":
                            pass
                        else:
                            for option_pay,options_filter_pay in poc.handler.payload_fun.option.items():
                                if poc_shell == option:
                                    if option_filter['default'] == "":
                                        pass
                                    elif option_filter['default'] != "":
                                        print poc_shell + " => unset" 
                                        option_filter['default'] = "" 
                                        option_filter['Required'] = "no"
                                    else:
                                        pass
                    for option, option_filter in poc.option.items():
                        if poc_shell == option:
                            if option_filter['default'] == "":
                                pass
                            elif option_filter['default'] != "":
                                print poc_shell + " => unset" 
                                option_filter['default'] = "" 
                                option_filter['Required'] = "no"
                            else:
                                pass
                except:
                    print setcolor.set_red("[!] ") + "参数设置错误"
            elif poc_shell_input[:3] == const.PL_USE:
                PL_POC_FILE = const.PL_PAYLOAD_DIR + poc_shell_input[3:].strip()
                if PL_POC_FILE == "":
                    return
                else:
                    PL_STATUS = operation.pl_judge_file_name(PL_PWD, PL_POC_FILE)
                    if PL_STATUS:
                        poc.handler.__init__()
                        poc_re = PL_POC_FILE
                        poc_module_path_first_name  = ch.pl_path_split_first_name(PL_POC_FILE)
                        poc_module_path_end_name    = ch.pl_path_split_end_name(PL_POC_FILE)
                        PL_POC_FILE = ch.pl_return_path(PL_PWD,PL_POC_FILE)
                        poc = getinfo.import_pocs(PL_POC_FILE)
                    else:
                        print setcolor.set_red(" [!] ") + "没有找到此模块 => ".decode('utf-8') + PL_POC_FILE
            else:
                #print "error please debug"
                pass

#-------------------------------------------------------------------------------
