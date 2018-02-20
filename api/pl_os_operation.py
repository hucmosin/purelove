#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
说明：该类执行系统操作，系统文件操作等相关操作。
"""
# python standard library
import os
import sys
import datetime
import platform
import re

root_path = "../"
sys.path.append(root_path)

# local pret classes
import modules.getinfo as getinfo
import pl_print_world_color as setcolor
from pl_print_str import print_tables


def pl_get_file_info(PL_POC_FILE):
    return pl_get_path(PL_POC_FILE) + pl_get_file_date(PL_POC_FILE)
def pl_get_file_path(PL_POC_FILE):
    pass
def pl_get_file_name(PL_POC_FILE):
    if PL_POC_FILE[-3:] == ".py":
        if os.path.isfile(PL_POC_FILE):
            file_path = os.path.split(PL_POC_FILE)  #分割出目录与文件
            lists = file_path[1].split('.')         #分割出文件与文件扩展名
            file_ext = lists[:-1]                   #取出文件名(列表切片操作)
            PL_POC_NAME = file_ext[0]
            return PL_POC_NAME
    else:
        PL_POC_FILE = PL_POC_FILE + ".py"
        if os.path.isfile(PL_POC_FILE):
            file_path = os.path.split(PL_POC_FILE)  #分割出目录与文件
            lists = file_path[1].split('.')         #分割出文件与文件扩展名
            file_ext = lists[:-1]                   #取出文件名(列表切片操作)
            PL_POC_NAME = file_ext[0]
            return PL_POC_NAME
def pl_get_file_date(PL_POC_FILE):
    if os.path.isfile(PL_POC_FILE):
        time = os.path.getctime(PL_POC_FILE)
        date = datetime.datetime.fromtimestamp(time)
        return str(date)[:10]
    else:
        return
def pl_judge_file(PL_POC_FILE):
    path_isfile = os.path.isfile(PL_POC_FILE)
    if path_isfile:
        return True
    else:
        return False
def pl_judge_file_name(PL_PWD, PL_POC_FILE):
    PL_POC_FILE = PL_PWD + '/'+PL_POC_FILE + '.py'
    path_isfile = os.path.isfile(PL_POC_FILE)
    if path_isfile:
        return True
    else:
        return False
def pl_get_poc_name(PL_PWD):
    from db.loader_db import loadDB
    loadDB(PL_PWD).check_modules()
def pl_show_all_poc_info(PL_PWD):
    #调用数据库
    from db.loader_db import loadDB
    loadDB(PL_PWD).show_modules()
def pl_del_suffix(poc_name_path):
    lists = poc_name_path.split('.')         #分割出文件与文件扩展名
    file_ext = lists[:-1]                   #取出文件名(列表切片操作)
    PL_POC_NAME = file_ext[0]
    return PL_POC_NAME
def pl_get_name(poc_name_path):
    lists = poc_name_path.split('/')         
    file_name = lists[-1:]
    return str(file_name)
def pl_get_path(PL_POC_FILE):
    if os.path.isfile(PL_POC_FILE):
        file_path = os.path.split(PL_POC_FILE)  #分割出目录与文件
        lists = file_path[0].split('.')         #分割出文件与文件扩展名
        #print lists
        file_ext = lists[0]                   #取出路径名(列表切片操作)
        return file_ext
def pl_del_path(PL_POC_FILE):
    if os.path.isfile(PL_POC_FILE):
        file_path = os.path.split(PL_POC_FILE)  #分割出目录与文件
        lists = file_path[1].split('.')         #分割出文件与文件扩展名
        #print lists
        file_ext = lists[0]                   #取出文件名(列表切片操作)
        return file_ext
def pl_del_path_name(PL_PWD,PL_PATH):
    tmp = PL_PATH.replace(PL_PWD,"")[1:]
    return pl_del_suffix(tmp)
def pl_get_UsePlatform():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        return sysstr
    elif(sysstr == "Linux"):
        return sysstr
    else:
        pass
def pl_clsc():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        os.system("cls")
    else:
        os.system("clear")
def print_poc_name_info(PL_PWD,PL_POC_NAME):
    #查询数据库
    from api.db.loader_db import loadDB
    loadDB(PL_PWD).search_modules(PL_POC_NAME)

def pl_os_shell():
    while True:
        ple = setcolor.UseStyle("ple-shell",mode = 'underline')
        cmd_shell = raw_input(ple + " > ").strip().lower()
        try:
            if cmd_shell == "back":
                return
            os.system(cmd_shell)
        except:
            pass
        
