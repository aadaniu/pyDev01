import subprocess

'''
kill win7下 ES的进程
'''

name = "Elasticsearch"
li = []


def doCMD(cmd):
    print("will execute CMD :" + cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    return p.stdout.readlines()


def doCMDPrintResult(cmd):
    for line in doCMD(cmd):
        print(line.decode("gbk")) # win系统


for line in doCMD("jps -l"):
    line = line.decode("utf-8")
    if name in line:
        print(line)
        arr = line.split()
        li.append(arr[0])

for ele in li:
    print("will kill process :" + ele)
    # /T 指定进程和它的子进程
    # /F 强行终止进程
    doCMDPrintResult('taskkill /T /F /PID  '+ele)
