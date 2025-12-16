import socket
import sys
from datetime import datetime

# 1. Setup the Target
target = input("Enter the IP address to scan (e.g., 127.0.0.1): ")

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

try:
    # 2. Loop through common ports (1 to 1024)
    for port in range(1, 1025):  
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) # Don't wait too long for a response
        
        # result 0 means the port is OPEN
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nServer not responding.")
    sys.exit()

print("-" * 50)
input("Scan complete! Press Enter to exit...")