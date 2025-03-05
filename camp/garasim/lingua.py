import requests

head = {'content-type':'application/gabibbo'}

a = requests.get("https://lingua.challs.olicyber.it/", headers=head)

print(a.text)