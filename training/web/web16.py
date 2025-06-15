import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def crawl(start_url):
    if start_url in visited:
        return None

    print(f"Visiting: {start_url}")
    visited.add(start_url)

    r = requests.get(start_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    titles = soup.find_all('h1')
    for h1 in titles:
        if 'flag' in h1.get_text().lower():
            print(f"flag: {h1.get_text()}")
            return True

    refs = soup.find_all('a', href=True)
    for ref in refs:
        next_url = urljoin(url, ref['href'])
        if next_url not in visited:
            if crawl(next_url):
                return True

    return False

url = "http://web-16.challs.olicyber.it/"
crawl(url)
