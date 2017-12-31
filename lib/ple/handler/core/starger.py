#-*- coding: utf-8 -*-

'''
@DATA:2017-12-25
@Author:Mosin
@Email: <hucmoxing@163.com>
@后门数据读取模块
'''

def get_win_rple():
    '''
    * win反弹型后门 reverse
    * 返回值为: dll_len,data
    * 读取dll文件，返回数据
    * 返回dll长度，数据
    '''
    #读取dll文件
    dll_file = "lib/soure/windows/win_reverse_dll.dll"
    try:
        f_data = open(dll_file,'rb')
        data = f_data.read()
    except:
        print "DLL File Reading Fail => " + dll_file
        return None,None
    #dll长度获取
    dll_len = str(len(data))
    return dll_len,data

def get_win_bple():
    '''
    win绑定型后门
    '''
    pass
def get_linux_rple():
    '''
    lINUX反弹型后门
    '''
    pass
def get_linux_bple():
    '''
    LINUX绑定型后门
    '''
    pass
def get_http_ple():
    '''
    HTTP型后门
    '''
    pass
