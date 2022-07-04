# Modules
import time
import socket
import sys


# Index
print("""
 _     _       ___   _____         _____   _____   _____        _   _____  
| |   / /     /   | |  _  \       /  ___| | ____| |_   _|      | | |  _  \ 
| |  / /     / /| | | |_| |       | |     | |__     | |        | | | |_| | 
| | / /     / / | | |  _  /       | |  _  |  __|    | |        | | |  ___/ 
| |/ /     / /  | | | | \ \       | |_| | | |___    | |        | | | |     
|___/     /_/   |_| |_|  \_\      \_____/ |_____|   |_|        |_| |_|    v1.0
""")
print("=========================================================================")

# User Input
host_name = input("Enter The Website Address: ")
print("--------------------")

# Variable
try:
    ip = socket.gethostbyname(host_name)

# Output Function

    print("Website Is: " +host_name)
    print("====================")
    print("IP Address Is: " ,ip)
    time.sleep(10)

except socket.gaierror:
    print("Enter Valid Website Address...!")
    time.sleep(5)
    exit()
