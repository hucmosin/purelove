#!/usr/bin/env python2
#coding=utf8

import os
import pl_print_world_color as setcolor
import toolscof as tool

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
        if shell_input[:4] == "show":
            tool.read_tool_env(PL_PWD)
        elif shell_input[:4] == "load":
            loads = shell_input[4:].strip()
            path = PL_PWD + "/thirdtools/" + loads + "/" + loads + ".py"
            os.system(path)
        elif shell_input == "help" or shell_input == "?":
            usage()
        elif shell_input == "exit" or shell_input == "quit":
            STATUS = True
        elif shell_input == "reload":
            tool.save_tool_env(PL_PWD)
        else:
            print setcolor.set_red('[-]') + u" 请输入正确命令"
        




















