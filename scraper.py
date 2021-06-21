import requests
from bs4 import BeautifulSoup
from product import Product


def scrapShop(url):
    prodcuts = []
    print('Reaching url...')
    r = requests.get(url)
    print('Parsing document...')
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.findAll('div', {'class': 'thumbnail'})
    for div in divs:
        price = div.find('h4', {'class': 'pull-right price'}).text
        currency = price[0]
        price = float(price[1:])
        a = div.find('a', {'class': 'title'})
        title = a.text.replace('...', '')
        link = a['href']
        description = div.find(
            'p', {'class': 'description'}).text.replace('"', '')
        prodcuts.append(
            Product(title, price, currency, description=description, link=link))

    return prodcuts
