#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：参数展示模块
"""

# python standard library

from color import *

#===================================================================================#
def pl_run_poc_show(poc,poc_re):
    print
    print (bcolors.GREEN + "Module options " + '(' + poc_re + ') :')
    print
    print
    print "\t{Name:<20}{CurrentSetting:<35}{Required:<20}{Descriptions:<35}".format( Name            = "Name",
                                                                                     CurrentSetting = "Current Setting",
                                                                                     Required        = "Required",
                                                                                     Descriptions    = "Description")
    print "\t{Name:<20}{DisclosureDate:<35}{Rank:<20}{Descriptions:<35}".format(     Name            = "----",
                                                                                     DisclosureDate  = "---------------",
                                                                                     Rank            = "--------",
                                                                                     Descriptions    = "-----------")
    for option, option_filter in poc.options.items():
        print "\t{option:<20}{default:<35}{Required:<20}{Descriptions:<35}".format( option       = option,
                                                                                    default      = str(option_filter['default']),
                                                                                    Required     = str(option_filter['Required']),
                                                                                    Descriptions = str(option_filter['desc']))
    print 
#===================================================================================#
#Modify:2018-12-12
def pl_info_poc_show(poc,poc_re):
    print
    print (bcolors.GREEN + "Module Info " + '(' + poc_re + ') :')
    print
    print
    #print infomations
    for option, option_filter in poc.info.items():
        print "\tName:    {}".format(str(option_filter['Name']))
        print "\tAuthor:  {}".format(str(option_filter['Author']))
        print "\tType:    {}".format(str(option_filter['Type']))
        print "\tRef:     {}".format(str(option_filter['Ref']))
        print "\tVersion: {}".format(str(option_filter['Version']))
        print "\tDesc:    {}".format(str(option_filter['Desc']))

    print 

#===================================================================================#
def controlset(poc,choice):
        #导入shellcode中info文件
        pl_run_poc_show(poc,choice)
#===================================================================================#
def controlinfo(poc,choice):
        #show文件中的info信息
        pl_info_poc_show(poc,choice)
#===================================================================================#
