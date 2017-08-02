
import os

#获取目录cd -> path
cd_dir = receive(client_socket)
#判断目录是否存在
if os.path.exists(cd_dir):
    if os.path.isdir(cd_dir):
        os.chdir(cd_dir) #改变目录位置
        path_name = get_path()
        resp = "Directory change successful"
        client.send(client_socket, resp)
    else:
        err = "[!] {}: Is not a directory\n".format(cd_dir)
        client.send(client_socket, err)
else:
    err = "[!] {}: No such directory\n".format(cd_dir)
    client.send(client_socket,err)
