import socket

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
c_msg = input("B: ")
s.sendall(c_msg.encode('utf-8'))
data = s.recv(1024)
s.close()
print('Received', repr(data))