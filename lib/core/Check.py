#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re


'''
Check IP
'''
class CheckIP:

    def __init__(self):
        pass
    
    def check_ip(self,ip):
        '''
        Check IP is True or False
        '''
        pat = re.compile(r'([0-9]{1,3})\.')  
        r = re.findall(pat,ip+".")
        if len(r)==4 and len([x for x in r if int(x)>=0 and int(x)<=255])==4:  
            return True
        return False

    def ip_into_int(self,ip):
        return reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))

    def is_internal_ip(self,ip):
        '''
        Check Intranet ip
        Return True Or False
        '''
        ip = self.ip_into_int(ip)
        net_a = self.ip_into_int('10.255.255.255') >> 24
        net_b = self.ip_into_int('172.31.255.255') >> 20
        net_c = self.ip_into_int('192.168.255.255') >> 16
        return ip >> 24 == net_a or ip >>20 == net_b or ip >> 16 == net_c
    
