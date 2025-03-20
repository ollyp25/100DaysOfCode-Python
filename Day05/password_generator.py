# Import Random Module
import random

# Initialize letters, symbols and digits for computer to use to generate a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greet the user
print("Welcome to the Python Password Generator!")

# Prompt the user for input
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

# Initialize password list (empty)
password = []

# Append n letters to the list
for l in range(1, nr_letters + 1):
    letter_index = random.randint(0, len(letters) - 1) # Fetch a random indexed letter from the list of letters
    password.append(letters[letter_index])

# Append n symbols to the list
for s in range(1, nr_symbols + 1):
    symbol_index = random.randint(0, len(symbols) - 1)
    password.append(symbols[symbol_index])

# Append n digits to the list
for n in range(1, nr_numbers + 1):
    number_index = random.randint(0, len(numbers) - 1)
    password.append(numbers[number_index])

# Shuffle the password list
random.shuffle(password)

# Print the result
result = "".join(password)
print(result)
