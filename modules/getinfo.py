#coding=utf-8
import imp
import os
import sys

root_path = "../"
sys.path.append(root_path)


#传入绝对路径，包含文件名
#返回poc文件信息
def import_poc(path):
    try:
        poc = imp.load_source('PocInfo', path)
        return poc.docs
    except:
        return 

#获取poc主函数
def import_pocs(path):
    poc = imp.load_source('PocInfo', path)
    poc =  poc.PLScan()
    return poc

#获取poc中的option参数。
def put_poc_info(path):
    poc = import_pocs(path)
    p = get_poc_class(poc)
    return p

#获取poc中的框架设置参数
def get_poc_class(bg_instance):
    return bg_instance.option.items

#path = "E:\\GitHub\\Purelove\\payloads\\exa.py"
#print put_poc_info(path)
