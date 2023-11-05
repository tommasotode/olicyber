import requests

x = requests.get("http://web-01.challs.olicyber.it/")

print(x.text)