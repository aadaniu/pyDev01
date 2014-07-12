from socketserver import TCPServer as TCP, StreamRequestHandler as SRH  
from time import ctime  
  
  
HOST = '127.0.0.1'  
PORT = 8080  
ADDR = (HOST, PORT)  
  
class MyRequestHandler(SRH):  
    def handle(self):  
        print('...connected from:', self.client_address)  
        self.wfile.write(('[%s] %s' %(ctime(), self.rfile.readline().decode())).encode())  
  
tcpServ = TCP(ADDR, MyRequestHandler)  
print('waiting for connection...')  
tcpServ.serve_forever()  
