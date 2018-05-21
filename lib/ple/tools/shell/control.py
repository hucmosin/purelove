#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：模块利用类
"""

# python standard library
import sys
import os
import imp
from core.color import *
from core.Comp import tab
from core.static_const import *
from api.pl_shell_cmd_const import PL_PWD

name = PL_PWD
sys.path.append(name)

#记录开始
tab.start()

#shell main class
class PLline(object):
    def __init__(self):
        self.disassembly = ""

    def imp_poc(self,path):
        poc = imp.load_source('PocInfo', path)
        poc = poc.Payload()
        return poc
    def gener(self,poc):
        from database.generator import generator
        poc.sld()
        self.disassembly = generator(poc)
        
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
                from core.help import shellcode_help  
                shellcode_help()
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

            elif terminal[:8] == PL_GENERATE:
                self.gener(poc)
                print self.disassembly

            elif terminal[:6] == PL_OUTPUT:
                terminal_str = terminal[6:].strip()
                str_exe  = terminal_str.split('.')[-1:]
                str_exe  = str(str_exe[0])
                str_name = terminal_str.split('.')[:1]
                str_name = str(str_name[0])

                if self.disassembly == "":
                    print ("[*] Please generate shellcode before save it.")
                    continue

                elif str_exe == "exe":
                    if "windows" in terminal.lower():
                        OS = "windows"
                        str_name = str_name.replace("windows","").strip()
                    else:
                        OS = None
                    from Outputs.exe import ExeFile
                    ExeFile(self.disassembly,OS,str_name)
                #开始写其他系统shellcode生成 date:2017-11-24 
                elif str_exe == "c":
                    pass
                else:
                    print (bcolors.RED + bcolors.BOLD + "[-] Unknown output type: {0}".format(terminal) + bcolors.ENDC)
            else:
                if terminal == "":
                    pass
                else:
                    print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: {0}".format(terminal) + bcolors.ENDC)

