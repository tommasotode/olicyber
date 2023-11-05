import requests

i = 0

for i in range(7):
	r = requests.get(f"http://gabibbo_friend.challs.olicyber.it/get-picture?id={-i}")
	print(r.text)