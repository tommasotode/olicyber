import requests

a = requests.post(
  "http://rpo.challs.olicyber.it/data",
  headers={"Content-Type": "application/x-www-form-urlencoded"},
  data={"p1s": "5", "p2s": "0", "time": "0"},
)

b = requests.get("http://rpo.challs.olicyber.it/verify")

print(a.content)

print(b.content)
