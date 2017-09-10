#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：返回出shellcode数量
"""

# python standard library


import os
from sys import platform

class PLogo(object):
    def __init__(self,dpath):
        self.db = ["database","OS"]
        self.ret = []
        self.magic = dpath + os.sep + "shell"

    def calculate(self,select,files = True):
        if files == True:
            self.cout = 0
            for root,dirs,files in os.walk(self.magic + os.sep + select):
                for x in dirs:
                    rootss = root+'/' + x
                    for roots,dirss,filess in os.walk(rootss):
                        for i in filess:
                            if i.split('.')[1] == 'py' and os.path.split(i)[1] != '__init__.py':
                                self.cout += 1
            return self.cout
        else:
            self.cout = 0
            for root, dirs, files in os.walk(self.magic + os.sep + select):
                for x in dirs:
                    if ".pyc" not in x and "__init__.py" not in x:
                        self.cout += 1
            return self.cout
    def start(self):
        for x in self.db:
            if x != "OS":
                self.ret.append( self.calculate( x, True))
            else:
                self.ret.append( self.calculate( "database", False))
        return self.ret
