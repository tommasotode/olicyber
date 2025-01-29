import zipfile

with open('zipception/rockyou.txt', 'r', encoding='latin-1') as file:
    psws = file.read()
    passwords = psws.splitlines()


for i in range(100):
    with zipfile.ZipFile(f"zipception/{100-i}.zip", 'r') as zip_ref:
        for password in passwords:
            try:
                zip_ref.extractall("zipception", pwd=password.encode('latin-1'))
                print(f"Password found: {password}")
                break
            except:
                continue