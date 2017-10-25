import socket


def create_tcp_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print ('[-] Create socket error.')
        return 0
    return sock
