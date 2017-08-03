# -*- coding: utf-8 -*-

#执行系统命令，返回字符串
import os
import subprocess

def os_exec(args):
    cmd_args = os.system(args)
    return cmd_args

def execute(command):
    output = subprocess.Popen(command, shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
    return output.stdout.read() + output.stderr.read()


