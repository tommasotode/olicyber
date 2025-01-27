cifrato = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
print(cifrato, len(cifrato))

def xor(a, b):
  return bytes([x^y for x,y in zip(a,b)])

for i in range(256):
  chiave = bytes([i]*len(cifrato))
  decifrato = xor(cifrato, chiave)
  print(decifrato.decode(errors='ignore'))