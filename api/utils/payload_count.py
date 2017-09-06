#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# python standard library
import os
import sys

root_path = "../../"
sys.path.append(root_path)


#打开payload文件，统计数量
def ret_num():
    pay_var = open("logs/poc_name_path.pl")
    lines = pay_var.readlines()
    return len(lines)
