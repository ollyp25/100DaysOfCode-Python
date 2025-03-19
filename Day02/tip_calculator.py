# Welcome message
print("Welcome to the tip calculator!")

# Prompt user for input and convert each value into a float/integer
bill = float(input("What's the bill total? $ "))
tip_percentage = int(input("What percentage would you like to tip? "))
people = int(input("How many people are splitting the bill? "))

# Calculate the total amount including the tip
total = bill * ((100 + tip_percentage) / 100)

# Calculate each person's share, rounded to 2 decimal points
share = round((total / people), 2)

# Print the formatted final result
print(f"Each person should pay ${share:.2f}")
