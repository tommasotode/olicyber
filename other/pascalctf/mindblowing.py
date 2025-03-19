from pwn import *

masks = [((1 << 40) - 1) << (i * 40) for i in range(20)]

conn = remote('mindblowing.challs.pascalctf.it', 420)

conn.sendlineafter(b'> ', b'1')
conn.sendlineafter(b'sentence: ', b'2')  # idx=2 (flag)
conn.sendlineafter(b'seeds: ', str(len(masks)).encode())

for mask in masks:
    conn.sendlineafter(b': ', str(mask).encode())

results = eval(conn.recvline().decode().split(': ')[1])
encoded_flag = sum(results)
flag = encoded_flag.to_bytes((encoded_flag.bit_length() + 7) // 8, 'big').decode()

print(f"Flag: {flag}")