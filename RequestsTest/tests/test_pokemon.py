import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea65c46376bba3287c731efc0c35b831'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 33511


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})   
    assert response_get.json()["data"][0]['id'] == '33511'


