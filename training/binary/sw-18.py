#!/usr/bin/env python3

from pwn import *

def main():
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)

    print(r.recv(1024).decode())  
    r.sendline("a".encode())

    for _ in range(100):
        msg = r.recvline().decode()
        print(msg)

        num = msg.split("0x")[1].split(" ")[0]        
        if "32-bit" in msg:
            r.send(p32(int(num, 16)))
        elif "64-bit" in msg:
            r.send(p64(int(num,16)))

        r.recvline()

    flag = r.recvline().decode()
    print(flag)
    
    r.close()

if __name__ == "__main__":
    main()