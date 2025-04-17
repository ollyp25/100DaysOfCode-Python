
# Day 15 - Local Development Environment Setup & the Coffee Machine

### Concepts Learned: 

Day 15 was dedicated to putting the previously learned concepts to practice by creating a program that simulates a coffee vending machine. 

## Project of the Day
- [Coffee Machine](Day15/main.py)

### How It Works

1. Menu & Resources: The program defines a drink menu with ingredients and prices, and tracks available resources.
2. User Interaction: The user selects a drink, requests a report, or turns off the machine.
3. Resource Check: For drink orders, the program checks if enough ingredients are available.
4. Payment: The user inserts coins; the program calculates if the payment covers the cost.
5. Transaction Result:
- If payment is insufficient, the money is refunded.
- If sufficient, change is returned (if needed), and ingredients are deducted.
6. Brew & Repeat: The drink is served, and the loop continues until "off" is entered.

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
- Feel free to modify the program, for example, by adding more advanced features like input validation, dynamic tip percentages, or a graphical user interface (GUI).
