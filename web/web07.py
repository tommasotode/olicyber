import requests

r = requests.head("http://web-07.challs.olicyber.it/")

print(r.headers)