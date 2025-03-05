import string
from pwn import *

chall = ELF('software/mic/MIC')

encrypted_key = list(chall.read(chall.sym['encrypted_key'], 36).decode())

inp = (string.ascii_uppercase + string.digits)
print(inp)

outp = "BHJTV3467YZN1PE9XR820QOGFDCLKWIU5AMS" #rsi (gdb)

mapping = []
for el in outp:
    mapping.append(inp.index(el))

decrypted_key = ["_"] * 36
for i in range(len(encrypted_key)):
    decrypted_key[mapping[i]] = encrypted_key[i]

print(''.join(decrypted_key))