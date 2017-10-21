from __future__ import absolute_import

from .autopwn import Exploit as BaseScanner


class Exploit(BaseScanner):
    """
    Scanner implementation for Beier vulnerabilities.
    """
    __info__ = {
        'name': 'Beier Scanner',
        'description': 'Scanner module for Beier devices',
        'authors': [
            'Mosin <hucmoxing@163.com>',  # routersploit module
        ],
        'references': (
            '',
        ),
        'devices': (
            'Beier',
        ),
    }
    modules = ['routers/beier', 'cameras/beier', 'misc/beier']
