from pwn import xor

flagfinale = b"\xaa\xa7\x7d\x74\x69\x81\x92\x62\xb8\x07\xcf\xa8\x9c\x07\x11\x63\x17\x77\x56\xd8\x79\xf1\x21\xac\x14\x82\x2a\x96\xaa\x73\x59\x9c\x29\xda\x92\x9b\xd0\x70\x73\xfc\xc3\x3f\x78\x40\xc6\x33\xfe\xef\x95\xde\xe4\xc7"
key = b"\x9a\xf8\x1f\x2b\x1b\xe0\xab\x1f\xc3\x62\xfe\xda\xa8\x3f\x70\x3c\x75\x19\x30\xa0\x48\xc1\x54\xca\x75\xe6\x75\xa6\xde\x16\x6e\xef\x18\xed\xe6\xfc\xe4\x11\x06\xa3\xaf\x5e\x1d\x24\xf6\x5d\xca\x8e\xa3\xea\x96\xa5"
unxored = xor(flagfinale, key)

perm = [
    0xD,
    0x19,
    0x1F,
    10,
    0xB,
    0xF,
    0x2C,
    0x33,
    4,
    0x2E,
    0x13,
    0x1C,
    0x16,
    0x32,
    9,
    0x1E,
    0x12,
    0x14,
    0,
    0x1A,
    0x2D,
    0x2A,
    6,
    0x30,
    2,
    0x27,
    0x10,
    7,
    8,
    0x18,
    0x22,
    0x11,
    0x25,
    0x24,
    0xE,
    3,
    0x29,
    0x21,
    0xC,
    0x17,
    1,
    0x28,
    0x23,
    0x31,
    0x1B,
    0x15,
    0x1D,
    0x2B,
    0x20,
    0x2F,
    5,
    0x26,
]

final = [b""] * 52
for i in range(len(unxored)):
    final[perm[i]] = chr(unxored[i])

print("".join(final))