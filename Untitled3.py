#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('13.124.80.47', 5001 ))
sock.send("hello".encode())

