import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '10.237.96.17'
host = '192.168.43.47'
port = 444

clientsocket.connect((host,port)) # connect to a remote socket. The argument varies depending on the address family

 message = clientsocket.recv(1024)
# socket.recv(bufsize): receive data from the socket. Returns bytes. 
# bufsize: max amount of data to be receive at once

clientsocket.close()

print(message.decode('ascii'))
