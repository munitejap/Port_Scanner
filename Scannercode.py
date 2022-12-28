#!/bin/python3

import sys
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
	target_ip =socket.gethostbyname(sys.argv[1])
else:
	print("ERROR")
	print("SYNTAX")

print("- "*50) #Adding a Starting Display
print("\n")
print(f"Scanning the IP =>{target_ip} ")
print(f"Started at => {str(dt.now())}")
print("\n")
print("- "*50)

try:
	for port in range(#starting_port,#ending_port):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # This will take the IP Address and TCP Stream
		socket.setdefaulttimeout(1) # Hit the port and wait for 1 sec and move on
		result=s.connect_ex((target_ip,port))#This will give the Boolean Output
		if result == 0:
			print(f"Port {port} is Opened")
		else:
			print(f"Port {port} is Closed")
		s.close
		        
    
except socket.gaierror: # Exception Handler if the Hostname cannot be identified
        print("Hostname Error")
        sys.exit()
except KeyboardInterrupt:# Exception Handler if there is a Keyboard Interrupt
 	print("Exiting the Program due to keyboard interrupt ")
 	sys.exit()
except socket.error: #Exception Handler if the server couldnt be reached or connected
	print("Couldnt connect to server")
	sys.exit()
