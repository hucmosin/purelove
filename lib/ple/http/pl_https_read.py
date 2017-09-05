#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
说明：该类用于访问http类网站
"""

# python standard library
import httplib

# local pret classes


def get_https(URL):
    httpsConn = httplib.HTTPSConnection(URL)
    httpsConn.request("GET", "/")
    res = httpsConn.getresponse()
    return res.status, res.reason, res.read()

def post_https(URL):
    httpsConn = httplib.HTTPSConnection(URL)
    httpsConn.request("POST", "/")
    res = httpsConn.getresponse()
    return res.status, res.reason, res.read()
