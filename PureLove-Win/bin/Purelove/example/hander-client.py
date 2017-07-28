#-*- coding: utf-8 -*-

import os,sys
from socket import *


HOST   = '0.0.0.0'
PORT   = 19954
BUFSIZ = 2048
ADDR   = (HOST, PORT)
sock   = socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)
STOP_CHAT = False

print "Hander Listening %s port:%s" %(HOST,PORT)
while not STOP_CHAT:
    tcpClientSock, addr=sock.accept()
    print('Start Listening %s  port %s.....') %(addr,PORT)
    while True:
        data = raw_input('pl-shell >')
        try:
            tcpClientSock.send(data.encode('utf8'))
            if data.upper()=="BACK":
                break
            os_result = tcpClientSock.recv(BUFSIZ)
        except:
            tcpClientSock.close()
            break
        STOP_CHAT = (data.decode('utf8').upper()=="QUIT")
        if STOP_CHAT:
            break
        print(os_result)

tcpClientSock.close()
sock.close()
    
