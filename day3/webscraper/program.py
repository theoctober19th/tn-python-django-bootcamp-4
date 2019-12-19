import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/list/ls055167700/')

soup = BeautifulSoup(page.content, 'html.parser')

h3s = soup.find_all('h3', {'class': 'lister-item-header'})

for h3 in h3s:
    name = h3.a.string
    print(name)