#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close()                     # Close the socket when done

"""
# Following would start a server in background.
$ python server.py & 

# Once server is started run client as follows:
$ python client.py

This would produce following result −

Got connection from ('127.0.0.1', 12345)
Thank you for connecting
"""