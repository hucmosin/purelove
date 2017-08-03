# -*- coding: utf-8 -*-
#

import datetime
import sys
import urllib

def wget(url):
    if not url.startswith('http'):
        return '[!] Error: URL must begin with http:// or https:// .'

    fname = url.split('/')[-1]
    if not fname:
        dt = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-')
        fname = 'file-{}'.format(dt)

    try:
        urllib.urlretrieve(url, fname)
    except IOError:
        return '[-] Error: Download failed.'

    return '[*] File {} downloaded.'.format(fname)

