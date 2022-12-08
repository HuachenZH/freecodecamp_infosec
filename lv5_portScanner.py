import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "137.74.187.100" # hackthissite.org
port = 21

def portScanner(port):
	if s.connect_ex((host, int(port))):
		print("The port is closed")
	else:
		print("The port is open")

portScanner(port)