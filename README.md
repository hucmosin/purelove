# Purelove  v1.1.5.0

#### 目录：

- 框架介绍
- 使用介绍
- 待扩展或已完成功能
- 适用系统
- 未来

### 框架介绍：

> 守住心中的一点光，不灭；坚信心中的期盼，不错；执著最后的努力，不败；我望见青春时光的恬静透明印满了我来时的脚印。 愿我们对任何事情一直都有最开始的热爱 -->PureLove



**PureLove**是一款轻量级渗透测试框架。

安全研究人员可以根据自己的经验编写合适的漏洞利用脚本, 按照平台的开发标准编写出对应的安全检测插件模块, 安全研究人员之间可以分享漏洞分析, 代码开发的相关技术，来获得更好的技术提升。 
**PureLove** 目前只开源客户端版，客户端版为漏洞检测利用框架，利用程序以模块的形式展现，方便安全研究人员的对漏洞的利用分析。


### 使用介绍：

框架采用模块化编写，界面和命令行操作延续Linux风格。

主要目录介绍

> api 
>
> lib 
>
> module     
>
> thirdtools       
>
> modules  
>
> Purelove.py 
>
> Shellsploit.py 
>
> thirdparty

`api` 目录为框架代码存放目录，`lib`目录为`POC`和框架调用的类库，里面集成了一些库来减少`POC`和框架的代码量，`module`目录是存放`POC`的地方，分类存储各个`POC`  ,`thirdparty`目录存放了常用的第三方库供`POC`和框架使用，`modules`目录存放的是`POC`框架模块的支持文件，thirdtools目录存放了第三方工具，存放在里面的工具，可以由Purelove自行调用，Purelove.py为框架主程序，Shellsploit.py 为shellcode框架启动程序。

**Purelove**的使用和常规框架一样，采用命令行形式，对相关漏洞进行检测只需调用对应模块就好。下图是对web后门的监听返回


**purelove主框架命令：**

```
Purelove Main Console Help
--------------------------

    ?           Show the main console help
    help        Show the main console help
    use         Select an module by name
    exit        Exit the console
    show        Display module by name and path payload/exploit/handler/scanner
    version     Show console version
    search      Find modules from directories
    shell       Windows cmd and Linux shell pl-shell > back = (EXIT)
    cls/clear   Clean screan
    load        In Load Others Tools shell
    reload      Reload payloads
```

**模块利用命令：**

```
Module Main Console Help
-------------------------

    use                 Select an module by name
    info                Display module information
    set                 Set module parameters
    back                Back purelove frame
    show options        Show options settings information
    run                 Run Module
    exploit             Run Module
    unset               Unset options
```

**编写POC模版：**

`poc`的模块是在`TangScan`的基础上加强而来，所以对以前写过插件的朋友来说，应该能很快上手。

在1.1.4版本后，在`“payload”`检测模式下，参数需保持不变，在“exploit”攻击模式下，参数除“mode”不能修改外，其余的都可以修改。

```
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

#模块使用说明，docs里内容可自定义

docs = '''
#title                  :example
#description            :This is poc speak
#author                 :mosin
#date                   :20170609
#version                :0.1
#usage                  :python example
#notes                  :
#python_version         :2.7.5
'''
from modules.exploit import BGExploit

class PLScan(BGExploit):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.info = {
            "name": "",  # 该POC的名称
            "product": "",  # 该POC所针对的应用名称,
            "product_version": "",  # 应用的版本号
            "desc": '''

            ''',  # 该POC的描述
            "author": [""],  # 编写POC者
            "ref": [
                {self.ref.url: ""},  # 引用的url
                {self.ref.bugfrom: ""},  # 漏洞出处
            ],
            "type": self.type.rce,  # 漏洞类型
            "severity": self.severity.high,  # 漏洞等级
            "privileged": False,  # 是否需要登录
            "disclosure_date": "2017-05-17",  # 漏洞公开时间
            "create_date": "2017-06-17",  # POC 创建时间
        }

        #自定义显示参数
        self.register_option({
            "target": {
                "default": "",
                "convert": self.convert.str_field,
                "desc": "目标",
                "Required":"no"
            },
            "port": {
                "default": "",
                "convert": self.convert.int_field,
                "desc": "端口",
                "Required":"no"
            },
            "mode": {
                "default": "payload",
                "convert": self.convert.str_field,
                "desc": "执行exploit,或者执行payload",
                "Required":"no"
            },
            #以下内容可以自定义
            "example": {
                "default": "",
                "prints": "HELLO PURELOVE",
                "desc": "例如",
                "Required":"no"
            }
        })
        
        #自定义返回内容
        self.register_result({
            #检测标志位，成功返回置为True,失败返回False
            "status": False,
            "exp_status":False, #exploit，攻击标志位，成功返回置为True,失败返回False
            #定义返回的数据，用于打印获取到的信息
            "data": {
            },
            #程序返回信息
            "description": "this is test ",
            "error": ""
        })

    def payload(self):
        """
        检测类型
        :return:
        """
        pass

    def exploit(self):
        """
        攻击类型
        :return:
        """
        pass

#下面为单框架程序执行，可以省略
if __name__ == '__main__':
    from main import main
    main(PLScan())
```



其中详细介绍请移步WIKI(太懒，写的很糟糕)

**Wiki：**[https://github.com/hucmosin/purelove/wiki/PureLove%E6%A1%86%E6%9E%B6%E4%BB%8B%E7%BB%8D](https://github.com/hucmosin/purelove/wiki/PureLove%E6%A1%86%E6%9E%B6%E4%BB%8B%E7%BB%8D)

### 待扩展或已完成功能

- [x] 漏洞主体利用框架
- [x] Shellcode生成框架
- [x] 后渗透框架

框架后续附带

- [x] 资源数据库
- [ ] 新增漏洞利用模块
- [ ] 新增后渗透利用模块

**如果您有好的技术支持和思路或者工具插件，欢迎提交。**

### 适用系统

- [x] *UX
- [x] MAC
- [ ] Windows (因为编码原因，暂移除Windows支持框架，后期支持)



### 使用问题
目前作者正在开发Shellcode自动生成模块,后渗透利用功能已经移除,等待后续完善后更新。
**如您在框架使用过程中出现BUG，请及时向作者提交。欢迎邮件，issues，谢谢！**

### 未来：

框架目前还处在开发前期，相关漏洞利用模块还没有集成,框架功能还大量未完善，再加上个人原因，这个框架的编写也是断断续续的，可能自身的技术短板，框架不如人意，所以希望感兴趣或有能力的朋友能够和我一起完善这个项目。

**Purelove**在多次升级改版后，已经初步具备了渗透能力。

当然，如果您有对框架有好的建议，欢迎探讨！