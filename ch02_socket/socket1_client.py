import socket
from time import ctime  
if "__main__" == __name__:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost',8080))
    sendStr=" shaoling2"
    sock.send(sendStr.encode())
    recv = sock.recv(1024).decode()
    print(recv)
    sock.close()
    print(ctime()+ ' client :end of the connecct')