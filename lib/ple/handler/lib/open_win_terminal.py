# -*- coding: utf-8 -*-
#开启3389

import os_exec

REG = r'"REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" Server /v fDenyTSConnections /t REG_DWORD /d 0 /f'
#REG = "whoami"
os_exec.os_exec(REG)

