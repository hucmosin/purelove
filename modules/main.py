#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2017-2018

"""

import json
import getargs
from exploit import BGLogLevel, BGSeverity, BGType


def main(bg_instance):

    getargs.bgarg(bg_instance)

    try:
        results = [bg_instance.result.to_python()]
        json.dumps(results)
    except Exception, e:
        print('result 无法被 json 序列化, 请不要将不可序列化的对象填写至 result 中')
        print(e)
        return


    #如果执行成功，打印信息
    if bg_instance.result.status:
        print(u'[POC 编写者]')
        print(u'\t{poc_author}'.format(poc_author=str(bg_instance.info.get('author', ''))))
        print(u'[存在风险]')
        print('\t目标 {target} 存在 {poc_name}'.format(target = bg_instance.option.target.default,
                                                poc_name  = bg_instance.info.get('name', '').strip()
                                                ))
        print('\t{desc_target}: {default_target}\n\t{desc_port}: {default_port}\r\n'.format(
            
                                                 desc_target        =   bg_instance.option.target.desc,
                                                 default_target    =   bg_instance.option.target.default,
                                                 desc_port        =   bg_instance.option.port.desc,
                                                 default_port     =   bg_instance.option.port.default
                                                 ))
        print(u'[详细说明]')
        print('\t{poc_desc}'.format(poc_desc=bg_instance.info.get('desc', '').strip()))

        print(u'[程序返回]')
        print('\t{poc_return}'.format(poc_return=bg_instance.result.get('description', '').strip()))

        print(u'[危害等级]')
        print('\t{poc_severity}'.format(poc_severity=bg_instance.info.get('severity', '')))

        print(u'[漏洞类别]')
        print('\t{poc_type}'.format(poc_type=bg_instance.info.get('type', '')))

        print(u'[相关引用]')
        for each_ref in bg_instance.info.get('ref', {}):
            if not each_ref:
                return

            ref_key = each_ref.keys()[0]
            print('\t* {ref_key}: {ref_value}'.format(ref_key=ref_key, ref_value=each_ref.get(ref_key).strip()))
    
    else:
        bg_instance.print_error(bg_instance.result.error)

