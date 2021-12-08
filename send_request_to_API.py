# !/usr/bin/python3
"""Use the requests module to send a GET"""

import json
import requests
url= "http://127.0.0.1:2224/list-json"
data = requests.get(url).json()
print(data)