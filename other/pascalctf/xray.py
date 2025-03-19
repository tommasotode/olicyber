from pwn import xor

a = b"*7^tVr4FZ#7S4RFNd2"

secret = b"xR\x08G$G\x07\x19kPhgCa5~"

print(xor(secret, a))