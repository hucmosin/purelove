#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
@Author:mosin
@date:2018-2-20
说明：该文件类主要为框架模块提供数据库支持，数据库为SQLite,默认无密码
'''

# python standard library
import os
import sqlite3

# local pret classes

#返回连接成功后的数据库操作
def connect_db(database):

    try:
        conn = sqlite3.connect(database)
        return conn
    except:
        print "[!] Sorry Datebase Not Connect."
    #c = conn.cursor()

class sql(object):
    #初始化数据库
    def __init__(self,conn):
        self.conn = conn

    #执行Sql语句操作
    def exec_sql(self,sql):
        if sql == "":
            print "[-] 执行语句为空，请重新输入！"
            return
        c = self.conn.cursor()
        cursor = c.execute(sql)
        return cursor

    #插入操作
    def insert(self,poc_name,poc_name_path,date):
        c = self.conn.cursor()
        c.execute("INSERT INTO POC (POC_NAME,POC_NAME_PATH,DATE) VALUES ('" + poc_name + "','" + poc_name_path + "','" + date + "')")
        self.conn.commit()

    #读取数据库数据操作
    def select(self,sql =""):
        if sql == "":
            c = self.conn.cursor()
            cursor = c.execute("SELECT POC_NAME,POC_NAME_PATH,DATE from POC")
            return cursor
        else:
            c = self.conn.cursor()
            cursor = c.execute(sql)
            return cursor
            

    #更新操作
    def update(self,sql = ""):
        if sql =="":
            pass
        else:
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()

    #删除操作
    def delete(self,sql = "",poc_name_path = ""):
        print poc_name_path
        if sql == "":
            c = self.conn.cursor()
            cursor = c.execute("DELETE FROM POC WHERE POC_NAME_PATH=\"" + poc_name_path+"\"")
            self.conn.commit()
        else:
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()

    #创建数据库表
    def create_table(self):
        cursor = self.conn.cursor()
        #执行语句
        sql = '''CREATE TABLE POC (
            POC_NAME CHAR, 
            POC_NAME_PATH CHAR, 
            DATE DATETIME);
        '''
        sql2 = '''CREATE TABLE STATUS (
            ID INT PRIMARY KEY ASC, 
            FLAG BOOLEAN);
        '''
        cursor.execute(sql)
        cursor.execute(sql2)
        #使用游标关闭数据库的链接
        self.conn.commit()
        self.db_close()

    #清除数据库
    def clean_table_data(self):
        c = self.conn.cursor()
        c.execute("DELETE FROM POC")
        self.conn.commit()
        self.db_close()
    #创建数据库
    def create_db(self):
        pass
    
    #关闭数据库
    def db_close(self):
        #self.conn.commit()
        self.conn.close()
