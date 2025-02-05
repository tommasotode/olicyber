m = 10 # message

p = 19
q = 7

n = p * q
print(f"n = {n}")

phi_n = (p - 1) * (q - 1)
print(f"phi(n) = {phi_n}")

# e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
e = 17
print(f"e = {e}")

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

# d such that (d * e) % phi(n) = 1
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

d = modinv(e, phi_n)
print(f"d = {d}")

c = pow(m, e, n)
print(f"c = {c}")

dec = pow(c, d, n)

print(f"{dec} == {m} : {dec == m}")