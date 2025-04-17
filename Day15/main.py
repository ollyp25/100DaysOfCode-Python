MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 150,
    "coffee": 100,
}

def report(money):
    '''Print the report of the coffee machine's resources'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")
    print(f"Money: ${money:.2f}")

def process_payment():
    '''User pays for their order with coins'''
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    inserted_coins = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return inserted_coins

def make_coffee(order):
    '''Brew coffee aka deduct ingredients from resources'''
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]

def coffee_machine():
    money = 0
    transaction_complete = False
    operations = ["espresso", "latte", "cappuccino", "report", "off"]
    while not transaction_complete:
        order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
        # Checks if input is programmed in the coffee machine
        while order not in operations:
            print("Invalid input.")
            order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
        # Turns the machines off aka ends the program
        if order == "off":
            return False
        # Prints out the report
        elif order == "report":
            report(money)
        else:
            # Checks if there's enough resources to brew coffee
            for item in MENU[order]["ingredients"]:
                if resources[item] < MENU[order]["ingredients"][item]:
                    print(f"Sorry, there's not enough {item}.")
                    break
            else:
                # Prints out the price of user's order
                drink_cost = MENU[order]["cost"]
                balance = drink_cost
                print(f"Total price: ${balance:.2f}")
                # Asks the user to insert coins to pay
                coins = process_payment()
                balance -= coins
                # Restarts the program due to insufficient funds
                if balance > 0:
                    print(f"Sorry that's not enough money. Money refunded.")
                    continue
                # Updates coffee machines funds
                money += drink_cost
                # Gives change
                if balance < 0:
                    change = balance * - 1
                    print(f"Here is ${change:.2f} in change.")
                # Deduct resources aka brew coffee
                make_coffee(order)
                print(f"Here's your {order}. Enjoy!")


if __name__ == "__main__":
    coffee_machine()