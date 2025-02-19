import math

s = list(range(20))

c = '''s[19] * -0xfa + (int)s[19] * (int)s[19] == -0x3d09
s[18] * -0x60 + (int)s[18] * (int)s[18] == -0x900
s[17] * -0xbe + (int)s[17] * (int)s[17] == -0x2341
s[16] * -0xca + (int)s[16] * (int)s[16] == -0x27d9
s[15] * -0xe8 + (int)s[15] * (int)s[15] == -0x3490
s[14] * -0xdc + (int)s[14] * (int)s[14] == -0x2f44
s[13] * -0xc2 + (int)s[13] * (int)s[13] == -0x24c1
s[12] * -0xdc + (int)s[12] * (int)s[12] == -0x2f44
s[11] * -0xd2 + (int)s[11] * (int)s[11] == -0x2b11
s[10] * -0xda + (int)s[10] * (int)s[10] == -0x2e69
s[9] * -0xe4 + (int)s[9] * (int)s[9] == -0x32c4
s[8] * -0xca + (int)s[8] * (int)s[8] == -0x27d9
s[7] * -0xe8 + (int)s[7] * (int)s[7] == -0x3490
s[6] * -0x66 + (int)s[6] * (int)s[6] == -0xa29
s[5] * -200 + (int)s[5] * (int)s[5] == -10000
s[4] * -0xf6 + (int)s[4] * (int)s[4] == -0x3b19
s[3] * -0xce + (int)s[3] * (int)s[3] == -0x2971
s[2] * -0xc2 + (int)s[2] * (int)s[2] == -0x24c1
s[1] * -0xd8 + (int)s[1] * (int)s[1] == -0x2d90
s[0] * -0xcc + (int)s[0] * (int)s[0] == -0x28a4'''

lines = c.split("\n")
for i, l in enumerate(lines):
    b = int(l.split("*")[1].split("+")[0].strip(), 16)
    c = int(l.split("==")[-1].strip(), 16)

    s[-i-1] = int( (-b + math.sqrt((b*b)+(4*c)) ) / 2 )

for i in s:
    print(chr(i), end="")