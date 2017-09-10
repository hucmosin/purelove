#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：模块遍历
"""

# python standard library
import os

def index_modules(DIR):
    """ Return list"""
    modules = []
    for root, dirs, files in os.walk(DIR):
        _, package, root = root.rpartition('shell/database/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))
    return modules

def python_ize_path(path):
    return path.replace('/', '.')

def human_ize_path(path):
    return path.replace('.', '/')

def return_modules(PWD,modules):
    for r in modules:
        m = human_ize_path(r)
        if PWD not in m:
            print '\t' + m
