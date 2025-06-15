def pairStrings(id1, id2, length):
    serial = []
    even = 0
    odd = 0
    i = 0
    while even < length or odd < length:
        if i % 2 == 0:
            serial.append(id1[even])
            even += 1
        else:
            serial.append(id2[odd])
            odd += 1
        i += 1
    return ''.join(serial)

def make_serial(userid):
    part3 = pairStrings(userid[18:26], userid[9:17], 8)
    part1 = pairStrings(userid[0:8], userid[18:26], 8)
    part2 = pairStrings(userid[9:17], userid[0:8], 8)
    return part3 + part1 + part2

print(make_serial('D4WaynFg-jkl5380H-k4ghFa4I'))