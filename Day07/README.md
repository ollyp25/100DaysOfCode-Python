
# Day 7 - Hangman

### Concepts Learned: 
Day 7 was dedicated to practicing all the concepts/syntax that I'd learned thus far:

- Python For & While Loops
- Conditionals (if and else statements)
- Python Lists
- Functions
- Python Modules

## Project of the Day - Hangman
This is a simple Hangman game written in Python, where the user is prompted to guess the letters of a randomly selected word. The game gives the player 6 lives, and with each incorrect guess, a life is lost. The player wins if they guess the word before running out of lives!
- [Hangman in Python](Day07/main.py)

### How It Works

1. User Interface: The game starts by displaying the Hangman logo and the placeholder for the word.
2. Game Loop: The player is repeatedly prompted to guess a letter. If the letter is part of the word, it's revealed in the correct positions; if not, the player loses a life.
3. End of Game: The game ends when the player either guesses the word correctly or runs out of lives.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
_________
Guess a letter: a
______a__

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: s
_s____a__

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: t
**************** WRONG GUESS // 5 LIVES LEFT ****************
_s____a__

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: n
_s___na__

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: m
**************** WRONG GUESS // 4 LIVES LEFT ****************
_s___na__

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: l
**************** WRONG GUESS // 3 LIVES LEFT ****************
_s___na__

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: k
**************** WRONG GUESS // 2 LIVES LEFT ****************
_s___na__

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: c
**************** WRONG GUESS // 1 LIVES LEFT ****************
_s___na__

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: b
**************** WRONG GUESS // 0 LIVES LEFT ****************
_s___na__

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

The word you were trying to guess was espionage.
******************** YOU LOST ********************
```

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.