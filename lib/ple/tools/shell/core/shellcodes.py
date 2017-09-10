#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：存在模块打印
"""

# python standard library

from color import *
from module_laz import *

def shellcodelist(PWD):
        #print modules all
        desc = '''
Shellcode Modules
=================

'''
        print desc
        PWD = PWD + "/purelove/lib/ple/tools/shell/database"
        m = index_modules(PWD)
        return_modules(PWD,m)
