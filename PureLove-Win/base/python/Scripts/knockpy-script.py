#!C:\PentestBox\base\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'knockpy==3.0','console_scripts','knockpy'
__requires__ = 'knockpy==3.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('knockpy==3.0', 'console_scripts', 'knockpy')()
    )
