#!/usr/bin/env python3

from pwn import *

exe = ELF("software/sw-19")
b = process(exe.path)

def solve(s):
    return hex(exe.sym[s])

HOST = "software-19.challs.olicyber.it"
PORT = 13002
r = remote(HOST, PORT)

print(r.recvuntil("iniziare ..."))
r.send("a".encode())

for _ in range(20):
    f = r.recvuntil(":").decode()
    f = f.split("->")[1].strip()[:-1]
    print(f)

    r.sendline(solve(f).encode())

flag = r.recvline().decode()
print(flag)

r.close()
