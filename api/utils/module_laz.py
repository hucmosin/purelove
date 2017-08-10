import os


def index_modules(DIR):
    """ Return list"""

    modules = []
    for root, dirs, files in os.walk(DIR):
        _, package, root = root.rpartition('datebase/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))

    return modules



def python_ize_path(path):
    """ Replace argument to valid python dotted notation.

    ex. foo/bar/baz -> foo.bar.baz
    """
    return path.replace('/', '.')


def human_ize_path(path):
    """ Replace python dotted path to directory-like one.

    ex. foo.bar.baz -> foo/bar/baz

    :param path: path to humanize
    :return: humanized path

    """
    return path.replace('.', '/')

#模块打印
def return_modules(PWD,modules):
    #当路径在时，转换，过滤
    #modules为index_modules得到模块名
    #PWD为相对路径，指向modules目录，不进入里面
    m = human_ize_path(modules)
    for r in m:
        #去除路径
        if PWD not in r:
            print r
        



