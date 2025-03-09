import json
import requests
import time

def main():
    name = input("Enter your user name: ")
    pokeballs = 5
    cash = 1000
    My_pokemon = []
    print(f"{name} You currently have {pokeballs} pokeballs and {cash} cash")
    first_pokemon = pokedex(first_pokemon)
    
    


def choose_pokemon():

    first_pokemon = input("Choose your first pokemon[Squirtl/Bulbasour/Charmender]: ")
    return first_pokemon




def pokedex(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon?limit=1010"
    
    response = requests.get(url)
    
    if response.status_code == 200:

        data = response.json()
        all_pokemon = {}
        
        for pokemon in data["results"]:
            name = pokemon["name"]
            url = pokemon["url"]  # Fetch individual Pokémon details
            
            # Fetch detailed data for each Pokémon
            details_response = requests.get(url)
            if details_response.status_code == 200:
                details = details_response.json()
                
                # Store Pokémon details in dictionary
                all_pokemon[name] = {
                    "id": details["id"],
                    "height": details["height"],
                    "weight": details["weight"],
                    "types": [t["type"]["name"] for t in details["types"]],
                    "moves": [move["move"]["name"] for move in details["moves"]]
                }
        
        return all_pokemon
    else:
        print("Failed to fetch Pokémon list.")
        return {}

def NameOfPokemon(pokemon_name):

    pokemon_name = input("Enter the name of the pokemon: ")
    pokemon_data = pokedex(pokemon_name)
    with open(f"{pokemon_name}.json", "w") as file:
        json.dump(pokemon_data, file, indent=4)
    print(json.dumps(pokemon_data, indent=4))

def select_town():
    town = input("Enter the town you want to enter: ")
    if town=="verdant grove":
        print("You are entering Verdant Groove")
        print("Loadding....")
        time.sleep(3)
        print("Welcome to Verdant Groove")




 


    






