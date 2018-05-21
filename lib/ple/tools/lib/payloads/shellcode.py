#! /usr/bin/env python
# -*- coding: utf-8
"""
说明：shellcode框架模块主体函数调用，用于继承
"""

# python standard library

"""
Copyright (c) 2016-2017
"""

from disassembly import Disassembly
from dotted import DottedDict
from re import findall
import codecs
from abc import ABCMeta, abstractmethod


def plaintext( string):
    string = codecs.encode(str.encode(string), 'hex')
    string = string.decode('utf-8')
    db = findall("..?", string)
    return "\\x"+"\\x".join(db)


def plaintextreverse( string):
    string = codecs.encode(str.encode(string), 'hex')
    string = string.decode('utf-8')
    db = findall("..?", string)
    return "\\x"+"\\x".join(db[::-1])

def rawSTR( string):
    db = []
    for x in string:
        first = codecs.encode(str.encode(x), 'hex')
        x = first.decode('utf-8')
        db.append("\\x"+x)
    return "".join(db)


def ARM( string):
    db = []
    if "/" in string:
        if len(string) % 4 == 0:
            string = string
        elif  len(string) % 4 == 1:
            string = filler( string, 4)
        elif len(string)	% 4 == 2:
            string = filler( string, 3)
        elif len(string) % 4 == 3:
            string = filler( string, 2)
        for x in range(0,len(string),4):
            db.append(ARMsplitter(string[x:x+4]))
        return "".join(db)


def ARMsplitter( hexdump, pushdword="None"):
    db = []
    if pushdword == "None":
        fixmesempai = findall('....?', hexdump)
        for x in fixmesempai[::-1]:
            first = codecs.encode(str.encode(x[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            db.append("\\x"+"\\x".join(second))
        return "".join(db)			


def stackconvertSTR(string, win=False):
    db = []
    if len(string) == 1:
        string = codecs.encode(str.encode(string), 'hex')
        string = string.decode('utf-8')
        return r"\x6a"+r"\x"+string

    if "/" in string:
        if len(string) % 4 == 0:
            string = string
        elif  len(string) % 4 == 1:
            string = filler( string, 4)
        elif len(string)	% 4 == 2:
            string = filler( string, 3)
        elif len(string) % 4 == 3:
            string = filler( string, 2)
        for x in range(0,len(string),4):
            db.append(splitter(string[x:x+4]))
        return "".join(db[::-1])
        #return "".join(db)

    #Linux_x86
    #68 PUSH DWORD
    #6668 PUSH WORD
    #6A PUSH BYTE
    if len(string) == 4:
        first = codecs.encode(str.encode(string[::-1]), 'hex')
        stack = first.decode('utf-8')
        data = findall("..?", stack)
        return "\\x68\\x"+"\\x".join(data)


    elif len(string) % 4 == 0:
        for x in range(0,len(string),4):
            db.append(splitter(string[x:x+4]))
        if win == True:
            return "".join(db[::-1]) #Windows
        else:
            return "".join(db) #Unix,Linux etc..

    elif len(string) ==3:
        first = codecs.encode(str.encode(hexdump[::-1]), 'hex')
        first = first.decode('utf-8')
        second = findall("..?", first)[::-1]
        for x in second:
            db.append("\\x"+x)
        return "\\x66\\x68"+"".join(db)


    else:
        db = []
        for x in range(0,len(string),4):
            if len(string[x:x+4]) == 4:
                db.append(splitter(string[x:x+4]))
            else:
                db.append(splitter(string[x:x+4], "WordTime"))
        if win == True:
            return "".join(db[::-1]) #Windows
        else:
            return "".join(db) #Unix,Linux etc..)


def filler( string, number):
    string = [x for x in string]
    for x in range(0, len(string)):
        if string[x] == "/":
            string[x] = "/"*number
            break
    return "".join(string) 


def splitter( hexdump, pushdword="None"):
    db = []
    if pushdword == "None":
        fixmesempai = findall('....?', hexdump)
        for x in fixmesempai[::-1]:
            first = codecs.encode(str.encode(x[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            db.append("\\x"+"\\x".join(second))
        return "\\x68"+"".join(db)	

    else:		
        #Byte ..
        if len(hexdump) == 1:
            string = codecs.encode(str.encode(hexdump), 'hex')
            string = string.decode('utf-8')
            return r"\x6a"+r"\x"+string
        else:
            first = codecs.encode(str.encode(hexdump[::-1]), 'hex')
            first = first.decode('utf-8')
            second = findall("..?", first)[::-1]
            for x in second:
                db.append("\\x"+x)
            return "\\x66\\x68"+"".join(db)


class Shellcode(Disassembly):
    __metaclass__ = ABCMeta   #虚拟抽象本类
    info = {
        "author": "",
        "credits": "",
        "name": "",
        "references": "",
        "platform": "",
        "disclosureDate": "",
        "reliability": "",
        "rawassembly": "",
        "size": "",
        "payload": "",
    }

    def __init__(self):
        super(Shellcode, self).__init__()
        Disassembly.__init__(self)
        self.options = {}

    def getpayload(self):
        return Shellcode.info["payload"][0]

    def getsize(self, x):
        return len(x.split("\\x"))
    
    @abstractmethod
    def sld(self):
        pass
    
    def register_option(self, dict_option):
        assert isinstance(dict_option, dict)
        self.options = DottedDict(dict_option)

    @staticmethod
    def prettyout(shellcode):
        from re import findall
        data = shellcode.replace("\\x", "")
        db = []
        print("\n")
        for x in [data[x:x + 40] for x in range(0, len(data), 40)]:
            db = findall("..?", x)
            if data.endswith(x):
                print('\t"\\x' + "\\x".join(db) + '"')
            else:
                print('\t"\\x' + "\\x".join(db) + '"' + ' +')
        print("\n")
