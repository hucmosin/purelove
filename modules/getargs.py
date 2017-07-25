#!/usr/bin/env python
# coding=utf-8


import sys
import infos
import printlogo
import getopt
from optparse import OptionError
from optparse import OptionParser




def usage():
    printlogo.printlogo()
    usage = "python %s -target www.example.com[-m[--mode] [payload,exploit]] [-d [--debug]]" \
            "\r\n example:python poc_001.py  --target[-t] www.example.com --mode[-m] payload " \
            "\r\n example:python poc_001.py  --target[-t] www.example.com --debug[-d] --mode[-m] payload"% sys.argv[0]
    return usage


def bgarg(bg_instance):
    """
    其他参数名约定：
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hu:m:d:', ['help', 'url=', 'mode=','debug='])
    except:
        usage()

    url = 'www.baidu.com'
    mode = 'payload'
    
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-u', '--url'):
            url = a
        elif o in ('-m', '--mode'):
            mode = a
            if mode == 'exploit': 
                bg_instance.exploit()       # 默认为 exploit，如果用户指定payload则重新赋值
            else:
                bg_instance.payload()
        elif o in ('-d', '--debug'):
            bg_instance.log_level = BGLogLevel.debug   
"""
    #换个参数好用的
    parser = OptionParser(usage=usage())
    try:
        parser.add_option("-t", "--target", dest="target", default = '') 
	parser.add_option("-m", "--mode", dest="mode", default = 'payload',  
		                  help="Exploit vuln or attack it, \"exploit\" for verify and \"payload\" for attack")
	parser.add_option("-d", "--debug", dest="debug", action="store_true", 
		                  help="Print debug info")
	(options, args) = parser.parse_args()
	
        bg_instance.option.target['default'] = options.target
        
        infos.bginfos(bg_instance)
        
        if options.debug == 'debug':
            bg_instance.log_level = BGLogLevel.debug
            
	if options.mode == 'exploit': 
	    bg_instance.exploit()       # 默认为 exploit，如果用户指定payload则重新赋值
	else:
            bg_instance.payload()

    except (OptionError, TypeError), e:
	parser.error(e)

