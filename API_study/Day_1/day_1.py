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

# E1: Request three different Pokémon. Print name, height, weight, and the first type for each.
# E2: Print r.status_code for each — confirm all 200.
# E3: Request a deliberately wrong name. Print the status code and r.ok. Don't let it crash — just observe.
# E4: Request https://api.github.com/users/Austin-Liss (your own GitHub). Print r.status_code and the keys of the response. Notice it's a completely different API with the same interface.
# E5: On that GitHub response, find public_repos and created_at.
# E6: Print r.elapsed on any request — how long it took. Useful later when you're making hundreds.

# E1
r1 = requests.get("https://pokeapi.co/api/v2/pokemon/greninja")
d1 = r1.json()
print(d1['name'])
print(f"{d1['name']}'s height: {d1['height']} inches. Weight: {d1['weight']}lbs")
print(f"{d1['name']}'s 1st type is : {d1['types'][0]['type']['name']}")

r2 = requests.get("https://pokeapi.co/api/v2/pokemon/gengar")
d2 = r2.json()
print(d2['name'])
print(f"{d2['name']}'s height: {d2['height']} inches. Weight: {d2['weight']}lbs")
print(f"{d2['name']}'s 1st type is : {d2['types'][0]['type']['name']}")

r3 = requests.get("https://pokeapi.co/api/v2/pokemon/gallade")
d3 = r3.json()
print(d3['name'])
print(f"{d3['name']}'s height: {d3['height']} inches. Weight: {d3['weight']}lbs")
print(f"{d3['name']}'s 1st type is : {d3['types'][0]['type']['name']}")