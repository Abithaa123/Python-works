import socket
import sys
import time

s=socket.socket()
host=input(str("Please enter host name:"))
port=5005
try:
    s.connect((host,port))
    print("Connected to server")
except:
    print("Connection to server is failed:(")
while 1:
    incoming_msg=s.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Server:>>",incoming_msg)
    msg=input(str("You:>>"))
    msg=msg.encode()
    s.send(msg)
    
   
       