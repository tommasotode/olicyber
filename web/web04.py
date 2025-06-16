import requests

x = requests.get("http://web-04.challs.olicyber.it/users", headers = {"Accept" : "application/xml"})

print(x.text)