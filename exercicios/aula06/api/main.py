import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if response.status_code == 200:
    print(response.json()['name'])