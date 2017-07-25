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

def pl_get_poc_name(PL_PWD,PL_POC_FILE):
    try:
        f = open('logs/poc_name_path.pl','w+')
        f1 = open('logs/poc_name.pl','w+')
        for root, dirs, files in os.walk(PL_POC_FILE):
            for name in files:
                if name.split('.')[1] == 'py' and os.path.split(name)[1] != '__init__.py':
                    file_path  = os.path.join(root.replace(PL_PWD,"")[1:], name)
                    file_path1 = os.path.join(root, name)
                    #把当前获取到的文件路径名称写入file_path.pl
                    f.write(file_path + '\n')
                    f1.write(file_path1 + '\n')
                else:
                    pass
        f.close()
        f1.close()
    except:
        print setcolor.set_red("[!] ") + "加载PAYLOAD失败，请重新运行！"
        f.close()
        f1.close()



def pl_show_all_poc_info(PL_PWD):
    PL_PWD = PL_PWD + "/logs/poc_name_path.pl"
    if pl_judge_file(PL_PWD):
        f = open(PL_PWD)
        lines = f.readlines()
        
#打印模块名称
        desc = '''
PureLove Modules
----------------
'''
        print desc
        print "   {Name:<55}{DisclosureDate:<20}{Rank:<20}{Descriptions:<40}".format(Name            = "Name",
                                                                                     DisclosureDate = "Disclosure Date",
                                                                                     Rank           = "Rank",
                                                                                     Descriptions   = "Descriptions")
        print "   {Name:<55}{DisclosureDate:<20}{Rank:<20}{Descriptions:<40}".format(Name            = "----",
                                                                                     DisclosureDate = "---------------",
                                                                                     Rank           = "----",
                                                                                     Descriptions   = "------------")
        try:
            for poc_name in lines:
                poc_name = poc_name.replace('\n',"")
                #去掉后缀
                #导入模块
                try:
                    poc = getinfo.import_pocs(poc_name) #导入poc主函数
                    print "   {poc_name:<55}{date:<20}{severity:<20}{name:<40}".format(poc_name = pl_del_suffix(poc_name),
                                                                                      date     = pl_get_file_date(poc_name),
                                                                                      severity = poc.info['severity'],
                                                                                      name     = poc.info['name'])
                    print
                except:
                    f.close()
        except:
            f.close()
    else:
        print setcolor.set_red("[!] ") + "payload加载出错" #红色字体
        return
        
#----------------------------------------------------------------------------
#去后缀名
def pl_del_suffix(poc_name_path):
    lists = poc_name_path.split('.')         #分割出文件与文件扩展名
    file_ext = lists[:-1]                   #取出文件名(列表切片操作)
    PL_POC_NAME = file_ext[0]
    return PL_POC_NAME


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

def pl_find_poc_name(PL_PWD, PL_POC_NAME):
    PL_PWD = PL_PWD + "/logs/poc_name.pl"
    if PL_POC_NAME[-3:] == ".py":
        try:
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name = poc_name.replace('\n',"")
                file_name = os.path.split(poc_name)     #分割出目录与文件
                file_name = file_name[1]                #取出文件名
                if  file_name == PL_POC_NAME :
                    return True
                else:
                    return False
        except:
            f.close()
            return False
    else:
        PL_POC_NAME = PL_POC_NAME + ".py"
        try:
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name = poc_name.replace('\n',"")
                file_name = os.path.split(poc_name)     #分割出目录与文件
                file_name = file_name[1]                #取出文件名
                if  file_name == PL_POC_NAME :
                    #print "True"
                    return True
                else:
                    return False
        except:
            f.close()
            return False
    
def print_poc_name_infos(PL_PWD, PL_POC_NAME):
    PL_PWD_TMP = PL_PWD
    PL_PWD     = PL_PWD + "/logs/poc_name.pl"
    if PL_POC_NAME[-3:] == ".py":
        try:
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name        =   poc_name.replace('\n',"")
                file_name       =   os.path.split(poc_name)     #分割出目录与文件
                file_name       =   file_name[1]                #取出文件名
                file_name_path  =   file_name[0]
                if  file_name == PL_POC_NAME :
                    file_date = pl_get_file_date(poc_name)
                    pname = pl_del_path_name(PL_PWD_TMP,poc_name)
                    pocname = pl_del_path(poc_name)
                    print u'filename\t\t\t' + 'name\t\t\t' + 'date'
                    print pname + '\t\t\t' + pocname + '\t\t\t' + file_date
                else:
                    pass
        except:
            f.close()
            return 
    else:
        PL_POC_NAME = PL_POC_NAME + ".py"
        #print PL_POC_NAME
        try:
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name        =   poc_name.replace('\n',"")
                file_name       =   os.path.split(poc_name)     #分割出目录与文件
                file_name       =   file_name[1]                #取出文件名
                if  file_name == PL_POC_NAME :
                    file_date = pl_get_file_date(poc_name)
                    pname = pl_del_path_name(PL_PWD_TMP,poc_name)
                    pocname = pl_del_path(poc_name)
                    print u'filename\t\t\t' + 'name\t\t\t' + 'date'
                    print pname + '\t\t\t' + pocname + '\t\t\t' + file_date
                else:
                    #以后看情况写
                    pass
        except:
            f.close()
            return 

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

def print_poc_name_info(PL_PWD, PL_POC_NAME):
    PL_PWD_TMP = PL_PWD
    PL_PWD     = PL_PWD + "/logs/poc_name.pl"
    if PL_POC_NAME:
        print
        print "\tDIRFILENAME"
        print "\t============="
        print
        print u'\tFILENAMEPATH\t\t\t' + 'NAME\t\t\t' + 'DATE'
        print
        try:
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name        =   poc_name.replace('\n',"")
                file_name       =   os.path.split(poc_name)     #分割出目录与文件
                file_name       =   file_name[1]                #取出文件名
                #模糊寻找匹配文件
                #循环遍历模糊查询到的poc文件
                if PL_POC_NAME in file_name:
                    file_date = pl_get_file_date(poc_name)
                    #获取无后缀文件名
                    pname = pl_del_path_name(PL_PWD_TMP,poc_name)
                    #去掉绝对路径
                    pocname = pl_del_path(poc_name)
                    print '\t' + pname + '\t\t\t' + pocname + '\t\t\t' + file_date
                else:
                    pass
                if not len(lines):
                    f.close()
        except:
            f.close()
            return 
    else:
        print
        print "\tDIRFILENAME"
        print "\t============="
        print
        print u'\tFILENAMEPATH\t\t\t' + 'NAME\t\t\t' + 'DATE'
        print 
        try:
            #调用加载的文件进行查找
            f = open(PL_PWD)
            lines = f.readlines()
            for poc_name in lines:
                poc_name        =   poc_name.replace('\n',"")
                #截取出文件名
                file_name       =   os.path.split(poc_name)     #分割出目录与文件
                file_name       =   file_name[1]                #取出文件名
                #模糊寻找匹配文件
                #循环遍历模糊查询到的poc文件
                if PL_POC_NAME in file_name:
                    print poc_name
                    file_date = pl_get_file_date(poc_name)
                    #获取无后缀文件名
                    pname = pl_del_path_name(PL_PWD_TMP,poc_name)
                    #去掉绝对路径
                    pocname = pl_del_path(ppoc_name)
                    print '\t' + pname + '\t\t\t' + pocname + '\t\t\t' + file_date
                else:
                    pass
                if not len(lines):
                    f.close()
        except:
            f.close()
            return 


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










    




