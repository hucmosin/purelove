#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: mosin <hucmoxing@163.com>
date:2018-06-09
"""

import base64

class BaseDecode(object):
  
  def base64_decode(data):
    '''
    return base64 decryption
    '''
    encode = base64.b32decode(data)
    return encode

  def base32_decode(data):
    '''
    return base32 decryption
    '''
    encode = base64.b32decode(data)
    return encode

  def base16_decode(data):
    '''
    return base16 decryption
    '''
    decode = base64.b16decode(data)
    return decode
