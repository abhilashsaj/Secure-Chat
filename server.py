import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)


while True:
    data = conn.recv(1024)
    if not data: 
    	break

    print("B: "+data.decode('utf-8'))
    
    if data.decode('utf-8') == "bye":

    	break

    
    

    s_msg = input("A: ")
    conn.sendall(s_msg.encode('utf-8'))
    # if data == 'bye': 
    # 	break

	
conn.close()