import requests
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
import base64


url = "http://localhost:1337/test.php" 

def xor(a, b):
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])

def pad(s):
    padding = AES.block_size - len(s) % AES.block_size
    return s + bytes([padding] * padding)

def unpad(s):
    return s[:-s[-1]]

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext))

def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext))


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

key = b'aaaaaaaaaaaaaaaa'
iv = b'bbbbbbbbbbbbbbbb'

plaintext = cookie[32:]

decrypted = decrypt(base64.b64decode(plaintext), key, iv)
print(f'Decrypted: {decrypted.decode()}')

