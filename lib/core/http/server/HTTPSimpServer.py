#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
Desc: This Class is HTTP server.
author: mosin <hucmoxing@163.com>
Date:2019-04-18
'''

# python standard library
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

# local pret classes

'''
This class USES two parameters to be submitted,Listen Host And Listen Port.
The default port is 8000.
The default host is 0.0.0.0

Example:
host = '0.0.0.0'
port = 8000
HTTP_SERVER(host,port).run()
'''
class HTTP_SERVER(object):

    def __init__(self,host='0.0.0.0',port=8000):
    
        HandlerClass = SimpleHTTPRequestHandler
        ServerClass  = BaseHTTPServer.HTTPServer
        Protocol     = "HTTP/1.1"
        self.host    = host
        self.port    = port
 
    def run(self):
        server_address = (self.host, self.port)
        HandlerClass.protocol_version = Protocol
        httpd = ServerClass(server_address, HandlerClass)
         
        sa = httpd.socket.getsockname()
        print "Serving HTTP on", sa[0], "port", sa[1], "..."
        httpd.serve_forever()
