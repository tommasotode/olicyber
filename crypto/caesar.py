alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(plaintext, key):
	ciphertext = ""
	for c in plaintext:
		ciphertext += alphabet[(alphabet.index(c) + key) % 26] 
	return ciphertext


for i in range(26):
	print(encrypt("QSGOFSIGOJOIBQWTFOFWCGWAWZS", i))