key1 = b"JIiEv3"
key2 = b"Kg9FRj"
key3 = b"xe8zh2"
map = [5, 1, 0, 2, 3, 4]

p1 = bytes([(c - 4) % 256 for c in key1])

p2 = bytes([c ^ 6 for c in key2])

p3 = bytearray(6)
for i in range(6):
    p3[map[i]] = key3[i]
p3 = bytes(p3)

key = p1 + b'-' + p2 + b'-' + p3

print(key.decode())