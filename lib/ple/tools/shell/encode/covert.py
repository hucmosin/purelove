#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# python standard library
import binascii
import socket

class CovertBin:

    def __init__(self,shellcode):
        self.shellcode = shellcode

    def little_covert_port(self,port=4444):
        '''
        @Escape in the little end format
        '''
        try:
            res_port = "%.4x" % int(port)
        except:
            print "[-] Convert port Error."
        default_port = self.shellcode.replace("\\x","").replace("115C",res_port)
        return default_port
        
    def little_covert_ip(self,ip="127.0.0.1"):
        '''
        @Escape in the little end format
        '''
        ip_shellcode_stage = binascii.hexlify(socket.inet_aton(ip))
        default_ip = self.shellcode.replace("\\x","").replace("7F000001",ip_shellcode_stage)
        return default_ip

    def little_covert_all(self,ip,port):
        #Covert port
        try:
            port_shellcode_stage = "%.4x" % int(port)
        except:
            print "[-] Convert port Error."

        #Covert Host
        ip_shellcode_stage = binascii.hexlify(socket.inet_aton(ip))
        #Replace Shellcode
        default_result = self.shellcode.replace("\\x","").replace("115C",port_shellcode_stage).replace("7F000001",ip_shellcode_stage)
        return default_result

    def big_covert_port(self,port=4444):
        '''
        @Escape in the big end format
        '''
        pass
    
    def big_covert_ip(self,ip="127.0.0.1"):
        '''
        @Escape in the big end format
        '''
        pass
