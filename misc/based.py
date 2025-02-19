from pwn import *

HOST = "based.challs.olicyber.it"
PORT = 10600

r = remote(HOST, PORT)
r.recvlines(4)

try:
    while True:
        instruction = r.recvline().decode()
        data = r.recvline().decode().split(":")[-1].strip()[1:-2]

        if 'esadecimale' in instruction:
            if 'da' in instruction:
                res = bytes.fromhex(data).decode()
            elif 'a' in instruction:
                res = data.encode().hex()

        elif 'base64' in instruction:
            if 'da' in instruction:
                res = b64d(data).decode()
            elif 'a' in instruction:
                res = b64e(data.encode())

        elif 'binario' in instruction:
            if 'da' in instruction:
                n = int(data, 2)
                res = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

            elif 'a' in instruction:
                res = ''.join(format(ord(char), '08b') for char in data).lstrip('0')

        a = '{"answer": "'+res+'"}'
        print(a)
        
        r.recvline()
        r.sendline(a.encode())
        r.recvlines(3)
        
except Exception as e:
    r.interactive()