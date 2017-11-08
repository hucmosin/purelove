#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date 2017/10/9 

import struts_scan as m

def s_main(url,filename):
    if url:
        m.check_url(url)
    elif filename:
        m.check_file(filename)
    else:
        print('[-] Exploit Error. ')
