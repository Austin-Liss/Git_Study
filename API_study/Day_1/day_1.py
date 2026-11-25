import requests

r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

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
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    r.raise_for_status()
    data = r.json()
    return [t['type']['name'] for t in data['types']]
print(get_type('pikachu '))