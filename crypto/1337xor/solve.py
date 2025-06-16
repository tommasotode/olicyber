def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

with open("crypto/1337xor/output.txt", "r") as f:
    c = f.read()

c = c.split("FLAG:")[-1].strip()
c = bytes.fromhex(c)
print(len(c))

start = b"flag{"
keystart = xor(start, c[:5])

for i in range((2**8)):
    keystart = keystart + bytes([i])
    print(xor(c, keystart * (len(c)//len(keystart) + 1)))
    keystart = keystart[:-1]