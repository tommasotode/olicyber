from base64 import b64decode

a = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
b = 664813035583918006462745898431981286737635929725
b = b.to_bytes(b.bit_length()//8 + 1, byteorder="big") 

print(f"{b64decode(a).decode()}{b.decode()}")