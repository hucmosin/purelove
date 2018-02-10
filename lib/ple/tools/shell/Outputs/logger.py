#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：shellcode编译生成
"""

# python standard library
from random import randint
import os

def logs(data=None, extension=None,filename = None):
    
    if filename == None:
        filename = "{0}".format(str(randint(0, 999999999)))
    elif extension == None and filename !=None:
        filename = "{0}".format(filename)
    else:
        filename = "{0}.{1}".format(filename,extension)

    if extension == "exe":
        logs = open(os.getcwd()+os.sep+filename, "wb")
    else:
        logs = open(os.getcwd()+os.sep+filename, "w")

    logs.write(data)
    logs.close()
    if not os.path.isfile(filename):
        print ("\n\t[+]Executable file : {0} saved !\n".format(os.getcwd()+os.sep+filename))
    else:
        print ("\n\t[+]Script file : {0} saved !\n".format(os.getcwd()+os.sep+filename))

