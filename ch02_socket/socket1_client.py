import socket
 
if "__main__" == __name__:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost',8008))
    sock.send(b'shaoling') #b 转换为字节发送
    
    szBuf = sock.recv(1024)
    byt = 'recv:' + szBuf.decode('gbk')
    print(byt)
    sock.close()
    print('end of the connecct')