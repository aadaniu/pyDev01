'''
pexpect 
    一个自动控制的 Python 模块,可以用来ssh、ftp、passwd、telnet 等命令行进行自动交互。
    官方网站是 http://www.noah.org
     wget http://pexpect.sourceforge.net/pexpect-2.3.tar.gz
      python ./setup.py install
               child = pexpect.spawn('ssh %s@%s' % (user,ip))
                child.expect ('password:')
                child.sendline (mypassword)
    https://pypi.python.org/pypi/pexpect/
Win PC 安装 winpexpect
参考：
    http://developer.51cto.com/art/201206/340118.htm
'''
import pexpect  
 
def ssh_cmd(ip, passwd, cmd):  
    ret = -1 
    ssh = pexpect.spawn('ssh root@%s "%s"' % (ip, cmd))  
    try:  
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)  
        if i == 0 :  
            ssh.sendline(passwd)  
        elif i == 1:  
            ssh.sendline('yes\n')  
            ssh.expect('password: ')  
            ssh.sendline(passwd)  
        ssh.sendline(cmd)  
        r = ssh.read()  
        print (r)
        ret = 0 
    except pexpect.EOF:  
        print ("EOF" )
        ssh.close()  
        ret = -1 
    except pexpect.TIMEOUT:  
        print ("TIMEOUT") 
        ssh.close()  
        ret = -2   
    return ret 