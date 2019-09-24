import requests
from bs4 import BeautifulSoup


def get_unaparolaalgiorno_wotd():
    response = requests.get('https://unaparolaalgiorno.it/')
    soup = BeautifulSoup(response.text, 'html.parser')

    unaparolaalgiorno_word = soup.find('div', {'id': 'home-todays'}).contents[1].contents[0].text
    unaparolaalgiorno_desc = soup.find(class_='word-significato')

    return unaparolaalgiorno_word, unaparolaalgiorno_desc
