
# Day 16 - Object Oriented Programming

### Concepts Learned: 

Day 16 focused on Object-Oriented Programming (OOP). I learned about:
- Classes and objects
- Creating objects and accessing their attributes and methods
- Installing Python packages using PyPi

To wrap up, I applied OOP principles by refactoring the previous day's Coffee Machine project—breaking it into modular components managed by individual classes.

## Project of the Day
- [Coffee Machine](Day16/main.py)

### How It Works

1. Modular Setup: The program uses three custom classes—Menu, CoffeeMaker, and MoneyMachine—to organize functionality into clear, manageable components.
2. User Prompt: The user selects a drink or enters "report" to view current machine status, or "off" to shut it down.
3. Drink Selection: The Menu class retrieves available drinks and provides drink details using find_drink().
4. Resource & Payment Check:
- The CoffeeMaker checks if there are enough ingredients.
- The MoneyMachine handles coin input and verifies payment.
5. Brew & Serve: If both checks pass, the drink is made and served using make_coffee().
6. Reporting: The user can print a report showing current resources and money collected from both the coffee maker and money machine.
7. Loop: The program runs continuously until "off" is entered, using object-oriented structure to keep logic clean and modular.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
What would you like to order? (espresso/latte/cappuccino): report
Water: 300ml
Milk: 150ml
Coffee: 100gr
Money: $0.00
What would you like to order? (espresso/latte/cappuccino): espresso
Total price: $1.50
Please insert coins.
How many quarters? 5
How many dimes? 4
How many nickels? 3
How many pennies? 2
Here is $0.32 in change.
Here's your espresso. Enjoy!
What would you like to order? (espresso/latte/cappuccino): report
Water: 250ml
Milk: 150ml
Coffee: 82gr
Money: $1.50
What would you like to order? (espresso/latte/cappuccino): off
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.