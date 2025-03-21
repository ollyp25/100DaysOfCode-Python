import art

print(art.logo)

# Initialise an empty dictionary to keep track of user bids
user_bids ={}

while True:
    # Prompt user for input
    user_name = input("What's your name? ")
    bid = int(input("What's your bid? $ "))
    # Update the dictionary
    user_bids[user_name] = bid

    # Check for additional bids
    new_bid = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if new_bid != "yes":
        break
    # Add line breaks to hide previous input
    print("\n" * 20)

# Find the highest bid amount
highest_bid = 0
for key in user_bids:
    if user_bids[key] > highest_bid:
        highest_bid = user_bids[key]

# Fetch the name of the user that won the bidding war from the dictionary
for key in user_bids:
    if user_bids[key] == highest_bid:
        winner = key

# Print the name and highest bid
print(f"The winner is {winner} with a bid of ${highest_bid}")



