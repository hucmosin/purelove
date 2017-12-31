#!/usr/bin/env python
# coding=utf-8

'''
* @Copyright (C) 2017 .
* @author:mosin
* @date:2017-11
* @Blog:http://imosin.com
* 本网络模块用于框架内模块的socket资源调用，简化代码量
'''

import socket
class TCP:
    
    def create_tcp_socket():
        '''
        @创建一个TCP套接字并返回
        return sock
        '''
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print('[-] Create socket error.')
            return 0
        return sock

    def create_tcp_server(addr,port):
        '''
        @创建一个tcp的socket服务端程序，本函数为阻塞监听,当有连接时，返回一个套接字流和
        连接IP端口信息，监听默认为listen(10)
        return conn,addrs
        '''
        try:
            sock_server = create_tcp_socket()
            sock_server.bind((addr, port))
            sock_server.listen(10)
        except:
            print('[-] Bind False.')
        while True:
            conn, addrs = sock_server.accept()
            if conn:
                return conn,addrs

    def create_tcp_connect(addr,port):
        '''
        @创建一个tcp的socket连接端程序，本函数连接一个IP和端口，返回一个连接后的字节流
        return conn_sock
        '''
        while True:
            conn_sock = create_tcp_socket()
            try:
                conn_sock.connect((addr, port))
            except Exception, e:
                print ('[-] Can not connect %s:%i!' % (addr, port))
                return
            print "[+] Connected to %s:%i" % (host, port)
            return conn_sock


        
