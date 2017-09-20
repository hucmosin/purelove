# -*- coding: utf-8 -*-

import os,subprocess
from client_handler import write_code

def write_client(name,lport,lhost):
    if name =="":
        name = "client_hander"
    a = write_code(lport,lhost)
    f = open("result/" + name + ".cpp",'w')
    f.write(a)
    pwd = os.getcwd()
    pwd = pwd + "/result/" + name + ".cpp"
    print pwd
    #f.close
    #ls = "gcc.exe temp.cpp -o " + name + ".exe"
    #ls = str(ls)
    #os.system(ls)
    #sub=subprocess.call(ls)
   # sub.wait()
    #print sub.read()
