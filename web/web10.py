import requests

r = requests.options("http://web-10.challs.olicyber.it/")

print(r.headers)

rr = requests.patch("http://web-10.challs.olicyber.it/")

print(rr.headers)