import requests

r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

print(type(r))  
print(r.status_code)
print(r.headers['Content-Type'])

print(r.text[:200])