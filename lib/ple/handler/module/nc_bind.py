#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#=====================================
# Fix Date:2018-10-30
# Fix Author:mosin
# Fix NC Handler Module
#=====================================
# https://github.com/hucmosin/purelove
#

import socket
import sys
import time
import nc_bind_handler

#启动监听
def run_handler(host = '127.0.0.1',port = 4444):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect((host, port))
    nc_bind_handler.nc(sock)
