import requests

r = requests.get("http://web-06.challs.olicyber.it/token")
c = r.cookies.get_dict()

r = requests.get("http://web-06.challs.olicyber.it/flag", cookies=c)
print(r.text)