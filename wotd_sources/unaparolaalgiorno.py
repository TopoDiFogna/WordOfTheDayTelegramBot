import requests
import json


def get_unaparolaalgiorno_wotd():
    url = 'https://v3.unaparolaalgiorno.it/api/words/home'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    body = json.loads(response.text)

    unaparolaalgiorno_word = body['oggi']['parola']
    unaparolaalgiorno_desc = body['oggi']['significato']

    return unaparolaalgiorno_word, unaparolaalgiorno_desc
