import nmap
# seems not working, the scan does not give results.
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

if resp == "1":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sS")
    print(">>> scanner info: ", scanner.scaninfo())
    print(">>> ip status: ", scanner[ip_addr].state())
    print(">>> protocols: ", scanner[ip_addr].all_protocols())
    print(">>> open ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == "2":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sU")
    print(">>> scanner info: ", scanner.scaninfo())
    print(">>> ip status: ", scanner[ip_addr].state())
    print(">>> protocols: ", scanner[ip_addr].all_protocols())
    print(">>> open ports: ", scanner[ip_addr]['udp'].keys())
elif resp == "3":
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", "-v -sS -sV -sC -A -O")
    print(">>> scanner info: ", scanner.scaninfo())
    print(">>> ip status: ", scanner[ip_addr].state())
    print(">>> protocols: ", scanner[ip_addr].all_protocols())
    print(">>> open ports: ", scanner[ip_addr]['tcp'].keys())
