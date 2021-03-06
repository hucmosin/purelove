#!/usr/bin/env python
# coding=utf-8

'''
* @Copyright (C) 2018 .
* @author:mosin
* @date:2018-05
* @Blog:http://imosin.com
* 本网络模块用于框架内模块的socket资源调用，简化代码量
'''

import socket

class UDP(object):

    def __init__(self):
        #sock循环开始或结束标记
        sock_flag = True
    
    def create_udp_socket(self):
        '''
        @创建一个UDP套接字并返回
        return sock
        '''
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            print('[-] Create socket error.')
            return 0
        return sock

    def create_udp_server(self,addr,port):
        '''
        @创建一个udp的socket服务端程序，本函数为阻塞监听,当有连接时，返回一个套接字流和
        连接IP端口信息，监听默认为listen(10)
        return conn,addrs
        '''
        try:
            sock_server = self.create_tcp_socket()
            sock_server.bind((addr, port))
            sock_server.listen(10)
        except:
            print('[-] Bind False.')
        while True:
            conn, addrs = sock_server.accept()
            if conn:
                return conn,addrs

    def create_udp_connect(self,addr,port):
        '''
        @创建一个udp的socket连接端程序，本函数连接一个IP和端口，返回一个连接后的字节流
        return conn_sock
        '''
        while True:
            conn_sock = self.create_tcp_socket()
            try:
                conn_sock.connect((addr, port))
            except Exception, e:
                print ('[-] Can not connect %s:%i!' % (addr, port))
                return
            print "[+] Connected to %s:%i" % (addr, port)
            return conn_sock


        
