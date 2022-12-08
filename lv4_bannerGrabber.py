import socket




def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    ip = "192.168.43.47"
    port = 22
    banner(ip, port)



if __name__ == '__main__':
	main()


