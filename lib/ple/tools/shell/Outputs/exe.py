#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：shellcode生成类
"""

# python standard library

def ExeFile( shellcode, OS=None,filename = None):
    if OS == None:
        OS = detectOS()
    from .logger import logs
    from .Database.exedb import Module_db

    db = Module_db()
    padd = ""
    if OS == "windows":
        padd = db[2]
    else:
        print "Not supported os .."
        return
    houz = "exe"
    shellcode = shellcode.replace("\\x", "")
    shellcode = padd.replace("SHELLCODE", shellcode)
    logs( shellcode.decode("hex"), houz,filename)


	
def architectureDetect():
    #https://github.com/kennethreitz/its.py/blob/master/its.py
    from struct import calcsize
    if calcsize('P') * 8 == 64:
        return 64
    elif calcsize('P') * 8 == 32:
        return 32
    else:
	#Are you on fcking 8bits OS ? or 128bits ?!
        return "Not supported architecture .."

def detectOS():
    from sys import platform 

    if architectureDetect() == 32:
        if platform.lower() == "linux" or platform == "linux2":
            return "linux86"
	    #elif platform.lower() == "darwin":
	    #print "mac osx"
        elif platform.lower() == "win32":
            return "windows"
        elif platform.lower() == "sunos":
            return "solarisx86"
        elif "freebsd" in platform.lower():
            return "freebsdx86"
        elif "openbsd" in platform.lower():
            return "openbsdx86"

            #I will fix it soon :(
        elif architectureDetect() == 64:
            if "freebsd" in platform.lower():
                return "freebsdx64"
            elif "win32" in platform.lower():
                return "windows"

    else:
	#This is can be possible ? ..
        print ("Not supported architecture ..")

