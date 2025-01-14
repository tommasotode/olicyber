import requests

form = {
  "username": "asdasdasdasd",
  "password": "asdasdasdasd",
  "invite": "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09",
}

r = requests.post("http://frittomisto.challs.olicyber.it/api/register", json=form)

print(r.text)