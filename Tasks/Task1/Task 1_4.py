import requests
from bs4 import BeautifulSoup

def usd_to_byn():
    usd = input('Enter the USD amount, please: \n')
    print('Loading...')
    r = requests.get('https://myfin.by/currency/minsk')
    soup = BeautifulSoup(r.content, 'html.parser')
    usd_ratio = soup.find('span', {'class': 'accent'}).text

    byn = float(usd_ratio) * float(usd)

    print(f'{usd}'" USD is " f'{byn}' ' BYN.')
    input('Press Enter to exit...')

try:
    usd_to_byn()
except:
    print('Error! The enter must be only digital.')
    input('Press Enter to exit...')

