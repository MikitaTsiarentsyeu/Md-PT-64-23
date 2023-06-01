from rounding import rouding
import requests
from bs4 import BeautifulSoup
from dots import presence_of_dots
from strings import string_of_numbers

def money_convector(usd, ratio):
    """A function that converts some amount of money from dollars to rubles."""
    byn = usd*ratio
    return byn

if __name__ == "__main__":
    u_s_d = input('Enter the dollar amount and currency ratio:\n')
    if presence_of_dots(u_s_d):
        string_u_s_d = string_of_numbers(u_s_d)
        r = requests.get('https://myfin.by/currency/minsk')
        soup = BeautifulSoup(r.content, 'html.parser')
        usd_ratio = soup.find('span', {'class': 'accent'}).text
        result =  money_convector(float(string_u_s_d), float(usd_ratio))
        x = int(input(('Enter the number of decimal places:\n')))
        if x < 1:
            print(int(result))
        else:
            print(rouding(result, x))
    else:
        print('Check your input')