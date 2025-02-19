def xor(a, b):
    return bytes([a[i]^b[i%len(b)] for i in range(len(a))])


messaggio = bytes.fromhex("502fee1138e7e3846f3aaf4334b3b38a7a28ab113cf5e7826a2fe24330f3f685682bee5329a0a1c73c27a24322e1fccb6c27af0d3eb4e08e712cbc0271e4f6997a2bba173eb8b3877d6eaf1625fbe1826634a7023cfbb38a3c3ebc0c32f1f78e6e2be0695bf2ff8a7b35a6530ef8a7b46e7ffb1361a1a4df3011a3570ee5e6df7011fd3c3da0cc8f2c23fa0d35a0ac9616440a")

original = bytes.fromhex("704e34bbff99f3fe")
cifrato = bytes.fromhex( "6c00fad8ae0d6015")

key = xor(cifrato, original)
print(xor(messaggio, key))