#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#
# https://github.com/hucmosin/purelove
#


from handler_server import *
from module import nc_bind


def lunch(host = '0.0.0.0',port = 4444):
    print "[*] Handler Start Open"
    run_handler(host , port)


def lunch_bind(host = '0.0.0.0',port = 4444):
    print "[*] Handler Start Open"
    nc_bind.run_handler(host , port)
