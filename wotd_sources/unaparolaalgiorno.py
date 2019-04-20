import requests
from bs4 import BeautifulSoup


def get_unaparolaalgiorno_wotd():
    response = requests.get('https://unaparolaalgiorno.it/')
    soup = BeautifulSoup(response.text, 'html.parser')

    unaparolaalgiorno_word = soup.find(class_='parola').contents[1].text
    unaparolaalgiorno_desc = soup.find(class_='significato').text[4:]

    return unaparolaalgiorno_word, unaparolaalgiorno_desc
