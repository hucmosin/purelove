#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
说明:自定义Process,Thread
"""

#
# https://github.com/hucmosin/purelove
#

from multiprocessing import Process
from threading import Thread

class PLProcess(object):
    '''
    Create a Process.
    '''

    def __init__(self,process,args):
        self.process = process
        self.args = args
        self.p = ""

    def create_process(self):
        self.p = Process(target = self.process ,args = self.args)
        self.p.start()
    
    def stop_process(self,p):
        self.p.stop()

class PLThread(object):
    '''
    Create a Thread.
    '''

    def __init__(self,plthread = "",args = ""):
        self.plthread = plthread
        self.args = args
        self.t_thread = ""

    def create_thread(self):
        if self.plthread == "":
            return
        elif self.args == "":
            self.t_thread = Thread(target = self.plthread)
            self.t_thread.start()
        else:   
            self.t_thread = Thread(target = self.plthread, args = self.args)
            self.t_thread.start()
    
    def stop_thread(self):
        self.t_thread.stop()



