#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: mosin <hucmoxing@163.com>
"""

'''
Used to transform data flow to HEX, 
or the perfect presentation of memory data.
'''
def hexdump(src,length=16):
    '''
    src = "This is Purelove! Hello Purelove!"
    This Function return 
    0000   54 68 69 73 20 69 73 20 50 75 72 65 6C 6F 76 65    T h i s   i s   P u r e l o v e
    0010   21 20 48 65 6C 6C 6F 20 50 75 72 65 6C 6F 76 65    !   H e l l o   P u r e l o v e
    0020   21                                                 !
    '''
    
    result = []
    digits = 4 if isinstance(src,unicode) else 2

    for i in xrange(0 , len(src) , length):
        s = src[i:i + length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b' '.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append(b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text))

    return b'\n'.join(result)

