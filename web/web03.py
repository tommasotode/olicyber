import requests

x = requests.get("http://web-03.challs.olicyber.it/flag", headers = {"X-Password" : "admin"})

print(x.text)