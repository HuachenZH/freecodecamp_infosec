import nmap

scanner = nmap.PortScanner()

ip_addr = input('[*] Enter the ipv4 address you want to scan: ')
print('>>> You entered: %s' % str(ip_addr))
print("\n")

resp = input("""[*] Enter the type of scan you want to run: 
        1: SYN ACK Scan
        2: UDP Scan
        3: Comprehensive Scan
        Enter 1 or 2 or 3: """)
print(">>> You have selected option: %s" % str(resp))
