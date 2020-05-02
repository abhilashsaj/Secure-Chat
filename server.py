import socket
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
print("Client A started...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

password = b"abhilash"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
print(key)
conn.sendall(key)

while True:
    data = f.decrypt(data).decode('utf-8')
    if not data: 
    	break

    print("B: "+ data)

    if f.decrypt(data).decode('utf-8') == "bye":
    	break
    	
    s_msg = input("A: ")
    token = f.encrypt(s_msg.encode('utf-8'))
    conn.sendall(token)
    # if data == 'bye': 
    # 	break

	
conn.close()