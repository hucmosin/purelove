#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
说明:此netcat只能用于hander后门使用
"""
#=====================================
# Fix Date:2018-10-30
# Fix Author:mosin
# Fix NC Handler Module
#=====================================
# https://github.com/hucmosin/purelove
#


from __future__ import print_function
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from select import select
from time import sleep
from sys import exit

listening   = False
clisock     = None
done        = False

try:
    input = raw_input 
except NameError:
    pass 

def listen(sock):
    global clisock, listening, done                                                
    listening   = True                   
    clisock     = sock                         
    data = ""
    while listening:
        try:
            rr, _, _ = select([s,], [], [], 1) 
            if rr:
                data = sock.recv(1024)             
                print("{}".format(data), end="")   
        except:
            exit()
    print("Done listening.")
    done = True

def write():
    global clisock, listening, done
    while True:
        if clisock:
            data = input()
            if data.strip().lower() in ["exit", "quit"]:
                clisock.close()
                exit()
                listening = False
                while not done: sleep(0.1)
                break
            _, wr, _ = select([], [clisock,], [], 1)
            if wr:
                clisock.sendall(data + "\n")
        else:
            pass


def nc(sock):
    listenThread    = Thread(target=listen, args=(sock,))
    writeThread     = Thread(target=write)
    listenThread.start()
    writeThread.start()

