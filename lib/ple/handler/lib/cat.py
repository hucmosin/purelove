# -*- coding: utf-8 -*-
#

import os

def cat(file_path):
    if os.path.isfile(file_path):
        try:
            with open(file_path) as f:
                return f.read(4000)
        except IOError:
            return '[!] Error: Permission denied.'
    else:
        return '[!] Error: File not found.'
