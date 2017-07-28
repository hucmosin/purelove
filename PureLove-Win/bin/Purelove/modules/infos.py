#!/usr/bin/env python
# coding=utf-8

def bginfos(bg_instance):
    for option, option_filter in bg_instance.option.items():
        if not hasattr(option_filter, 'default'):
            option_filter['default'] = ''
        if not hasattr(option_filter, 'desc'):
            option_filter['desc'] = ''
        if option_filter['default']:
            option_filter['default'] = option_filter['convert'](option_filter['default']) #转换option的类型
