import socket
import json

# Define to server adress and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

# Listen for information
s.listen(1)
l = True
debug1= "No bugs hurray!"
while l is True:

#   Wait for somebody to connect
    conn, addr = s.accept()
#   Retrreive the data
    data = conn.recv(buffer_size)

#   Decode and print the data
    test = data.decode()
    print(test)
    l = False

print(debug1)
conn.close()
