import socket

print("Client B started...")
host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while(True):
	c_msg = input("B: ")
	s.sendall(c_msg.encode('utf-8'))

	data = s.recv(1024)
	print("A: " + data.decode('utf-8'))

	if data.decode('utf-8') == "bye":
	    break



s.close()
