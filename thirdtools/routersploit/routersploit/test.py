import os
MODULES_DIR = r"E:\pure\PureLove-Win\bin\Purelove\thirdtools\routersploit\routersploit"
def index_modules(MODULES_DIR):
    """ Return list of all exploits modules """

    modules = []
    for root, dirs, files in os.walk(MODULES_DIR):
        _, package, root = root.rpartition('routersploit/modules/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))

    return modules


a =  index_modules(MODULES_DIR)

for i in a:
    print i
