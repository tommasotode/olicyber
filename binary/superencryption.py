c = "6423522322238023102381231023652522102341238229023572002300237725721123462522002313213201235725725729023752902340233223302377280232023"

def lvl1(encoded):
    dec = []
    for ch in encoded:
        c = ord(ch)
        if c < 80:
            orig_code = c + 20
        elif c > 199:
            orig_code = c - 100
        
        dec.append(chr(orig_code))
    return "".join(dec)

def lvl2(encoded):
    dec = []
    i = 0
    while i < len(encoded):
        num_digits = int(encoded[i])
        i += 1
        ascii_str = encoded[i:i+num_digits]
        i += num_digits
        ascii_val = int(ascii_str)
        dec.append(chr(ascii_val))
    return "".join(dec)

l3 = c[::-1]
l2 = lvl2(l3)
l1 = lvl1(l2)

print(l1)