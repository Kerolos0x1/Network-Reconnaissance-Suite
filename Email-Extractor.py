# Module
import re
import os
try:
    from requests_html import HTMLSession
except ModuleNotFoundError:
    os.system('pip3 install requests-html')
import time
from websockets import client

# Index
index = """
 _____       ___  ___       ___   _   _       _____  
| ____|     /   |/   |     /   | | | | |     /  ___/ 
| |__      / /|   /| |    / /| | | | | |     | |___  
|  __|    / / |__/ | |   / / | | | | | |     \___  \ 
| |___   / /       | |  / /  | | | | | |___   ___| | 
|_____| /_/        |_| /_/   |_| |_| |_____| /_____/ v1.0
"""
line = "=================================================================="
print(index)
print(line)

# User Input
url = input("URL : ")

# Variables
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
session = HTMLSession()
r = session.get(url)
r.html.render()

# Function
for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(re_match.group())
