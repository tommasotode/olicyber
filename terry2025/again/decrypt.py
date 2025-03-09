from pwn import xor
import string

with open("terry2025/again/again_output.txt", "r") as f:
    ciphertext_hex = f.read().strip()

ciphertext = bytes.fromhex(ciphertext_hex)

SBOX = [23, 46, 93, 178, 209, 80, 169, 227, 246, 14, 79, 139, 196, 109, 176, 76, 188, 74, 163, 187, 130, 110, 101, 241, 202, 239, 53, 117, 114, 72, 131, 217, 71, 55, 253, 45, 212, 191, 59, 30, 104, 190, 251, 20, 94, 211, 84, 85, 68, 73, 237, 205, 174, 97, 197, 199, 36, 180, 100, 215, 107, 62, 89, 81, 111, 119, 32, 156, 214, 88, 183, 238, 18, 125, 231, 92, 127, 219, 138, 193, 141, 103, 37, 236, 157, 41, 158, 135, 120, 9, 250, 172, 106, 136, 2, 123, 247, 248, 26, 52, 54, 57, 204, 232, 7, 15, 140, 66, 245, 170, 144, 22, 203, 1, 56, 167, 34, 244, 137, 19, 225, 143, 6, 184, 10, 60, 151, 165, 91, 40, 133, 70, 128, 121, 220, 16, 152, 13, 58, 185, 254, 154, 198, 113, 160, 132, 206, 50, 122, 116, 192, 179, 153, 47, 95, 200, 112, 145, 5, 126, 105, 243, 164, 181, 146, 161, 129, 3, 48, 182, 189, 33, 148, 162, 69, 43, 234, 35, 39, 63, 150, 142, 61, 90, 64, 78, 42, 83, 21, 155, 168, 229, 96, 173, 208, 207, 221, 82, 242, 240, 27, 4, 186, 115, 17, 51, 159, 175, 75, 201, 44, 29, 218, 216, 108, 8, 99, 28, 102, 118, 24, 230, 195, 86, 226, 166, 11, 0, 171, 65, 228, 38, 223, 31, 67, 77, 49, 194, 124, 249, 222, 177, 252, 98, 235, 12, 210, 134, 233, 87, 255, 147, 149, 213, 25, 224]

REVERSE_SBOX = [0] * 256
for i, val in enumerate(SBOX):
    REVERSE_SBOX[val] = i

printable_chars = set(string.printable.encode())
def is_printable(bstring):
    for b in bstring:
        if b not in printable_chars and b != ord('|'):
            return False
    return True

def try_key_length(key_length):
    print(f"key length: {key_length}")

    key = b''
    for key_pos in range(key_length):
        for key_byte in range(256):
            valid = True
            for i in range(key_pos, len(ciphertext), key_length):
                xored = ciphertext[i] ^ key_byte
                plain = REVERSE_SBOX[xored]
                if not (is_printable(bytes([plain]))):
                    valid = False
                    break

            if valid:
                key += bytes([key_byte])
                break
        
    return key

def decrypt_and_check(key):
    repeated_key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decrypted_sboxed = xor(ciphertext, repeated_key)
    decrypted = bytes([REVERSE_SBOX[b] for b in decrypted_sboxed])

    try:
        decoded = decrypted.decode('ascii', errors='replace')
        if is_printable(decrypted):
            if '|' in decoded:
                text, flag = decoded.split('|', 1)
                return True, key, text, flag    
    except Exception as e:
        pass
        
    return False, None, None, None

for key_length in range(6, 13):
    key = try_key_length(key_length)
    if len(key) == 0:
        print(f"no valid key for length {key_length}")
        continue

    success, found_key, text, flag = decrypt_and_check(key)
    if success:
        print("key found")
        print(f"flag({flag})")