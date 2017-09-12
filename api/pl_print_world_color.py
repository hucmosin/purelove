#! /usr/bin/env python
#coding=utf-8
#只对windows下的cmd命令行有效
import ctypes,sys
sys.path.insert(0, '../thirdparty')
import colorama

colorama.init()
'''
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
#字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
#由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中
 
# Windows CMD命令行 字体颜色定义 text colors , 平台支持，Linux下不兼容
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.
 
 
# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.
 
 
 
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
###############################################################
 
#暗蓝色
#dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#暗绿色
#dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()
 
#暗天蓝色
#dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#暗红色
#dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()
 
#暗粉红色
#dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()
 
#暗黄色
#dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()
 
#暗白色
#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()
 
#暗灰色
#dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()
 
#蓝色
#blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()
 
#绿色
#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
 
#天蓝色
#sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#红色
#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 
#粉红色
#pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()
 
#黄色
#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()
 
#白色
#white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()
 
##################################################
 
#白底黑字
#white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()
 
#白底黑字
#white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()
 
 
#黄底蓝字
#white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 
''' 
##############################################################


#===========================================================================
#Linux下使用,兼容不好，下次修改改进，以后再说。
"""
#----------------------------------------------------------------------------
#其他可以用颜色

#   格式：\033[显示方式;前景色;背景色m
#   说明:
#
#   前景色            背景色            颜色
#   ---------------------------------------
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
#
#   显示方式           意义
#   -------------------------
#      0           终端默认设置
#      1             高亮显示
#      4            使用下划线
#      5              闪烁
#      7             反白显示
#      8              不可见
#
#   例子：
#   \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
#   \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]
"""

STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
}


def UseStyle(string, mode = '', fore = '', back = ''):

    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''

    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''

    back  = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end   = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, string, end)


#test
def TestColor():

    print UseStyle('正常显示')
    print ''

    print "测试显示模式"
    print UseStyle('高亮',   mode = 'bold'),
    print UseStyle('下划线', mode = 'underline'),
    print UseStyle('闪烁',   mode = 'blink'),
    print UseStyle('反白',   mode = 'invert'),
    print UseStyle('不可见', mode = 'hide')
    print ''


    print "测试前景色"
    print UseStyle('黑色',   fore = 'black'),
    print UseStyle('红色',   fore = 'red'),
    print UseStyle('绿色',   fore = 'green'),
    print UseStyle('黄色',   fore = 'yellow'),
    print UseStyle('蓝色',   fore = 'blue'),
    print UseStyle('紫红色', fore = 'purple'),
    print UseStyle('青蓝色', fore = 'cyan'),
    print UseStyle('白色',   fore = 'white')
    print ''


    print "测试背景色"
    print UseStyle('黑色',   back = 'black'),
    print UseStyle('红色',   back = 'red'),
    print UseStyle('绿色',   back = 'green'),
    print UseStyle('黄色',   back = 'yellow'),
    print UseStyle('蓝色',   back = 'blue'),
    print UseStyle('紫红色', back = 'purple'),
    print UseStyle('青蓝色', back = 'cyan'),
    print UseStyle('白色',   back = 'white')
    print ''

#-----------------------------------------------------------------------------
#任何系统可以用
    
def set_yellow(strs):
    yell = ("{yellow_color}{strs}{color_reset}".format(
                    yellow_color = colorama.Fore.YELLOW, strs = strs, color_reset = colorama.Fore.RESET))
    return  yell

def set_red(strs):
    red = ("{red_color}{strs}{color_reset}".format(
                    red_color = colorama.Fore.RED, strs = strs, color_reset = colorama.Fore.RESET))
    return  red

def set_blue(strs):
    blue = ("{blue_color}{strs}{color_reset}".format(
                    blue_color = colorama.Fore.BLUE, strs = strs, color_reset = colorama.Fore.RESET))
    return  blue

def set_green(strs):
    green = ("{green_color}{strs}{color_reset}".format(
                    green_color = colorama.Fore.GREEN, strs = strs, color_reset = colorama.Fore.RESET))
    return  green

def set_white(strs):
    white = ("{white_color}{strs}{color_reset}".format(
                    white_color = colorama.Fore.WHITE, strs = strs, color_reset = colorama.Fore.RESET))
    return  white
def set_cyan(strs):
    cyan = ("{cyan_color}{strs}{color_reset}".format(
                   cyan_color = colorama.Fore.CYAN, strs = strs, color_reset = colorama.Fore.RESET))
    return  cyan


#s = "r[*]\aaaa[SAS]a" 
#print set_red(s)






    
