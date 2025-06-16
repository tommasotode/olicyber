import requests

x = requests.get("http://web-02.challs.olicyber.it/server-records", params = {"id" : "flag"})

print(x.text)