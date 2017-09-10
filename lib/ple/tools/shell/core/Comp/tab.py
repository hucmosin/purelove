#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
说明：TAB
"""

# python standard library

import readline
#Just test it, readline works on windows too.Readline obsolete, so fck it.



class SimpleCompleter(object):
    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            if text:
                self.matches = [s 
                    for s in self.options
                    if s and s.startswith(text)
                ]
            else:
                self.matches = self.options[:]

        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


#Control 1 = Shellsploit
#Control 2 = control.py
def start( control=1):
    if control == 1:
        from .db import ret2
        readline.set_completer(SimpleCompleter(ret2()).complete)
        readline.parse_and_bind('tab: complete')
    else:
        from .db import ret
        readline.set_completer(SimpleCompleter(ret()).complete)
        readline.parse_and_bind('tab: complete')


