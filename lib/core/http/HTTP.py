#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
说明：该类用于访问http类网站
'''

# python standard library
import httplib
import httppost

# local pret classes

class https(object):
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
        self.hh = httppost.httppost()
        
    def post(self,url,data="",headers=""):
        r'''
        @POST数据,retuen code,head,html,redirect,log
        url_request = url_request()
        url = "http://httpbin.org/post"
        data = "key1=val1&key2=val2"
        # proxy_str = ('127.0.0.1', 9119)
        headers = {
            'X-Forwarder-For': 'https://www.test.com',
            'Test-Http': 'Header Dict Val'
        }
        code,head,html,redirect,log = url_request.post(url,data,headers)
        
        print log['request']
        print "============="
        print log['response']
        '''
        
        if data == "" and headers !="":
            code,head,html,redirect,log = self.hh.http(url, headers = headers)
            return code,head,html,redirect,log
        elif headers == "" and data !="":
            code,head,html,redirect,log = self.hh.http(url, post = data)
            return code,head,html,redirect,log
        elif headers != "" and data !="":   
            code,head,html,redirect,log = self.hh.http(url, post = data, headers = headers)
            return code,head,html,redirect,log

    def post_raw(self,url,raw_data):
        '''
        @retuen code, head, html, redirect, log
        url_request = url_request()
        
        raw_data = \'''POST /post HTTP/1.1
        Host: httpbin.org
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
        Accept-Encoding: gzip, deflate
        Connection: close
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 19
        key1=val1&key2=val2
        \'''
        code, head, html, redirect, log = url_request.post_raw('http://httpbin.org/post', raw=raw)
        print log['request']
        '''
        
        code, head, html, redirect, log = self.hh.http(url, raw_data = raw_data)
        return code, head, html, redirect, log

    def http_proxy(self,url, proxy_str):
        '''
        url_request = url_request()
        proxy_str = ('127.0.0.1',80)
        url_request.http_proxy(proxy_str)
        '''
        code, head, body, redirect, log = self.hh.http(url, proxy=proxy_str)
        return code, head, body, redirect, log

    def get(self,url):
        '''
        @GET数据 retuen code, head, html, redirect, log
        url_request = url_request()
        code, head, body, redirect, log = url_request.get('https://www.test.com')
        '''
        
        code, head, html, redirect, log = self.hh.http(url)
        return code, head, html, redirect, log
        
