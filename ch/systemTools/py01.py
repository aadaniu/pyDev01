'''
Created on 2014年7月13日

主要模块：sys and os
#glob    For filename expansion
#socket For network connections and Inter-Process Communication (IPC)
#threading, _thread, queue
    For running and synchronizing concurrent threads
#time, timeit     For accessing system time details
#subprocess, multiprocessing
        For launching and controlling parallel processes
#signal, select, shutil, tempfile, and others
        For various other system-related tasks

Third-party extensions such as pySerial (a serial port interface), Pexpect (an Expect
work-alike for controlling cross-program dialogs), and even Twisted (a networking
framework) can be arguably lumped into the systems domain as well.

sys exports components related to the Python interpreter itself
os contains variables and functions that map to the operating system on which Python is run.





@author: sl
'''


import sys
d=''
print("====了解模块导出的Func======")
#d=dir(sys) 
print(d)
print("=====If   dir(sys)   not enough,=====")
#d=sys.__doc__
print(d)

#help
print(help(sys))







