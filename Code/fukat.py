cash = 1500


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


items_in_bag = {}


def update_bag(item, quantity):
    global items_in_bag
    if item in items_in_bag:
        items_in_bag[item] += quantity
    else:
        items_in_bag[item] = quantity


def store():
    print("Entered the store")
    print(f"Balance: ${cash}")

    item_list = {
        1: ("Poké Ball", 200),
        2: ("Great Ball", 600),
        3: ("Potion", 300),
        4: ("Super Potion", 700),
        5: ("Revive", 1500),
        6: ("TM01 - Water Pulse", 1000),
        7: ("TM02 - Dragon Claw", 2000),
        8: ("TM03 - Toxic", 1500),
        9: ("TM04 - Hidden Power", 1200)
    }

    for key, store_item in item_list.items():
        print(f"{key}. {store_item[0]} - ${store_item[1]}")

    choice = int(input("What would you like to buy? "))
    while choice not in item_list:
        print("Invalid input")
        choice = int(input("What would you like to buy? "))

    item_name, item_cost = item_list[choice]
    quantity = int(input(f"How many {item_name} would you like to buy? "))

    final_price = quantity * item_cost
    print(f"Your subtotal is ${final_price}")

    confirmation = input(f"Confirm purchase of {quantity} {item_name}(s)? [Y/N]: ")
    if confirmation.upper() == "Y":
        update_cash(final_price, transaction_type="spend")
        update_bag(item_name, quantity)
        print("Thank you!")
