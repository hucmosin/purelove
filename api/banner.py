#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#导入model数量
import pl_print_world_color as color
from utils.payload_count import ret_num



payloads = ret_num()
#读取pl里的payload数量
def pl_get_banner():
    #打开缓存文件，取出文件个数
    #poc_count = pl_get_poc_count()
    desc = '''

       =[               purelove v1.1.0	                              ]
+ -- --=[                                                             ]
+ -- --=[                  by mosin                                   ]
+ -- --=[                 email: hucmoxing@163.com                    ]
+ -- --=[    Guthub Url: https://github.com/hucmosin/purelove         ]
+ -- --=[    Shellcode - (0) Different OS                             ]
+ -- --=[    Payload   - ({payload}) (Payloads and Exploits Module)   ]
'''.format(payload = color.set_yellow(payloads))
    print desc


