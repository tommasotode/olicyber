#!/usr/bin/env python3.8

import requests
import time
from datetime import datetime
import hmac
import hashlib
import random
import string

def get_random_string(length):
  letters = string.ascii_lowercase
  result_str = ''.join(random.choice(letters) for i in range(length))
  return result_str

def sign(text, key):
  textAsBytes = bytes(text, encoding='ascii')
  keyAsBytes  = bytes(key, encoding='ascii')
  signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256)
  return signature.hexdigest()

r = requests.get("http://trulyrandomsignature.challs.olicyber.it/")

t = r.headers['X-Uptime']
uptime = int( (time.time()-int(t)) ) - 1

seed = datetime.utcfromtimestamp(uptime).strftime('%Y-%m-%d %H:%M:%S')
print(f"uptime: {seed}")
random.seed(seed)
SUPER_SECRET_KEY = get_random_string(32)
print(f"SUPER_SECRET_KEY: {SUPER_SECRET_KEY}")

user = "admin"
cookies = {
  "user" : user,
  "signature" : sign(user, SUPER_SECRET_KEY)
}

r2 = requests.get("http://trulyrandomsignature.challs.olicyber.it/admin", cookies=cookies)

print(r2.text)