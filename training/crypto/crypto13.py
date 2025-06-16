from Crypto.Util import number
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

# while True:
#     q = number.getPrime(1024 - 1)
#     p = 2 * q + 1

#     if number.isPrime(p):
#         print(f"q (primo di Sophie Germain) [{q.bit_length()} bit]: {q}")
#         print(f"p (safe prime) [{p.bit_length()} bit]: {p}")
#         break

p = 104396974640085006879783557080583400368716479543908575488678452964468993626714586274340618315995031780098093334595530782379113729384150944028478182942773942590342368549465676231261362039384562608787880174010257758464559910838912965796863082975100041774814702789920372623906405851539701183202243705690757616023
q = (p - 1) // 2

g = 5

a = secrets.randbelow(q - 2) + 2
print(f"(a) chiave privata: {a}\n")

B = pow(g, a, p)
print(f"(B) chiave pubblica: {B}\n")

print(f"(p) safe prime: {p}\n")

print(f"(g) generatore: {g}\n")


# Alice
A_hex = "127f97c6bc16c3d9db84306bfc69c26167783b05f9a3215f158681c8d3524297132212247d75ffe05f135074e97e48b74492e6ac6255e00945d465215c12d0359cd848bae4295296f836f12aaddbf36809360f9c40338e0074260e84c4cbc597eaa2d301425c28bc3e5e75b151714658d8781ab6bf57b620f18ad6a719002104"
iv_hex = "43dd5e3faba204bdbded35e12d4dee36"
c_hex = "a7de8b5d6b35e789e9fdf1e797c4d4d8a76e005f218c247d7f9f9bed88527542cdf61b8ca6884700e45f9826141126d2efa0b9569dd6d046d7c275300a8dc634"

