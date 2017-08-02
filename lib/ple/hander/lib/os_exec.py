# -*- coding: utf-8 -*-

#执行系统命令，返回字符串
import os

def os_exec(args):
    cmd_args = os.system(args)
    return cmd_args

