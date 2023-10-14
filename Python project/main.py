import requests

token = '69783f56c4cd6fe76fb62a98898da47f'

response_create = requests.post('https://api.pokemonbattle.me:9104//pokemons', 
              json = {"name": "Бульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
              headers = {'Content-Type':'application/json','trainer_token': token })

print (response_create.text)

response_pokemonname = requests.put ('https://api.pokemonbattle.me:9104//pokemons', 
                                json = {"pokemon_id":"12476",
                                        "name":"New Name",
                                        "photo":"https://dolnikov.ru/pokemons/albums/008.png"},
                                headers = {'Content-Type':'application/json','trainer_token': token } )

print (response_pokemonname.text)


response_in_pokball = requests.post ('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                                     json={"pokemon_id": "12477"},
                                     headers ={'Content-Type':'application/json','trainer_token': token})

print (response_in_pokball.text)


                        