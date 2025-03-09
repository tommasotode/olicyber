import os
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(filename):
    key = sha256(filename.encode()).digest()
    iv = b'\x00' * 16
    
    chunk_files = sorted(
        [f for f in os.listdir('chunks3') if f.startswith(f"{filename}_")],
            key=lambda x: int(x.split('_')[-1].split('.')[0])
        )
    
    decrypted_content = b''
    for chunk_file in chunk_files:
        with open(os.path.join('chunks3', chunk_file), 'rb') as f:
            ciphertext = f.read()
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        chunk = cipher.decrypt(ciphertext)
        decrypted_content += unpad(chunk, AES.block_size)
    
    with open(f"decrypted_{filename}", 'wb') as f:
        f.write(decrypted_content)
    
    print(f"File decrypted to decrypted_{filename}")


decrypt_file('immagine3.png')