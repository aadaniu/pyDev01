'''

@author: sl
Created on 2014年7月13日
'''
N=2
#open('file').read() # read entire file into string
#open('file').read(N) # read next N bytes into string
#open('file').readlines() # read entire file into line strings list
#open('file').readline() # read next line, through '\n'
file =open('spam.txt', 'w') # create file spam.txt
file.write(('spam' * 5) + '\n') # write text: returns #characters written
file.close()

###########################################################
##################Using Programs in Two Ways################
#   the file to be used in either of two ways—as a script or as a library
'''
    every Python module has a built-in __name__ variable that Python sets to the
__main__ string only when the file is run as a program, not when it’s imported as a library.
    by coding program logic as functions rather than as top-level code, you can also
import and reuse it in other scripts.
    参考 more.py
'''
###########################################################
import sys
print(sys.platform, sys.maxsize, sys.version)
if sys.platform[:3] == 'win': print('hello windows')
################# The Module Search Path  #########################
print(sys.path)
# window路径：
#        "C:\\dir"
#或    r"C:\dir"

#################     The Loaded Modules Table    ################# 
print(sys.modules)
print("=========keys=====")
print(sys.modules.keys())
print("======sys.modules['sys']=======")
print(sys.modules['sys'])

#################    Exception Details    #################   
print("--------Exception Details 1------")
try:
        raise IndexError
except:
        print(sys.exc_info())
print("--------Exception Details 2------")     
import traceback
def grail(x):
    raise TypeError('already got one')

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
#The traceback module can also format messages as strings and route them to specific file objects;

print(sys.argv)
'''
os.environ    
        Shell variables
os.popen, os.execv, os.spawnv
        Running programs os.system, 
os.fork, os.pipe, os.waitpid, os.kill
        Spawning processes 
os.open, os.read, os.write
        Descriptor files, locks 
os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
        File processing 
 os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access
            Administrative tools
os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
        Portability tools 
os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')
        Pathname tools 
'''






