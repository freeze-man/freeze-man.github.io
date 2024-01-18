#!usr/bin/python

import socket

t_host = str(raw_input("Enter the host to be scanned: "))   # Target Host, www.example.com
t_ip = socket.gethostbyname(t_host)     # Resolve t_host to IPv4 address

print(t_ip)      # Print the IP address


def port_scanner(ip_user_input):

	while True:
		t_port = int(raw_input("Enter the port: "))	   # Enter the port to be scanned
		try:
			sock = socket.socket()
			sock.connect((t_ip, t_port))
			response = sock.recv(1024)
			print("Port {}: Open" .format(t_port))
			print("")
			print("Info for port ", PORT)
			print(response)
			sock.close()
		except KeyboardInterrupt:
			print("Port Scanning complete")
		except:
			print("Port {}: Closed" .format(t_port))


def port_test(ip_user_input):
	s = socket.socket()
	ip_address = ip_user_input
	ports = [20, 21, 22, 23, 25, 53, 79, 88, 389, 515]
	for PORT in ports:
		print("Testing IP: ",ip_address, PORT)
		try:
			s.connect((ip_address,PORT))
			response = s.recv(1024)
			print("")
			print("Info for port ",PORT)
			print(response)
			print("")
			s.close()
		except:
			print("error connecting to port ", PORT)

# port_test(t_host)
