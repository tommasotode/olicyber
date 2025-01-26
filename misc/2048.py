#!/usr/bin/env python3

from pwn import *

def main():
    HOST = "2048.challs.olicyber.it"
    PORT = 10007
    r = remote(HOST, PORT)

    print(r.recvuntil(':'))

    for _ in range(2048):
        operation = r.recvuntil(" ").decode().strip()
        n1 = int(r.recvuntil(" ").decode().strip())
        n2 = int(r.recvuntil(" ").decode().strip())
        
        print(f"{operation} {n1} {n2}")

        res = 0
        if operation == "PRODOTTO":
            res = n1 * n2
        elif operation == "SOMMA":
            res = n1 + n2
        elif operation == "DIFFERENZA":
            res = n1 - n2
        elif operation == "DIVISIONE_INTERA":
            res = n1 // n2
        elif operation == "POTENZA":
            res = n1 ** n2
        
        r.sendline(str(res).encode())


    flag = r.recvline().decode()
    print(flag)
    
    r.close()

if __name__ == "__main__":
    main()