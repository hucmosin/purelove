from __future__ import absolute_import

from .autopwn import Exploit as BaseScanner


class Exploit(BaseScanner):
    """
    Scanner implementation for Fenghuo vulnerabilities.
    """
    __info__ = {
        'name': 'Beier Scanner',
        'description': 'Scanner module for Fenghuo devices',
        'authors': [
            'Mosin <hucmoxing@163.com>',  # routersploit module
        ],
        'references': (
            '',
        ),
        'devices': (
            'Fenghuo',
        ),
    }
    modules = ['routers/fenghuo', 'cameras/fenghuo', 'misc/fenghuo']
