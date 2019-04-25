#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: mosin <hucmoxing@163.com>
desc:This file is Get Shellcode.
Date:2019-04-21
"""

class GetShellcode:

    def __init__(self,data):
        self.shellceode_data = data

    def coverdata(self):
        default_result = self.shellceode_data.replace("\\x","")
        return default_result.decode("hex")
