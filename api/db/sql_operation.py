#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
@Author:mosin
@date:2018-2-20
说明：该文件类主要为框架模块提供数据库支持，该文件封装了于Sqlite数据库交互的函数，方便整体的POC模块调用
'''

# python standard library
import os

# local pret classes
import api.pl_print_world_color as setcolor
#from sqlconn import *

class SqlExec(object):
    '''
    @sql数据处理类，主要完成当前模块文件的数据库操作，sqlExec类接受一个参数，参数
    为PL_PWD，PL_PWD路径到框架启动根目录.
    '''
    def __init__(self, PL_PWD, times, sql_exec):
        self.PWD = PL_PWD + "/module/" #模块存放路径（完整路径）
        self.date = times.get_date()
        self.sql_exec = sql_exec

    #把参数插入数据库，此函数只执行一次，当且仅当第一次运行时执行时
    def insert_poc_name(self):
        #date = self.times.get_date()   #获取日期
        sql = "UPDATE STATUS set FLAG = 'True' WHERE ID = 1"
        try:
            for root, dirs, files in os.walk(self.PWD):
                for name in files:
                    if name[-3:] == '.py' and name != '__init__.py':
                        file_name  = root.replace(self.PWD,"") + "/" + name
                        file_path  = root + "/" + name
                        self.sql_exec.insert(file_name,file_path,self.date) #插入数据
                        #print file_name
                        #print file_path
                    else:
                        pass
        except:
            print setcolor.set_red("[!] ")  + "加载PAYLOAD失败，请重新运行！"
            self.sql_exec.db_close()
        self.sql_exec.update(sql)
        self.sql_exec.db_close()
    
    #读取poc进行比较是否相同
    def cmp_module(self,cursor,file_name,file_path):
        for row in cursor:
            if file_name == row[0] or  file_path == row[1]:
                return False
        return True

    #每次启动执行
    def exist_poc(self):
        #date = self.times.get_date()   #获取日期
        #首先遍历整个目录，看是否有存在新增文件
        cursor = self.sql_exec.select()  #读取所有模块文件
        try:
            for root, dirs, files in os.walk(self.PWD):
                for name in files:
                    if name[-3:] == '.py' and name != '__init__.py':
                        file_name  = root.replace(self.PWD,"") + "/" + name
                        file_path  = root + "/" + name
                        #判断是否存在
                        poc_flag = self.cmp_module(cursor,file_name,file_path )
                        if poc_flag == True:
                            self.sql_exec.insert(file_name,file_path,self.date) #插入数据
                    else:
                        pass
        except:
            print setcolor.set_red("[!] ")  + "加载PAYLOAD失败，请重新运行！"
            self.sql_exec.db_close()
        self.sql_exec.db_close()

'''
@模块信息展示类
'''
from modules import getinfo
from api.pl_os_operation import pl_del_suffix

class ShowSql(object):

    '''
    @初始化数据库链接参数
    '''
    def __init__(self,sql_exec):
        self.sql_exec = sql_exec

    '''
    @show 当前模块的各项信息
    '''
    def pl_show_all_poc_info(self):
        cursor = self.sql_exec.select()
        desc = '''
        PureLove Modules
        ----------------
        '''
        print desc
        print "   {Name:<55}{DisclosureDate:<20}{Rank:<7}{Descriptions:<35}".format(Name            = "Name",
                                                                                        DisclosureDate = "Disclosure Date",
                                                                                        Rank           = "Rank",
                                                                                        Descriptions   = "Descriptions")
        print "   {Name:<55}{DisclosureDate:<20}{Rank:<7}{Descriptions:<35}".format(Name            = "----",
                                                                                        DisclosureDate = "---------------",
                                                                                        Rank           = "----",
                                                                                        Descriptions   = "------------")
        try:
            for row in cursor:
                poc_name =  row[0]
                poc_name_path =  row[1]
                date = row[2]
                try:
                    poc = getinfo.import_pocs(poc_name_path) #导入poc主函数
                    print "   {poc_name:<55}{date:<20}{severity:<7}{name:<35}".format(poc_name = pl_del_suffix(poc_name),
                                                                                        date     = date,
                                                                                        severity = poc.info['severity'],
                                                                                        name     = poc.info['name'])
                    print
                except:
                    pass
            self.sql_exec.db_close()
        except:
            self.sql_exec.db_close()
    '''
    @该函数用于搜索模块名，为模糊查询
    '''
    def print_poc_name_info(self,PL_POC_NAME):
        cursor = self.sql_exec.select()
        desc = '''

    DirFileName
    -----------

        '''
        if PL_POC_NAME:
            print desc
            print "   {FileName:<55}{Name:<25}{Date:<20}".format(FileName       = "FileName",
                                                                    Name           = "Name",
                                                                    Date           = "Date",)
            print "   {FileName:<55}{Name:<25}{Date:<20}".format(FileName       = "--------",
                                                                    Name           = "----",
                                                                    Date           = "----",)
            print

            try:
                for row in cursor:
                    poc_name =  row[0]
                    poc_name_path =  row[1]
                    date = row[2]
                    file_name  = os.path.split(poc_name_path)[1] #分割出目录与文件
                    #file_name  = file_name[1]                  #取出文件名

                    if PL_POC_NAME in file_name:
                        file_date = date
                        pname   = pl_del_suffix(poc_name) #模块文件路径
                        pocname = pl_del_suffix(file_name) #
                        print "   {FileName:<55}{Name:<25}{Date:<20}".format(FileName  = pname,
                                                                            Name      = pocname,
                                                                            Date      = date)
                    else:
                        pass
            except:
                self.sql_exec.db_close()
                return 

        else:
            print setcolor.set_red("[-] ") + "Sorry！ Not Found Module."
            self.sql_exec.db_close()
        self.sql_exec.db_close()