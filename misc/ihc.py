#!/usr/bin/env python3

from pwn import *

HOST = "ihc.challs.olicyber.it"
PORT = 34008
r = remote(HOST, PORT)

print(r.recvuntil('premi invio!'))
r.sendline()

while True:
    req = r.recvline().decode()
    s = "Qual è il risultato di: 54 * 116?"
    



flag = r.recvline().decode()
print(flag)

r.close()
