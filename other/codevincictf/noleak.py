ciphertext_hex = "b3f0716f4a94ef6a6d6ce2b908d52d53c64696af67477dcade387770829324f23852fe78aff3266b5780"
ciphertext = bytes.fromhex(ciphertext_hex)

known_prefix = b"CodeVinciCTF{Fl4g_"
recovered_key = bytes(c ^ p for c, p in zip(ciphertext[:len(known_prefix)], known_prefix))

flag = bytes(c ^ k for c, k in zip(ciphertext, recovered_key * (len(ciphertext) // len(recovered_key) + 1)))
print(flag.decode())