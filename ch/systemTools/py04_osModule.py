'''

@author: sl
Created on 2014年7月13日
'''
import os
import subprocess
from sys import argv  # example client code
import sys


print(os.getcwd())
os.chdir(r"c:\users")
print(os.getcwd())
# Portability Constants  
# os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
print(os.pathsep, os.sep, os.pardir, os.curdir, os.linesep)
print(os.path.isdir(r'C:\Users'), os.path.isfile(r'C:\Users'))
print(os.path.exists(r'c:\Users\Brian'))
#print(os.path.getsize(r'C:\autoexec.bat'))
print(os.path.split(r'C:\temp\data.txt'))
os.path.join(r'C:\temp', 'output.txt')
name = r'C:\temp\data.txt' # Windows paths
os.path.dirname(name), os.path.basename(name)
t=os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw')
print(t) #('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyw')
os.path.normpath('C:\\temp\\public/files/index.html')
os.path.abspath('temp')

#Running Shell Commands from Scripts
'''
os.system
    Runs a shell command from a Python script
os.popen
    Runs a shell command and connects to its input or output streams
    
    the relatively new subprocess module provides finer-grained control over
streams of spawned shell commands and can be used as an alternative to,
    
'''
print(r'==========os.system("dir /B") 以下命令win7/8需要管理员权限CMD==========')
t=os.system('dir /B')
print(t)#0执行成功
t=os.popen('dir /B').readlines()
print(t)

#os.system('python helloshell.py') # run a Python program

#########The subprocess module alternative
'''
the subprocess module can achieve the same
effect as os.system and os.popen; it generally requires extra code but gives more control
over how streams are connected and used.
'''
#subprocess.call('python helloshell.py') # roughly like os.system()
#subprocess.call('cmd /C "type helloshell.py"') # built-in shell cmd

#Command-Line Arguments
sys.argv

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-': # find "-name value" pairs
            opts[argv[0]] = argv[1] # dict key is "-name" arg
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts

if __name__ == '__main__':
    from sys import argv # example client code
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)
#python testargv2.py -i data.txt -o results.txt
#{'-o': 'results.txt', '-i': 'data.txt'}


# programming_python_4th_edition P109






