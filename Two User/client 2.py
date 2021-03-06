import socket
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


print("Client B started...")
host = socket.gethostname()    
port = 12345                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

key = s.recv(1024)
f = Fernet(key)
print(key)

while(True):
	c_msg = input("B: ")
	token = f.encrypt(c_msg.encode('utf-8'))
	s.sendall(token)

	data = f.decrypt(s.recv(1024)).decode('utf-8')
	print("A: " + data )

	if data == "bye":
	    break
	    



s.close()
