#!C:\PentestBox\base\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pystache==0.5.4','console_scripts','pystache'
__requires__ = 'pystache==0.5.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pystache==0.5.4', 'console_scripts', 'pystache')()
    )
