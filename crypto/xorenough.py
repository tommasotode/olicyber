# from pwn import xor

def xor(a, b):
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])

flag = bytes.fromhex("1e03132c3e681e300b7b30063301423c1a1c165f070c0d06015f07140e3748182d7a31064c031e36")
crib = bytes.fromhex(b"flag{".hex())

key = xor(crib, flag[:5])
key += b'Y'

plain = xor(flag, key)

print(plain)