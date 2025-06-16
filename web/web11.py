import requests

sess = requests.session()
login = sess.post("http://web-11.challs.olicyber.it/login", json={'username':'admin', 'password':'admin'})
token = login.json().get('csrf')

flag = ""
for i in range(4):
    args = {
        'index' : i,
        'csrf' : token
    }

    r = sess.get(f"http://web-11.challs.olicyber.it/flag_piece", params=args)
    token = r.json().get('csrf')
    flag += r.json().get('flag_piece')

print(flag)