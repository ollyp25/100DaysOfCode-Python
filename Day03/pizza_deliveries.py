# Greet the user
print("Welcome to Python Pizza Deliveries!")

#Prompt the user for the pizza size
size = input("What size pizza do you want? S, M or L: ")

# Ask the user if they want pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Ask the user if they want extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Keep track of the order's total
total = 0 # Initialize it to 0

# Adjust the value of the order's total according to the user's input
if size == "S":
    total += 15
    if pepperoni == "Y":
        total += 2
elif size == "M":
    total += 20
    if pepperoni == "Y":
        total += 3
elif size == "L":
    total += 25
    if pepperoni == "Y":
        total += 3
if extra_cheese == "Y":
    total += 1

# Print out the final result
print(f"Your final bill is: ${total:.2f}.")
