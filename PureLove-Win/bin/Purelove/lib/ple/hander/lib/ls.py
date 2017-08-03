# -*- coding: utf-8 -*-
#

import os

def ls(path):
    if not path:
        path = '.'
    if os.path.exists(path):
        try:
            return '\n'.join(os.listdir(path))
        except OSError:
            return '[!] Error: Permission denied.'
    else:
        return '[!] Error: Path not found.'
