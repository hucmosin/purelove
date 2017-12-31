#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
@DATA:2017-12-28
@Author:mosin
说明:此netcat只能用于hander后门使用
"""

#
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

#Beta script for listener.
#Same effect nc -vlp [PORT]


def listen(server_sock):
    global clisock, listening, done                              
    listening   = True                  
    clisock     = server_sock.current_client.conn
    data = ""
    while listening:
        try:
            rr, _, _ = select([server_sock.current_client.conn,], [], [], 1) 
            if rr:
                data = server_sock.current_client.conn.recv(1024)             
                print("{}".format(data), end="")   
        except:
            break
    server_sock.current_flag = True
    done = True

def write():
    global clisock, listening, done
    while True:
        if clisock:
            data = raw_input()
            if data.strip().lower() in ["exit", "quit"]:
                clisock.send(data)
                listening = False
                while not done: sleep(0.1)
                break
            _, wr, _ = select([], [clisock,], [], 1)
            if wr:
                clisock.sendall(data + "\n")
        else:
            pass


def nc(server_sock):
    listenThread    = Thread(target=listen, args=(server_sock,))
    writeThread     = Thread(target=write)
    listenThread.start()
    writeThread.start()
            

    
