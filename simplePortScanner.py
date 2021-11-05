#!/usr/bin/env python3

'''
simplePortScanner.py
Author: Nik Alleyne
Author Blog: www.securitynik.com

Reference:
https://docs.python.org/3/howto/sockets.html
https://docs.python.org/3/library/socket.html?highlight=socket#socket.socket

'''

# import the functions needed for this task

import socket
import time

print('[*] Welcome to simplePortScanner.py! Let us scan some ports')

# Grab the target IP to scan
target_system = input('[+] Please enter the IP of the host you would like to scan: ')
print(f'[*] Preparing to scan host {target_system}')

# Setup the socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print the socket to see what is there
print(f'This is the socket: {my_socket}')

''' 
Making a single connection
Before running the script, consider launching tcpdump in a window on the host you are running this script on. Something similar to:

# tcpdump -nnt --interface any port 22

In my tcpdump, I'm targeting port 22. 
You can change the port above as well as in the tcp command to suit you.
'''

result = my_socket.connect_ex((target_system, 22))
if (result != 0):
	print('[!] Bummer! Looks like we run into a problem')
else:
	print('[*] Good stuff! Initial test connected Successfully! \n\n')
	
	
'''
	Building on what was done above, to scan multiple ports	
'''

start_port = int(input('[*] Enter the starting port number:'))
end_port = int(input('[*] Enter the ending port number:'))
print(f'[*] Preparing to scan host {target_system} on ports {start_port}-{end_port}')


# Setup the socket for scanning multiple ports
for port in range(start_port, end_port, 1):
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f'Scanning ... {target_system}:{ port}')
	result = my_socket.connect_ex((target_system, port))
	if (result == 0):
		print(f'Port {port} is OPEN')
	else:
		pass
	my_socket.close()
	time.sleep(1)
