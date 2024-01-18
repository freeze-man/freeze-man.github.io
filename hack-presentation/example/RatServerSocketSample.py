#!/usr/bin/python
import socket
import os
import time

port = 25565

main_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_co.bind(('0.0.0.0', port))
main_co.listen(1)
while 1:
	try:
		os.system("clear")
		print('[*] Listening for upcoming connections...')

		client_co , info = main_co.accept()
		print('[+] New client found from ip ' + str(info[0]) + ' !')
		
		try:
			msg = b''
			while msg != 'end':
				try:
					msg = input(str(info[0]) + ' > ')
					if(msg == b''):
						pass
					else:
						msg = msg.encode()
						client_co.send(msg)
						recv = client_co.recv(1024*3)
						recv = recv.decode()
						print(recv)
				except BrokenPipeError:
					print('[-] Client disconnected...')
					break
		except KeyboardInterrupt:
			print('\n[-] Session Closed')
			msg = 'end'
			msg = msg.encode()
			client_co.send(msg)
			client_co.close()
			time.sleep(2)
	except KeyboardInterrupt:
		print('\n[-] Shutting down the server...')
		break