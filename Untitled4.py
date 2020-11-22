#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind('13.124.80.47', 5001)

server.listen(0)

client, addr = server.accept()
data = client.recv(65535)

print("recieve Data : ", data.decode())

