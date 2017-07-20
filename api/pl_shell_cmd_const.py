#! /usr/bin/env python
#coding=utf-8

import os


#定义了shell命令的内容，用于将来功能的扩展。
#-------------------------------------------------------------------------------
#shell执行命令
PL_SHOW         =       "show"
PL_HELP         =       "help"
PL_USE          =       "use"
PL_SEARCH       =       "search"
PL_SET          =       "set"
PL_WINDOWS_CLS  =       "cls"                           #windows系统清屏
PL_LINUX_CLEAR  =       "clear"                         #liux系统清屏
PL_EXIT         =       "exit"
PL_SHOW_OPTIONS =       "show options"
PL_RUN          =       "run"
PL_EXPLOIT      =       "exploit"
PL_INFO         =       "info"
PL_VERSION      =       "version"
PL_OS_SHELL     =       "shell"
#-------------------------------------------------------------------------------
#全局常量
PL_EMPTY        =       ""
PL_POC_NAME     =       ""                              #利用程序获取到POC路径文件名 example:ms17-010
PL_FILE_PATH    =       ""  	            		#poc文件目录，不加文件名 example:explot/windows/smb/
PL_PWD          =       os.getcwd()                              #获取当前绝对路径
PL_PAYLOAD_DIR  =       "/payloads"                     #poc所在目录
PL_POC_FILE     =       ""  				#完整的路径加文件名 example:explot/windows/smb/ms17-010
PL_BACK         =       "back"
PL_STATUS       =       True
PL_POC_OPTION   =       {}                              #存储set命令



