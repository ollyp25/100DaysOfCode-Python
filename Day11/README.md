
# Day 11 - Blackjack Capstone Project

### Concepts Learned: 
Day 11 was focused on reviewing everything I had learned up to that point in building a simple Blackjack game.

## Project of the Day - Blackjack
- [Blackjack Game](Day11/main.py)

### How It Works

1. User Input: The game begins by asking the player if they want to play Blackjack. If the player types "y", the game starts; otherwise, it ends.
2. Card Dealing: Two cards are dealt to both the player and the computer from a deck. The deck contains values representing card ranks (Ace as 11, and 10 for face cards).
3. Blackjack Check: If the player's initial cards sum to 21, the player wins instantly with a "Blackjack!" and the game continues to the next round.
4. Player's Turn: The player is shown their hand and the computer's first card. They can choose to take another card or stop. If the player's hand exceeds 21, they lose.
5. Ace Adjustment: If the player's hand goes over 21 and contains an Ace (which is initially worth 11), the Ace is converted to 1 to prevent busting.
6. Dealer's Turn: The computer (dealer) draws cards until their total score is at least 17.
7. Final Result: After both the player and dealer have completed their turns, the final scores are compared. The player wins if their score is higher than the dealer's or if the dealer busts. If the dealer has a higher score, the player loses, otherwise, it’s a tie.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
Do you want to play a game of Blackjack?(Type y/n): y

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [9, 2], current score: 11
Computer's first card: 10
Would you like another card (type y/n): y
Your cards: [9, 2, 10], current score: 21
Computer's first card: 10
Your final hand: [9, 2, 10], final score: 21
Computer's final hand: [10, 3, 3, 10], final score: 26
You win! :)
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.