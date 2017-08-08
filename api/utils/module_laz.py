
def index_modules(DIR):
    """ Return list"""

    modules = []
    for root, dirs, files in os.walk(DIR):
        _, package, root = root.rpartition('routersploit/modules/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))

    return modules
