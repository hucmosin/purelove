# -*- coding: utf-8 -*-
#

import zipfile
import os

def unzip(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return '[*] File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return '[!] Error: Failed to unzip file.'
    else:
        return '[-] Error: File not found.'
