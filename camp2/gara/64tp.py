from pwn import *

with open('m.txt', 'r') as f:
    c = f.readlines()

for i in c:
    print(b64d(i).hex()) #mtp