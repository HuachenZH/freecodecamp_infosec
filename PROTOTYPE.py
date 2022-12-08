import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# create a socket using the address family and type
    # address family:
        # AF_INET (default)
        # AF_INET6
        # AF_UNIX
        # AF_CAN
        # AF_PACKET
        # AF_RDS
    # type:
        # SOCK_STREAM (default)
        # SOCK_DGRAM
        # SOCK_RAW
host = socket.gethostbyname()
port = 444

serversocket.bind(host, port)
# .bind(addressss), bind addressss to the socket. 
# The format of adressss depends on the address family when initializing socket
# the socket must not already be bound

serversocket.listen(3) # in parameter, specify how many connections we can listen to at a time

for i in range(10):
    clientsocket, address = serversocket.accept()
    # socket.accept(): Accept a connection. The socket must be bound and listening. 
    # return value is a pair (conn, address)
        # conn: new socket object, usable to send and receive data on the connection.
        # address: the address bound to the socket on the other end of connection.
    print("Receive data from %s" % str(address))
    message = "Thx for connecting\n"
    clientsocket.send(message) # the argument should be bytes
    clientsocket.close()


