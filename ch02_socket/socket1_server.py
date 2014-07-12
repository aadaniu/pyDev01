'''
socket 用于描述IP地址和端口，是一个通信链的句柄
'''
import socket

if "__main__" == __name__:
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("create socket successcess!")
        
        sock.bind(('localhost',8008))
        print('bind socket success!')
        sock.listen(5) #backlog
        print('listen socket success!')      
    except:
        print("init socket error!")
        
    while True:
        print('listren for client...')
        conn,addr = sock.accept()
        print('get client')
        print(addr)
        conn.settimeout(5)
        szBuf = conn.recv(1024)
        byt = 'recv:' + szBuf.decode('gbk')
        print(byt)
        if '0' == szBuf:
            conn.send(b'exit')
        else:
            conn.send(b'welcome client!')
        conn.close()
        print('end of the service')