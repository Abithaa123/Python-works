import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("Server will start on host:",host)
port=5005
s.bind((host,port))
print("Server is bind successfully")
s.listen(1)
conn,addr=s.accept()
print(addr,"has connected")
while 1:
    msg=input(str("You:>>"))
    msg=msg.encode()
    conn.send(msg)
    incoming_msg=conn.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Client:>>",incoming_msg)
