#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
说明：该类用于访问http类网站
'''

# python standard library
import httplib

# local pret classes

class https:
    '''
    @此类用于处理https数据
    注：效果不好，待修改
    '''
    def get_https(URL):
        '''
        @get_https(URL)函数用于连接htts的get型数据包，效果不好，高版本修改
        return res.status, res.reason, res.read()
        '''
        httpsConn = httplib.HTTPSConnection(URL)
        httpsConn.request("GET", "/")
        res = httpsConn.getresponse()
        return res.status, res.reason, res.read()

    def post_https(URL):
        '''
        @post_https(URL)函数用于连接htts的post型数据包，效果不好，高版本修改
        return res.status, res.reason, res.read()
        '''
        httpsConn = httplib.HTTPSConnection(URL)
        httpsConn.request("POST", "/")
        res = httpsConn.getresponse()
        return res.status, res.reason, res.read()

class http:
    '''
    @此类处理http数据
    '''
    pass
class url_request(object):
    '''
    @此类处理url的提交问题，调用request模块
    '''
    def __init__(self):
        '''
        @初始化数据
        '''
        pass
    def post(self,*args, **kwargs):
        '''
        @POST数据
        '''
        pass
    def get(self,*args, **kwargs):
        '''
        @GET数据
        '''
        pass
    

