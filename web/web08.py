import requests

data = {
    'username' : 'admin',
    'password' : 'admin'
}

r = requests.post("http://web-08.challs.olicyber.it/login", data=data)

print(r.text)