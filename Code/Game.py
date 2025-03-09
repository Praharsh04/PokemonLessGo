import time


# =================== CASH MANAGEMENT ===================
class Cash:
    def __init__(self, initial_amount=1500):
        self.balance = initial_amount

    def update_cash(self, amount, transaction_type):
        if transaction_type == "spend":
            if self.balance >= amount:
                self.balance -= amount
                print(f"Purchase Successful! ${amount} deducted. Current balance: ${self.balance}")
                return True
            else:
                print("Insufficient Balance!")
                return False
        elif transaction_type == "earn":
            self.balance += amount
            print(f"Earned ${amount}! Current balance: ${self.balance}")

# =================== BAG MANAGEMENT ===================
class Bag:
    def __init__(self):
        self.items = {}

    def update_bag(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} {item}(s) to your bag!")

# =================== GAME CLASS ===================
class Game:
    def __init__(self):
        self.name = None
        self.player_pokemon = None
        self.cash = Cash()
        self.bag = Bag()
        self.town_name = None

    def start_game(self):
        self.name = input("Hey! What's your name: ")
        print(f"Hey {self.name}, your Pokémon journey begins!")

        first_pokemon = {
            1: ("Charmander", "Fire"),
            2: ("Bulbasaur", "Grass"),
            3: ("Squirtle", "Water")
        }

        print('Professor Oak: "Choose your first Pokémon!"')
        for key, (name, pokemon_type) in first_pokemon.items():
            print(f"{key}. {name} - {pokemon_type} Type")

        choice = int(input("Enter Number: "))
        while choice not in first_pokemon:
            print("Invalid Number")
            choice = int(input("Enter the Number: "))

        self.player_pokemon = first_pokemon[choice][0]
        print(f"Congratulations! {self.player_pokemon} is your buddy now.")
        
        # Initial rewards
        self.cash.update_cash(1000, "earn")
        self.bag.update_bag("Poké Ball", 5)


# =================== TOWN CLASS ===================
class Town:
    def __init__(self, game_instance):
        self.game = game_instance
        self.town_name = None
        self.town_type = None
        self.town_leader = None
        self.town_badge = None

    def enter_town_name(self):
        towns = {
            1: ("Pewter City", "Rock", "Brock", "Boulder Badge"),
            2: ("Cerulean City", "Water", "Misty", "Cascade Badge"),
            3: ("Celadon City", "Grass", "Erika", "Rainbow Badge"),
            4: ("Vermilion City", "Electric", "Lt. Surge", "Thunder Badge"),
            5: ("Cinnabar Island", "Fire", "Blaine", "Volcano Badge")
        }

        for key, town in towns.items():
            print(f"{key}. {town[0]} - {town[1]} Type Pokémon")

        t_choice = int(input("Enter: "))
        while t_choice not in towns:
            print("Invalid choice")
            t_choice = int(input("Enter Number: "))

        self.town_name, self.town_type, self.town_leader, self.town_badge = towns[t_choice]
        self.game.town_name = self.town_name  # Update player's town

        print(f"Welcome to {self.town_name}! Known for {self.town_type} type Pokémon.")

# =================== EXPLORE CLASS ===================
class Explore:
    def __init__(self, town_instance):
        self.town = town_instance

    def explore_town(self):
        places = {
            1: "Store",
            2: "Gym",
            3: "Pokémon Center",
            4: "Jungle",
            5: "Tall Grass",
            6: "Cave",
            7: "Battle With a Trainer"
        }

        for key, value in places.items():
            print(f"{key}. {value}")

        choice = int(input("Where would you like to go? "))
        if choice == 1:
            store = Store(self.town.game.cash, self.town.game.bag)
            store.buy_item()

# =================== STORE CLASS ===================
class Store:
    def __init__(self, cash, bag):
        self.cash = cash
        self.bag = bag
        self.items = {
            1: ("Poké Ball", 200),
            2: ("Great Ball", 600),
            3: ("Potion", 300),
            4: ("Super Potion", 700),
            5: ("Revive", 1500)
        }

    def buy_item(self):
        print("Welcome to the PokéMart!")
        for key, (item, price) in self.items.items():
            print(f"{key}. {item} - ${price}")

        choice = int(input("Enter the item number to purchase: "))
        while choice not in self.items:
            print("Invalid input, try again.")
            choice = int(input("Enter the item number to purchase: "))

        item_name, item_price = self.items[choice]
        quantity = int(input(f"How many {item_name}s would you like? "))

        total_price = quantity * item_price
        if self.cash.update_cash(total_price, "spend"):
            self.bag.update_bag(item_name, quantity)
            print(f"Purchased {quantity} {item_name}(s)!")
        else:
            print("Not enough money!")

# =================== MAIN GAME LOOP ===================
player = Game()
player.start_game()

town = Town(player)
town.enter_town_name()

explore = Explore(town)
explore.explore_town()
