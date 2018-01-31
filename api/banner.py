#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#导入model数量
import pl_print_world_color as color
from utils.payload_count import ret_num



payloads = ret_num()
def pl_get_banner():
    desc = '''

       =[               purelove v1.1.4.5                               ]
+ -- --=[                                                             ]
+ -- --=[    Guthub Url: https://github.com/hucmosin/purelove         ]
+ -- --=[    Shellcode - (1) Different OS                             ]
+ -- --=[    Payload   - ({payload}) (Payloads and Exploits Module)   ]
'''.format(payload = color.set_yellow(payloads))
    print desc


