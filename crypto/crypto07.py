from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import ChaCha20


def get_des(k, plaintext):
    key = bytes.fromhex(k)
    plain = plaintext

    iv = bytes.fromhex("0000000000000000")
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plain = pad(plain.encode(), DES.block_size, style="x923")
    ciphertext = cipher.encrypt(padded_plain)

    print(ciphertext.hex(), end="\n")


def get_aes(k, plaintext):
    key = k.hex()
    print(key, end="\n")
    plain = plaintext

    iv = get_random_bytes(AES.block_size)
    print(iv.hex(), end="\n")
    cipher = AES.new(k, AES.MODE_CFB, iv, segment_size=24)
    padded_plain = pad(plain.encode(), AES.block_size, style="pkcs7")
    ciphertext = cipher.encrypt(padded_plain)

    print(ciphertext.hex())


def get_chacha20(k, nonce, cipher):
    key = bytes.fromhex(k)
    nonce = bytes.fromhex(nonce)
    ciphertext = bytes.fromhex(cipher)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    print(plaintext.decode("ascii"))

# get_des('1d25ad4de1d73850', 'La lunghezza di questa frase non è divisibile per 8')
# get_aes(get_random_bytes(32), 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.')
# get_chacha20('13355d5fcb93a7e123b97321fdbf897cf9af58cfa81b417788a676b171f5e567',
#  'a06f5b9c75cd51ac',
#  'd2a1024d2c1d94ae94d5bae283393987822ef65edd74290698292f38')