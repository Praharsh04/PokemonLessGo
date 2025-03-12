import time
def Game():
    start()
    choose_first_pokemon()
    city_name, trainer_name = city()
    Explore(city_name,trainer_name)

cash = 0
def update_cash(amount, transaction_type):
    global cash

    if transaction_type == "spend":
        if cash >= amount:
            cash -= amount
            print(f"Purchase Successful! ${amount} was deducted. Current balance: ${cash}")
        else:
            print("Insufficient Balance")
    elif transaction_type == "earn":
        cash += amount
        print(f"Earned ${amount}! Current balance: ${cash}")
bag = {}
def update_bag(bag, item, quantity):
    if item in bag:
        bag[item] += quantity
    else:
        bag[item] = quantity
def use_bag_item(bag, item, quantity):
    if item in bag and bag[quantity] >= 1:
        bag[item] -= quantity
        
    else:
        print("Item not available")

    

def start():
    import time

    def slow_print(text, delay=1):
        print("\n" + text)
        time.sleep(delay)


    slow_print("Professor Oak: Hello! Welcome to the world of POKÉMON!")
    slow_print("This world is inhabited by creatures called POKÉMON. Some battle, some bond, and many mysteries remain!")
    name = input("\nOak: Now, what's your name? Enter: ")

    slow_print(f"Oak: {name}, your adventure begins now! A world of dreams and challenges awaits! ")
    slow_print("Choose your first Pokémon! ")




def choose_first_pokemon():
    first_pokemon_dict = {
        1 : ("Charmender", "Fire"),
        2 : ("Bulbausaur", "Grass"),
        3 : ("Squirtel", "Water")
    }
    for key, (name, pokemon_type) in first_pokemon_dict.items():
            print(f"{key}. {name} - {pokemon_type} Type")
    first_pokemon = int(input("Enter Choice: "))
    f_name = first_pokemon_dict[first_pokemon][0]
    f_type = first_pokemon_dict[first_pokemon][1]
    time.sleep(1)
    print(f"Bravo! {f_name} is your Buddy now")
    time.sleep(1)
    print(f"{f_name} is {f_type} type, {f_name}")
    print(f"Best of luck for your pokemon journey1")
    print("Recived $1500 cash from proffessor Oak,")
    update_cash(amount=1500, transaction_type="earn")
    print("")
    
def city():
    print("Where you want to head towards")
    time.sleep(1)
    city = {
        1: ("Pewter City", "Rock", "Brock", "Boulder Badge"),
        2: ("Cerulean City", "Water", "Misty", "Cascade Badge"),
        3: ("Celadon City", "Grass", "Erika", "Rainbow Badge"),
        4: ("Vermilion City", "Electric", "Lt. Surge", "Thunder Badge"),
        5: ("Cinnabar Island", "Fire", "Blaine", "Volcano Badge")
    }
    
    for key, city_d in city.items():
        print(f"{key}. {city_d[0]} known for {city_d[1]} type Pokémon, Here you can battle {city_d[2]} to gain {city_d[3]}.")
    choose = int(input("Enter num: "))
    time.sleep(1)
    chosen_city = city[choose]
    city_name = city[choose][0]
    trainer_name = city[choose][2]
    print(f"Welcome to {chosen_city[0]}!")
    return city_name, trainer_name
    


def Explore(city_name,trainer_name):
    
    place = {
          1 : ("Store","Buy Items"),
          2 : ("Pokemon Gym",f"Battle{trainer_name}"),
          3 : ("Wild grass","Catch wild pokemons"),
          4 : ("Cave","Catch ground type pokemons"),
          5 : ("Battle","Battle local trainer's"),
     }
    for key, places in place.items():
         print(f"{key}. {places[0]} where you can {places[1]}")
    choose = int(input("Enter: "))

    if choose == 1:
        print(f"Hola! Welcome to {city_name} store,")
        store()
    elif choose == 2:
         Gym()
    elif choose == 3:
         grass()
    elif choose == 4:
         cave()
    elif choose == 5:
         trainer()

def store():
    
    print("What would you like to buy?: ")
    store_items = {
         
            1: ("Poké Ball", 200),
            2: ("Great Ball", 600),
            3: ("Potion", 300),
            4: ("Super Potion", 700),
            5: ("Revive", 1500)
    }
    for key , products in store_items.items():
         print(f"{key}. {products[0]} - {products[1]}")
    choose = int(input("Enter: "))
    product_name = store_items[choose][0]
    product_price = store_items[choose][1]
    quantity = int(input(f"How many {product_name} would you like to buy: "))
    confirmation = input("Do you want to proceed[Y/N]: ")
    if confirmation == "Y":
         final_price = product_price*quantity
         print(f"Your subtotal is {final_price}")
         update_cash(amount=final_price,transaction_type = "spend")
    elif confirmation == "N":
         pass
    repurchase = input("Do you want to buy anything else[Y/N]: ")
    if repurchase == "Y":
         return store()
    else:
        print("Goodbye, Visit Again!")
        return Explore()

         
    
    
Game()





    






