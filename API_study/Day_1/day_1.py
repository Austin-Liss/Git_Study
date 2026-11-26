import requests

r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
def get_data(pokemon) :
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    r.raise_for_status()
    return r.json()
# print(type(r))  
# print(r.status_code)
# print(r.headers['Content-Type'])

# print(r.text[:200]) # the first 200 characters from the RESPONSE 'r'
data = r.json() # r.json() takes the JSON text and converts it to Python objects. JSON objects become dicts, JSON arrays become lists, and from there it's ordinary Python. 
# print(type(data)) 
# print(data['id'])
# print(data['name'])
# print(data['types'])

# A. Deep navigation
    # A1 — Get all type names for a dual-type Pokémon
    # Do this: Request charizard and produce a list of its type names: ['fire', 'flying'].
def get_type(name) :
    data = get_data(name)
    return [t['type']['name'] for t in data['types']]
# print(get_type('pikachu'))

    # A2 — Pull the base stats into the shape you already know
    # Do this: Produce a dict like {'hp': 78, 'attack': 84, ...} for any Pokémon.
def get_stat(name) :
    data = get_data(name)
    return {t['stat']['name']:t['base_stat'] for t in data['stats']}
# print(get_stat('greninja'))

    # A3 — Count moves and find the hidden ability
    # Do this: Print how many moves the Pokémon can learn, the first five move names, and whether it has a hidden ability.
def get_moveset(name) :
    data = get_data(name)
    moves = [t['move']['name'] for t in data['moves']]
    hidden = next((a['ability']['name'] for a in data['abilities'] if a['is_hidden']),'None')
    return {'name':data['name'],
            'move_count':len(moves),
            'first_five': moves[:5],
            'hidden_abilities':hidden}
sample = get_moveset('bulbasaur')
print(sample)