import requests
import sys

def main():
    try:
        if len(sys.argv) < 2:
            print("Missing command line argument")
            sys.exit()  # Exit if no argument is provided
        else:
            value = sys.argv[1]
            try:
                value = float(value)  # Convert input to float
            except ValueError:
                print("Command line argument is not a number")
                sys.exit()
    except ValueError:
        print("Command line argument is not a number")
        sys.exit()

    amount = get_price()
    final_amount = amount * value
    print(f"${final_amount}")

def get_price():
    r = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    d = r.json()
    data = d["data"]
    amount = data["priceUsd"]
    return float(amount)  # Convert price to float before returning

main()
