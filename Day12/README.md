
# Day 12 - Scope and Number Guessing Game

### Concepts Learned: 
- The concept of Scope in programming
- Local and global variables

## Project of the Day 
- [Number Guessing Game](Day12/main.py)

### How It Works

1. Welcome Message: The game starts by displaying a welcome message and showing an ASCII art logo.
2. Choosing Difficulty: The player is asked to choose a level of difficulty ("easy" or "hard"). This determines how many lives the player will have in the game.
3. Generating a Random Number: The computer selects a random number between 1 and 100 that the player needs to guess.
4. Player's Guess: The player takes a guess, and the program checks if the guess is too high, too low, or correct:
5. If the guess is too low or too high, the player loses a life and is prompted to try again.
6. If the guess is correct, the player wins and is shown the number they were guessing.
7. Lives: The player has a set number of lives based on the chosen difficulty. If the player uses up all their lives without guessing correctly, they lose and the correct number is revealed.
8. Repeat or Quit: After each round, the player is asked if they want to play another round. If they choose to continue, the game restarts; otherwise, it ends.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a level of difficulty (type 'easy' or 'hard'): easy
Take a guess: 50
Too high. Try again.
You have 9 lives remaining.
Take a guess: 25
Too low. Try again.
You have 8 lives remaining.
Take a guess: 35
Too low. Try again.
You have 7 lives remaining.
Take a guess: 40
Too high. Try again.
You have 6 lives remaining.
Take a guess: 37
Too low. Try again.
You have 5 lives remaining.
Take a guess: 38
Too low. Try again.
You have 4 lives remaining.
Take a guess: 39
You got it! The number I was thinking of was 39.
Would you like to play another round? (Type 'y' or 'n'): n
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.