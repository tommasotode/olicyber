import sympy
from Crypto.Cipher import AES
import binascii

p = 26111774174045932649
q = 20840856256353988787
e = 65537

n = p * q
phi_n = (p - 1) * (q - 1)

d = sympy.mod_inverse(e, phi_n)

print(f"n: {n}")
print(f"phi(n): {phi_n}")
print(f"d è: {d}")

def string_to_int(s):
    return int.from_bytes(s.encode(), 'big')

def int_to_string(i):
    return i.to_bytes((i.bit_length() + 7) // 8, 'big').decode()

k = pow(int('7a3e01bb030281dde1ca380fd64dc1e3', 16), d, n)
key = k.to_bytes((k.bit_length() + 7) // 8, 'big')

print(f"chiave: {binascii.hexlify(key).decode()}")

iv = binascii.unhexlify('9e4b6ee523efe7bf7a6c21a5b4039289')
c = binascii.unhexlify('496965f50062f82c0341fb75905c95d34128f582480bf675e31679e475e511e3')

aes = AES.new(key, AES.MODE_CBC, iv)
flag = aes.decrypt(c), AES.block_size

print(f"token: {flag}")
