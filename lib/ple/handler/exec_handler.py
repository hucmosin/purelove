#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date:2018-05-17
# Author:mosin
# https://github.com/hucmosin/purelove
#

from ..handler.module import nc
#from multiprocessing import Process
from threading import Thread
import sys

'''
对Handler模块进行判断
'''
class judgeHandler(object):
    
    def __init__(self, poc):
        self.poc = poc
        
    def judge_str(self):
        t_list = []
        if self.poc.handler.payload == "":
            #未指定则默认调用NC
            '''
            p1 = Process.PLThread(plthread = nc.run_handler, args = ['0.0.0.0',4444])
            p2 = Process.PLThread(plthread = self.poc.exploit)
            p1.create_thread()
            p2.create_thread()
            '''
            try:
                t1 = Thread(target = nc.run_handler,args = [self.poc.handler.payload_fun.option.LHOST['default'],self.poc.handler.payload_fun.option.LPORT['default']])
                t_list.append(t1)
                t2 = Thread(target = self.poc.exploit)
                t_list.append(t2)
                for t in t_list:
                    t.start()
                for t in t_list:
                    t.join()
            except:
                pass
            #sys.exit(0)

            #module.nc.run_handler(host = '0.0.0.0', port = 19954)
        else:
            #执行handler
            try:
                self.poc.handler.payload_fun.exploit()
            except:
                pass

            
