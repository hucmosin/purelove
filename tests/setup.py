#coding=utf-8
 
from distutils.core import setup
import py2exe
 
options = { "py2exe":
                                 {  "compressed": 1, 
                                     "optimize": 2,
                                     "ascii":1,
                                     "bundle_files": 1
                                    }
}
 
setup(
              version = "1.0",
              description = "",
              name = "client",
              options = options,
              zipfile=None, 
              console=[ { "script": "hander_client.py", 
                               "icon_resources": [] } ]
)
