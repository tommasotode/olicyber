import requests
from bs4 import BeautifulSoup
import re

s = requests.session()
url = "http://infinite.challs.olicyber.it/"
r = s.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for i in range(520):
    print(i)

    test = soup.find("h2")
    if "MATH" in str(test):
        operation = str(soup.find("p")).split("+")
        n1 = int(operation[0].split(" ")[2].strip())
        n2 = int(operation[1].split("?")[0].strip())

        data = {"sum": (n1 + n2)}
        res = s.post(url, data=data)
        if "WRONG" in res.text:
            break
        elif "flag" in res.text:
            break

    elif "ART" in str(test):
        color = str(soup.find("p"))
        color = color.split(" ")[-1][:-5].strip()

        data = color + "="
        res = s.post(url, data=data)
        if "WRONG" in res.text:
            break
        elif "flag" in res.text:
            break

    elif "GRAMMAR" in str(test):
        domanda = str(soup.find("p"))
        lettera = domanda.split(" ")[1][1:-1]
        parola = domanda.split(" ")[6][1:-6]

        c = len(re.findall(lettera, parola))

        data = {"letter": c}
        res = s.post(url, data=data)
        if "WRONG" in res.text:
            break
        elif "flag" in res.text:
            break

    soup = BeautifulSoup(res.text, "html.parser")
