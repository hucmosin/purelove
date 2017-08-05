#!/usr/bin/env python2
# -*- coding: utf-8 -*-



# python standard library
import os, sys, argparse

# local pret classes
import pl_shell_cmd_const as const
import pl_os_operation as operation
import pl_file_ch as ch
import pl_poc_frame as execute
import pl_print_world_color as setcolor


def usage():
    usages = '''

Purelove Main Console Help
--------------------------

    ?           Show the main console help
    help        Show the main console help
    use	        Select an module by name
    exit        Exit the console
    show        Display module by name and path
    version	Show console version
    search      Find modules from directories
    shell       Windows cmd and Linux shell pl-shell > back = (EXIT) 
    cls/clear   Clean screan
    load        In Load Others Tools shell

'''
    print usages

def shell(PL_PWD):
    while True:
        ple = setcolor.UseStyle("ple",mode = 'underline')
        shell_input = raw_input(ple + " > ").strip().lower()
        switch_shell(PL_PWD, shell_input)

def read_cmd_line(PL_PWD,poc_re,PL_POC_FILE, poc_module_path_first_name, poc_module_path_end_name):
    execute.read_cmd_lines(PL_PWD,poc_re,PL_POC_FILE, poc_module_path_first_name, poc_module_path_end_name)

def switch_shell(PL_PWD, shell_input):
    if shell_input[:3] == const.PL_USE:
        PL_POC_FILE = shell_input[3:].strip()
        if PL_POC_FILE == "":
            return
        else:
            PL_STATUS = operation.pl_judge_file_name(PL_PWD, PL_POC_FILE)
            if PL_STATUS:
                poc_re = PL_POC_FILE
                poc_module_path_first_name  = ch.pl_path_split_first_name(PL_POC_FILE)
                poc_module_path_end_name    = ch.pl_path_split_end_name(PL_POC_FILE)
                PL_POC_FILE = ch.pl_return_path(PL_PWD,PL_POC_FILE)
                read_cmd_line(PL_PWD,poc_re,PL_POC_FILE, poc_module_path_first_name, poc_module_path_end_name)
            else:
                print setcolor.set_red("[!] ") + "没有找到此模块 => " + PL_POC_FILE
    else:
        if shell_input   == const.PL_SHOW:
            operation.pl_show_all_poc_info(PL_PWD)
        elif shell_input == const.PL_HELP or shell_input == "?":
            usage()
        elif shell_input[:6] == const.PL_SEARCH:
	    PL_POC_NAME = shell_input[6:].strip()
	    if PL_POC_NAME == "":
                return
            else:
                operation.print_poc_name_info(PL_PWD, PL_POC_NAME)
        elif shell_input == const.PL_EXIT:
            sys.exit()
        elif shell_input == const.PL_VERSION:
            ch.pl_show_version(PL_PWD)
        elif shell_input == (const.PL_LINUX_CLEAR) or shell_input == (const.PL_WINDOWS_CLS):
            os.system('cls')
        elif shell_input == const.PL_OS_SHELL:
            operation.pl_os_shell()
        elif shell_input == "load":
            load.exec_load(PL_PWD)
        else:
            #print u"ple => " + shell_input
            pass

