import requests
from bs4 import BeautifulSoup
import re
from decimal import Decimal as D

usd = input('Enter the USD amount, please: \n').replace(',','.')

if re.search(r'[a-zA-Zа-яА-я]',usd):
    print('Enter must contain only numbers, no letters.')
elif len(usd) == 0:
    print("Input can't be empty.")
elif re.search(r'[!@#$%:,"#?°]',usd):
    print("Don't use special characters!")
elif re.search(r'[ ]',usd):
    print("Don't use spaces!")
elif float(usd) <= 0:
    print('The entered value is too low. The value must be more then 0.')
else:
    print('Loading...')
    r = requests.get('https://myfin.by/currency/minsk')
    soup = BeautifulSoup(r.content, 'html.parser')
    usd_ratio = soup.find('span', {'class': 'accent'}).text

    byn = D(usd_ratio) * D(usd)
    print(f'{usd}'" USD is " f'{byn}' ' BYN.')
    input('Press Enter to exit...')


