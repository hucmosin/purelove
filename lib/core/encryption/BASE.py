#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: mosin <hucmoxing@163.com>
date:2018-06-09
"""

import base64

class BaseEncode(object):
  
  def base64_encode(data):
    '''
    return base64 encryption
    '''
    encode = base64.b64encode(data)
    return encode

  def base32_encode(data):
    '''
    return base64 encryption
    '''
    encode = base64.b32encode(data)
    return encode

  def base16_encode(data):
    '''
    return base64 encryption
    '''
    encode = base64.b16encode(data)
    return encode

