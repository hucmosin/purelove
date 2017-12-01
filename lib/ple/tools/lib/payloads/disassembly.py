#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：HEX编译替换
"""

# python standard library

class Disassembly(object):
    "Require shellcode format to disassembly \xFF\xFF\xFF\xFF .."
    def startdisas(self, shellcode, string):
        if string == "None":
            print("[+] Shellcode must be generate before disassembly !")
            return None

        shellcode = self.getrawhex(shellcode)
        if "linux_mips" not in string or "linux_mips" not in string:
            from shell.disassembly.dis import disas

            try: 
                if "64" in string:
                    print(disas(str(bytearray(shellcode.decode("hex"))), 64))
                elif "86" in string:
                    print(disas(str(bytearray(shellcode.decode("hex"))), 32))
                else: 
                    print(disas(str(bytearray(shellcode.decode("hex"))), 32))
            except TypeError:
                print("Disassembly failed.Please do not forget report.")

        else:
            from shell.disassembly.dis2 import disasNOTintel
            try:
                print("\n\n")
                if "mips" in string:
                    print(disasNOTintel(shellcode.decode("hex"), "mips", 32))
                else:
                    if "64" in string:
                        print(disasNOTintel(shellcode.decode("hex"), "arm", 64))
                    elif "86" in string:
                        print(disasNOTintel(shellcode.decode("hex"), "arm", 32))
                print("\n\n")
            except TypeError as err:    
                print("[+] Disassembly failed.Please do not forget report.")

    def getrawhex(self, x):
        return x.replace("\\x", "")
