import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ea65c46376bba3287c731efc0c35b831'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Дед Бом Бом",
    "photo_id": 1
}


body_rename = {
    "pokemon_id": "321637",
    "name": "Python",
    "photo_id": 1
}

body_add_pokeball = {
    "pokemon_id": "321637"
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)


response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)
message = response_rename.json()['message']
print(message)


response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
message = response_add_pokeball.json()['message']
print(message)







