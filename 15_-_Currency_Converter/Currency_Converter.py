from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def get_currencies():
    """
    Retrieves a sorted list of currencies available from the API.

    Returns:
    - list: List of tuples containing (currency_id, currency_name, currency_symbol).
    """
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    # Convert dictionary to list of tuples and sort by currency_id
    currencies = [(currency['id'], currency['currencyName'], currency.get('currencySymbol', ''))
                  for currency in data.values()]
    currencies.sort()

    return currencies

def print_currencies(currencies):
    """
    Prints a formatted list of currencies.

    Args:
    - currencies (list): List of tuples (currency_id, currency_name, currency_symbol).
    """
    for _id, name, symbol in currencies:
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    """
    Retrieves and prints the exchange rate between two currencies.

    Args:
    - currency1 (str): Base currency code.
    - currency2 (str): Target currency code.
    """
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if not data:
        print('Invalid currencies or no data available.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    """
    Converts an amount from one currency to another and prints the result.

    Args:
    - currency1 (str): Base currency code.
    - currency2 (str): Target currency code.
    - amount (str): Amount to convert.

    Returns:
    - float: Converted amount.
    """
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    """
    Main function to interact with the user for currency conversion commands.
    """
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

if __name__ == "__main__":
    main()
