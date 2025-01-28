import requests
from bs4 import BeautifulSoup

s = requests.Session()
for i in range(520):
    print(i)

    r = s.get("http://infinite.challs.olicyber.it/")    
    if 'flag' in r.text:
        print(r.text)
        break
    
    soup = BeautifulSoup(r.text, 'html.parser')
    test = soup.find('h2')
    
    if "MATH" in str(test):
        operation = str(soup.find('p')).split("+")
        n1 = int(operation[0].split(" ")[2].strip())
        n2 = int(operation[1].split("?")[0].strip())
        
        data = f'sum={n1+n2}'
        s.post("http://infinite.challs.olicyber.it/", data=data)

    elif "ART" in str(test):
        color = str(soup.find('p'))
        color = color.split(" ")[-1][:-5].strip()        
        
        data = f'{color}:""'
        s.post("http://infinite.challs.olicyber.it/", data=data)

    elif "GRAMMAR" in str(test):
        domanda = str(soup.find('p'))
        lettera = domanda.split(" ")[1][1:-1]
        parola = domanda.split(" ")[6][1:-6]

        c = 0
        for i in parola:
            if i == lettera:
                c += 1

        data = f'letter:"{c}"'
        s.post("http://infinite.challs.olicyber.it/", data=data)



pass