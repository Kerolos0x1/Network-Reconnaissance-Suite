# Module
import requests



# Index
index = """
 _____   _   _   _____        _____   _____       ___   __   _  
/  ___/ | | | | |  _  \      /  ___/ /  ___|     /   | |  \ | | 
| |___  | | | | | |_| |      | |___  | |        / /| | |   \| | 
\___  \ | | | | |  _  {      \___  \ | |       / / | | | |\   | 
 ___| | | |_| | | |_| |       ___| | | |___   / /  | | | | \  | 
/_____/ \_____/ |_____/      /_____/ \_____| /_/   |_| |_|  \_| v1.0
"""
line = "=================================================================="
print(index)
print(line)

# Variables
domain = input("Domain : ")
file = open("subdomains.txt")
content = file.read()
subdomains = content.splitlines()
discovered_subdomains = []

# Function
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain:", url)
        discovered_subdomains.append(url)
