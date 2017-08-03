
import os

#获取目录cd -> path
cd_dir = ""
#判断目录是否存在
def cd_path(cd_dir):
    if os.path.exists(cd_dir):
        if os.path.isdir(cd_dir):
            os.chdir(cd_dir) #改变目录位置
            path_name = get_path()
            return parh_name
        else:
            err = "[!] {}: Is not a directory\n".format(cd_dir)
            return err
    else:
        err = "[!] {}: No such directory\n".format(cd_dir)
        return err
