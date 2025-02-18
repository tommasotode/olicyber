def xor(a, b):
    return bytes([a[i]^b[i%len(b)] for i in range(len(a))])

a = bytes.fromhex("002a00104503423c07377f091f12384e67390d03461903331b203030101b3a30333e110b530d3d36030d380e111a3d0d2800150b7e120d2d1b33001a1d2c3c0a352b08044801032b002f")
key = b"G_ab!bb_oR_oss_o"

print(xor(a, key))