#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# python standard library
import os
import sys
from api.db.loader_db import conn_db


def count_modules():
    sql = "SELECT COUNT(*) FROM POC"
    result = conn_db().sql_exec.exec_sql(sql)
    for row in result:
        num = row[0]
    conn_db().sql_exec.db_close()
    return num

#打开payload文件，统计数量
def ret_num():
    pay_var = open("logs/poc_name_path.pl")
    lines = pay_var.readlines()
    return len(lines)
