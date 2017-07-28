#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
说明：该类用于接收框架的参数,并提供文件操作函数
"""

# python standard library
import os
import sys
import json

root_path = "../"
sys.path.append(root_path)


# local pret classes
#import pl_shell_cmd_const as const
import pl_os_operation as operation
import pl_poc_frame as frame
import modules.getinfo as getinfo
from modules.exploit import BGLogLevel, BGSeverity, BGType


def pl_path_split_first_name(file_path):
    system = operation.pl_get_UsePlatform()
    try:
        if system == 'Windows':
            lists = file_path.split('\\')   #分割出文件名
            return lists[0]
        elif system == 'Linux':
            lists = file_path.split('/')         #分割出文件名
            return lists[0]
        else:
            pass
    except:
        return

def pl_path_split_end_name(file_path):
    system = operation.pl_get_UsePlatform()
    try:
        if system == 'Windows':
            lists = file_path.split('\\')       #分割出文件名
            #print lists
            return lists[-1]
        elif system == 'Linux':
            lists = file_path.split('/')         #分割出文件名
            return lists[-1]
        else:
            pass
    except:
        return

def pl_show_poc_info(PL_POC_FILE):
    try:
        if PL_POC_FILE[-3:] == ".py":
            poc_info = getinfo.import_poc(PL_POC_FILE)
            print poc_info
        else:
            PL_POC_FILE = PL_POC_FILE + '.py'
            poc_info = getinfo.import_poc(PL_POC_FILE)
            print poc_info
    except:
        print u"[-] 加载文件信息出错 "


#返回绝对路径
def pl_return_path(pwd, path):
    PL_POC_FILE = pwd + '/' + path
    try:
        if PL_POC_FILE[-3:] == ".py":
            return PL_POC_FILE
        else:
            PL_POC_FILE = PL_POC_FILE + '.py'
            return PL_POC_FILE
    except:
        print u"[-] 加载出错,查看是否存在该文件 "
    
def pl_run_poc(poc):
    pl_bg_arg(poc)
    try:
        results = [poc.result.to_python()]
        json.dumps(results)
    except Exception, e:
        print(u'[-] result 序列化失败')
        print(e)
        return
    
    if poc.option.debug.default == "":
        if poc.result.status:
            print(u'[ 编写作者 ]')
            print(u'\t{poc_author}'.format(poc_author = str(poc.info.get('author', ''))))
            print(u'[风险]')
            print('\t目标存在 {poc_name}'.format(poc_name  = poc.info.get('name', '').strip()
                                                    )).decode('utf-8')
            print('\t{desc_target}: {default_target}\n\t{desc_port}: {default_port}\r\n'.format(
                                                     desc_target      =   poc.option.target.desc,
                                                     default_target   =   poc.option.target.default,
                                                     desc_port        =   poc.option.port.desc,
                                                     default_port     =   poc.option.port.default
                                                     )).decode('utf-8')
            print(u'[详细说明]')
            print('\t{poc_desc}'.format(poc_desc = poc.info.get('desc', '').strip())).decode('utf-8')

            print(u'[程序返回]')
            print('\t{poc_return}'.format(poc_return = poc.result.get('description', '').strip())).decode('utf-8')

            print(u'[危害等级]')
            print('\t{poc_severity}'.format(poc_severity = poc.info.get('severity', ''))).decode('utf-8')

            print(u'[漏洞类别]')
            print('\t{poc_type}'.format(poc_type = poc.info.get('type', ''))).decode('utf-8')

            print(u'[相关引用]')
            for each_ref in poc.info.get('ref', {}):
                if not each_ref:
                    return

                ref_key = each_ref.keys()[0]
                print('\t* {ref_key}: {ref_value}'.format(ref_key = ref_key, ref_value = each_ref.get(ref_key).strip())).decode('utf-8')
        
        elif poc.result.exp_status:
            print u"[*]Start Exploit...."
        else:
            pass

    elif poc.option.debug.default == "debug":
        pass
    else:
        error = "[!] debug error"
        poc.print_error(error)
        

def pl_get_poc_option(PL_POC_FILE):
    try:
        if PL_POC_FILE[-3:] == ".py":
            poc_option = getinfo.import_pocs(PL_POC_FILE)
            if poc_option == None:
                pass
            else:
                return poc_option.option
        else:
            PL_POC_FILE = PL_POC_FILE + '.py'
            poc_option = getinfo.import_pocs(PL_POC_FILE)
            if poc_option == None:
                pass
            else:
                return poc_option.option
    except:
        print u"[-] 加载文件信息出错 "

def pl_add_option(dicts,key,value):
    if key in dicts:
        dicts[key] = value
        return dicts
    else:
        dicts.setdefault(key,value)
        return dicts
#pl_add_option(p,option_key,option_value)


def pl_bg_arg(poc):
    try:
        if poc.option.debug.default == 'debug':
            poc.log_level = BGLogLevel.debug
            if poc.option.mode.default == 'exploit': 
                poc.exploit()       # 默认为 exploit，如果用户指定payload则重新赋值
            else:
                poc.payload()
        else: 
            if poc.option.mode.default == 'exploit': 
                poc.exploit()       # 默认为 exploit，如果用户指定payload则重新赋值
            else:
                poc.payload()
    except:
	print u"[-] 载入失败 "

	

def pl_run_poc_show(poc,poc_re):
    print
    print "Module options " + '(' + poc_re + ') :'
    print
    print
    print "\t{Name:<35}{CurrentSetting:<35}{Required:<35}{Descriptions:<35}".format( Name            = "Name",
                                                                                     CurrentSetting = "Current Setting",
                                                                                     Required        = "Required",
                                                                                     Descriptions    = "Description").decode('utf-8')
    print "\t{Name:<35}{DisclosureDate:<35}{Rank:<35}{Descriptions:<35}".format(     Name            = "----",
                                                                                     DisclosureDate  = "---------------",
                                                                                     Rank            = "--------",
                                                                                     Descriptions    = "-----------").decode('utf-8')
    for option, option_filter in poc.option.items():
       # t = option + " " + str(option_filter['default']) + " " + str(option_filter['Required']) + " " + str(option_filter['desc'])
        print "\t{option:<35}{default:<35}{Required:<35}{Descriptions:<35}".format( option       = option,
                                                                                    default      = str(option_filter['default']),
                                                                                    Required     = str(option_filter['Required']),
                                                                                    Descriptions = str(option_filter['desc'])).decode('utf-8')
        #print '\t' + option + '\t\t' + str(option_filter['default']) + '\t\t\t\t\t\t\t' + str(option_filter['Required']) + '\t\t\t\t\t\t' + str(option_filter['desc'])
    print 





#show version
def pl_show_version(PL_PWD):
    print
    print "PureLove Version Info"
    print "---------------------"
    print
    f = open(PL_PWD + '/bin/Purelove/api/config/poc_config.ini')
    ff = f.readlines()
    for i in ff:
        i = i.replace('\n',"")
        print "\t" + i
 

    f.close()








    
    




