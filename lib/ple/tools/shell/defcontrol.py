#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：模块利用类,
@本模块为自定义shellcoed生成类,主要是改写，输出非汇编成的机器码，主要为完整文件
@date:2017-12-24
@author:mosin
"""

# python standard library
import sys
import os
import imp
from core.color import *
from core.Comp import tab
from core.static_const import *

name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)

#记录开始
tab.start()

#shell main class
class DPLline(object):
    def __init__(self):
        self.disassembly = ""

    def imp_poc(self,path):
        poc = imp.load_source('PocInfo', path)
        poc = poc.Payload()
        return poc
        
    def control(self, string):

        path = name + PL_DATA_PATH + string + ".py"
        poc = self.imp_poc(path)
        while True:
            bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "sle" + bcolors.ENDC
            bash += ":"
            bash += bcolors.RED + string+ bcolors.ENDC
            bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
            try:
                terminal = raw_input(bash)
            except NameError:
                terminal = input(bash)
            if terminal[:4] == PL_HELP:
                from core.help import def_shellcode_help 
                def_shellcode_help()
            elif terminal[:4] == PL_BACK:
                return
            elif terminal[:4] == PL_EXIT:
                from sys import exit
                exit()
            elif terminal[:3] == PL_SET:
                poc_shell = terminal[3:].strip()
                if poc_shell == "":
                    pass
                else:
                    try:
                        poc_shells   = poc_shell.split(" ")
                        option_key   = poc_shells[0]
                        option_value = poc_shells[1]
                        for option, option_filter in poc.options.items():
                            if option_filter['default'] == None:
                                option_filter['default'] = ''
                            if option_filter['desc'] == None:
                                option_filter['desc'] = ''
                        for option, option_filter in poc.options.items():
                            if option_key == option:
                                if option_filter['Required'] == "":
                                    print u"[-] 参数为固定值,无法修改!"
                                else:
                                    print option_key + " => " + option_value
                                    option_filter['default'] = option_value
                                    option_filter['Required'] = "yes"
                                if not option_key:
                                    pass
                    except:
                        print u"[!] 参数错误"

            elif terminal[:12] == PL_SHOW_OPTIONS:
                from core.SHELLoptions import controlset
                controlset(poc,string)

            elif terminal[:6] == PL_OUTPUT:
                poc.payload()
                
            else:
                if terminal == "":
                    pass
                else:
                    print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: {0}".format(terminal) + bcolors.ENDC)

