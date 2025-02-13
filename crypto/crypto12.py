import random


def discrete_log(p, a, b):
    value = 1
    for i in range(p):
        if value == a:
            return i
        value = (value * b) % p
    return None

print(discrete_log(101, 35, 2))


def private_key(p):
    return random.randint(1, p-2)

def public_key(p, g, private_key):
    return pow(g, private_key, p)

def shared_key(p, public_key, private_key):
    return pow(public_key, private_key, p)

p = 167
g = 2

your_private_key = private_key(p)
your_public_key = public_key(p, g, your_private_key)

my_private_key = private_key(p)
my_public_key = public_key(p, g, my_private_key)

shared_key = shared_key(p, your_public_key, my_private_key)

print(f"your public: {your_public_key}")
print(f"my public: {my_public_key}")
print(f"shared: {shared_key}")


