#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author:mosin
@date:2018-6-05
说明：该文件类主要为框架模块提供时间支持，方便提取整数和其他需要的时间格式
'''

import time
import os

class Time(object):
    """
    Time Arr
    """
    def __init__(self):
        pass

    def get_date(self):
        '''
        @ 获取当前日期，如：2018-06-01
        '''
        this_date = time.strftime("%Y-%m-%d", time.localtime())
        return this_date

    def TimeStampToTime(self,timestamp):
        '''
        把时间戳转化为时间: 1479264792 to 2016-11-16
        '''
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d',timeStruct)

    def get_now_time(self):
        '''
        @获取当前年月日时间，整体时间..
        格式化成2018-01-01 11:45:39形式
        '''
        this_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return this_date
    
    def get_createfile_time(self,filePath):
        '''
        获取文件的创建时间
        '''
        filePath = unicode(filePath,'utf8')
        t = os.path.getctime(filePath)
        return self.TimeStampToTime(t)

    def get_time_hhmmss(self):
        '''
        Returns the current time, used to display
        example:[11:11:11]
        '''
        this_date = time.strftime("%H:%M:%S", time.localtime())
        this_date = "[" + this_date + "]"
        return this_date

