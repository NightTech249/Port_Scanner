#!usr/bin/python

import socket

t_host = str(raw_input("Enter IP or Host name: "))
t_ip = socket.gethostbyname(t_host)

print t_ip

while 1:
	t_port = int(raw_input("Enter port: "))
	
	try:
		sock = socket.socket()			
		res = sock.connect((t_ip, t_port))
		print "Port {}: Open" .format(t_port)
		sock.close()
	except:
		print "Port {}: Closed" .format(t_port)
	
print "Port Scanning complete"