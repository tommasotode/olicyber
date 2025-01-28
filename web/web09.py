import requests

data = {
    'username' : 'admin',
    'password' : 'admin'
}

r = requests.post("http://web-09.challs.olicyber.it/login", json=data)

print(r.text)