'''
socket 用于描述IP地址和端口，是一个通信链的句柄
'''
import socket
from time import ctime  


try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5) #backlog
except:
    print("init socket error!")
    
while True:
    print('listren for client...')
    conn,addr = sock.accept()
    print( 'get client',addr )
    conn.settimeout(5)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if '0' == data:
            conn.send(('[%s] %s server : exit'% ctime(), data).encode())
        else:
            conn.send(data.encode())
conn.close()
print('end of the service')


