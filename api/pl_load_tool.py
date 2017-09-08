#!/usr/bin/env python2
#coding=utf8

import os
import pl_print_world_color as setcolor
import toolscof as tool
import pl_shell_cmd_const as const

def usage():
    usages = '''

Purelove Load Console Help
--------------------------

    ?                   Show the main console help
    help                Show the main console help
    exit                Exit the console
    quit                Exit the console
    show                Display module by name and path
    load <tools>        Load example:<load reoutersploit>
    reload              return loading
'''
    print usages
def exec_load(PL_PWD):
    tool.save_tool_env(PL_PWD)
    STATUS = False
    while not STATUS:
        load = setcolor.UseStyle("load",mode = 'underline')
        shell_input = raw_input(load + " > ").strip().lower()
        if shell_input[:4] == const.PL_SHOW:
            tool.read_tool_env(PL_PWD)
        elif shell_input[:4] == const.PL_LOAD:
            loads = shell_input[4:].strip()
            path = "python " + PL_PWD + "/thirdtools/" + loads + "/" + loads + ".py"
            print setcolor.set_blue('[*] ') + u'Loding .....'
            os.system(path)
        elif shell_input == const.PL_HELP or shell_input == "?":
            usage()
        elif shell_input == const.PL_EXIT or shell_input == "quit":
            STATUS = True
        elif shell_input == const.PL_RELOAD_POC:
            tool.save_tool_env(PL_PWD)
        else:
            print setcolor.set_red('[-]') + u" 请输入正确命令"
        
