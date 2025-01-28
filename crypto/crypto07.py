from Crypto.Cipher import DES

key = bytes.fromhex('b1cba8c7f3b744c6')
cipher = DES.new(key, DES.MODE_CBC)
print(cipher.encrypt(bytes('La lunghezza di questa frase non è divisibile per 8    ', 'utf-8')).hex(), end="\n\n")
print(cipher.IV.hex())