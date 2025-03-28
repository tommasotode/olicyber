from pwn import xor

a = b"\x95c\x7f\x9d3\xb2\xd9W<\xe34\xecpc0,\xb6\x9fDp\xa0\xbex\xf7\xb9\x00\x00"

k = bytes.fromhex("f30f1efa4883ec08488b05d92f00004885c07402ffd04883")



addr = 0x000055555555522e
base = addr-0x22e
print(hex(base))
print(len(k))

print(xor(a,k))