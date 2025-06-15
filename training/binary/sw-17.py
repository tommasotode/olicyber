#!/usr/bin/env python3

from pwn import *

def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    t = r.recv(1024)
    print(t.decode())  
    r.sendline("a".encode())

    for _ in range(10):
        step = r.recvline().decode()
        print(step)

        numbers = r.recvline().decode()
        numbers = numbers.strip('[]\n').split(', ')

        _ = r.recvline().decode()

        s = sum([int(x) for x in numbers])
        r.sendline(str(s).encode())
        
    flag = r.recvline().decode()
    print(flag)
    
    r.close()

if __name__ == "__main__":
    main()