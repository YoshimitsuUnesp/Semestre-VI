# https://pokemondb.net/pokedex/all

import requests
from bs4 import BeautifulSoup

response = response.get('https://pokemondb.net/pokedex/all')
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

with open('pagina.html', 'w', encoding="utf-8") as file:
    file.write(response.text)
    file.close()

# soup = BeautifulSoup(response.content, 'html.parser')

# pokemon_table = soup.find('table', id='pokedex')

# pokemon_rows = pokemon_table.tbody.find_all('tr')

# pokemons: list[dict] = []

# for row in pokemon_rows:
#     columns = row.find_all('td')

#     name = columns[1].text.strip()
#     tipo = columns[2].text.strip()

#     pokemon_dict = {
#         "nome": name,
#         "tipo": tipo
#     }

#     pokemons.append(pokemon_dict)
