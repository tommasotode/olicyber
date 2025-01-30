def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


a = 61
b = 150
gcd, x, y = extended_gcd(a, b)

print(f"x = {x}, y = {y}")


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    return None if gcd != 1 else (x % m)


inverse = mod_inverse(a, b)
if inverse is not None:
    print(f"mod inverse of {a} modulo {b} is {inverse}")

a = 64
m = 75
inverse = mod_inverse(a, m)
if inverse is not None:
    print(f"mod inverse of {a} modulo {m} is {inverse}")
