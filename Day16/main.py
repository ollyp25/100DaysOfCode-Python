from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

operations = menu.get_items().split("/")
operations.remove(operations[3])
operations.extend(["off", "report"])

def coffee_machine():
    is_on = True
    while is_on:
        order = input("What would you like to order?(Type espresso/latte/cappuccino): ").lower()
        while order not in operations:
            print("Invalid input")
            order = input("Please select one of the following: espresso, latte, cappuccino. ").lower()
        if order == "off":
            print("Coffee machine is turning off. Bye!")
            is_on = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


coffee_machine()