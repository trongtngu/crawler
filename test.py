import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

results = soup.find_all("p", {"class": "location"})

for loc in results:
    print(loc.text.strip())