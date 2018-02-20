#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
@Author:mosin
@date:2018-2-20
说明：该文件类主要为框架模块提供时间支持，方便提取整数和其他需要的时间格式
'''

import time

class Mytime(object):
    '''
    @ 封装时间操作类
    '''
    def __init__(self):
        pass

    def get_date(self):
        '''
        @ 获取当前日期，如：2018-01-01
        '''
        this_date = time.strftime("%Y-%m-%d", time.localtime())
        return this_date
    def get_now_time(self):
        '''
        @获取当前年月日时间，整体时间..
        格式化成2018-01-01 11:45:39形式
        '''
        this_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return this_date