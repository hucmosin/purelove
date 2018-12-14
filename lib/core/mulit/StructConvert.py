#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
* Author: Mosin
* Desc  : This class is mainly to complete the Struct function encapsulation.
* This class is mainly for the transformation plastic data.
'''


class StructConvert:
    """
    参数转换，工具调用,Need Decimal data.
    """
    @staticmethod
    StructConvert_big_L(string):
        '''retuen HEX Sting'''
        a = struct.pack('>L', int(str(string)))
        return a.encode('hex')
        
    @staticmethod
    StructConvert_little_L(string):
        '''retuen HEX Sting'''
        a = struct.pack('<L', int(str(string)))
        return a.encode('hex')

    @staticmethod
    StructConvert_big_I(string):
        '''retuen HEX Sting'''
        a = struct.pack('>I', int(str(string)))
        return a.encode('hex')
        
    @staticmethod
    StructConvert_little_I(string):
        '''retuen HEX Sting'''
        a = struct.pack('<I', int(str(string)))
        return a.encode('hex')
