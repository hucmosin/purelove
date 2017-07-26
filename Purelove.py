#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：漏洞利用框架主程序
"""
# python standard library
import os

# local pret classes
import api.pl_os_operation as  operation
import api.pl_shell_cmd_const as const 
import api.parsers as parser
import modules.printlogo as logo
import api.banner as banner
import api.pl_print_world_color as setcolor

# ----------------------------------------------------------------------

def main():
  #PL_PWD = os.getcwd()
  const.PL_POC_FILE = const.PL_PWD + const.PL_PAYLOAD_DIR
  #加载poc
  print setcolor.set_blue("[*] ") + "Loding....."
  operation.pl_get_poc_name(const.PL_PWD, const.PL_POC_FILE)
  #交互shell死循环,传入绝对路径
  #打印出框架LOGO
  print setcolor.set_green("[*] ") + "Loding down..."
  logo.purelove_logo()
  banner.pl_get_banner()
  parser.shell(const.PL_PWD)

# ----------------------------------------------------------------------

# clean exit
if __name__ == '__main__':
  try:
    main()
  # catch CTRL-C
  except (KeyboardInterrupt):
    pass
  finally:
    print("")
