# Web Tool is Used For Help In Web Pentesting
# This Tool Made By Kerolos osama
# If Error Happend Please Text Me : w.technology22@gmail.com
# Version : v1.0
# Visit (url) For Get Latest Update
# Download Modules : pip3 install <module name>
# For Best Experiment Use It In Linux
#==========================================================================

# Modules
import time
import os

#==========================================================================

# Variables
index = """
 _          __  _____   _____  
| |        / / | ____| |  _  \ 
| |  __   / /  | |__   | |_| | 
| | /  | / /   |  __|  |  _  { 
| |/   |/ /    | |___  | |_| | 
|___/|___/     |_____| |_____/ v1.0
"""

line = "============================================"

#===========================================================================

# print
def fun1():
    os.system('clear')
    print(index)
    print(line)
    print("1.Emails Extractor")
    print("2.Subdomains Scanner")
    print("3.FTP Brute-Force")
    print("4.HTTP Sniffing")
    print("5.Get Website IP")
    print(line)

#============================================================================

# User Input
    user_input_1 = int(input("Choose : "))

#============================================================================

# Conditions

    if user_input_1 == 1:
        os.system('clear')
        os.system('python3 Email-Extractor.py')

    elif user_input_1 == 2:
        os.system('clear')
        os.system('python3 Subdomains-Scanner.py')
    
    elif user_input_1 == 3:
       os.system('clear')
       os.system('python3 FTP-Brute-Force.py')
    
    elif user_input_1 == 4:
        os.system('clear')
        os.system('sudo python3 HTTP-Sniff.py')
    
    elif user_input_1 == 5:
        os.system('clear')
        os.system('python3 Get-IP.py')
    
    else:
        print("Please Choose Correctly...!")
        time.sleep(2)
        os.system('clear')
        return fun1()
fun1()
