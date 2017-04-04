#!/usr/bin/env python
import json
import socket

# Connect to server adress and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


# Message to send
message_json = json.dumps([{"Value":"42"}])
#message_json = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)


# Send data to the server
s.send(message_json.encode())

# Close socket after use
s.close()
