#coding=utf-8
import imp
import os
import sys

root_path = "../"
sys.path.append(root_path)


def import_poc(path):
    try:
        poc = imp.load_source('PocInfo', path)
        return poc.docs
    except:
        return 

def import_pocs(path):
    poc = imp.load_source('PocInfo', path)
    poc =  poc.PLScan()
    return poc

def put_poc_info(path):
    poc = import_pocs(path)
    p = get_poc_class(poc)
    return p

def get_poc_class(bg_instance):
    return bg_instance.option.items
