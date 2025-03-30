import hashlib

with open("aa.txt", "r") as f:
    hashes = f.readlines()

for i in range(len(hashes)):
    hashes[i] = hashes[i].strip()

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}-!"

flag = ""
for i, target_hash in enumerate(hashes):
    found = False
    for c in charset:
        candidate = flag + c
        h = hashlib.sha256(candidate.encode()).hexdigest()
        
        if h == target_hash:
            flag += c
            print(f"Step {i+1}: Found char '{c}' → Partial flag: '{flag}'")
            found = True
            break
    
    if not found:
        print(f"Step {i+1}: Failed to find next character for hash {target_hash}")
        break

print("\nFinal Flag:", flag)