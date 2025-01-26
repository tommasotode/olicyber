#!/usr/bin/env python3

from math import gcd
from pwn import *

def solve(N):
    if N <= 2:
        return None
    return (N - 1, 1)


def main():
    HOST = "nt-master.challs.olicyber.it"
    PORT = 11001
    r = remote(HOST, PORT)

    print(r.recvuntil('tests.'))

    for _ in range(10):
        print(r.recvuntil("= ").decode().strip(), end=" ")
        n = int(r.recvline().decode().strip())
        print(n)
        
        res = "{} {}".format(*solve(n))
        r.sendline(res.encode())


    r.recvline().decode()
    flag = r.recvline().decode()
    print(flag)
    
    r.close()

if __name__ == "__main__":
    main()