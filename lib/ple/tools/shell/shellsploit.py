#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# python standard library
import os
import sys

#os.path.dirname(os.path.realpath(__file__))
name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)


from core.logo.logo import banner
from core.color import bcolors
from core.logo.counter import *
from core.Comp import tab
from core.static_const import *

dpath = name + PL_SHOW_PATH
tab.start(1)
db = PLogo(dpath).start()

def start():
    print (banner(db[0],db[1]))
    shellsploit()
def shellsploit():
    try:
        bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "sle" + bcolors.ENDC
        bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
        try:
            terminal = raw_input(bash)
        except NameError:
            terminal = input(bash)
        if terminal[:4] == PL_HELP:
            from core.help import main_help
            main_help()
            shellsploit()
        elif terminal[:6] == PL_BANNER:
            print (banner( db[0], db[1]))
            shellsploit()
        elif terminal[:3] == PL_USE:
            from api.pl_os_operation import pl_judge_file_name
            from control import PLline
            terminal = terminal[3:].strip()
            PL_STATUS = pl_judge_file_name(name, PL_USE_PATH + terminal)
            if PL_STATUS:
                #自定义脚本处理
                if "payload" in terminal:
                    #执行自定义脚本处理程序
                    from defcontrol import DPLline
                    DPLline().control(terminal)
                else:    
                    PLline().control(terminal)
                    shellsploit()
            else:
                print ("\n[-] Module not avaible !\n")
                shellsploit()
        elif terminal[:12] == PL_SHOW_MODULES:
            from core.shellcodes import shellcodelist
            shellcodelist(name)
            shellsploit()    
        elif terminal[:4] == PL_EXIT:
            sys.exit("\n[*] Thanks for using shellsploit !\n")    
        else:
            if terminal == "":
                shellsploit()
            else:
                print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC)
                shellsploit()
    except(KeyboardInterrupt):
        print("\n[*] (Ctrl + C ) Detected, Trying To Exit ...")
        from sys import exit
        sys.exit()
def main():
    start()
