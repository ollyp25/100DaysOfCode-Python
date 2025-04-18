
# Day 9 - Dictionaries, Nesting and the Secret Auction

### Concepts Learned:

- Python Dictionaries
- Nested dictionaries & lists

## Project of the Day - Blind Auction

This program simulates an auction process where multiple users can place bids for an item.

- [Blind Auction](Day09/main.py)

### How It Works

1. User Input: Each user is prompted to input their name and bid amount.
2. Bid Tracking: All bids are stored in a dictionary where the keys are the users' names, and the values are their corresponding bid amounts.
3. Repeat Bidding: The program asks if there are more users who want to place a bid. If there are, it will continue to prompt for new bids. If no more bids are placed, the auction ends.
4. Determine the Winner: The program compares all the bids to find the highest bid and announces the winner.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What's your name? Jane Doe
What's your bid? $ 150
Are there any other bidders? Type 'yes or 'no': yes


What's your name? John Doe
What's your bid? $ 250
Are there any other bidders? Type 'yes or 'no': No
The winner is John Doe with a bid of $250
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.