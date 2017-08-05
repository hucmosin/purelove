#!/usr/bin/env python2
#coding=utf8

import os

import pl_shell_cmd_const as c
import pl_print_world_color as setcolor

def save_tool_env(PL_PWD):
    try:
        f = open(PL_PWD + "/bin/Purelove/logs/third_tool.ini",'w+')
    except:
        print setcolor.set_red('[!] ') + u"工具载入失败"
        return
    path = PL_PWD + c.PL_TOOL_DIR
    dirs = os.listdir(path)
    for d in dirs:
        ds = path + '/' + d
        t = os.path.isfile(ds)
        if not t:
            f.write(d + '\n')
    f.close()
    
def read_tool_env(PL_PWD):
    try:
        f = open(PL_PWD + "/bin/Purelove/logs/third_tool.ini",'r')
    except:
        print setcolor.set_red('[!] ') + u"工具载入失败"
        return
    print_tools()
    dirs = f.readlines()
    for d in dirs:
        d = d.replace('\n',"")
        print "\t" + d
    print
    f.close()
    
def print_tools():
    desc = '''
Tools Show
==========
'''
    print desc
    
    
