
'''
#Создание покемона

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'dfa20871e0af16c1164efb018b843405'}

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
'''

'''
#Отправить в накаут

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'dfa20871e0af16c1164efb018b843405'}

body = {
    "pokemon_id": "189"
}

response = requests.post(url=f'{URL}/pokemons/knockout', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
'''

'''
# Смена имени покемона

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'dfa20871e0af16c1164efb018b843405'}

body = {
    "pokemon_id": "196",
    "name": "Bulls",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
'''

# Поймать покемона в покебол

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token': 'dfa20871e0af16c1164efb018b843405'}

body = {
    "pokemon_id": "196"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')