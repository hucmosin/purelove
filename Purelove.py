#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：漏洞利用框架主程序
"""
# python standard library
import os

# local pret classes
import api.pl_os_operation as  operation
from api.db.loader_db import *
import api.pl_shell_cmd_const as const 
import api.parsers as parser
import modules.printlogo as logo
import api.banner as banner
import api.pl_print_world_color as setcolor

# -------------------------------------------show---------------------------

def main():
  #const.PL_POC_FILE = const.PL_PWD + const.PL_PAYLOAD_DIR
  #加载poc
  print setcolor.set_blue("[*] ") + "Loding....."
  check_db = loadDB(const.PL_PWD)
  check_db.check_modules()
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
