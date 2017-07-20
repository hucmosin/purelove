#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
说明：格式化输出字符串
"""

# python standard library


# local pret classes
    
def print_tables(headers, *args):
    """
    headers = []
    args = [] 可以为数组或者指针
    """

    if not all(map(lambda x: len(x) == len(headers), args)):
        print ("Headers and args should be the same length.")
        return

    def custom_len(x):
        try:
            return len(x)
        except TypeError:
            return 0

    fill = []
    headers_line = '    '
    headers_separator_line = '    '
    for idx, header in enumerate(headers):
        column = [custom_len(arg[idx]) for arg in args]
        column.append(len(header))

        current_line_fill = max(column) + 5
        fill.append(current_line_fill)
        headers_line = "".join((headers_line, "{header:<{fill}}".format(header=header, fill=current_line_fill)))
        headers_separator_line = "".join((
            headers_separator_line,
            '{:<{}}'.format('-' * len(header), current_line_fill)
        ))
        
   # print (headers_line)
    #print (headers_separator_line)
    #print
    
    for arg in args:
        content_line = '    '
        for idx, element in enumerate(arg):
            content_line = "".join((
                content_line,
                '{:<{}}'.format(element, fill[idx])
            ))
    return (headers_line,headers_separator_line,content_line)











