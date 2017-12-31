#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：帮助
"""

# python standard library

from color import *

def main_help():
	print (bcolors.GREEN+"""
Usage Commands
===============
\tCommands		Description
\t------------		-------------
\thelp           		Help menu
\tuse 			Select Module For Use
\tshow modules    	Show Modules of Current Database
""")

def shellcode_help():
	print (bcolors.GREEN+"""
Shellcode Commands
===================
\tCommands		Description
\t------------		-------------
\tback			Exit Current Module
\tgenerate 		Generate shellcode 
\toutput 			Save option to shellcode(txt,py,c,cpp,exe)
\tshow options		Show Current Options Of Selected Module
""")

def def_shellcode_help():
	print (bcolors.GREEN+"""
Shellcode Commands
===================
\tCommands		Description
\t------------		-------------
\tback			Exit Current Module
\toutput 			Save option to shellcode(txt,py,c,cpp,exe)
\tshow options		Show Current Options Of Selected Module
""")






	
