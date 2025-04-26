
# Day 25 - Working with CSV Files + U.S. States Game

### Concepts Learned: 

Today I learned how to work with CSV files and analyze data using the Pandas library. We built a fun quiz-style game where you guess U.S. state names, and correct guesses appear on a blank map.

This project taught me:
- How to read CSV data
- Use Pandas for data handling
- Combine user input with turtle graphics

## Project of the Day
- [US State Guessing Game](Day25/main.py)

### How It Works

This interactive program is a U.S. States guessing game built with Turtle graphics and Pandas. When run, it displays a blank map of the U.S. and prompts the user to guess the names of states. Correct guesses are marked on the map at their corresponding coordinates using data from a CSV file. The game continues until the user has correctly guessed all 50 states or types “Exit” to stop. If the user exits early, a list of missed states is saved to a new CSV file (states_to_learn.csv) for further study.

### Usage

To run the program, execute the script in your Python environment:

```
python main.py
```

### Example

![Game demo](images/us-states-game.gif)

### Technologies Used
- Python 3.x

### Notes

- This is one of the earliest projects I completed during the **100 Days of Code** Python Bootcamp on Udemy.
- Feel free to modify the program by adding more advanced features.
