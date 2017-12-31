# -*- coding: utf-8 -*-
#
'''
@DATA:2017-12-28
@Author:mosin
@Email:<hucmoxing@163.com>
说明:windows系统shell反弹监听连接处理，集成handler中，只可特定应用
'''


def exec_shell(sock):
    '''
    @本函数需传入一个socket套接字，因为为了与windows下的命令管道相连接，配合本监听程序
    '''
    from .core import nc_cmd_shell
    while True:
        nc_cmd_shell.nc(sock)
        prompts = raw_input()
        if not prompts:
            continue
        if prompts == "exit" or prompts == "quit":
            break
sock = "sss"
exec_shell(sock)
