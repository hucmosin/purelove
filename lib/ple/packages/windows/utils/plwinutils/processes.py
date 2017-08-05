
from ctypes import byref, c_bool, windll, c_void_p, POINTER, WinError
import psutil
import platform
import subprocess
import os

INVALID_HANDLE_VALUE = c_void_p(-1).value
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
MAX_PATH=260

IsWow64Process=None
if hasattr(windll.kernel32,'IsWow64Process'):
    IsWow64Process=windll.kernel32.IsWow64Process
    IsWow64Process.restype = c_bool
    IsWow64Process.argtypes = [c_void_p, POINTER(c_bool)]

def is_process_64(pid):
    """ Take a pid. return True if process is 64 bits, and False otherwise. """
    is64=False
    if not "64" in platform.machine():
        return False
    hProcess = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, pid)
    if hProcess==INVALID_HANDLE_VALUE:
        raise WinError("can't OpenProcess for PROCESS_QUERY_INFORMATION. Insufficient privileges ?")
    is64=is_process_64_from_handle(hProcess)
    windll.kernel32.CloseHandle(hProcess)
    return is64

def is_process_64_from_handle(hProcess):
    """ Take a process handle. return True if process is 64 bits, and False otherwise. """
    iswow64 = c_bool(False)
    if IsWow64Process is None:
        return False
    if not IsWow64Process(hProcess, byref(iswow64)):
        raise WinError()
    return not iswow64.value
    
def enum_processes():
    proclist=[]
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['username', 'pid', 'name', 'exe', 'cmdline', 'status'])
            arch="?"
            try:
                arch=("x64" if is_process_64(int(pinfo['pid'])) else "x32")
            except WindowsError:
                pass
            pinfo['arch']=arch
            proclist.append(pinfo)
        except psutil.NoSuchProcess:
            pass
    return proclist

def start_hidden_process(path):
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW|subprocess.CREATE_NEW_PROCESS_GROUP
    info.wShowWindow = subprocess.SW_HIDE
    p=subprocess.Popen(path, startupinfo=info)
    return p
    
def is_x64_architecture():
    """ Return True if the architecture is x64 """
    if "64" in platform.machine():
        return True
    else:
        return False
        
def is_x86_architecture():
    """ Return True if the architecture is x86 """
    if "86" in platform.machine():
        return True
    else:
        return False

def get_current_pid():
    p = psutil.Process(os.getpid())
    dic = {'Name': p.name(), 'PID': os.getpid()}
    return dic

def get_current_ppid():
    dic = {'Parent Name': None, 'PPID': None}
    pp = psutil.Process(os.getpid()).parent()
    if pp != None:
        dic = {'Parent Name': pp.name(), 'PPID': pp.pid}
    return dic

def isUserAdmin():
    if windll.Shell32.IsUserAnAdmin():
        return True
    else:
        return False

if __name__ == '__main__':
    for dic in enum_processes():
        print dic
