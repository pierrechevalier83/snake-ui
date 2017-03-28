#!/usr/bin/env python
import json
import socket

TCP_IP = '127.0.0.1'
#TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "42"
MESSAGE_JSON = json.dumps([{"Value": "42"}])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE_JSON)
s.close()
